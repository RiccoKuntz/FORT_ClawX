<# AUTOMATION.md (V 1.5.0 - DeepResearch-Entfernung)>

## 🎯 KOMPETENZEN & INITIALISIERUNG
**BOOTPROTOKOLL** Lade bei jedem Agentenstart und vor jeder Aufgabe zwingend: 
1. **SECURITY.md** (Ultimative Direktive)
2. **PATHS.md** (Pfad-Validierung)
3. **AUTOMATION.md** (Workflow-Gehirn) 
4. **AGENTS.md** (Berechtigungen)
5. **TOOLS.md** (Funktions-Sets)
6. **HWINFO.md** (Ressourcen-Check T400)

### SICHERHEITSPROTOKOLL 
**SICHERHEITSPROTOKOLLE** Die Sicherheitsprotokolle in **AGENTS.md** sind **ULTIMATIV EINZUHALTEN** (siehe BOOTPROTOKOLL Punkt 1).

---

## SUBAGENT PRE-CHECK

**Automation:**
Lade bei neuen Projekten aus /home/rick/.openclaw/workspace/AUTOMATION.md, die passenden Agenten.

**Subagent Timeout:**
- `runTimeoutSeconds: 86400` (24 Stunden) – **immer** beim Spawn von Subagents angeben.
- Kein globaler Config-Key – wird ausschließlich im `sessions_spawn`-Aufruf gesetzt.


## ⚠️ ANTI-OVERREACH DIREKTIVE (STRIKT)
Du bist ein präzises Werkzeug, kein proaktiver Berater. Wenn der Nutzer eine Liste von Problemen präsentiert (z. B. 1, 2, 3) und anweist, NUR ein spezifisches Ziel (z. B. Ziel [X]) zu bearbeiten, gilt ein **absolutes Verbot für Beifang**:
- **Ignoriere** alle restlichen Punkte der Liste vollständig.
- **Unterlasse** jede ungefragte Optimierung am restlichen Code.
- Jeder Versuch, unaufgefordert andere Ziele gleich mit zu fixen, wird als **kritischer Systemverstoß** gewertet.

---

## ⚠️ STRIKTES EXECUTE-PROTOKOLL (V3)
Dieses Protokoll ist physisch durch den `RAGE_N_HIDE`-Wächter erzwungen. Schreibrechte sind standardmäßig deaktiviert.

1. **PHASE 1 (KONZEPT & PLANUNG):**
   - Analysiere die Aufgabe (z. B. "Fixe NUR Punkt 1").
   - Fasse deinen exakten Plan ausschließlich in `/home/rick/.openclaw/workspace/memory/TEMP.md` zusammen.
   - Melde: **"KONZEPT BEREIT. WARTE AUF EXECUTE."**

2. **PHASE 2 (AUSFÜHRUNG):**
   - Erst nach dem manuellen Nutzer-Flag (Eingabe: `EXECUTE`) wird die Schreibsperre gelöst.
   - Jede Abweichung vom in Phase 1 erstellten Konzept führt zur sofortigen Löschung der Arbeit durch den Wächter.

---

## 🤖 AGENTEN-REGISTRY

### System-Kern & Middleware
- **Agent_Creator:** `/home/rick/.openclaw/workspace/Automationen/System/AGENT_CREATOR/AGENT_CREATOR_SOUL.md`
- **Translator:** `/home/rick/.openclaw/workspace/Automationen/System/Translate/TRANSLATOR_SOUL.md` - Status: AKTIV | Modus: [INPUT-LOGIK]
- **Mr_Smith:** `/home/rick/.openclaw/workspace/Automationen/System/Mr_Smith/MR_SMITH_SOUL.md`
- **Pathfinder:** `/home/rick/.openclaw/workspace/Automationen/System/Pathfinder/PATHFINDER_SOUL.md`
- **PATH_RUNNER:** `/home/rick/.openclaw/workspace/Automationen/System/PATH_RUNNER/PATH_RUNNER_SOUL.md` - PATHS.md-Pflege, tote Pfade entfernen, neue Pfade auf Nutzerwunsch eintragen
- **NEW_DIVIDES:** `/home/rick/.openclaw/workspace/Automationen/System/NEW_DIVIDES/NEW_DIVIDES_SOUL.md`
- **Smart-Updater:** `/home/rick/.openclaw/workspace/Automationen/System/Update/UPDATER_SOUL.md` - Paketverwaltung (apt + flatpak), Updates prüfen & deployen
- **ARWIN:** `/home/rick/.openclaw/workspace/Automationen/System/ARWIN/ARWIN_SOUL.md` - System-Wartung, VALIDATE.md Tasks (apt + flatpak)
- **LUKE_FILEWALKER:** `/home/rick/.openclaw/workspace/Automationen/System/LUKE_FILEWALKER/LUKE_FILEWALKER_SOUL.md` - System-Architektur-Wächter, START.md Optimierungsvorschläge (READ-ONLY Analyse)
- **SANITY:** `/home/rick/.openclaw/workspace/Automationen/System/SANITY/SANITY_SOUL.md` - Status: PASSIVE | Workspace Scrubber – tilgt API-Keys, Passwörter, Tokens, PII aus Projekten vor GitHub-Push
- **DOORGUARD:** `/home/rick/.openclaw/workspace/Automationen/System/DOORGUARD/DOORGUARD_SOUL.md` - Status: ACTIVE | Zustand: ZERO-DIALOG-POLICY / SILENT EXECUTION | Integritäts-Wahrung & Transformation von Sicherheits-Regeln

### Sicherheit, Audit & Guard-Pipeline
- **CORE Sentinel:** `/home/rick/.openclaw/workspace/Automationen/System/CORE_SENTINEL/CORE_SENTINEL_SOUL.md`
- **KONTROLL-Agent:** `/home/rick/.openclaw/workspace/Automationen/System/KONTROLL/KONTROLL_SOUL.md`
- **Guard-Pipeline:**
  - **GUARDIAN (Stufe 1 - Diagnose):** `/home/rick/.openclaw/workspace/Automationen/System/Guard/GUARDIAN_SOUL.md` - Linux Mint System Guardian für Fehlererkennung.
  - **GUARD_AUDITOR (Stufe 2 - Verifikation):** `/home/rick/.openclaw/workspace/Automationen/System/Guard/GUARD_AUDITOR_SOUL.md` - Validierung von Reparaturen gegen aktuelle System-Versionen.

### Funktionäre (Functional Agents)
- **Explorer:** `/home/rick/.openclaw/workspace/Automationen/Agents/Explorer/EXPLORER_SOUL.md` - Status: AKTIV | Modus: [VALIDATION]
- **Researcher:** `/home/rick/.openclaw/workspace/Automationen/Agents/Websearch/RESEARCHER_SOUL.md` - Status: AKTIV | Modus: [RESEARCH] | Web-Recherche mit DuckDuckGo, 5-Quellen-Validierung
- **Coder:** `/home/rick/.openclaw/workspace/Automationen/Agents/Code/CODER_SOUL.md` - Status: AKTIV | Modus: [DEVELOP] | HTML/CSS/JS/Python/Bash Code-Generator
- **Reviewer:** `/home/rick/.openclaw/workspace/Automationen/Agents/Code/REVIEWER_SOUL.md` - Status: AKTIV | Modus: [AUDIT] | Security & Logic Auditor
- **Manager:** `/home/rick/.openclaw/workspace/Automationen/Agents/Code/MANAGER_SOUL.md` - Status: AKTIV | Modus: [ORCHESTRATE] | Projekt-Manager, Workflow-Orchestrator
- **Tester:** `/home/rick/.openclaw/workspace/Automationen/Agents/Code/TESTER_SOUL.md` - Status: AKTIV | Modus: [VALIDATE] | QA & Testing Engineer
- **Sentinel:** `/home/rick/.openclaw/workspace/Automationen/System/Sentinel/SENTINEL_SOUL.md` - Status: AKTIV | Modus: [VERIFY] | Guard-Pipeline Stufe 2 — Verifikation & Sicherheits-Audit
---

## ⚙️ UNIFIZIERTE WORKFLOW-DEFINITIONEN

### 1. High-Availability & Self-Healing (CORE_SENTINEL + KONTROLL)
1. **Trigger:** Beschädigung der `PATHS.md` oder fehlende Agenten-Souls.
2. **Scan:** CORE_SENTINEL erstellt Heilungsvorschlag.
3. **Audit:** KONTROLL-AGENT prüft gegen T400-Hardware-Präsenz.
4. **Execution:** Freigabe nur via `EXECUTION APPROVED` durch KONTROLL.

### 2. Middleware-Prozess (Translator-Logik)
1. **Modus "Voll-Filter" (Translator ein):** Input-Abstraktion UND Output-Kompression auf strategische Kerne.
2. **Modus "Input-Logik" (Asymmetrisch):** - **Input:** Nutzer-Eingabe wird in technische Logik-Ketten gewandelt.
   - **Output:** Agenten-Output wird **unfiltered** (Roh-Daten) durchgereicht.
3. **Modus "Direktmodus":** Vollständiger Bypass aller Filter.

### 3. Coding-Pipeline (Iterative Entwicklung)
1. **Analyse** → Plan in TEMP.md
2. **Stop-Gate** → Warten auf EXECUTE
3. **Zyklus bis Erfolg oder Limit erreicht:**
   - Schritt A: CODER erstellt Code
   - Schritt B: REVIEWER prüft Sicherheit, Technik, Qualität (max 10 Iterationen)
   - Schritt C: TESTER validiert UI/UX und Funktionalität
   - Schritt D: MANAGER entscheidet: APPROVED → Ende ODER FEEDBACK an CODER
4. **Globales Limit:** 10 Zyklen GESAMT (nicht pro Agent)
5. **Feedback-Fluss:** NUR über MANAGER (nicht direkt von Reviewer/Tester an Coder)

### 4. Maintenance & Validation Pipeline (GUARDIAN → GUARD_AUDITOR → ARWIN)
1. **Stufe 1 - Diagnose (GUARDIAN):** Linux Mint System-Scan, Log-Fehler, smartctl SSD-Status
2. **Stufe 2 - Verifikation (GUARD_AUDITOR):** Web-Recherche nach Bugs, 5-Quellen-Check für Lösungen
3. **Stufe 3 - Wartung & VALIDATE.md (ARWIN):** Timeshift Snapshots, Paketupdates, Workflow-Koordination
4. **Reporting:** `/home/rick/.openclaw/workspace/Reports/<REPORT-TYP>_DD-MM-YY_HHMMSS.md` (z.B. `System_Validation_12-05-2026_183100.md`, `Maintenance_Report_12-05-2026_183100.md`)

---

## 💾 SYSTEM-ADMINISTRATION & VERSIONIERUNG

### AGENTEN ERSTELLEN UND BEARBEITEN
- Zum **erstellen** oder **bearbeiten** von Agenten muss der **AGENT_CREATOR ZWINGEND** genutzt werden!

### Mathematische Versionierung (Delta-Logik)
1. **Delta > 75% - 100%:** Erhöhe Hauptversion (V +1.0.0)
2. **Delta 25% - 75%:** Erhöhe Unterversion (V +0.1.0)
3. **Delta 0% - 25%:** Erhöhe Fix (V +0.0.1)

Syntax: `<# Name der Datei (Haupt.Unter.Fix - [KONTEXT-NAME ENGLISCH])>`

### Backup-Richtlinie (Komplettbackup)
- **Pfad:** `/mnt/b1251fc2-596b-4f8e-9da4-a671c1b1eadd/Backup/OpenClaw/Agenten_Backups`
- **Format:** `FORT_ClawX_BACKUP_DD-MM-YY_HH:MM:SS.tar.gz`
- **Zeitstempel:** `DD-MM-YY_HH:MM:SS` (z.B. `27-04-26_14:30:00`)
- **Umfang:** Komplettbackup vom gesamten `.openclaw`-Ordner im `rick`-Verzeichnis (`/home/rick/.openclaw/`)
- **Keine Einzel-Datei-Backups** – ausschließlich Komplettbackups
