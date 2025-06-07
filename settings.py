import json
import os

ROOT_DIR = os.path.expanduser("~/.pl")
os.makedirs(ROOT_DIR, exist_ok=True)


DEFAULT_CONFIG = {
    "ip": "192.168.50.1",
    "username": "admin",
    "password": "DT$pi@7519",
    "interval": 30,  # Fetching interval in seconds
    "retention_days": 30,  # Number of days to keep historical data
}

CONFIG_FILE = os.path.join(ROOT_DIR, "config.json")
if not os.path.exists(CONFIG_FILE):
    print("No config found! Creating the default one...")
    with open(CONFIG_FILE, "w") as jp:
        json.dump(DEFAULT_CONFIG, jp, indent=2)


API_TIMEOUT = 5

APP_DIR = os.path.dirname(os.path.realpath(__file__))

CRASH_FILE = os.path.join(ROOT_DIR, "crash.dump")

TB_PROVISION_KEY = "vdaqr94sbwi73kk99852"
TB_PROVISION_SECRET = "bign9911autaf0rg8vez"
TB_SERVER_URL = "http://tracker.mobilelinq.com:8080"

INIT_SCREEN = "overview"  # Initial screen to show

try:
    from local_settings import *
except ImportError:
    pass
