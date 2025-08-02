#!/bin/bash

# A script to add a 'version' property with the last git commit timestamp
# and daily commit count to a specified JSON file using jq.

# --- Script Configuration ---
# Set a temporary file name for the jq output
TEMP_FILE=$(mktemp)

# --- Function Definitions ---
# Function to check for required commands
check_dependencies() {
    local dependencies=("git" "jq")
    for cmd in "${dependencies[@]}"; do
        if ! command -v "$cmd" &> /dev/null; then
            echo "Error: Required command '$cmd' is not installed."
            echo "Please install '$cmd' and try again."
            exit 1
        fi
    done
}

# Function to clean up the temporary file on exit
cleanup() {
    rm -f "$TEMP_FILE"
}
trap cleanup EXIT

# --- Main Script Logic ---
# Check dependencies
check_dependencies

# Check for both arguments: base_url and file path
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <base_url> <path_to_json_file>"
    exit 1
fi

BASE_URL="$1"
JSON_FILE="$2"

# Check if the file exists and is a regular file
if [ ! -f "$JSON_FILE" ]; then
    echo "Error: File not found at '$JSON_FILE'."
    exit 1
fi

# Check if the file is tracked by git
if ! git ls-files --error-unmatch "$JSON_FILE" &> /dev/null; then
    echo "Warning: File '$JSON_FILE' is not tracked by Git."
    echo "The version will be set to 'untracked' and the file will be updated."
    GIT_VERSION="untracked"
else
    # Get the timestamp of the last commit that modified the file in YYYYMMDD format
    GIT_TIMESTAMP=$(git log -1 --format=%cd --date=format:%Y%m%d -- "$JSON_FILE")

    # Check if git log command was successful
    if [ $? -ne 0 ]; then
        echo "Error: Could not get git commit timestamp for '$JSON_FILE'."
        exit 1
    fi

    # Get the date of the last commit for the file in YYYY-MM-DD format
    LAST_COMMIT_DATE=$(git log -1 --format=%cd --date=format:%Y-%m-%d -- "$JSON_FILE")

    # Count the number of commits for that file on the day of the last commit
    # We use --since and --until to specify the date range
    # --pretty=oneline ensures each commit is one line, which we then count with wc -l
    COMMIT_COUNT=$(git log --since="$LAST_COMMIT_DATE 00:00:00" --until="$LAST_COMMIT_DATE 23:59:59" --pretty=oneline -- "$JSON_FILE" | wc -l)

    # Check if the commit count was successful
    if [ $? -ne 0 ]; then
        echo "Error: Could not get git commit count for '$JSON_FILE'."
        exit 1
    fi

    # Pad the commit count with a leading zero if it's a single digit
    PADDED_COMMIT_COUNT=$(printf "%02d" "$COMMIT_COUNT")

    # Combine the timestamp and padded commit count
    GIT_VERSION="${GIT_TIMESTAMP}${PADDED_COMMIT_COUNT}"
fi

# Use jq to update the JSON file with the updateSerial information
# '--arg' is used to safely pass the bash variable to jq without escaping issues
# '.updateSerial = $version' sets/updates the 'updateSerial' key to the value of the 'version' argument
if ! jq --arg version "$GIT_VERSION" '.updateSerial = $version' "$JSON_FILE" > "$TEMP_FILE"; then
    echo "Error: Failed to process JSON file with jq. Check if the file is valid JSON."
    exit 1
fi

mv "$TEMP_FILE" "$JSON_FILE"

VATIS_UPDATE_URL="${BASE_URL}$(basename "$JSON_FILE")"

# Use jq to update the JSON file with the updateUrl information
if ! jq --arg url "$VATIS_UPDATE_URL" '.updateUrl = $url' "$JSON_FILE" > "$TEMP_FILE"; then
    echo "Error: Failed to process JSON file with jq. Check if the file is valid JSON."
    exit 1
fi
# Overwrite the original file with the modified content from the temporary file
mv "$TEMP_FILE" "$JSON_FILE"
