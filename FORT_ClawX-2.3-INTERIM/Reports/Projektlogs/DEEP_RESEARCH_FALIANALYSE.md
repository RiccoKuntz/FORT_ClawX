# DeepResearch Fallanalyse & Reparaturplan

**Datum:** 2026-05-29
**Analyst:** Garvis (Detektiv-Modus)
**Status:** REPARATUR BEREIT

---

## PROBLEME (8 identifiziert)

### P1: Falsches Timeout (Kritisch)
- **Symptom:** Agent nach 30 Min abgewürgt
- **Ursache:** `runTimeoutSeconds: 1800` statt `86400`
- **Lösung:** Immer 86400 setzen (AUTOMATION.md Vorgabe)

### P2: Keine Checkpoints geschrieben (Kritisch)
- **Symptom:** Alle Cache-Verzeichnisse leer
- **Ursache:** Modell überspringt Checkpoint-Schritt bei komplexen Tasks
- **Lösung:** SOUL.md muss Checkpoint als ERSTEN Schritt definieren, nicht als "nachher"

### P3: AUTOMATION.md veraltet (Mittel)
- **Symptom:** Registry zeigt V2.0.0 statt V5.0.0
- **Lösung:** AUTOMATION.md aktualisieren

### P4: Cache-Verzeichnis leer (Folge von P2)
- **Lösung:** Entfällt mit P2-Fix

### P5: Kein EXECUTE für Schreibzugriff (Hoch)
- **Symptom:** Agent darf nicht schreiben
- **Lösung:** Explizites EXECUTE bei Subagent-Spawn

### P6: START.md Boot-Sequenz ignoriert (Mittel)
- **Symptom:** Agent startet ohne System-Dateien zu laden
- **Lösung:** Task-Definition muss Boot-Sequenz erzwingen

### P7: Sub-Queries zu komplex (Hoch)
- **Symptom:** Token-Überlastung → Absturz
- **Lösung:** Max 3 Sub-Queries, jede fokussiert auf EIN Thema

### P8: Hardware-Limitierung (Mittel)
- **Symptom:** Gateway-Reloads bei langen Runs
- **Lösung:** Kompakte Subagents, kurze Kontexte

---

## REPARATUR-PLAN

### Phase 1: SOUL.md final fixen
- Checkpoint als ABSOLUTER ERSTER Schritt nach Startup
- Max 3 Sub-Queries (nicht 5)
- Explizite EXECUTE-Freigabe im Task
- Timeout 86400 in SOUL verankern

### Phase 2: AUTOMATION.md aktualisieren
- V2.0.0 → V5.0.0 Eintrag

### Phase 3: Test-Run mit EXECUTE
- Klare, fokussierte Forschungsfrage
- Max 3 Sub-Queries
- Checkpoint-Überwachung

### Phase 4: Ergebnis-Validierung
- Existiert subquery_*.md?
- Existiert last_status.md?
- Report vollständig?

---

## BEREIT FÜR: EXECUTE
