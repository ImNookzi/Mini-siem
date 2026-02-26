
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogEvent:
    timestamp: datetime
    source_ip: str
    user: str
    message: str
    raw: str

@dataclass
class Alert:
    rule_name: str
    severity: str
    description: str
    source_ip: str
    score: int
