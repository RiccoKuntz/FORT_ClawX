# SYSTEM-VALIDIERUNGS-PROTOKOLL - GARVIS (v1.0.1)

**Identität:**
 - **Name:** VALIDATE
 - **Typ:** GARVIS WORKFLOW
 - **Status:** PASSIVE

## HOW TO USE
 - Führe die Schritte **1. ANALYSE** und **2. REPORT** beim Laden der Datei auf **USERWUNSCH** aus!
 - Der Schritt **3. BUGFIX** wird mit dem **USER** zusammen bearbeitet. **KEINE ALLEINGÄNGE**.
 - Bugfixing ist **IMMER interaktiv**.
 - Nutze ein **Agententeam** aus `AUTOMATION.md` (EISERNE REGEL).
 - `FAILS.md` darf beim Ausführen von `VALIDATE.md` ohne **EXECUTE-GATE** bearbeitet werden.

### PATHS
 - **VALIDATE.md:** `~/.openclaw/workspace/WorkFlows/VALIDATE.md`
 - **FAILS.md:** `~/.openclaw/workspace/FAILS.md`
 - **SECURITY.md** `~/.openclaw/workspace/SECURITY.md`

### EISERNE REGELN
 - Fehler müssen nach **ABSCHLUSS** dieses Skripts behoben sein!
 - KEINE **ALLEINGÄNGE**
 - Beachte das **EXECUTE-GATE** der `SECURITY.md`

## BOOTSEQUENZ
- **Bootsequenz:** Lade aktiv `START.md`
- Halte dich strikt an `SECURITY.md`

## 1. ANALYSE & WARTUNG

### LINUX MINT
1. **Linux Mint Updates:**
 - Installiere **Linux Mint Updates** (APT, neue Linux Mint Versionen und Major-Releases)
 - Installiere **Flatpak Updates** (flatpak update)
 - Installiere **APPIMAGE Updates** (Brave, Gearlever, PCloud usw.)
2. Führe einen **Deepscan** auf Fehler in **Linux Mint** durch.
 - APT (Paketreste, veraltete Dateien, verwaiste Dateien)
 - Flatpaks (Paketreste, veraltete Dateien, verwaiste Dateien)
 - Temporäre Dateien
 - Logs
 - Reports
 - Veraltete oder fehlerhafte Kernel (Behalte immer einen Kernel als **FALLBACK**)
 - TIMESHIFT (tägliche automatische Updates aktiv, bisherige Backups integer)

### OPENCLAW
1. Prüfe das **openclaw / FORT_ClawX** Framework auf Updates.
2. Führe einen **Deepscan** auf Fehler in **openclaw / FORT_ClawX** durch.
 - **Agenten** (Versionierung, Identität, Registry, benötigte Skills, Funktionalität)
 - **Markdown-Dateien** (ab ~/workspace rekursiv, Redundanzen, Konflikte, Benennung, intigrität)
 - **openclaw.json** (veraltete Models, timeout = 60 Minuten, Integrität)
 - **Logdateien**
 - **Konfigurationsdateien**
 - **Skills** (Updates, Funktionalität, veraltet)
 - **SESSIONS** (veraltete und abgelaufene Sessions, obsolete Subagentensessions)

## 2. REPORT
1. Lösche den **INHALT** von `FAILS.md` komplett.
 - Die Datei **MUSS LEER* sein.
2. Schreibe deinen Bericht in die **LEERE** `FAILS.md`.
 - Ordne die Fehler von kritisch nach nur Info.
 - Markiere, welche Fehler von dir **autonom** gefixt werden können.
 - Markiere, welche Fehler die Aufmerksamkeit des **USERS** erfordern.
 - Nach einem **RESET** muss der Bericht abgearbeitet werden können.

## 3. BUGFIX
1. Erstelle ein **TIMESHIFT-BACKUP**.
 - Warte, bis das **TIMESHIFT-BACKUP** abgeschlossen ist, bevor du Fehler behebst.
 - Überprüfe das **TIMESHIFT-BACKUP** auf Integrität.
 - Ist das **TIMESHIFT-BACKUP** am richtigen Ort? (`/mnt/b1251fc2-596b-4f8e-9da4-a671c1b1eadd/timeshift`)
2. Lade `FAILS.md`.
3. Erstelle einen Fehlerbericht.
 - Ordne die Fehler von kritisch nach nur Info.
 - Gib die Fehler, die die Aufmerksamkeit des **USERS** erfordern, als offen aus.
 - **Sortiere:** nach dem Schema <Fehler 1 und Lösung 1, Fehler 2 und Lösung 2>.
 - **Erkläre** jeden Fehler kurz und verständlich im **Fehlerbericht!**
4. Fixe zusammen mit dem **USER** interaktiv die Fehler.
 - Liste Autonom lösbare Fehler zuerst auf.
 - Gelöste Fehlereinträge werden aus `FAILS.md` gelöscht.
 - `FAILS.md` muss bei Abschluss wieder leer sein und alle Fehler gelöst.
