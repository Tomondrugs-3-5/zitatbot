# 💬 Among Us Zitat-Bot

Ein Discord-Bot, der mit `/zitat` schöne Crewmate-Zitat-Embeds postet.

## Befehl

```
/zitat nachricht:(text) von_wem:(optional) wann:(optional)
```

**Beispiele:**
- `/zitat nachricht:Mach das Handy weg und spring weiter`
- `/zitat nachricht:Sus! von_wem:Tom wann:Sunday, March 15, 2026`

---

## Setup: Discord Developer Portal

1. Gehe zu https://discord.com/developers/applications
2. Klicke **New Application** → Namen eingeben
3. Links auf **Bot** → **Add Bot**
4. Unter **Privileged Gateway Intents**: nichts nötig für diesen Bot
5. Klicke **Reset Token** → Token kopieren (brauchst du gleich!)
6. Gehe zu **OAuth2 → URL Generator**:
   - Scopes: `bot`, `applications.commands`
   - Bot Permissions: `Send Messages`, `Embed Links`
7. Den generierten Link im Browser öffnen → Bot zu deinem Server einladen

---

## Deployment auf Railway

1. Gehe zu https://railway.app und logge dich ein (mit GitHub)
2. Klicke **New Project → Deploy from GitHub repo**
   - Oder: **Deploy from local** → diese 3 Dateien hochladen
3. Im Projekt: **Variables** → neue Variable hinzufügen:
   - Key: `DISCORD_TOKEN`
   - Value: (dein Bot-Token von oben)
4. Railway startet den Bot automatisch!

---

## Dateien

| Datei | Beschreibung |
|-------|-------------|
| `bot.py` | Der Bot-Code |
| `requirements.txt` | Python-Abhängigkeiten |
| `railway.toml` | Railway-Konfiguration |
