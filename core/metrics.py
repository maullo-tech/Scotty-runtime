import psutil
import subprocess

def get_temperature():
    try:
        output = subprocess.check_output(["sensors"]).decode()
        for line in output.splitlines():
            if "Package id 0" in line or "Tctl" in line:
                parts = line.split()
                for p in parts:
                    if "°C" in p:
                        return float(p.replace("+", "").replace("°C", ""))
    except:
        pass
    return None

def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    temp = get_temperature()
    if temp is None:
        temp = 40.0  # fallback conservador
    energy = cpu * 0.6 + ram * 0.2 + temp * 0.2  # placeholder hasta integrar RAPL
    return {
        "cpu": cpu,
        "ram": ram,
        "temp": temp,
        "energy": round(energy, 2)
    }
