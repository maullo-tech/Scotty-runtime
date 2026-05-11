#!/bin/bash
set -e

INSTALL_DIR="/opt/scotty"
echo "=== Scotty v8.3 – Instalador ==="

echo "[*] Copiando archivos a $INSTALL_DIR..."
sudo mkdir -p "$INSTALL_DIR"
sudo cp -r . "$INSTALL_DIR"
sudo chown -R root:root "$INSTALL_DIR"

cd "$INSTALL_DIR"
python3 -m venv venv
source venv/bin/activate
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi
deactivate

# Script de arranque
cat << 'EOS' | sudo tee "$INSTALL_DIR/start.sh" > /dev/null
#!/bin/bash
cd /opt/scotty
source venv/bin/activate
python main.py
EOS
sudo chmod +x "$INSTALL_DIR/start.sh"

# Servicio systemd
read -p "¿Instalar servicio systemd para iniciar con el sistema? (s/N): " resp
if [[ "$resp" =~ ^[sS]$ ]]; then
    echo "[*] Instalando servicio systemd..."
    cat << EOSD | sudo tee /etc/systemd/system/scotty.service > /dev/null
[Unit]
Description=Scotty v8.3 – Emergent GPU‑Aware Resonant Runtime
After=multi-user.target

[Service]
Type=simple
User=root
WorkingDirectory=$INSTALL_DIR
ExecStart=$INSTALL_DIR/venv/bin/python $INSTALL_DIR/main.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOSD
    sudo systemctl daemon-reload
    sudo systemctl enable scotty.service
    echo "[+] Servicio instalado. Para iniciar: sudo systemctl start scotty"
fi

echo "=== Instalación completada ==="
echo "Para ejecutar: sudo $INSTALL_DIR/start.sh"
