import shutil
import pyuac
import glob
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

file_path = "C:\\Users\\User\\Downloads"
storage_path = "D:\\Storage\\Downloads\\"

class FileHandler(FileSystemEventHandler):
    def on_created(self, event: FileSystemEvent) -> None:
        file = event.src_path.strip()
        file_type = file[file.rfind("."):].replace(".", "")
        if not os.path.exists(storage_path + file_type):
            os.mkdir(storage_path + file_type)
        shutil.move(file, storage_path + file_type + file.replace(file_path, ""))

def main():
    for file in glob.glob(file_path + "\\*.*"):
        file_type = file[file.rfind("."):].replace(".", "")
        if not os.path.exists(storage_path + file_type):
            os.mkdir(storage_path + file_type)
        shutil.move(file.strip(), storage_path + file_type + file.strip().replace(file_path, ""))

    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler=event_handler, path=file_path, recursive=False)
    observer.start()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            observer.stop()

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Restarting as Admin...")
        pyuac.runAsAdmin()
    else:
        main()