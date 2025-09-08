import random

def ai_loan_approval(applicant_name):
    # Simulate AI logic (for demonstration, randomly approve or deny)
    # In a real scenario, this would be replaced with actual AI model logic
    approval = random.choice(["Approved", "Denied"])
    print(f"Loan approval for {applicant_name}: {approval}")

# Test with different names
names = ["John", "Priya", "Ahmed", "Maria", "Wei", "Fatima"]
for name in names:
    ai_loan_approval(name)