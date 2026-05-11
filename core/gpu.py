# core/gpu.py – Monitoreo de GPU NVIDIA (temperatura y uso por nvidia-smi)
import subprocess
import warnings
warnings.filterwarnings("ignore")

class GpuManager:
    def __init__(self):
        self.available = False
        try:
            import pynvml
            pynvml.nvmlInit()
            self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            self.available = True
        except:
            pass

    def get_metrics(self):
        if not self.available:
            return None, None, None
        try:
            import pynvml
            temp = pynvml.nvmlDeviceGetTemperature(self.handle, pynvml.NVML_TEMPERATURE_GPU)
            utilization = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
            usage = utilization.gpu
            power_mW = pynvml.nvmlDeviceGetPowerUsage(self.handle)
            power = power_mW / 1000.0 if power_mW is not None else None
            return temp, usage, power
        except:
            # fallback con nvidia-smi
            try:
                out = subprocess.check_output(["nvidia-smi", "--query-gpu=temperature.gpu,utilization.gpu", "--format=csv,noheader"], text=True)
                parts = out.strip().split(',')
                temp = float(parts[0].strip())
                usage = float(parts[1].replace('%','').strip())
                return temp, usage, None
            except:
                return None, None, None
