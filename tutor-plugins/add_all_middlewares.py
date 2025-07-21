from tutor import hooks
import os

# Path to the git-reqs directory, relative to this plugin file.
GIT_REQS_DIR = os.path.join(
    os.path.dirname(__file__),
    "../env/build/openedx/requirements/git-reqs"
)

# Resolve the absolute path for safety
GIT_REQS_DIR = os.path.abspath(GIT_REQS_DIR)

# Loop over every folder in the git-reqs directory
for folder_name in os.listdir(GIT_REQS_DIR):
    folder_path = os.path.join(GIT_REQS_DIR, folder_name)
    # Only add if it's a directory (not a file)
    if os.path.isdir(folder_path):
        # Add the folder as a mounted directory for the 'openedx' image
        # This tells Tutor to mount this directory inside the container
        hooks.Filters.MOUNTED_DIRECTORIES.add_item(("openedx", folder_name))
        # You can print for debugging (remove in production)
        print(f"Added mount for: {folder_name}")

