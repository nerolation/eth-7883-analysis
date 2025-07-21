#!/usr/bin/env python3
"""
EIP-7883 ModExp Gas Cost Calculator
Based on the updated EIP-7883 specification
"""

import math


class ModExpGasCalculator:
    """Calculate ModExp gas costs for EIP-2565 and EIP-7883"""
    
    @staticmethod
    def calculate_multiplication_complexity_eip2565(base_length, modulus_length):
        """Calculate multiplication complexity for EIP-2565"""
        max_length = max(base_length, modulus_length)
        words = math.ceil(max_length / 8)
        return words**2
    
    @staticmethod
    def calculate_multiplication_complexity_eip7883(base_length, modulus_length):
        """Calculate multiplication complexity for EIP-7883"""
        max_length = max(base_length, modulus_length)
        words = math.ceil(max_length / 8)
        multiplication_complexity = 16
        if max_length > 32:
            multiplication_complexity = 2 * words**2
        return multiplication_complexity
    
    @staticmethod
    def calculate_iteration_count_eip2565(exponent_length, exponent):
        """Calculate iteration count for EIP-2565"""
        iteration_count = 0
        if isinstance(exponent, str):
            exponent = int(exponent, 16) if exponent.startswith('0x') else int(exponent)
        
        if exponent_length <= 32 and exponent == 0:
            iteration_count = 0
        elif exponent_length <= 32:
            iteration_count = exponent.bit_length() - 1
        elif exponent_length > 32:
            iteration_count = (8 * (exponent_length - 32)) + ((exponent & (2**256 - 1)).bit_length() - 1)
        
        return max(iteration_count, 1)
    
    @staticmethod
    def calculate_iteration_count_eip7883(exponent_length, exponent):
        """Calculate iteration count for EIP-7883"""
        iteration_count = 0
        if isinstance(exponent, str):
            exponent = int(exponent, 16) if exponent.startswith('0x') else int(exponent)
        
        if exponent_length <= 32 and exponent == 0:
            iteration_count = 0
        elif exponent_length <= 32:
            iteration_count = exponent.bit_length() - 1
        elif exponent_length > 32:
            # Changed from 8 to 16 in EIP-7883
            iteration_count = (16 * (exponent_length - 32)) + ((exponent & (2**256 - 1)).bit_length() - 1)
        
        return max(iteration_count, 1)
    
    @staticmethod
    def calculate_eip2565_cost(base_length, modulus_length, exponent_length, exponent):
        """Calculate gas cost according to EIP-2565"""
        multiplication_complexity = ModExpGasCalculator.calculate_multiplication_complexity_eip2565(
            base_length, modulus_length
        )
        iteration_count = ModExpGasCalculator.calculate_iteration_count_eip2565(
            exponent_length, exponent
        )
        return max(200, math.floor(multiplication_complexity * iteration_count / 3))
    
    @staticmethod
    def calculate_eip7883_cost(base_length, modulus_length, exponent_length, exponent):
        """Calculate gas cost according to EIP-7883"""
        multiplication_complexity = ModExpGasCalculator.calculate_multiplication_complexity_eip7883(
            base_length, modulus_length
        )
        iteration_count = ModExpGasCalculator.calculate_iteration_count_eip7883(
            exponent_length, exponent
        )
        # Changed from division by 3 to no division, and minimum from 200 to 500
        return max(500, math.floor(multiplication_complexity * iteration_count))


def recalculate_costs(df):
    """Recalculate costs for all entries in the dataframe"""
    import pandas as pd
    
    # Create new columns for recalculated costs
    df['eip2565_cost_new'] = df.apply(
        lambda row: ModExpGasCalculator.calculate_eip2565_cost(
            row['Bsize'], row['Msize'], row['Esize'], row['E']
        ), axis=1
    )
    
    df['eip7883_cost_new'] = df.apply(
        lambda row: ModExpGasCalculator.calculate_eip7883_cost(
            row['Bsize'], row['Msize'], row['Esize'], row['E']
        ), axis=1
    )
    
    df['cost_increase_new'] = df['eip7883_cost_new'] - df['eip2565_cost_new']
    df['cost_ratio_new'] = df['eip7883_cost_new'] / df['eip2565_cost_new']
    
    return df