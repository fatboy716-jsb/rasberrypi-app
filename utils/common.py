import json
import os
import platform
import subprocess
import threading

from settings import CONFIG_FILE
from utils.logger import logger

is_rpi = platform.system() == "Linux" and os.path.exists("/proc/device-tree/model")


def disable_screen_saver():
    if is_rpi:
        os.system('sudo sh -c "TERM=linux setterm -blank 0 >/dev/tty0"')


def get_serial():
    """
    Get serial number of the device
    :return:
    """
    if is_rpi:
        cpuserial = "0000000000000000"
        f = open("/proc/cpuinfo", "r")
        for line in f:
            if line.startswith("Serial"):
                cpuserial = line[10:26].lstrip("0")
        f.close()
        return cpuserial[-8:]
    else:
        return "12345678"


def drop_cache():
    """Drop system cache to free memory"""
    if is_rpi:
        try:
            subprocess.run(["sync"], check=True)
            with open("/proc/sys/vm/drop_caches", "w") as f:
                f.write("3")
        except Exception as e:
            logger.error(f"Error dropping cache: {str(e)}")


def kill_process_by_name(proc_name, use_sudo=False, sig=None):
    """Kill process by name"""
    try:
        if platform.system() == "Windows":
            subprocess.run(["taskkill", "/F", "/IM", proc_name], check=True)
        else:
            cmd = ["pkill"]
            if sig:
                cmd.extend(["-SIGTERM"])
            if use_sudo:
                cmd.insert(0, "sudo")
            cmd.append(proc_name)
            subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Error killing process {proc_name}: {str(e)}")


_c_lock = threading.Lock()


def update_dict_recursively(dest, updated):
    """
    Update dictionary recursively.
    :param dest: Destination dict.
    :type dest: dict
    :param updated: Updated dict to be applied.
    :type updated: dict
    :return:
    """
    for k, v in updated.items():
        if isinstance(dest, dict):
            if isinstance(v, dict):
                r = update_dict_recursively(dest.get(k, {}), v)
                dest[k] = r
            else:
                dest[k] = updated[k]
        else:
            dest = {k: updated[k]}
    return dest


def update_config_file(data):
    old_data = update_dict_recursively(dest=get_config(), updated=data)
    with _c_lock:
        with open(CONFIG_FILE, "w") as jp:
            json.dump(old_data, jp, indent=2)


def get_config():
    with _c_lock:
        try:
            conf = json.loads(open(CONFIG_FILE).read())
        except Exception as e:
            logger.error(f"Failed to read config file ({e})")
            conf = {}
    return conf
