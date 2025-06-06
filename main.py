import time
import schedule
from utils.hash_db import init_db
from config import HIDS_WATCH_DIRECTORY, HIDS_IS_HASHED
from utils.hash_comparator import generate_file_hashes, compare_all_hashes

if __name__ == "__main__":
    from utils.init_hids import init_hids_environment

    init_hids_environment()
    init_db()

if not HIDS_IS_HASHED:
    generate_file_hashes(HIDS_WATCH_DIRECTORY)
    HIDS_IS_HASHED = True


def job() -> None:
    if not compare_all_hashes(HIDS_WATCH_DIRECTORY):
        print("Hash comparison failed! Possible file tampering detected.")
        # Optionally, add more actions here (logging, alerting, etc.)
    else:
        print("Hash comparison successful.")  # pragma: no cover


# Schedule the job every 10 minutes
schedule.every(5).seconds.do(job)

print("HIDS is running. Press Ctrl+C to exit.")
job()  # Run once at startup

while True:
    schedule.run_pending()
    time.sleep(1)
