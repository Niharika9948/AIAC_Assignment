import re

def extract_unique_sorted_emails(file_path):
    # Regex pattern for valid emails (suggested by AI)
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                found = re.findall(email_pattern, line)
                emails.update(found)
    except FileNotFoundError:
        pass
    return sorted(emails)

# --- Test Cases ---
if __name__ == "__main__":
    # Create a sample log file for testing
    sample_content = """Support ticket: user1@example.com
Invalid: user@@example.com
Contact: admin@shop.com, helpdesk@shop.com
"""
    test_file = "sample_log.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(sample_content)

    result = extract_unique_sorted_emails(test_file)
    print(result)
    # Expected Output:
    # ["admin@shop.com", "helpdesk@shop.com", "user1@example.com"]