import subprocess
import time
import sys

subprocess.run(["python", "index_creations.py"])

wait_seconds = 3
for i in range(wait_seconds, 0, -1):
    sys.stdout.write(f"\rWaiting {i} seconds... ")
    sys.stdout.flush()
    time.sleep(1)
print("\n")

subprocess.run(["python", "number_from_json.py"])

wait_seconds = 3
for i in range(wait_seconds, 0, -1):
    sys.stdout.write(f"\rWaiting {i} seconds... ")
    sys.stdout.flush()
    time.sleep(1)
print("\n")

subprocess.run(["python", "inventory.py"])
subprocess.run(["python", "hinventory.py"])