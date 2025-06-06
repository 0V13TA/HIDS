from config import HIDS_WATCH_DIRECTORY
import hashlib
import os


def hash_file(file_path) -> None | str:
    """Generate SHA-256 hash of the file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as file_handle:
            # Read the file in chunks to avoid memory issues with large files
            for byte_block in iter(lambda: file_handle.read(4096), b""):
                sha256_hash.update(byte_block)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    return sha256_hash.hexdigest()


def compare_hashes(file_path: str, known_hash: str) -> bool:
    """Compare the SHA-256 hash of a file with a known hash."""
    current_hash = hash_file(file_path)
    if current_hash is None:
        return False
    return current_hash == known_hash


def get_file_hashes(directory: str) -> dict:
    """Get a dictionary of file paths and their SHA-256 hashes in the given directory."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = hash_file(file_path)
            if file_hash is not None:
                file_hashes[file_path] = file_hash
    return file_hashes
