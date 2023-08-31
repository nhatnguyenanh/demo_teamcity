import os
import time
import sys

if __name__ == '__main__':
    start_time = time.monotonic()
    branch = os.getenv("branch")
    print(f"=========== checkout from {branch} ===========")
    print(f"=========== test trigger 12345 ===========")
    sleep_time = os.getenv("SLEEP_TIME")
    if not sleep_time:
        sys.exit(0)
    if not sleep_time.isnumeric():
        sys.exit(0)
    time.sleep(int(sleep_time))
    print(f"Total execute time {time.monotonic() - start_time}")
