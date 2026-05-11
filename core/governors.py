import os

CPU_PATH = "/sys/devices/system/cpu"

def available_governors():
    try:
        with open(
            f"{CPU_PATH}/cpu0/cpufreq/scaling_available_governors"
        ) as f:
            return f.read().strip().split()

    except:
        return []

def current_governor():
    try:
        with open(
            f"{CPU_PATH}/cpu0/cpufreq/scaling_governor"
        ) as f:
            return f.read().strip()

    except:
        return "unknown"

def set_governor(governor):

    cpus = [
        cpu for cpu in os.listdir(CPU_PATH)
        if cpu.startswith("cpu") and cpu[3:].isdigit()
    ]

    for cpu in cpus:

        path = (
            f"{CPU_PATH}/{cpu}/cpufreq/scaling_governor"
        )

        try:
            with open(path,"w") as f:
                f.write(governor)

            print(f"Setting {cpu}")

        except Exception as e:
            print(f"Error {cpu}: {e}")
