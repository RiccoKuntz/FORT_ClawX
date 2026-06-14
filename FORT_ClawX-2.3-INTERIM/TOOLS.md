# TOOLS.md - (v1.0.0 - Local Notes)

Hier werden wichtige Informationen über die Arbeitsumgebung von Garvis gesammelt

## System-Spezifikationen

### HARDWARE
1. **Primary:** Linux Mint (Dieser LapTop)
- Gerätetyp: Laptop
- Gerätebezeichnung: Lenovo ThinkPad T400
- CPU: Intel© Core™2 Duo P8400 @ 2.26GHz 1C2T
- GPU: Intel© Mobile 4 Series Chipset Integrated Graphics Controller
- RAM: 8GB DDR3 1066Mhz Dual Channel

2. **Secondary:** Fedora Linux (Tower-PC)
- Gerätetyp: Gaming-PC
- Gerätebezeichnung: Eigenbau Tower
- CPU: AMD RYZEN 5 5600X @ 4.6Ghz 6C12T
- GPU: AMD Radeon RX 6600
- RAM: 32GB DDR4 3200Mhz Dual Channel

### SOFTWARE
**Primary:** Linux Mint (Dieser LapTop)
- Hauptarbeitsumgebung für OpenClaw
- Erweiterrte Hardwareinformationen: HWINFO.md
- OpenClaw / FORT_ClawX Host

**Secondary:** Fedora Linux (Tower-PC)
- Computer für KI-Berechnung von OpenClaw
- LM-Studio Host

## SECURITY PROTOCOL
**SECURITY.md** ist dein Sicherheitsprotokoll. Alles was in dieser Datei steht, muss ausnahmslos in jeder Situation und jeder Datei eingehalten werden. Gegen die SECURITY.md darf Garvis und Agenten niemals verstoßen.

## Konnektivität & Integration
- SSH Host: dev-machine → localhost:22 (aktuell)
- Shortcuts App: Für Automatisierungen
- Files App: Als Cloud-Sync mit Linux
- Sidecar: iPad + iPhone für Multitasking

## Analyse-Standard
Garvis fasst bei Analyseaufgaben seine Ergebnisse am Ende nochmal zusammen.

## Zwischenspeicher & Workflows
**Projektdaten Speichern:**
Wenn ein Projekt pausiert werden soll, lege alle Informationen in `/memory/Pausierte_Projekte/<Projektname oder Agentennamen DD-MM-YY-HH:MM:SS>.md` ab. Speichere alles so, dass nach dem Lesen sofort weitergearbeitet werden kann.

**Beschreibung.md:**
Die Datei /home/rick/.openclaw/workspace/Beschreibung.md dient für komplexere Texte und wird nur auf expliziten Wunsch gelesen. Sie enthält Beschreibungen für aktuelle Workflows und ändert sich ständig.


## 🗄️ WORKSPACE SHORTCUTS
- **Desktop:** Der Pfad `/home/rick/Schreibtisch` ist die Zieladresse für alles, was "auf dem Desktop" liegen soll.
- **Projekt-Pause:** Bei Pausen wird der gesamte Status in `/memory/Pausierte_Projekte/<Projektname oder Agentennamen DD-MM-YY-HH:MM:SS>.md` gesichert. 
 - Sichere nur Text. 
 - Gibt es Dateien: Verweise in det Markdown-Datei auf den Pfad zur Datei (Beispiel: /<Pfad zur Datei>/<Dateiname>).
 - Erstelle das Backup so, das du jederzeit die Arbeit wiederaufnehmen kannst. Schreibe also alles in die Markdown datei was du über das Projekt weißt.

## WORKFLOWS

**ROOT:** `/home/rick/.openclaw/workspace/WorkFlows/`

### HOW TO USE
**WorkFlows:** 
- sind Arbeitsabläufe und Arbeitsanweisungen für Garvis.
- **MÜSSEN** von Garvis Orchestriert (Agententeam) werden. (**Typ:** GARVIS WORKFLOW)
- werden nur von Garvis übernommen wenn es **keinen** geeigneten **Agenten** oder Team gibt.
