
import argparse
from core.parser import parse_auth_log
from core.correlation import detect_bruteforce
from core.scoring import calculate_risk_score
from core.alerting import generate_alerts, export_alerts

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", required=True)
    parser.add_argument("--threshold", type=int, default=5)
    args = parser.parse_args()

    events = parse_auth_log(args.log)
    suspects = detect_bruteforce(events, args.threshold)

    for ip in suspects:
        failed_count = sum(1 for e in events if ip in e.message)
        score = calculate_risk_score(failed_count)
        alerts = generate_alerts([ip], score)
        export_alerts(alerts)

    print("Detection complete.")

if __name__ == "__main__":
    main()
