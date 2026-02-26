
import re
from datetime import datetime
from .models import LogEvent

LOG_PATTERN = re.compile(r"(\d+\.\d+\.\d+\.\d+)")

def parse_auth_log(file_path):
    events = []
    with open(file_path) as f:
        for line in f:
            ip_match = LOG_PATTERN.search(line)
            if ip_match:
                events.append(LogEvent(
                    timestamp=datetime.now(),
                    source_ip=ip_match.group(1),
                    user="unknown",
                    message=line.strip(),
                    raw=line.strip()
                ))
    return events
