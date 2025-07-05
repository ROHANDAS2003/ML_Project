import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from processor_regex import classify_with_regex
from processor_lr import classify_with_logistic_regression
from processor_llm import classify_with_llm


def classify(logs):
    labels = []
    for source, log_msg in logs:
        label = classify_log(source, log_msg)
        labels.append(label)
    return labels

def classify_log(source, log_message):
    if source == "LegacyCRM":
        label = classify_with_llm(log_message)
    else:
        label = classify_with_regex(log_message)
        if label is None:
            label = classify_with_logistic_regression(log_message)
    return label

if __name__ == "__main__":
    logs =[
        ("ModernCRM", "IP 192.168.133.114 blocked due to potential attack"),
        ("BillingSystem", "User User12345 logged in."), 
        ("AnalyticsEngine", "File data_6957.csv uploaded successfully by user User265."), 
        ("AnalyticsEngine", "Backup completed successfully."), 
        ("ModernHR", "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1 RCODE 200 len: 1583 time: 0.1878400"),
        ("ModernHR", "Admin access escalation detected for user 9429"), 
        ("LegacyCRM", "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."), 
        ("LegacyCRM", "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module."),
    ]
    classified_log = classify(logs)
    print(classified_log)