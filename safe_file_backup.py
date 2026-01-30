import shutil
from datetime import datetime
from pathlib import Path

def backup_file(file_path):
    path = Path(file_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{path.stem}_backup_{timestamp}{path.suffix}"

    shutil.copy(file_path, backup_name)
    return backup_name


if __name__ == "__main__":
    print(backup_file("example.txt"))
