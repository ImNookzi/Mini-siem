Mini SIEM v3 - Advanced Detection Engine

OVERVIEW
Modular detection engine capable of:

* Log parsing
* Brute force detection
* Risk scoring
* Alert export (JSON)
* Extensible correlation logic



HOW TO USE

1. Install dependencies:
   pip install -r requirements.txt
2. Run detection:
   python mini\_siem.py --log sample.log --threshold 5
3. Output:
   Alerts are exported to alerts.json
