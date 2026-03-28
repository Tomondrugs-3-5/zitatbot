import discord
from discord import app_commands
import os
from datetime import datetime

# ─── Farb-Palette ─────────────────────────────────────────────────────────────
EMBED_COLOR = 0x7B2FBE   # leuchtendes Lila/Violett (Among-Us-Style)


def build_zitat_embed(
    nachricht: str,
    autor: str,
    zeitpunkt_str: str,
    user: discord.User,
    guild_name: str,
) -> discord.Embed:

    embed = discord.Embed(color=EMBED_COLOR)

    # Titel + Zitat als Code-Block (monospace, lesbar, copyable)
    embed.description = (
        "### 🗣  Zitat des Crewmates\n"
        f"```\n{nachricht}\n```"
    )

    # Felder: Autor | Zeitpunkt | (leer für symmetrie)
    embed.add_field(
        name="👤  Gesagt von",
        value=f"**@{autor}**",
        inline=True,
    )
    embed.add_field(
        name="📅  Zeitpunkt",
        value=f"🕐  {zeitpunkt_str}",
        inline=True,
    )
    # Dritte leere Spalte hält die 2 Felder links ausgerichtet
    embed.add_field(name="\u200b", value="\u200b", inline=True)

    # Optische Trennlinie
    embed.add_field(
        name="\u200b",
        value="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        inline=False,
    )

    # Footer mit Zeitstempel + Server-Name
    jetzt = datetime.now().strftime("%-d.%-m.%Y %H:%M")
    embed.set_footer(
        text=f"Hinzugefügt von {user.display_name}  •  {guild_name}  •  {jetzt} Uhr",
        icon_url=user.display_avatar.url if user.display_avatar else None,
    )

    return embed


intents = discord.Intents.default()
client  = discord.Client(intents=intents)
tree    = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"✅  Bot online als {client.user}  (ID: {client.user.id})")


@tree.command(name="zitat", description="📌 Verewige ein Crewmate-Zitat")
@app_commands.describe(
    nachricht = "Das Zitat – was wurde gesagt?",
    von_wem   = "Wer hat das gesagt? (optional – Standard: du)",
    wann      = "Wann? (optional – z.B. 'gestern', 'IMMER', '15.03.2026')",
)
async def zitat(
    interaction: discord.Interaction,
    nachricht: str,
    von_wem:   str = None,
    wann:      str = None,
):
    autor      = von_wem if von_wem else interaction.user.display_name
    guild_name = interaction.guild.name if interaction.guild else "Among Us Server"

    if wann:
        zeitpunkt_str = wann
    else:
        now    = datetime.now()
        tage   = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
        monate = ["Januar","Februar","März","April","Mai","Juni",
                  "Juli","August","September","Oktober","November","Dezember"]
        zeitpunkt_str = (
            f"{tage[now.weekday()]}, {now.day}. {monate[now.month-1]} {now.year}, "
            f"{now.strftime('%H:%M')} Uhr"
        )

    embed = build_zitat_embed(
        nachricht=nachricht,
        autor=autor,
        zeitpunkt_str=zeitpunkt_str,
        user=interaction.user,
        guild_name=guild_name,
    )

    await interaction.response.send_message(embed=embed)


if __name__ == "__main__":
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        raise ValueError("❌  DISCORD_TOKEN Umgebungsvariable nicht gesetzt!")
    client.run(token)
