import os
import hashlib
from logger import print_to_file


def hash_file(file_path: str) -> str | None:
    """Generate SHA-256 hash of the file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as file_handle:
            # Read the file in chunks to avoid memory issues with large files
            for byte_block in iter(lambda: file_handle.read(4096), b""):
                sha256_hash.update(byte_block)
    except FileNotFoundError:
        print_to_file(
            f"File not found: '{file_path}', while attempting to generate hash.",
            "error",
        )
        return None
    return sha256_hash.hexdigest()


def compare_hashes(file_path: str, known_hash: str) -> bool:
    """Compare the SHA-256 hash of a file with a known hash."""
    current_hash = hash_file(file_path)
    if current_hash is None:
        return False
    return current_hash == known_hash


def get_file_hashes(directory: str) -> dict[str, str]:
    """
    Recursively get a dictionary of file paths and their SHA-256 hashes in the given directory.
    This function is similar to get_file_hashes but explicitly emphasizes recursion.
    """
    file_hashes: dict[str, str] = {}

    if not os.path.isdir(directory):
        print_to_file(f"Directory not found: '{directory}'", "error")
        return file_hashes

    def _recursive_hash(dir_path: str):
        try:
            for entry in os.scandir(dir_path):
                if entry.is_file():
                    file_hash = hash_file(entry.path)
                    if file_hash is not None:
                        file_hashes[entry.path] = file_hash
                elif entry.is_dir():
                    _recursive_hash(entry.path)
        except Exception as e:
            print_to_file(f"Error accessing '{dir_path}': {e}", "error")

    _recursive_hash(directory)
    return file_hashes
