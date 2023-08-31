import os
import time
import sys

if __name__ == '__main__':
    branch = os.getenv("branch")
    print(f"=========== checkout from {branch} ===========")
    sleep_time = os.getenv("SLEEP_TIME")
    if not sleep_time:
        sys.exit(0)
    if not sleep_time.isnumeric():
        sys.exit(0)
    time.sleep(int(sleep_time))
