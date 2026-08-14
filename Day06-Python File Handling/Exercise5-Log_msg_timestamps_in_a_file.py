from datetime import datetime


def log_message(filename, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"[{timestamp}] {message}\n")
    print(f"Logged: [{timestamp}] {message}")


print("Log messages with timestamps into a file.")
print("Type 'exit' to quit.")

filename = input("Enter the log file name: ")
while True:
    message = input("Enter your message: ")
    if message.lower() == "exit":
        print("Exiting logger.")
        break
    log_message(filename, message)
