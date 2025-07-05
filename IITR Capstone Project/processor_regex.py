import re 
def classify_with_regex(log_message): 
    regex_patterns = { 
    r"\s*User .* logged (in|out).*": "User Action", 
    r"\s*Backup (started|ended) at .*": "System Notification", 
    r"\s*Backup completed successfully.": "System Notification", 
    r"\s*System updated to version.*": "System Notification", 
    r"\s*File .*\.csv uploaded successfully by user .*": "System Notification", 
    r"\s*Disk cleanup completed successfully.": "System Notification", 
    r"\s*System reboot initiated by user .*": "System Notification", 
    r"\s*Account with ID .* created by .*": "User Action",
    r"\s*Anomalous traffic from .* flagged for review": "Security Alert",
    r"\s*IP .* blocked due to potential attack": "Security Alert",
    r"\s*Warning: potential password cracking attempt from .*": "Security Alert",
    r"\s*Possible hacking attempt identified from IP .*": "Security Alert",
    r"\s*IP .* flagged for potential (security|cyber) threat": "Security Alert",
    r"\s*(Unusual|Unauthorised) access attempt from .* (logged|detected)": "Security Alert",
    r"\s*Alert: brute force login attempt from .* detected": "Security Alert",
    r"\s*Brute force login detected from IP .* address": "Security Alert"
    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None


if __name__ == "__main__":
    print(classify_with_regex('  User u409 logged out.'))