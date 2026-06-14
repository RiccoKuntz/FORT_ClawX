# FEHLERLÖSUNGSBERICHT - 06-06-2026 18:05

## AUFRÄUM-AUSFÜHRUNG

### Sessions
| Session | Status | Aktion |
|---------|--------|--------|
| Subagent 9ac693a0 (4d alt, aborted) | ✅ Gelöscht | Trajectory-Dateien + sessions.json Eintrag |
| Main Session (5d alt, qwen3.5-9b) | ✅ Gelöscht | Trajectory-Dateien + sessions.json Eintrag |
| Aktuelle Telegram-Session | ⏭️ Behalten | Aktiv, kann nicht gelöscht werden |

**Verbleibend:** 1 Session (aktive Telegram-Session)
**sessions.json:** Bereinigt (2 Einträge entfernt)

---

## HAUPTPROBLEME & LÖSUNGSVORSCHLÄGE

### 1. Device Timeout bei Boot (UUID 83a625d2-...)
**Schwere:** Mittel | **Häufigkeit:** Bei JEDEM Boot
**Problem:** systemd wartet auf eine nicht existierende Partition → Boot-Verzögerung

**Ursache:** Eine Disk/Partition mit UUID `83a625d2-74c8-463d-bb27-bb094f5ad15d` ist nicht vorhanden.
- Mögliche Ursachen: Alte Live-USB-Partition, entfernte Platte, oder UUID hat sich geändert

**Lösungsvorschläge:**

**Option A – Eintrag aus /etc/fstab entfernen (empfohlen):**
```bash
# 1. UUID des missing device identifizieren
cat /etc/fstab | grep 83a625d2

# 2. Kommentarzeichen # davor setzen ODER Eintrag löschen
sudo sed -i 's/.*83a625d2.*/# &/' /etc/fstab

# 3. System neu starten
sudo reboot
```

**Option B – systemd-Service ignorieren lassen:**
```bash
# Device-Unit deaktivieren falls vorhanden
sudo systemctl mask dev-disk-by\x2duuid-83a625d2\x2d74c8\x2d463d\x2dbb27\x2dbb094f5ad15d.device
```

**Prüfen nach Fix:**
```bash
systemd-analyze blame | head -20  # Zeigt Boot-Dauer pro Service
```

---

### 2. gkr-pam Keyring nicht entsperrbar
**Schwere:** Mittel | **Häufigkeit:** Bei JEDEM Login
**Problem:** GNOME Keyring kann beim Login nicht entsperrt werden → Passwort-Manager funktioniert nicht

**Ursache:** GNOME Keyring ist installiert/konfiguriert, aber der Login-Schlüsselbund wurde entweder nie eingerichtet oder das Passwort wurde zurückgesetzt.

**Lösungsvorschläge:**

**Option A – Keyring zurücksetzen (einfachste Lösung):**
```bash
# 1. Keyring-Verzeichnis umbenennen
mv ~/.local/share/keyring/ ~/.local/share/keyring.old

# 2. Neu starten
# Beim nächsten Login wird ein neuer Keyring erstellt
# Man wird nach einem neuen Passwort gefragt (kann leer sein = kein Passwort)
```

**Option B – Keyring mit Login-Passwort verknüpfen:**
```bash
# 1. pam-gnome-keyring installieren (falls nicht vorhanden)
sudo apt install gnome-keyring

# 2. Autostart prüfen
ls ~/.config/autostart/ | grep keyring

# 3. Neues Keyring-Passwort setzen
 Seahorse (Password and Keys) → "Login" → Rechtsklick → "Change Password"
```

**Option C – Keyring komplett deaktivieren (wenn nicht benötigt):**
```bash
# Autostart-Datei deaktivieren
mv ~/.config/autostart/gnome-keyring-pw-autostart.desktop ~/.config/autostart/gnome-keyring-pw-autostart.desktop.disabled
```

---

### 3. Xorg Crash (30. Mai)
**Schwere:** Mittel | **Häufigkeit:** Einmalig
**Problem:** Xorg Server abgestürzt → möglicherweise Display/Session verloren

**Ursache:** Intel GM45 Grafiktreiber (i915) auf altem Hardware-Chipset (Penryn) kann unter bestimmten Bedingungen instabil sein.

**Lösungsvorschläge:**

**Option A – Kernel-Parameter für i915 optimieren:**
```bash
# /etc/default/grub bearbeiten
sudo nano /etc/default/grub

# GRUB_CMDLINE_LINUX_DEFAULT Zeile anpassen:
# Vorher: "quiet splash"
# Nachher: "quiet splash i915.enable_rc6=0 i915.enable_fbc=1"

# grub aktualisieren
sudo update-grub
sudo reboot
```

**Option B – Alternative Desktop-Umgebung testen:**
```bash
# XFCE ist ressourcenschonender und stabiler auf alter Hardware
sudo apt install xfce4
# Beim Login: "XFCE" statt "Cinnamon" auswählen
```

**Prüfen:**
```bash
# Xorg-Logs auf wiederkehrende Fehler prüfen
grep -i "error\|crash\|fail" /var/log/Xorg.0.log
```

---

## ZUSÄTZLICHE KLEINERE PROBLEME

### 4. casper-md5check.service
**Problem:** Live-ISO-Prüfdienst auf installiertem System → nutzlos
**Lösung:**
```bash
sudo systemctl disable casper-md5check.service
sudo systemctl mask casper-md5check.service
```

### 5. pam_lastlog.so fehlt
**Problem:** PAM-Modul für Login-Logging nicht gefunden
**Lösung:**
```bash
sudo apt install libpam-lastlog
# ODER: Eintrag in /etc/pam.d/common-session entfernen
```

### 6. OpenClaw Update verfügbar
**Aktuell:** 2026.5.28 | **Neu:** 2026.6.1
**Lösung:**
```bash
openclaw update
```

### 7. smartctl nicht installiert
**Problem:** Kein SSD-Health-Check möglich
**Lösung:**
```bash
sudo apt install smartmontools
sudo smartctl -a /dev/sda  # SSD-Health prüfen
```

---

## EMPFOHNE REIHENFOLGE DER LÖSUNG

1. **casper-md5check** deaktivieren (2 Min, keine Risiken)
2. **Device Timeout** aus /etc/fstab entfernen (5 Min, Boot-Verzögerung weg)
3. **Keyring** zurücksetzen (5 Min, Passwort-Manager funktioniert wieder)
4. **OpenClaw updaten** (2 Min)
5. **smartmontools** installieren + SSD-Health prüfen (2 Min)
6. **pam_lastlog** installieren (1 Min)
7. **Xorg-Parameter** optimieren (falls Xorg wieder crasht)

**Gesamtaufwand:** ~15 Minuten
