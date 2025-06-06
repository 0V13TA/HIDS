import os
import hashlib
from logger import print_to_file
from hash_db import get_hash, write_hash


def hash_file(file_path: str) -> str | None:
    """Generate SHA-256 hash of the file and write it to the database."""
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
    file_hash = sha256_hash.hexdigest()
    write_hash(file_path, file_hash)  # Write hash to DB
    return file_hash


def compare_hashes(file_path: str, known_hash: str) -> bool:
    """Compare the SHA-256 hash of a file with a known hash."""
    current_hash = hash_file(file_path)
    if current_hash is None:
        return False
    return current_hash == known_hash


def compare_all_hashes(directory: str) -> bool:
    all_hashes = get_hashes_from_db(directory)
    for file_path, known_hash in all_hashes.items():
        if not compare_hashes(file_path, known_hash):
            print_to_file(f"Hash mismatch for file: {file_path}", "severe")
            return False
    return True


def generate_file_hashes(directory: str) -> dict[str, str]:
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
                    file_hash = hash_file(entry.path)  # hash file writes to DB
                    if file_hash is not None:
                        file_hashes[entry.path] = file_hash
                elif entry.is_dir():
                    _recursive_hash(entry.path)
        except Exception as e:
            print_to_file(f"Error accessing '{dir_path}': {e}", "error")

    _recursive_hash(directory)
    return file_hashes


def get_hashes_from_db(directory: str) -> dict[str, str]:
    """
    Recursively get a dictionary of file paths and their hashes from the database in the given directory.
    """
    file_hashes: dict[str, str] = {}

    if not os.path.isdir(directory):
        print_to_file(f"Directory not found: '{directory}'", "error")
        return file_hashes

    def _recursive_hash(dir_path: str):
        try:
            for entry in os.scandir(dir_path):
                if entry.is_file():
                    db_hash = get_hash(entry.path)
                    if db_hash is not None:
                        file_hashes[entry.path] = db_hash
                    else:
                        print_to_file(
                            f"No hash found in DB for: {entry.path}", "warning"
                        )
                elif entry.is_dir():
                    _recursive_hash(entry.path)
        except Exception as e:
            print_to_file(f"Error accessing '{dir_path}': {e}", "error")

    _recursive_hash(directory)
    return file_hashes
