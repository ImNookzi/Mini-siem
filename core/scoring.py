
def calculate_risk_score(failed_attempts):
    if failed_attempts > 20:
        return 90
    if failed_attempts > 10:
        return 70
    if failed_attempts > 5:
        return 50
    return 10
