# HWINFO ThinkPad T400 & Installationsübersicht (v3.0.0)

---

## 🖥️ Hardware

### System & BIOS
- **Modell:** LENOVO ThinkPad T400 (6475G68)
- **BIOS:** 3.24 (2012-10-17)

### CPU
- **Modell:** Intel Core2 Duo P8400 (Penryn)
- **Kerne:** 2 Cores | 64-bit
- **Takt:** 800–2267 MHz
- **Cache:** 3 MiB L2
- **Flags:** vmx, sse4_1, nx, pae, lm

### Grafik & Display
- **GPU:** Intel Mobile 4 Series (GM45 Express)
- **Treiber:** i915 (Mesa 25.2.8)
- **Monitor:** 14.1" LVDS (1280×800 @ 107 dpi)
- **APIs:** OpenGL 4.5, Vulkan 1.3.275, EGL 1.5 (Crocus)

### Speicher & Laufwerke
- **RAM:** 8 GB (7.65 GB verfügbar)
- **Swap:** 8 GB File
- **SSD:** 111.8 GiB Intenso SSD (/dev/sda) | SATA 3.0 Gb/s
- **HDD:** 1.82 TiB Seagate ST2000LM007 (/dev/sdb) | SATA 3.0 Gb/s
- **Partitionen:** `/` (ext4) 109 GiB | `/boot/efi` (vfat) 512 MiB

### Netzwerk & Audio
- **LAN:** Intel 82567LM Gigabit (e1000e) | Status: Up (1000 Mbps)
- **WLAN:** Qualcomm Atheros AR242x/AR542x (ath5k) | Status: Down
- **Audio:** Intel 82801I HD Audio | Server: PipeWire 1.0.5 / WirePlumber
- **Bluetooth:** Bluetooth 5.72 | blueman 2.4.4

---

## 🐧 Software & OS

### System & OS
- **Modell:** LENOVO ThinkPad T400 (6475G68) | BIOS: 3.24 (2012-10-17)
- **OS:** Linux Mint 22.3 Zena (Ubuntu 24.04 noble)
- **Kernel:** 6.17.0-35-generic
- **Desktop:** Cinnamon 6.6.7 | WM: Muffin | Display: X.Org 21.1.11 / Xwayland 23.2.6
- **Shell:** Bash 5.2.21 | Compiler: GCC 13.3.0

### Paketübersicht
| Quelle | Anzahl |
|--------|--------|
| dpkg (apt) | 2440 Pakete |
| Flatpak-Apps | 6 |
| Flatpak-Runtimes | 9 |
| pip3-Pakete | ~100 |
| npm-global | 2 |
| Snap | 0 (nicht installiert) |

---

## 🖥️ Desktop & Window Manager

- **Desktop:** Cinnamon 6.6.7
- **WM:** Muffin / Metacity
- **Dateimanager:** Nemo 6.6.3

---

## 🌐 Browser

- **Firefox** 151.0.4 (linuxmint1+zena)
- **Falkon** 24.01.75
- **Epiphany** 46.5
- **Brave** (Flatpak) 1.91.171

---

## 💬 Messenger & Chat

- **Telegram Desktop** (Flatpak) 6.8.2

---

## 📧 E-Mail & Kalender

- **Thunderbird** 140.11.1esr (linuxmint1+zena)
- **Evolution Data Server** 3.52.3

---

## 📦 Flatpak-Apps

| App | Version | Channel |
|-----|---------|---------|
| Brave Browser | 1.91.171 | stable / flathub |
| Touché (Touchpad-Tuning) | 2.0.15 | stable / flathub |
| ClamUI | 0.2.0 | stable / flathub |
| Gearlever | 4.5.4 | stable / flathub |
| Resources (System-Monitor) | 1.10.2 | stable / flathub |
| Telegram Desktop | 6.8.2 | stable / flathub |

### Flatpak-Runtimes
- freedesktop-sdk 25.08
- GNOME 49, 50
- GTK 3.22

---

## 🔧 Entwicklung & Programmierung

### Compiler & Build
- **GCC** 13.3.0 | **G++** 13.3.0
- **CMake** 3.28.3
- **GDB** 15.1
- **make** 4.3
- **DKMS** 3.0.11

### Sprache & Laufzeiten
- **Python** 3.12.3
- **Node.js** 22.22.3 (nodesource)
- **npm** 10.9.8 | **corepack** 0.34.6
- **pip** 24.0

### Version Control
- **Git** 2.43.0

### Qt (5 + 6)
- Qt5: 5.15.13 (WebEngine 5.15.16)
- Qt6: 6.4.2

---

## 🐍 Wichtige pip3-Pakete

beautifulsoup4, lxml, cryptography, requests, rich, Pygments, PyYAML, Pillow, mutagen, yt-dlp, websockets, pyudev, netifaces, psutil, filelock, markdown-it-py, pycryptodomex, PyNaCl, pyinotify, pyelftools, pyatspi, python-gnupg, pyxdg, xlrd, tldextract, oauthlib, pyjwt, pyparsing, packaging

---

## 🛡️ Sicherheit

- **ClamAV** 1.4.4 (Daemon + FreshClam)
- **Gufw** 24.04.0 (Firewall-UI)
- **UFW** 0.36.2
- **AppArmor** 4.0.1
- **GnuPG** 2.4.4
- **KeepassXC** 2.7.6 (Passwort-Manager)
- **Fprintd** 1.94.3 (Fingerabdruck)
- **fwupd** 2.0.20 (Firmware-Updates)
- **Bolt** 0.9.7 (Thunderbolt)

---

## 🖨️ Drucken & Scan

- **CUPS** 2.4.7
- **HPLIP** 3.23.12
- **Printer-Driver:** brlaser, foo2zjs, gutenprint, hpcups, splix, min12xxw, pnm2ppa, ptouch, pxljr, sag-gdi
- **ipp-usb** 0.9.24

---

## 📁 Dateimanager & Dateisystem

- **Nemo** 6.6.3 (+ emblems, fileroller, preview, share)
- **GParted** 1.5.0
- **File Roller** (Archiv-Manager) 43.0
- **dconf-editor** 45.0.1
- **Dateisystem-Unterstützung:** btrfs, exfat(fuse), ntfs-3g, fuse3
- **gvfs** 1.54.4

---

## 🎵 Multimedia

- **Audio-Server:** PipeWire 1.0.5 | WirePlumber 0.4.17
- **ALSA:** 1.2.9
- **GStreamer** 1.24.2 (Plugins: base, good, bad, ugly, libav, vaapi)
- **Celluloid** (MPV-Wrapper) 0.21
- **Drawing** (Zeichenprogramm) 1.0.2
- **Blueman** 2.4.4 (Bluetooth-Manager)

---

## 🔍 System-Tools

- **btop** 1.3.0 (System-Monitor)
- **htop** 3.3.0
- **inxi** 3.3.34
- **neofetch** 7.1.0
- **curl** 8.5.0
- **wget** 1.21.4
- **tmux** 3.4
- **rsync** 3.2.7
- **jq** 1.7.1
- **lm-sensors** 1:3.6.0
- **hdparm** 9.65
- **smartmontools** 7.4
- **ethtool** 6.7
- **lsof** 4.95
- **7zip / p7zip-full** 16.02 / 23.01

---

## 📝 Büro & Dokumente

- **LibreOffice** 24.2.7 (Writer, Calc, Impress, Draw)
- **Evince** (PDF-Betrachter) 46.3.1
- **Pandoc** 3.1.3
- **TeX Live** 2023 (base, latex, pictures, xetex)
- **Ghostscript** 10.02.1
- **html2text** 1.3.2a

---

## 📱 Mobile & Geräte

- **libimobiledevice** 1.3.0
- **ideviceinstaller** 1.1.1
- **ifuse** 1.1.4
- **usbmuxd** 1.1.1

---

## 🎮 Gaming

- **GameMode** 1.8.1

---

## 🔐 Authentifizierung

- **Fingerprint:** fprintd 1.94.3 + libfprint-2
- **GNOME Keyring** 46.1
- **KeepassXC** 2.7.6
- **Pinentry:** curses + GNOME3
- **libsodium** 1.0.18

---

## 🧹 Bereinigung & Wartung

- **BleachBit** 4.6.0
- **Timeshift** 25.12.4 (System-Snapshots)
- **Mint Update** 7.1.4
- **GDebi** 0.9.5.7 (DEB-Installer)
- **Unattended-Upgrades** 2.9.1
- **Aptitude** 0.8.13

---

## 📡 Netzwerk & Server

- **OpenSSH Client** 9.6p1
- **NetworkManager** 1.46.0 (+ GNOME, OpenVPN, PPTP)
- **Netplan** 1.1.2
- **Avahi** 0.8 (mDNS/DNS-SD)
- **dnsmasq** 2.90

---

## 📊 Speicher & System (letzte Messung)

```
Disk: 327G
Kernel: 6.17.0-35-generic
RAM: Gesamt: 7,6Gi, Verwendet: 1,5Gi, Frei: 282Mi, Buff/Cache: 34Mi, Available: 6,3Gi
Swap: Gesamt: 8,0Gi, Verwendet: 1,7Gi, Frei: 6,3Gi
Uptime: up 1 day, 10 hours, 24 minutes
```

---

## 📦 Sonstige nennenswerte Pakete

- **bulky** 4.2 (Batch-Dateiumbenennung)
- **captain** 1.1.2
- **fingwit** 1.0.8
- **folder-color-switcher** 1.7.1
- **hypnotix** 5.6 (IPTV)
- **imagemagick** 6.9.12
- **yt-dlp** 2024.04.09 (Video-Downloader)
- **circle-flags-svg** 2.7.0

---

*Erstellt: 13.06.2026 | Stand: Installationsübersicht Migriert aus INSTALLÜBERSICHT.md*
