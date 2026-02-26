
from collections import defaultdict

def detect_bruteforce(events, threshold=5):
    counter = defaultdict(int)
    for e in events:
        if "Failed password" in e.message:
            counter[e.source_ip] += 1
    return [ip for ip, count in counter.items() if count >= threshold]
