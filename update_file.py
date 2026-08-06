from datetime import datetime

FILE_NAME = "data.txt"

current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

with open(FILE_NAME, "a", encoding="utf-8") as file:
    file.write(f"Updated: {current_time}\n")

print("File updated successfully.")
