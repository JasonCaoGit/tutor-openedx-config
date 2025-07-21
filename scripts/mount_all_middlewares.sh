#!/usr/bin/env bash


# Set the base directory where your git-reqs folders are located
GIT_REQS_DIR="../env/build/openedx/requirements/git-reqs"

# Loop over every folder in the git-reqs directory
for SRC in "$GIT_REQS_DIR"/*; do
  # Only process if it's a directory (not a file)
  if [ -d "$SRC" ]; then
    # Get the absolute path of the folder
    ABS_PATH=$(cd "$SRC" && pwd)
    # Print which folder we're adding
    echo "Adding mount for: $ABS_PATH"
    # Add the mount using tutor
    tutor mounts add "$ABS_PATH"
  fi
  # If not a directory, skip
  # (No else needed, just continues)
done
