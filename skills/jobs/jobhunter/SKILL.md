---
name: jobhunter
description: Multi-API Jobsuche (DE, remote) mit Dedupe, Scoring und operativem Reportpaket (JSON+MD).
metadata: { "openclaw": { "os": ["linux"] } }
---

# JOBHUNTER SKILL (V2.1.1 - Operational Reporting Skill)

**Name:** JobHunter
**Typ:** FUNKTION (Skill)
**Status:** ACTIVE

- **Task:** Suche remote Jobs in Deutschland, dedupliziere, score und liefere ein **abnahmefähiges Ergebnispaket** statt nur Hintergrundlauf.
- **Ziel:** Ergebnisse müssen filterbar, nachvollziehbar und auswertbar sein.

## 🔄 Workflow-Logik
1. **Run-Init:** Lade Config, prüfe Secrets/Quellen, bestimle Zeitfenster.
2. **Suche:** Rufe aktivierte APIs mit aktuellen Suchparametern ab. Respektiere Delays und Fehlerkontingente.
3. **Dedupe & Score:** Schreibe nur neue Jobs in SQLite, score nach Relevanz.
4. **Reporting-Paket:** Schreibe pro Run ein Berichtspaket als Markdown und JSON nach `Arbeitsordner/Output/JobHunter/`.
5. **Statusrückgabe:** Gebe an Manager/Anfragenden immer ein strukturiertes Statuspaket zurück, nie nur pauschale „läuft“-Aussagen.
6. **Fehlerklassifikation:** Unterscheide sauber in `API_FAIL`, `FILTER_MISMATCH`, `DB_ERROR`, `CONFIG_ERROR`, `AUTH_FAIL`.

## Ausgabe-Interface
- Output-Root: `~/.openclaw/workspace/Arbeitsordner/Output/JobHunter/`
- Report: `jobhunter_run_<YYYYMMDD_HHMMSS>.md`
- JSON: `jobhunter_run_<YYYYMMDD_HHMMSS>.json`

### jobhunter_report.json Schema (Pflicht)
{
  "status": "SUCCESS | PARTIAL | FAILED",
  "iteration": 1,
  "run_started_at": "ISO-8601",
  "run_finished_at": "ISO-8601",
  "target": "MANAGER",
  "config_snapshot": {
    "keywords": [],
    "salary_min": 45000,
    "location": "Deutschland",
    "remote_only": true
  },
  "source_status": [
    {
      "source": "bundesagentur|jooble|adzuna",
      "enabled": true,
      "status": "OK|API_FAIL|AUTH_FAIL|CONFIG_ERROR",
      "jobs_fetched": 0,
      "jobs_new": 0,
      "error": null
    }
  ],
  "dedupe": {
    "total_seen": 0,
    "new_jobs": 0,
    "duplicates_skipped": 0
  },
  "score_summary": {
    "min_score": 0,
    "max_score": 100,
    "mean_score": 0.0,
    "top_n": 20
  },
  "top_jobs": [
    {
      "id": "hash",
      "title": "Job-Titel",
      "company": "Firma",
      "location": "Ort",
      "remote": true,
      "salary_min": 45000,
      "url": "https://...",
      "source": "bundesagentur",
      "score": 85,
      "matched_keywords": ["AI Agent","Automation Specialist"]
    }
  ],
  "errors": [
    {
      "code": "API_FAIL",
      "source": "jooble",
      "message": "Timeout bei Suchanfrage",
      "suggestion": "Retry später oder API-Key prüfen"
    }
  ],
  "deliverables": {
    "report": "<pfad md>",
    "json": "<pfad json>",
    "db": "./db/jobs.db"
  }
}

## Regeln für Manager-freundliches Verhalten
1. Keine sensiblen Secrets im Report ausgeben.
2. Fehler immer mit Code, Quelle und Handlungsoption.
3. Keine Leerruns ohne Befundstillstand melden; `PARTIAL` ist eine gültige Endstatus.
4. Halte den Output kompatibel zu anderen Funktionsagenten: JSON zuerst, optional Report dahinter.

## Pfad-Autorität
- Root: `./skills/jobs/jobhunter/`
- Config: `./config.yaml`
- DB: `./db/jobs.db`
- Logs: `./logs/jobhunter.log`
- Output: `~/.openclaw/workspace/Arbeitsordner/Output/JobHunter/`
