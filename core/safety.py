def emergency_detected(cpu, temp, loadavg, cores,
                       cpu_emerg=95, temp_emerg=85, load_per_core=2.5):
    if temp is not None and temp >= temp_emerg:
        return True
    if cpu >= cpu_emerg:
        return True
    if loadavg[0] >= cores * load_per_core:
        return True
    return False
