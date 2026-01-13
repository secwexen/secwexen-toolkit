import os


def file_exists(path: str) -> bool:
    return os.path.isfile(path)


def read_file(path: str) -> str:
    if not file_exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
