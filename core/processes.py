import psutil
import os

SCOTTY_PID = os.getpid()

def get_top_processes(limit=10):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'nice']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    processes.sort(key=lambda p: p['cpu_percent'], reverse=True)
    return processes[:limit]

def detect_heavy_process(cpu_limit=50.0, mem_limit=35.0):
    processes = get_top_processes()
    for proc in processes:
        if proc['pid'] == SCOTTY_PID:
            continue
        if proc['pid'] < 100 or (proc['name'] or '').startswith('idle_inject'):
            continue
        if proc['nice'] >= 10:
            continue
        if proc['cpu_percent'] > cpu_limit or proc['memory_percent'] > mem_limit:
            return proc
    return None

def renice_process(pid, nice_value=10):
    try:
        proc = psutil.Process(pid)
        proc.nice(nice_value)
        return True
    except Exception as e:
        print(f"[Scotty] Error al renice: {e}")
        return False
