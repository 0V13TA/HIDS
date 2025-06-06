import os
import json
from datetime import datetime
from config import HIDS_LOG_FOLDER, HIDS_HASHES_FILE


def print_to_file(message: str, ty: str) -> None:
    date_str = datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H:%M:%S")
    log_filename = f"log_{date_str}.txt"
    log_path = os.path.join(HIDS_LOG_FOLDER, log_filename)
    log_entry = f"[{time_str}] [{ty.upper()}] {message}"
    with open(log_path, "a") as f:
        f.write(log_entry + "\n")


def write_hashes(hash_dict: dict[str, str]):
    with open(HIDS_HASHES_FILE, "w") as f:
        json.dump(hash_dict, f)
