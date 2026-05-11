import subprocess
import warnings
warnings.filterwarnings("ignore")

def calcular_fgpu(t_gpu: float, u_gpu: float, t_th: float = 40.0, delta_t: float = 30.0, f_max: float = 2.0) -> float:
    perturbacion_temp = 1.0 + ((t_gpu - t_th) / delta_t) * (f_max - 1.0)
    perturbacion_uso = 1.0 + (u_gpu / 100.0) * (f_max - 1.0)
    return max(1.0, perturbacion_temp, perturbacion_uso)

class GpuManager:
    def __init__(self):
        self.available = False
        self.handle = None
        try:
            import pynvml
            pynvml.nvmlInit()
            self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            self.available = True
        except Exception:
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
        except Exception:
            try:
                out = subprocess.check_output(["nvidia-smi", "--query-gpu=temperature.gpu,utilization.gpu", "--format=csv,noheader"], text=True)
                parts = out.strip().split(',')
                temp = float(parts[0].strip())
                usage = float(parts[1].replace('%','').strip())
                return temp, usage, None
            except Exception:
                return None, None, None