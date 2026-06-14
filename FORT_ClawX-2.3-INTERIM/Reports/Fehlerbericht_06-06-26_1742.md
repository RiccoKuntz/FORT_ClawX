# FEHLERBERICHT - 06-06-2026 17:42

## 1. System-Health

### Gateway
- **Status:** ✅ Reachable (142ms)
- **Event Loop:** ✅ OK (p99 42ms, CPU 0.529)
- **Telegram:** ✅ Konfiguriert
- **Update verfügbar:** npm 2026.6.1 (aktuell: 2026.5.28)

### Hardware
- **RAM:** 7,6 GiB gesamt, 2,2 GiB belegt, 5,5 GiB verfügbar → ✅ OK
- **Swap:** 8 GiB, 12 KiB belegt → ✅ OK
- **SSD (/dev/sda3):** 109 GiB, 34 GiB belegt (33%) → ✅ OK
- **HDD (/dev/sdb1):** 1,8 TiB, 58 GiB belegt (4%) → ✅ OK
- **smartctl:** Nicht installiert (`smartmontools` fehlt)

### Kernel
- 6.17.0-35-generic (aktuell)

---

## 2. Journalctl Fehler (System-Logs)

### A. casper-md5check.service (WIEDERHOLEND)
- **Fehler:** `Failed to start casper-md5check.service - casper-md5check Verify Live ISO checksums`
- **Häufigkeit:** Bei JEDEM Boot seit Mai 27
- **Ursache:** casper-md5check ist ein Live-ISO-Prüfdienst, der auf einem installierten System unnötig ist
- **Schwere:** Gering (kosmetisches Problem)

### B. gkr-pam: Keyring-Fehler (WIEDERHOLEND)
- **Fehler:** `gkr-pam: couldn't unlock the login keyring` + `unable to locate daemon control file`
- **Häufigkeit:** Bei JEDEM Login seit Mai 27
- **Ursache:** GNOME Keyring ist konfiguriert, aber beim Login nicht korrekt initialisiert
- **Schwere:** Mittel (Passwort-Manager-Funktionalität beeinträchtigt)

### C. Device Timeout (WIEDERHOLEND)
- **Fehler:** `Timed out waiting for device dev-disk-by\x2duuid-83a625d2\x2d74c8\x2d463d\x2dbb27\x2dbb094f5ad15d.device`
- **Häufigkeit:** Bei JEDEM Boot seit Mai 27
- **Ursache:** Eine Disk/Partition mit UUID 83a625d2-74c8-463d-bb27-bb094f5ad15d ist nicht verfügbar (fehlende Platte, getrennt, oder UUID geändert)
- **Schwere:** Mittel (kann Boot verzögern)

### D. Xorg Crash (30. Mai)
- **Fehler:** `Process 984 (Xorg) dumped core`
- **Ursache:** Xorg Server abgestürzt (möglicherweise Grafikkentreiber/Display-Problem)
- **Schwere:** Mittel (einmaliger Vorfall)

### E. chrome_crashpad Handler Crashes (mehrfach)
- **Fehler:** Chrome/Cloudflare-Warp Crash Handler abgestürzt
- **Häufigkeit:** 2x (27. Mai, 1. Juni)
- **Schwere:** Gering (Prozess-Crash, kein Systemproblem)

### F. Cinnamon Session Errors (31. Mai)
- **Fehler:** `g_variant_unref: assertion 'value != NULL' failed` + `Unable to close Cinnamon's end session dialog`
- **Ursache:** Cinnamon-Desktop-Sitzung hat Fehler beim Herunterfahren/Wechseln
- **Schwere:** Gering

### G. PAM Module Fehler (31. Mai)
- **Fehler:** `PAM unable to dlopen(pam_lastlog.so): No such file`
- **Ursache:** pam_lastlog.so fehlt oder Pfad falsch
- **Schwere:** Gering (nur Logging, keine Auth)

---

## 3. OpenClaw-Status

### Sessions (3 aktiv)
| Session | Typ | Alter | Modell | Tokens |
|---------|-----|-------|--------|--------|
| agent:main:telegram:direct:575674022 | direct | 6m | qwen3.6-35b | 23k/128k |
| agent:main:subagent:9ac693a0-f4… | spawn-child | 4d | qwen3.6-35b | unknown |
| agent:main:main | direct | 5d | qwen3.5-9b | 0k/64k |

### Tasks
- 0 aktiv, 0 wartend, 0 laufend
- 37 Issues, 9 Warnungen, 55 getrackt

### Plugins
- Memory: aktiv (memory-core), nicht geprüft
- Plugin-Compatibility: keine

---

## 4. Zusammenfassung

**Kritische Probleme:** Keine

**Mittlere Probleme:**
1. Device Timeout bei Boot (UUID 83a625d2-...) → Boot-Verzögerung
2. gkr-pam Keyring nicht verfügbar → Passwort-Manager-Probleme
3. Xorg Crash (einmalig, 30. Mai)

**Geringe Probleme:**
1. casper-md5check.service fehlschlägt bei jedem Boot
2. chrome_crashpad Handler Crashes
3. Cinnamon Session Errors
4. pam_lastlog.so fehlt
5. OpenClaw Update verfügbar (2026.6.1)
6. smartctl nicht installiert (SSD-Health-Check unmöglich)
