# Scotty v8.3 – Emergent Governance Resonant Runtime

Scotty es un **runtime adaptativo** que gestiona automáticamente el modo de funcionamiento de la CPU en Linux.

No usa reglas fijas. En su interior, un **campo resonante de 8 nodos** evoluciona y se reorganiza solo. La decisión de qué governor usar **emerge** de ese campo, sin que nadie la programe.

---

## 🧠 ¿Qué hace?

- Monitorea CPU, GPU, RAM, temperatura y potencia eléctrica (RAPL).
- Mantiene un campo dinámico con nodos, frecuencias y fases que se acoplan por resonancia.
- Detecta estados globales del campo (chaotic, fragmented, meta‑stable, harmonic) y elige el governor más apropiado mediante **atractores emergentes**.
- Protege el hardware forzando `powersave` si la temperatura, la carga o la potencia superan límites seguros.
- Controla procesos que acaparan recursos (renice automático).
- Guarda memoria de los últimos 100 estados del campo resonante.

---

## 🔬 Inspiración

Este proyecto está profundamente inspirado por las ideas de **Pablo Pacheco** sobre optimización mediante exploración periódica de configuraciones y por los principios de los **sistemas físicos resonantes**. Lo que en la teoría es un mecanismo de dinámica no lineal, acá se traduce en un runtime que siente, vibra y se adapta en tiempo real.

---

## ⚙️ Requisitos

- Linux (probado en Manjaro KDE)
- Python 3.9 o superior
- `cpupower`, `lm-sensors` (para leer temperatura y cambiar governors)
- Paquetes Python: `psutil`

---

## 📦 Instalación

```bash
git clone https://github.com/maullo-tech/scotty.git
cd scotty
chmod +x install.sh
sudo ./install.sh

# scotty
## 📄 Licencia

Este proyecto se distribuye bajo la licencia **GNU General Public License v3.0 (GPL‑3.0)**.  
Esto significa que podés usar, modificar y distribuir el código libremente, pero cualquier trabajo derivado debe mantener la misma licencia y compartir su código fuente.

Si necesitás una licencia comercial (sin obligación de liberar el código), contactame a: *lignux-soluciones@gmx.com*.

© 2026 Mauricio Ulloa
