import time
import os

class PowerMeter:
    def __init__(self):
        self.rapl_path = None
        base = "/sys/class/powercap"
        if os.path.exists(base):
            for entry in os.listdir(base):
                if entry.startswith("intel-rapl:"):
                    full = os.path.join(base, entry, "energy_uj")
                    if os.path.exists(full):
                        self.rapl_path = os.path.join(base, entry)
                        break
        self.last_energy = None
        self.last_time = None
        self.cached_power = None  # para devolver un valor estable entre actualizaciones

    def _read_energy_uj(self):
        if not self.rapl_path:
            return None
        try:
            with open(os.path.join(self.rapl_path, "energy_uj"), "r") as f:
                return int(f.read().strip())
        except Exception:
            return None

    def update(self):
        """Actualiza la medición de potencia. Debe llamarse en cada ciclo."""
        energy = self._read_energy_uj()
        if energy is None:
            self.cached_power = None
            return
        now = time.time()
        if self.last_energy is None:
            self.last_energy = energy
            self.last_time = now
            self.cached_power = None
            return
        delta_uj = energy - self.last_energy
        delta_s = now - self.last_time
        self.last_energy = energy
        self.last_time = now
        if delta_s > 0.5 and delta_uj > 0:
            self.cached_power = round(delta_uj / (delta_s * 1_000_000), 2)
        else:
            self.cached_power = None

    def get_power_watts(self):
        """Devuelve la última potencia calculada, o None si no hay dato."""
        return self.cached_power

power_meter = PowerMeter()
