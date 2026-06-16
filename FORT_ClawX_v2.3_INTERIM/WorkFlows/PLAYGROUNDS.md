#  PLAYGROUNDS (v1.0.0 - PlayGrounds)

**Identität:**
- **Name:** PLAYGROUNDS
- **Typ:** GARVIS WORKFLOW
- **Status:** PASSIVE

## HOW TO USE
1. **Zweck:** PlayGround ist eine sichere Testumgebung auf dem ThinkPad T400. Neue Ideen und Tests werden hier entwickelt, bevor sie ins Produktiv-System integriert werden.
2. **PlayGround** wird **NUR** aktiviert, wenn der Nutzer (Rick) eine explizite Anfrage stellt:
 - Erlaubt: "Starte PlayGround", "Lade diese Datei in PlayGround als Test-Kopie".
 - Nicht erlaubt: Automatische Aktivierung, Hintergrund-Skripte ohne User-Knowledge.
 - Jeder **TEST** in **PLAYGROUNDS** braucht einen **TESTNAMEN**

### PATHS
**workspace-Original:** `~/.openclaw/workspace`
**Testumgebung:** `~/.openclaw/workspace/PlayGround/Test`
**Protokolldatei:** `~/.openclaw/workspace/PlayGround/REPORTS/<TESTNAME_DD.MM.YYYY_HH:MM:SS>`
**Agenten-SOULS:** `~/.openclaw/workspace/Automationen/*`

## WORKFLOW
Wenn Rick eine Datei oder ein Verzeichnis in **PlayGround** laden möchte:
1. **Klone** zuerst `~/.openclaw/workspace` nach `~/.openclaw/workspace/PlayGround/Test`
 - Ignoriere dabei: `~/.openclaw/workspace/PlayGround/` und `~/.openclaw/workspace/WorkFlows/PLAYGROUNDS.md`
 - Verändere keine Dateien. Klone nur 1:1
2. **Dateiänderungen** finden ab jetzt nur noch in `~/.openclaw/workspace/PlayGround/Test` statt.
 - **Dateiänderungen** werden in `~/.openclaw/workspace/PlayGround/REPORTS/` protokolliert.
 - **Protokolle** werden so angelegt, das Änderungen in **PLAYGROUNDS** später ins `workspace` deployed werden können.
 - **Protokolle** werden nach folgendem Schema benannt: <TESTNAME_DD.MM.YYYY_HH:MM:SS>
 - Eine **Protokoll-Markdown-Datei** pro Test.

## **Sicherheit & Regeln**
- **EXECUTE-GATE:** Bleibt aktiv (Recherchemodus Standard, EXECUTE für Schreibzugriff)
- **System-Kern-Schutz:** `~/.openclaw/workspace/Automationen/*` nur lesen (Agenten SOUL.md unveränderbar)
- **Read-Only RICK/:** Garvis darf den Rick-Ordner niemals schreiben - nur lesen!

## **Workflow-Zusammenfassung**
1. Nur auf User-Anfrage aktiviert (kein Auto-Pilot!)
2. Kopie-Umgebung: Originale bleiben im Workspace erhalten
3. Zeitstempel immer in UTC Format: <TESTNAME_DD.MM.YYYY_HH:MM:SS>
4. Keine Hintergrund-Aktivitäten ohne explizite Anfrage
