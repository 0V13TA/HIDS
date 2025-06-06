from config import HIDS_WATCH_DIRECTORY
from utils.hash_comparator import generate_file_hashes

print(generate_file_hashes(HIDS_WATCH_DIRECTORY))
