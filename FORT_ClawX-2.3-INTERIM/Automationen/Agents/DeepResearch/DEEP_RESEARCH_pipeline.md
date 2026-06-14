# DeepResearch Pipeline Orchestrator (V2.0.0 - Full Autonomous Pipeline)

## Zweck
Automatisierte Kette von Subagenten für DeepResearch. Nach jedem Checkpoint wird automatisch der nächste Subagent gestartet.

## Pipeline-Architektur

```
Forschungsfrage → Sub-Query Zerlegung
  → RecoveryAgent (Sub-Query Recherche, Checkpoint nach 5 Tool Calls)
  → RecoveryAgent (Follow-up, setzt fort wo aufgehört)
  → RecoveryAgent (wiederholt bis alle Sub-Queries abgeschlossen)
  → ReportGenerator (alle subquery_*.md → report.md)
  → Reports/ (finaler Report)
```

## Pipeline-Phasen

### Phase 0: Sub-Query-Zerlegung
1. Garvis zerlegt die Forschungsfrage in max 5 Sub-Queries
2. Jede Sub-Query wird als eigenständiger Subagent gestartet
3. Subagent-Parameter: runTimeoutSeconds=86400, mode="run"
4. Cache-Initialisierung: phase=waiting, last_status.md erstellen

### Phase 1: Sub-Query-Recherche (RecoveryAgent)
Der RecoveryAgent führt aus:
1. Lese phase.md und last_status.md
2. Wenn phase=waiting → setze phase=research_in_progress
3. Finde unvollständige Sub-Queries
4. Setze aktive Sub-Query fort
5. Führe web_search + web_fetch durch (max 5 Tool Calls)
6. Schreibe subquery_XXX.md mit Fakten, Confidence Scores, Quellen
7. Nach jedem 5. Tool Call: Schreibe Checkpoint (subquery + last_status + phase) → STOP
8. Redundanz-Check: used_search_terms aus last_status.md prüfen
9. Wenn alle Sub-Queries abgeschlossen → setze phase=report_complete → STOP

### Phase 2: Report-Generierung (ReportGenerator)
1. Lese ALLE subquery_XXX.md Dateien
2. Schreibe report.md mit:
   - Executive Summary (3-5 Sätze)
   - Detaillierte Analyse mit Confidence Scores
   - Widersprüche & Wissenslücken
   - Quellenverzeichnis mit Autoritätsscore
3. Kopiere report.md nach Reports/
4. Setze phase=report_complete

### Phase 3: Cleanup
1. Prüfe ob Reports/ die neueste report.md enthält
2. Erstelle Report-Log in Reports/Agentenlogs/
3. Setze phase=waiting für zukünftige Researchs

## Agenten-Referenz

### RecoveryAgent
- **Pfad:** `Automationen/Agents/DeepResearch/RecoveryAgent/RECOVERYAGENT_SOUL.md`
- **Aufgabe:** Sub-Query-Recherche, Checkpoint-Management, Follow-up Recovery
- **Tool-Limit:** 5 Tool Calls pro Phase

### ReportGenerator
- **Pfad:** `Automationen/Agents/DeepResearch/ReportGenerator/REPORTGENERATOR_SOUL.md`
- **Aufgabe:** Zusammenführung aller Sub-Query-Ergebnisse zum finalen Report
- **Tool-Limit:** Kein festes Limit (Lesen + Schreiben)

## Fehlerbehandlung

### Kein Fortschritt nach Checkpoint
- Wenn last_status.md existiert aber Subagent nicht weitermacht:
  - Prüfe ob used_search_terms alle relevanten Begriffe abdecken
  - Wenn ja → zu Phase 2 (Report) wechseln
  - Wenn nein → neue Suchbegriffe generieren und Subagent neu starten

### Subagent-Timeout
- Wenn Subagent nach 24h nicht fertig:
  - Prüfe phase.md und last_status.md
  - Wenn phase=research_in_progress → neuen Subagenten mit angepassten Suchbegriffen starten
  - Max 3 Wiederholungsversuche pro Sub-Query

### Keine Quellen gefunden
- Wenn web_search keine relevanten Quellen liefert:
  - Suchbegriff anpassen (Synonyme, breitere/narrowere Begriffe)
  - Neue Begriffe in last_status.md unter used_search_terms eintragen
  - Max 3 Anpassungen pro Sub-Query

## Pfad-Autorität
- **Root:** `/home/rick/.openclaw/workspace/Automationen/Agents/DeepResearch/`
- **Cache:** `cache/comp/`
- **Reports:** `Reports/`
- **Logs:** `Reports/Agentenlogs/`

## Status
- **Pipeline:** V2.0.0
- **Modus:** AUTOMATED
- **Letzte Aktualisierung:** 2026-06-01
