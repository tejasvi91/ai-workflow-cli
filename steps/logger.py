import os
import datetime


def save_trace(output):

    if not os.path.exists("traces"):
        os.makedirs("traces")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"traces/trace_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(output)

    print(f"📁 Trace saved: {filename}")