#!/usr/bin/env python3
import os
import json
import codecs
from datetime import datetime
from duckduckgo_search import DDGS

# Pfade definieren
ROOT_DIR = "/home/rick/.openclaw/workspace/Automationen/Agents/LinkedInHunter"
OUTPUT_DIR = "/home/rick/.openclaw/workspace/Arbeitsordner/Output/LinkedInHunter"
HISTORY_FILE = os.path.join(ROOT_DIR, "history.json")
LEADS_FILE = os.path.join(OUTPUT_DIR, "leads.md")

# Verzeichnisse anlegen falls nicht existent
os.makedirs(ROOT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def search_linkedin_leads():
    history = load_history()
    new_leads = []

    # Such-Strings für die Zielgruppe
    queries = [
        'site:linkedin.com/in/ "Agentic AI" AND (CTO OR Founder OR "Gründer") Germany',
        'site:linkedin.com/in/ "LLMOps" AND (CTO OR Founder OR "Gründer") Germany'
    ]

    try:
        with DDGS() as ddgs:
            for query in queries:
                results = ddgs.text(query, max_results=15)
                for r in results:
                    url = r.get("href", "")
                    title = r.get("title", "")
                    snippet = r.get("body", "")

                    # Validierung: Ist es ein echtes Profil und noch nicht in der History?
                    if "linkedin.com/in/" in url and url not in history:
                        # Bereinige den Titel (LinkedIn-Muster entfernen)
                        clean_title = title.split("-")[0].strip()

                        lead = {
                            "title": clean_title,
                            "url": url,
                            "snippet": snippet,
                            "date_found": datetime.now().strftime("%Y-%m-%d %H:%M")
                        }
                        new_leads.append(lead)
                        history.append(url)
    except Exception as e:
        print(f"Fehler bei der Suche: {str(e)}")
        return

    if new_leads:
        write_leads_to_markdown(new_leads)
        save_history(history)
        print(f"[SUCCESS] {len(new_leads)} neue Leads gefunden und exportiert.")
    else:
        print("[INFO] Keine neuen Leads in diesem Zyklus gefunden.")

def write_leads_to_markdown(leads):
    file_exists = os.path.exists(LEADS_FILE)

    with codecs.open(LEADS_FILE, "a", "utf-8") as f:
        if not file_exists:
            f.write("# 🎯 Generierte LinkedIn Leads - Agentic AI & LLMOps\n\n")
            f.write("| Datum | Name / Position | Profil-Link | Beschreibung |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")

        for lead in leads:
            f.write(f"| {lead['date_found']} | {lead['title']} | [{lead['url']}]({lead['url']}) | {lead['snippet']} |\n")

if __name__ == "__main__":
    search_linkedin_leads()
