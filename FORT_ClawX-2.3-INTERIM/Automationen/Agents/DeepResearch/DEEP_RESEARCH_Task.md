# DEEP_RESEARCH Task Reference (V1.0.0)

## Ausgabeformat für DeepResearch Reports

Jeder DeepResearch Report MUSS folgende Struktur haben:

### 1. Executive Summary
- 3-5 Sätze mit den Kernergebnissen

### 2. Detaillierte Analyse
- Unterpunkte mit Fakten und Confidence Scores
- Quellenreferenzen pro Fakt

### 3. Widersprüche & Wissenslücken
- Explizite Auflistung widersprüchlicher Aussagen
- Offene Fragen und warum sie nicht beantwortet werden konnten

### 4. Quellenverzeichnis
- Nummerierte Liste mit Titel, URL und Autoritätsscore

## Verwendung

Rick schreibt die Forschungsfrage direkt im Chat.
Garvis analysiert die Frage, fasst sie zusammen und präsentiert einen Recherche-Plan.
Nach Bestätigung und EXECUTE wird DeepResearch als Subagent mit 24h Timeout geparst.

## Status
READ-ONLY für Agenten (AGENTS.md Protokoll)
Nur Rick darf diese Datei bearbeiten.
