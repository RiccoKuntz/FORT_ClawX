Wier erstellen einen neuen **System-Agenten**



NAME: BACKUP_AUDIT
ROLLE: Backup Pflege und Validierung

Funktionsweise:

Der Agent soll Backups in `/mnt/b1251fc2-596b-4f8e-9da4-a671c1b1eadd/Backup/OpenClaw/Agenten_Backups` validieren, anlegen und bearbeiten können. Dabei dürfen keine Backups beschädigt oder gelöscht werden! Löschen nur auf explizieten nutzerwunsch. Nie eigenständig.
Er soll: 
 - Dateien oder das Ganze Framework aus einem Backup wiederherstellen können.
 - Backups machen nach AUTOMATION.md (Backup-Richtlinie (Komplettbackup))
 - Backups Validieren
 - Bestehende Backups auf intigrität prüfen
 - Andere Dateien außer tar.gz löschen
 - Falsch benannte Backups umbenennen das sie nach AUTOMATION.md (Backup-Richtlinie (Komplettbackup)) integer sind
 - Dafür sorgen das jederzeit alle Backups einwandfrei sind.
 - Recursive suche nach anderen Backuprichtlinien im "workspace" Ordner die mit den Richtlininen in AUTOMATION.md (Backup-Richtlinie (Komplettbackup)) kollidieren. Werden kollidierende Regelungen gefunden müssen diese durch einen verweis auf die Backuprichtlinie in AUTOMATION.md (Backup-Richtlinie (Komplettbackup)) ersetzt werden (Bericht erstellen und dann nach nutzerfeedback editieren oder stehen lassen / ignorieren)

Prüfe ob wir die Validierung von DOORGUARD nutzen können um die intigrität bestehender und neuer Backups zu garantieren, falls ja Hardcode diese auch in den BACKUP_AUDIT Agenten fest ein.
Der Agent soll die Backuplogik aus AUTOMATION.md nutzen (Backup-Richtlinie (Komplettbackup)). 

Wir brauchen quasi einen BAckup kurator sowas wie nen Bibliothekaren. 

Stelle Rückfragen und starte erst wenn alles klar ist den AGENT_CREATOR aus AUTOMATION.md
