import datetime
import json

class Log:
    message: str = "default"

    def full(self) -> str:
        return f"[{datetime.datetime.now()}] {self.message}"


def write_log(
        file: str, 
        log: Log
    ):
    with open(file, "a") as f:
        f.write(log.full())


def main():
    print("Hello World!")
    
if __name__ == "__main__":
    main()
