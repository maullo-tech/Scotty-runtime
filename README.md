# Scotty-runtime v8.3 – Emergent Governance Resonant Runtime

Scotty es un **runtime adaptativo para gestión dinámica de recursos en sistemas Linux**, orientado a la optimización continua de CPU mediante telemetría del sistema y políticas de control no estáticas.

El sistema implementa un modelo de control basado en un **estado interno dinámico (resonant field)** que influye en la selección de *CPU governors*, la priorización de procesos y las restricciones de consumo de recursos.

---

## 🧠 Objetivo del sistema

Scotty tiene como objetivo:

* Monitorizar el estado del sistema en tiempo real.
* Ajustar automáticamente políticas de CPU scaling (governors).
* Prevenir condiciones de sobrecarga térmica o energética.
* Redistribuir carga de procesos de forma dinámica.
* Mantener un estado operativo estable bajo variabilidad de carga.

---

## 🏗️ Arquitectura

El sistema está dividido en tres subsistemas principales:

### 1. `core/` – Control y gobernanza

Responsable de la lógica operativa del sistema:

* Recolección de métricas (`metrics.py`)
* Gestión de gobernadores de CPU (`governors.py`)
* Control de procesos (`processes.py`)
* Gestión de energía y límites (`power.py`)
* Políticas de seguridad (`safety.py`)
* Logging del sistema (`logger.py`)

---

### 2. `resonance/` – Modelo dinámico de estado

Implementa un **modelo de estado interno no lineal**, representado como un campo resonante.

* El sistema mantiene un conjunto de nodos dinámicos.
* Los nodos interactúan mediante acoplamiento de estado.
* El sistema clasifica estados globales como:

  * `chaotic`
  * `fragmented`
  * `metastable`
  * `harmonic`

Este estado influye en la selección de políticas de control del sistema.

Archivos:

* `resonant_field.py`
* `governor_attractor.py`

---

### 3. `topology/` – Reconfiguración estructural

Encargado de la adaptación estructural del sistema en tiempo de ejecución:

* Modela relaciones entre componentes como un grafo dinámico.
* Permite reconfiguración de interacciones entre módulos.
* Controla transiciones estructurales bajo restricciones de estabilidad.

Archivo:

* `morphogenesis.py`

---

### 4. `memory/` – Estado persistente

Gestiona memoria operativa y persistente del sistema:

* `runtime_memory.json`: estado reciente del sistema.
* `persistent_memory.py`: interfaz de lectura/escritura de memoria.

---

## 🔄 Flujo de operación

1. Recolección de métricas del sistema (CPU, GPU, RAM, temperatura, energía).
2. Actualización del campo resonante (`resonance`).
3. Evaluación del estado global del sistema.
4. Selección de política de CPU governor.
5. Aplicación de ajustes de:

   * frecuencia de CPU
   * prioridad de procesos
   * límites de energía/térmicos
6. Registro del estado en memoria y logs.

---

## 🧯 Mecanismos de seguridad

El sistema incluye **override determinista de seguridad**:

* Si la temperatura o consumo energético supera umbrales definidos:

  * Se fuerza el governor a `powersave`.
  * Se reduce prioridad de procesos de alto consumo.
  * Se limitan estados dinámicos del sistema.

Este mecanismo es independiente del estado resonante.

---

## ⚙️ Requisitos

* Linux (probado en Manjaro KDE)
* Python ≥ 3.9
* Herramientas del sistema:

  * `cpupower`
  * `lm-sensors`
  * soporte RAPL (si disponible)

### Dependencias Python

```bash
psutil
numpy
nvidia-ml-py
```

---

## 📦 Instalación

```bash
git clone https://github.com/maullo-tech/scotty.git
cd scotty

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

chmod +x install.sh
sudo ./install.sh
```

---

## 📊 Observabilidad

El sistema genera logs en:

```
logs/scotty_metrics.csv
```

Estos incluyen:

* métricas de hardware
* estados del sistema
* transiciones del campo resonante
* eventos de control

---

## 🔬 Modelo conceptual

Scotty se basa en la interacción entre:

* **Sistema físico observado** (hardware)
* **Modelo interno dinámico** (resonant field)
* **Controladores adaptativos** (governors)
* **Restricciones estructurales** (topology)

El comportamiento global emerge de la interacción entre estos subsistemas.

---

## 📚 Inspiración

El diseño de esta nueva versión de Scotty-runtime está inspirado en modelos de:

- sistemas dinámicos no lineales  
- control adaptativo basado en estados  
- optimización por exploración de configuraciones  
- dinámica de campos acoplados  

El proyecto incorpora ideas discutidas en conversaciones con Pablo Pacheco, relacionadas con sistemas adaptativos, resonancia y organización topológica de procesos en entornos complejos.

---

## 📄 Licencia

Este proyecto se distribuye bajo licencia **GNU General Public License v3.0 (GPL-3.0)**.

Esto permite:

* uso
* modificación
* redistribución

bajo la condición de mantener la misma licencia en trabajos derivados.

Para licencias comerciales o excepciones de distribución, contactar:

**[lignux-soluciones@gmx.com](mailto:lignux-soluciones@gmx.com)**

---

2026 Mauricio Ulloa
