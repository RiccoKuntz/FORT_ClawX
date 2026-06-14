# 🔧 Stufe 3: Snapshot & Fix (Execution Protocol)

**Sicherheits-Check vor Ausführung:**
1. **Timeshift-Check:** Prüfe, ob ein Snapshot-System aktiv ist.
2. **Snapshot-Erstellung:** Triggere einen neuen Snapshot via CLI (`timeshift --create`), bevor Systemdateien verändert werden.
3. **Vollautonome Korrektur:** - Führe den verifizierten Befehl aus (z.B. `apt-get install -f` oder Repository-Fix).
   - Validiere den Erfolg durch einen erneuten Log-Scan.

**Abbruch-Bedingung:**
Falls `timeshift` fehlschlägt oder der Speicherplatz auf `/dev/sda3` kritisch ist (< 5GB), stoppe den Prozess und informiere den User.
