# PATHS.md - FORT_ClawX Central Path Registry (v1.0.2)

Diese Datei definiert die physische Struktur des Workspaces. Alle Agenten laden diese Pfade bei der Initialisierung, um autonom navigieren zu können.

---

## 🏗️ Kern-Verzeichnisse (Core)

| Pfad | Funktion |
|:--- |:--- |
| `/home/rick/.openclaw/workspace/` | **Root-Verzeichnis:** Basis für alle relativen Pfade und Konfigurationsdateien. |
| `/home/rick/.openclaw/workspace/memory/` | **Langzeitgedächtnis:** Speicherort für `TEMP.md` und projektübergreifende Daten. |


## 🔄 Core Workspace Subdirectories

| Pfad | Funktion |
|:--- |:--- |
| `/home/rick/.openclaw/workspace/core/` | **TUI-CORE:** Asynchroner Status-Monitoring & Agent-Orchestration. |
| `/home/rick/.openclaw/workspace/core/config/` | **Konfiguration:** Agent-Souls, PATHS.md, Automation-Registry. |
| `/home/rick/.openclaw/workspace/core/output/` | **Ausgabe:** TUI-Ausgaben & Status-Logs (Buffered). |

---

## 🤖 Automatisierung & Logik

| Pfad | Funktion |
|:--- |:--- |
| `/home/rick/.openclaw/workspace/Automationen/` | **Workflow-Hub:** Hauptordner für alle Agenten-Souls und Prozessbeschreibungen. |
| `/home/rick/.openclaw/workspace/Automationen/System/` | **SysAdmin-Zentrale:** Beherbergt Guards (Linux/OpenClaw) und den Updater. |
| `/home/rick/.openclaw/workspace/Automationen/System/PATH_RUNNER/` | **PATH_RUNNER:** System-Agent für PATHS.md-Pflege und -Audit. |
| `/home/rick/.openclaw/workspace/Automationen/System/Mr_Smith/` | **Mr_Smith:** System-Agent (Infrastruktur). |
| `/home/rick/.openclaw/workspace/Automationen/System/Pathfinder/` | **Pathfinder:** System-Agent (Infrastruktur). |
| `/home/rick/.openclaw/workspace/skills/` | **Werkzeugkasten:** Enthält Python-Skripte und Tools (Websearch, Filesystem etc.). |

---

## 📁 WorkFlows

| Pfad | Funktion |
|:--- |:--- |
| `/home/rick/.openclaw/workspace/WorkFlows/` | **WorkFlows:** Zentrale Ablage für Garvis-Arbeitsabläufe und Anweisungen. Werden nur von Garvis orchestriert (Typ: GARVIS WORKFLOW). |

### HOW TO USE
**WorkFlows:**
- sind Arbeitsabläufe und Arbeitsanweisungen für Garvis.
- **MÜSSEN** von Garvis Orchestriert (Agententeam) werden. (**Typ:** GARVIS WORKFLOW)
- werden nur von Garvis übernommen wenn es **keinen** geeigneten **Agenten** oder Team gibt.

## 📂 Arbeitsbereiche (Workspace Operations)

| Pfad | Funktion |
|:--- |:--- |
| `/home/rick/.openclaw/workspace/Arbeitsordner/Input/` | **Eingang:** Hier legst du Dateien ab, die die Agenten verarbeiten sollen (Read-Only). |
| `/home/rick/.openclaw/workspace/Arbeitsordner/Work/` | **Baustelle:** Aktive Bearbeitung von Projekten durch Agenten (Read/Write). |
| `/home/rick/.openclaw/workspace/Arbeitsordner/Output/` | **Ergebnis:** Ablageort für finalisierte und durch Tester geprüfte Projekte. |
| `/home/rick/.openclaw/workspace/PlayGround/` | **PlayGround:** Kontrollierte Testumgebung für neue Ideen und Prototypen. |

---

## 📊 Monitoring & Reporting

| Pfad | Funktion |
|:--- |:--- |
| `/home/rick/.openclaw/workspace/Reports/` | **Zentrales Reporting:** Basisordner für alle Logs und Analysen. |
| `/home/rick/.openclaw/workspace/Reports/Projektlogs/` | **Fehleranalyse:** Explizite Log-Dateien für Debugging und Projekthistorie. |


# OPERATIVE PFADE 
DIR_SYSTEM_AGENTS: "/home/rick/.openclaw/workspace/Automationen/System/"
DIR_REGULAR_AGENTS: "/home/rick/.openclaw/workspace/Automationen/Agents/"
DIR_WORKFLOWS: "/home/rick/.openclaw/workspace/WorkFlows/"

---

## 💾 Externe Speichermedien (Storage)

| Pfad | Funktion |
|:--- |:--- |

| `/home/rick/Schreibtisch/` | **Desktop Shortcut:** Referenzpunkt für schnelle Dateiablage ("auf dem Desktop"). |

---

## 🔗 Referenzen
- **Agenten-Souls:** Die spezifischen `.md`-Pfade der Agenten sind in der `AUTOMATION.md` unter `## AGENTENPFADE` hinterlegt.
- **Sicherheits-Ausnahmen:** Pfadspezifische Erlaubnisse (z.B. für den Updater) sind in der `SECURITY.md` definiert.

**Autonomie-Hinweis:**
Sollte diese Datei beschädigt werden, nutzt der **OpenClaw Guardian** diese Struktur-Vorgabe, um die Verzeichnisse durch einen Tiefenscan ab `/home/rick/.openclaw/workspace/` wiederherzustellen.
