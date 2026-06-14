---
name: deepresearch-checkpoint
description: "Checkpoint-based DeepResearch with hard 5-tool-call limit and automatic recovery"
---

# DeepResearch Checkpoint Workflow V5.0.0

Stabile DeepResearch-Subagents durch harte Tool-Call-Limits und Checkpoint-Kompaktion.

## Problem
Subagents stürzen ab, wenn der Kontext ~128k Tokens erreicht. Die automatische Kompaktion von OpenClaw bricht die Tool-Calling-Struktur des Modells.

## Lösung: Hardlimit-Checkpoint-Workflow

### Regel #1: 5 Tool Calls = Checkpoint + STOP
Jeder Subagent hat ein hartes Limit von **5 Tool Calls** pro Phase.
Nach 5 Tool Calls MUSS ein Checkpoint geschrieben werden.
Keine Ausnahmen.

### Regel #2: Checkpoint VOR allem anderen
Erster Schritt beim Checkpoint:
1. `write(cache/comp/subquery_XXX.md)` – Ergebnisse speichern
2. `write(cache/comp/last_status.md)` – Fortschritt aktualisieren
3. `write(cache/comp/phase.md)` – Phase aktualisieren
4. **STOP** – Session sauber beenden

### Regel #3: Follow-up liest phase.md
Jeder neue Subagent liest ZUERST `cache/comp/phase.md` und `last_status.md`.
Nur wenn `phase=research_complete` → Report schreiben.
Wenn `phase=research_in_progress` → Genau dort weiter.

## Token-Management

### Geschätzte Token-Verbrauch pro Tool Call
| Tool | Geschätzte Tokens |
|------|------------------|
| duckduckgo-search | ~1.500 |
| web_search | ~1.500 |
| web_fetch | ~5.000-15.000 |
| write (klein) | ~500 |
| write (groß) | ~2.000-5.000 |

### Safe-Zone
- **0-5 Tool Calls:** < 30k Tokens – sicher
- **5-10 Tool Calls:** 30-60k Tokens – Checkpoint empfohlen
- **10-15 Tool Calls:** 60-90k Tokens – **Checkpoint ZWINGEND**
- **15+ Tool Calls:** 90k+ Tokens – **CRITICAL**

### Faustregel
**Nach 5 Tool Calls → Checkpoint. Immer.**
Das hält den Kontext unter 30k Tokens und ist weit entfernt vom 128k-Limit.

## Cache-Struktur
```
cache/comp/
├── last_status.md       # IMMER aktuell
├── phase.md             # Phase-Status
├── subquery_001.md      # Sub-Query 1 Ergebnisse
├── subquery_002.md      # Sub-Query 2 Ergebnisse
└── report.md            # Finaler Report
```

## Workflow

### Phase 1 – Research (Subagent A)
1. Prüfe phase.md – existiert bereits ein Checkpoint?
2. Wenn nein: Zerlege Query in max 5 Sub-Queries
3. Pro Sub-Query:
   - duckduckgo-search → web_fetch → MAX 1 Link Following
   - write(subquery_XXX.md) → write(last_status.md) → write(phase.md)
4. Nach jedem Sub-Query: Tool-Call-Counter prüfen
5. Bei 5 total: STOP

### Phase 2 – Continue (Subagent B)
1. Lese phase.md + last_status.md
2. Wenn phase=research_in_progress:
   - Lese alle subquery_*.md
   - Fahre mit nächstem Sub-Query fort
   - Checkpoint nach max. 5 Tool Calls
3. Wenn phase=research_complete:
   - Lese alle subquery_*.md
   - Schreibe report.md
   - update(phase.md) → report_complete
   - STOP

## Critical Rules
- `last_status.md` und `phase.md` sind IMMER aktuell
- Keine Ergebnisse im Kontext lassen – alles in `cache/comp/` schreiben
- **5 Tool Calls = Checkpoint + STOP** (absolute Regel)
- Follow-up-Subagent MUSS `phase.md` lesen bevor es handelt
- Wenn `phase=research_in_progress` → Recherche fortsetzen, NICHT Report schreiben
- **Max 5 Sub-Queries pro Recherche**
