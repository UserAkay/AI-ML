import re

text = input("Enter your text: ")

# Regex pattern to match email addresses
email_pattern = r"[\w\.+-]+@[\w-]+\.[\w\.-]+"

emails = re.findall(email_pattern, text)
print("Emails found:", emails)

# Replace all email addresses with [REDACTED]
replaced_text = re.sub(email_pattern, "[REDACTED]", text)
print("Text after replacement:", replaced_text)
