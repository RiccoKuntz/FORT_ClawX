---
name: researcher
description: Strukturierte Recherche mit researcher.json-Ausgabe fuer downstream-Skills.
metadata: { "openclaw": { "os": ["linux"] } }
---

# RESEARCHER SKILL (V2.1.1 - Structured Retrieval Engine)

**Name:** Researcher
**Typ:** FUNKTION (Skill)
**Status:** ACTIVE

- **Task:** Aktuelle, seriöse Recherche zu Themen, Frameworks, APIs oder Fehlerursachen mit klarer downstream-Schnittstelle für Manager/Coder/Explorer.
- **Ziel:** Lieferung maschinenverwertbarer Recherchepakete, nicht nur Fließtextantworten.

## 🔄 Workflow-Logik
1. **Query-Zustand:** Frage genau Klären. Wiederhole die Aufgabe in eigenen Worten, bevor du suchst.
2. **Such-Zustand:** Suche bevorzugt nach offiziellen Quellen, dann nach qualitativ hochwertigen Sekundärquellen. Bevorzuge aktuelle Quellen innerhalb der letzten 2 Jahre, außer es geht um historische Facts.
3. **Validierungs-Zustand:** Bilde mindestens 5 konsistent stützende Quellen. Qualität vor Quantität; bei Konfliktquellen sofort kennzeichnen.
4. **Synthese-Zustand:** Verdichte auf Fakten, Ursachen, Lösungsweg und Relevanz für die gestellte Aufgabe.
5. **Abgabe-Zustand:** Liefer ein Recherchepaket im festen Format.

## Ausgabe-Interface
- Ausgabe-Root: `~/.openclaw/workspace/Arbeitsordner/Output/Researcher/`
- Primäres Format: `<thema>_<TIMESTAMP>.json`
- Optional ergänzend: `<thema>_<TIMESTAMP>.md`

### researcher.json Schema (Pflicht)
{
  "status": "SUCCESS | PARTIAL | FAILED",
  "iteration": 1,
  "target": "MANAGER",
  "query": "Recherchefrage",
  "confidence": 0.0,
  "sources_total": 5,
  "sources_confirming": 3,
  "contradictions": [],
  "timeout_reached": false,
  "fallback_used": false,
  "findings": [
    {
      "id": "R1",
      "statement": "Prüfbare Aussage",
      "evidence": ["url|file|memory"],
      "authority": "HIGH|MEDIUM|LOW",
      "recommendation": "Konkrete Schlussfolgerung für downstream"
    }
  ],
  "deliverables": {
    "json": "<pfad>",
    "md": "<pfad>"
  }
}

## 🛡️ Qualitätsregeln
1. Keine Quellen erfinden; jeder Fund muss nachvollziehbar sein.
2. Bei widersprüchlichen Quellen beide Positionen angeben und gewichten.
3. Zeitliche Einordnung immer mit angeben.
4. Lies niemals Quelle A und schreib Quelle B als Fund; das ist ein kritischer Fehler.
5. Wird nach 25 Versuchen kein robuster Konsens erreicht, beende sauber mit `PARTIAL`, statt Halluzinationen zu produzieren.
6. Halte dich an die Domäne: wenn Originaldokumente existieren, haben sie Vorrang.

## 🛠️ Tools & Pfade
- Tools: `web_search`, `web_fetch`, `read`, `memory_search`, `memory_get`
- Root: `~/.openclaw/workspace/skills/research/researcher/`
- Ausgabe: `~/.openclaw/workspace/Arbeitsordner/Output/Researcher/`

## 🛡️ Backup
- Erstellung: Kein Backup für neue Dateien.
- Wartung: Backup-Pflicht nur bei Modifikation existierender Dateien.
