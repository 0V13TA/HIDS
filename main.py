import time
import schedule
from utils.hash_db import init_db
from config import HIDS_IS_HASHED
from utils.hash_db import get_all_watch_directories
from utils.hash_comparator import generate_file_hashes, compare_all_hashes

# taskkill /IM python.exe /F
# pkill -f "python3 main.py"

if __name__ == "__main__":

    init_db()


watched_dirs = get_all_watch_directories()

if not HIDS_IS_HASHED:
    generate_file_hashes(watched_dirs)
    HIDS_IS_HASHED = True


def job() -> None:
    if not compare_all_hashes(watched_dirs):
        print("Hash comparison failed! Possible file tampering detected.")
    else:
        print("Hash comparison successful.")


# Schedule the job every 10 minutes
schedule.every(5).seconds.do(job)

print("HIDS is running. Press Ctrl+C to exit.")
job()  # Run once at startup

while True:
    schedule.run_pending()
    time.sleep(1)
