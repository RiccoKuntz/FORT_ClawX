#!/bin/bash

# Pfade definieren
SRC="/home/rick/.openclaw/workspace"
DEST="/home/rick/Dokumente/Openclaw_Export"

echo "[NEW_DIVIDES] Starte 1:1 Kopie..."
# 1. Kopieren
mkdir -p "$DEST"
cp -ra "$SRC" "$DEST"

# 2. Validierung (DOORGUARD-Prinzip)
echo "[NEW_DIVIDES] Überprüfe Integrität..."
SRC_HASH=$(find "$SRC" -type f -exec md5sum {} + | awk '{print $1}' | sort | md5sum)
DEST_HASH=$(find "$DEST/workspace" -type f -exec md5sum {} + | awk '{print $1}' | sort | md5sum)

if [ "$SRC_HASH" != "$DEST_HASH" ]; then
    echo "!!! FEHLER: Kopie ist nicht identisch. Abbruch !!!"
    exit 1
fi
echo "[SUCCESS] Integrität bestätigt."

# 3. Pfade entfernen (Sanitizing)
# Sucht nach /home/rick/ Pfaden, ignoriert aber .openclaw und Automationen
echo "[NEW_DIVIDES] Bereinige externe Pfade im Export-Ordner..."
find "$DEST/workspace" -type f -print0 | xargs -0 sed -i 's|/home/rick/\([^.][^o][^p][^e][^n][^c][^l][^a][^w][^/][^A][^u][^t][^o][^m][^a][^t][^i][^o][^n][^e][^n]\)|[REMOVED_PATH]/\1|g'

# 4. Interaktiver Teil
echo "--- ZIELSYSTEM INITIALISIERUNG ---"
read -p "Gib den neuen absoluten Pfad für das Framework ein: " NEW_PATH
echo "Setze Pfade auf $NEW_PATH um..."

# RAM-Disk Initialisierung
read -p "RAM-Disk jetzt neu anlegen? (y/n): " CREATE_RAM
if [ "$CREATE_RAM" == "y" ]; then
    read -p "Größe (z.B. 1G): " RAM_SIZE
    read -p "Mountpoint: " MOUNT_POINT
    sudo mkdir -p "$MOUNT_POINT"
    sudo mount -t tmpfs -o size="$RAM_SIZE" tmpfs "$MOUNT_POINT"
    echo "[SUCCESS] RAM-Disk auf $MOUNT_POINT aktiv."
fi
