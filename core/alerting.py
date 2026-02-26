
import json
from .models import Alert

def generate_alerts(suspects, score):
    alerts = []
    for ip in suspects:
        alerts.append(Alert(
            rule_name="SSH Brute Force",
            severity="HIGH",
            description="Multiple failed SSH login attempts detected",
            source_ip=ip,
            score=score
        ))
    return alerts

def export_alerts(alerts, output="alerts.json"):
    with open(output, "w") as f:
        json.dump([a.__dict__ for a in alerts], f, indent=4)
