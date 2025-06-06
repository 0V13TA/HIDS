import os
from config import HIDS_LOG_FOLDER, HIDS_HASHES_FILE


def init_hids_environment():
    # Create log folder if it doesn't exist
    if not os.path.exists(HIDS_LOG_FOLDER):
        os.makedirs(HIDS_LOG_FOLDER)
        print(f"Created log folder: {HIDS_LOG_FOLDER}")

    # Ensure parent directory for hashes file exists
    hashes_dir = os.path.dirname(HIDS_HASHES_FILE)
    if hashes_dir and not os.path.exists(hashes_dir):
        os.makedirs(hashes_dir)
        print(f"Created hashes directory: {hashes_dir}")

    # Create hashes file if it doesn't exist
    if not os.path.exists(HIDS_HASHES_FILE):
        with open(HIDS_HASHES_FILE, "w"):
            pass  # Create an empty file
        print(f"Created hashes file: {HIDS_HASHES_FILE}")


if __name__ == "__main__":
    init_hids_environment()
