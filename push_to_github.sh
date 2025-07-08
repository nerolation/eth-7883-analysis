#!/bin/bash

# EIP-7886 Analysis GitHub Push Script
# This script stages all changes, removes old analyses, and pushes to GitHub

echo "=== EIP-7886 Analysis GitHub Push Script ==="
echo

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not in a git repository"
    exit 1
fi

# Show current git status
echo "Current git status:"
git status --short
echo

# Remove old/outdated files that will be replaced
echo "Removing outdated files from GitHub..."
FILES_TO_REMOVE=(
    # Old entity analysis script (replaced by generate_entity_analysis.py)
    "entity_analysis.py"
    # Old analysis output folder will be replaced with new one
    # "analysis_output"  # Uncomment if you want to remove and re-add the whole folder
)

for file in "${FILES_TO_REMOVE[@]}"; do
    if [ -f "$file" ] || [ -d "$file" ]; then
        echo "Removing: $file"
        git rm -rf "$file" 2>/dev/null || rm -rf "$file"
    fi
done

# Check if there are any other old report files
echo "Checking for any other old report files..."
OLD_REPORTS=$(find . -maxdepth 1 -name "*_report.md" -o -name "*_analysis_report.md" | grep -v "eip7883_comprehensive_analysis.md" | grep -v "eip7883_entity_analysis.md")
if [ ! -z "$OLD_REPORTS" ]; then
    echo "Found old reports to remove:"
    echo "$OLD_REPORTS"
    for report in $OLD_REPORTS; do
        git rm "$report" 2>/dev/null || rm "$report"
    done
fi

# Add all new and modified files
echo
echo "Adding all changes..."
git add -A

# Show what will be committed
echo
echo "Files to be committed:"
git diff --cached --name-status
echo

# Prompt for commit message
read -p "Enter commit message (or press Enter for default): " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Update EIP-7883 comprehensive analysis with enhanced entity reports"
fi

# Commit changes
echo
echo "Committing changes..."
git commit -m "$commit_msg"

# Show commit details
echo
echo "Commit created:"
git log -1 --oneline

# Confirm before pushing
echo
read -p "Ready to push to GitHub? (y/N): " confirm
if [[ $confirm =~ ^[Yy]$ ]]; then
    echo "Pushing to GitHub..."
    git push
    echo
    echo "✓ Successfully pushed to GitHub!"
else
    echo "Push cancelled. You can run 'git push' manually when ready."
fi