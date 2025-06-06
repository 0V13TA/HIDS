from config import HIDS_WATCH_DIRECTORY
from utils.hash_comparator import get_file_hashes

print(get_file_hashes(HIDS_WATCH_DIRECTORY))