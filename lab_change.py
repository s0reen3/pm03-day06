"""Меняет только подготовленный учебный config.txt."""
from pathlib import Path
import sys
p = Path(__file__).with_name("config.txt")
settings = dict(line.split("=", 1) for line in p.read_text().splitlines() if line)
mode = sys.argv[1]
if mode == "early":
    settings["support_hours"] = "08:30-17:00"
elif mode == "late":
    settings["support_hours"] = "09:00-18:00"
elif mode == "bad":
    settings["response_minutes"] = "0"
else:
    raise SystemExit("Используйте early, late или bad")
p.write_text("\n".join(f"{key}={value}" for key, value in settings.items()) + "\n")
print(p.read_text())
