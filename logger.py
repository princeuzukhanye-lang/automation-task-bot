def log_task(message):
    with open("logs.txt", "a") as file:
        file.write(message + "\n")
