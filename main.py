#!/usr/bin/env python3
import random, time, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import psutil
from core.power import power_meter
from core.gpu import GpuManager, calcular_fgpu
from core.governors import available_governors, current_governor, set_governor
from core.logger import init_logger, log_state
from core.safety import emergency_detected
from core.processes import detect_heavy_process, renice_process
from resonance.resonant_field import ResonantField
from topology.morphogenesis import topology_state, morphogenesis
from memory.persistent_memory import load_memory, save_memory, register_state
from resonance.governor_attractor import select_governor
import json

print("=== Scotty v8.3 – Emergent GPU-Aware Resonant Runtime ===")
with open('config.json') as f:
    config = json.load(f)
governors = available_governors()
print(f"[Scotty] Governors: {governors}")
memory = load_memory()
field = ResonantField(size=8)
init_logger()
gpu = GpuManager()
if gpu.available:
    print("[Scotty] GPU NVIDIA detectada.")
else:
    print("[Scotty] GPU NVIDIA no detectada o driver no accesible.")

annealing_temp = 1.0
last_heavy_pid = None
emergency_streak = 0

while True:
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    temp = 40.0
    try:
        out = subprocess.check_output(["sensors"]).decode()
        for line in out.splitlines():
            if "Package id 0" in line or "Tctl" in line:
                parts = line.split()
                for p in parts:
                    if "°C" in p:
                        temp = float(p.replace("+", "").replace("°C", ""))
    except Exception:
        pass

    loadavg = psutil.getloadavg()
    power_meter.update()
    power = power_meter.get_power_watts()
    if power is None or power < 5.0:
        power = round(cpu * 0.6 + ram * 0.2 + temp * 0.2, 2)

    gpu_temp_raw, gpu_usage_raw, _ = gpu.get_metrics()
    fgpu = calcular_fgpu(gpu_temp_raw, gpu_usage_raw) if gpu_temp_raw is not None else 1.0

    gpu_temp = gpu_temp_raw if gpu_temp_raw is not None else 40.0
    gpu_usage = gpu_usage_raw if gpu_usage_raw is not None else 0.0

    metrics = {
        "cpu": cpu, "ram": ram, "temp": temp, "power": power,
        "energy": power, "gpu_temp": gpu_temp, "gpu_usage": gpu_usage, "gpu_factor": fgpu
    }

    coherence = field.coherence()
    density = field.topology_density()
    avg_res = field.average_resonance()
    field_state = topology_state(density, coherence)
    rewrites = morphogenesis(field)
    current = current_governor()

    emergencia = emergency_detected(cpu, temp, loadavg, 4, 95, 85, 2.5)
    if emergencia:
        emergency_streak += 1
    else:
        emergency_streak = 0

    if emergency_streak >= 2:
        target = "powersave"
        print("\n[Scotty] Emergency state - Forzando powersave")
    else:
        target = select_governor(field, governors, current, annealing_temp)

    if target != current:
        print(f"[Scotty] {current} -> {target}")
        set_governor(target)

    heavy = detect_heavy_process()
    if heavy and heavy['pid'] != last_heavy_pid:
        print(f"\n[Scotty] Process {heavy['name']} (PID {heavy['pid']}) controlado")
        if heavy['nice'] < 10:
            renice_process(heavy['pid'])
        last_heavy_pid = heavy['pid']

    register_state(memory, {"coherence": coherence, "density": density, "state": field_state})
    save_memory(memory)
    log_state(metrics, target, coherence, density, field_state)

    print("\n-------------------")
    print(f"CPU: {cpu}%")
    print(f"RAM: {ram}%")
    print(f"TEMP: {temp}°C")
    print(f"POTENCIA: {power} W")
    print(f"GPU TEMP: {gpu_temp}°C  GPU USO: {gpu_usage}%  GPU FACTOR: {round(fgpu, 2)}")
    print(f"FIELD STATE: {field_state}")
    print(f"COHERENCE: {coherence}")
    print(f"DENSITY: {density}")
    print(f"AVG RESONANCE: {avg_res}")
    print(f"NODES: {len(field.nodes)}")
    print(f"NETWORK LINKS: {sum(len(n.links) for n in field.nodes)}")
    print(f"TOPOLOGY REWRITES: {rewrites}")
    print(f"GOVERNOR: {target}")
    print(f"ANNEALING TEMP: {round(annealing_temp,2)}")

    field.evolve(annealing_temp, fgpu)
    annealing_temp += random.uniform(-0.05, 0.05)
    annealing_temp = max(0.1, min(annealing_temp, 2.0))
    time.sleep(4)