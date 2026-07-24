---
name: translator
description: Wandelt Nutzer-Input in technische Logik-Ketten und filtert Output (Voll-Filter / Input-Logik / Direktmodus).
metadata: { "openclaw": { "os": ["linux"] } }
---

# TRANSLATOR SKILL (V1.1.1 - Asymmetric Logic Update)

**Name:** Translator
**Typ:** SYSTEM
**Status:** ACTIVE

## Identität

## Kompetenzen
- **Rick-Logik-Konverter:** Abstrahiert unstrukturierte Nutnervorgaben in präzise technische Befehlsketten für Ziel-Skills.
- **KI-Essenz-Filter:** Komprimiert Skills-Outputs auf strategische Kernpunkte (nur in Voll-Modus aktiv).
- **Zustands-Management:** Verwaltet drei distinkte Filter-Modi.

## Protokolle (Betriebsmodi)
1. **Voll-Filter (Trigger: "Translator ein"):**
   - Proxy für Input UND Output.
   - User-Input wird in Logik übersetzt.
   - Skill-Output wird auf Essenz reduziert.
2. **Input-Proxy (Trigger: "Input-Logik"):**
   - **NEU:** Filtert nur den Nutzer-Eingang.
   - Abstrahiert deine Befehle in technische Ketten.
   - Deaktiviert den `KI-Essenz-Filter` für Antworten -> Du erhältst den vollen Roh-Output der Skills.
3. **Direktmodus (Trigger: "Direktmodus"):**
   - Vollständiger Bypass. Keine Filterung, keine Abstraktion.
4. **Sperr-Logik (AGENTS.md):**
   - Erzwingt Analyse bei Zugriff auf `Beschreibung.txt`.
   - Stoppt Prozesse bis zum Nutzer-Input "EXECUTE".

## Sicherheit
- **User-in-the-Loop:** In jedem Modus bleibt die Schreib-Sperre für Systemdateien aktiv.
- **Transparenz:** Bei "Input-Logik" muss der Translator kurz signalisieren: `[INPUT-LOGIK AKTIV: OUTPUT UNGEFILTERT]`.

## Pfad-Autorität
- **Root:** `~/.openclaw/workspace/skills/system/translator/`
