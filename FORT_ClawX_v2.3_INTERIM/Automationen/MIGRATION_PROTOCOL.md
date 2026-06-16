# 📂 OpenClaw Migration & Re-Location Protocol (v1.0.0)

Dieses Protokoll steuert die autonome Umbenennung und Verschiebung von Kern-Verzeichnissen innerhalb des Workspaces. Es dient als externe Referenz während der physischen Dateioperationen.

---

## 🛠️ Prozess-Logik (Master-Workflow)

1. **Vorbereitung (Snapshot)**
   - Erstelle ein Backup der aktuellen `PATHS.md` in `./Backup Temp/`.
   - Identifiziere alle betroffenen Pfad-Strings in der `PATHS.md`.

2. **System-Lock**
   - Erstelle die Datei `maintenance.lock` im Root-Verzeichnis.
   - Alle Agenten müssen bei Vorhandensein dieser Datei jegliche Schreibvorgänge pausieren.

3. **Logische Anpassung (Virtual Move)**
   - Scanne alle `.md`-Dateien im Ordner `./Automationen/`.
   - Ersetze den alten Pfad-String durch den neuen Pfad-String (Regex-Replacement).
   - Aktualisiere die entsprechenden Zeilen in der `PATHS.md`.

4. **Physische Ausführung (The Move)**
   - Führe den Rename-Befehl auf OS-Ebene aus (z. B. `mv old_path new_path`).

5. **Validierung (Post-Flight)**
   - Teste den Lesezugriff auf die `PATHS.md`.
   - Verifiziere die Existenz des neuen Verzeichnisses.
   - Sende Bestätigung an Rick.

6. **Cleanup**
   - Lösche `maintenance.lock`.

---

## ⚠️ Sicherheits-Vorgaben
- **Atomarität:** Schlägt Schritt 4 fehl, muss Schritt 3 mithilfe des Backups aus Schritt 1 sofort rückgängig gemacht werden.
- **Veto-Recht:** Der `AGENT_CREATOR` zeigt Rick die geplante Liste der Dateiänderungen und wartet auf ein `EXECUTE`.
