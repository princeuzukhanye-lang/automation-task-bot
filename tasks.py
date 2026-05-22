from datetime import datetime
from logger import log_task

def run_task():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    message = f"Task executed at {now}"
    
    print(message)
    log_task(message)
