import os
from config import HIDS_LOG_FOLDER, HIDS_HASHES_FILE


def init_hids_environment():
    # Create log folder if it doesn't exist
    if not os.path.exists(HIDS_LOG_FOLDER):
        os.makedirs(HIDS_LOG_FOLDER)
        print(f"Created log folder: {HIDS_LOG_FOLDER}")

    # Create hashes file if it doesn't exist
    if not os.path.exists(HIDS_HASHES_FILE):
        with open(HIDS_HASHES_FILE, "w"):
            pass  # Create an empty file
        print(f"Created hashes file: {HIDS_HASHES_FILE}")


if __name__ == "__main__":
    init_hids_environment()
