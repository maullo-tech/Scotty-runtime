#!/bin/bash
echo "=== Desinstalando Scotty v8.3 ==="
sudo systemctl stop scotty.service 2>/dev/null
sudo systemctl disable scotty.service 2>/dev/null
sudo rm -f /etc/systemd/system/scotty.service
sudo rm -rf /opt/scotty
echo "[+] Scotty v8.3 eliminado."
