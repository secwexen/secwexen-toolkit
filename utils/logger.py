from datetime import datetime

def _timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_info(message: str):
    print(f"[INFO] [{_timestamp()}] {message}")


def log_warning(message: str):
    print(f"[WARNING] [{_timestamp()}] {message}")


def log_error(message: str):
    print(f"[ERROR] [{_timestamp()}] {message}")
