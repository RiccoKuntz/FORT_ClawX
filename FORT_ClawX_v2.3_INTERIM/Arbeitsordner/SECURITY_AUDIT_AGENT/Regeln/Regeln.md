SECURITY.md

 - Im Ordner `~/.openclaw/agents/main/sessions` soll Garvis nur maximal 20 Zeilen oder 2000 Zeichen pro Datei lesen, bevor er zur nächsten Datei geht. So verhindern wir plötzliche Tokenansiege von über 400k Tokens.
 - Garvis oder Agenten dürfen das Gateway nie selber neu starten. Sie müssen dafür immer Rick um erlaubnis fragen. KEINE ALLEINGÄNGE.
