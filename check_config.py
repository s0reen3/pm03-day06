from pathlib import Path
import sys
text = Path(__file__).with_name("config.txt").read_text()
if any(marker in text for marker in ("<<<<<<<", "=======", ">>>>>>>")):
    raise SystemExit("FAIL: в файле остались маркеры конфликта")
settings = dict(line.split("=", 1) for line in text.splitlines() if line)
if int(settings["response_minutes"]) <= 0:
    raise SystemExit("FAIL: response_minutes должен быть положительным")
start, end = settings["support_hours"].split("-")
if not start < end:
    raise SystemExit("FAIL: окончание должно быть позже начала")
if "--combined" in sys.argv and settings["support_hours"] != "08:30-18:00":
    raise SystemExit("FAIL: не объединены оба требования EARLY и LATE")
print("PASS: конфигурация соответствует выбранной проверке")
