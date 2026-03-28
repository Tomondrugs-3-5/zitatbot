import discord
from discord import app_commands
from discord.ui import View
import os
from datetime import datetime

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Bot ist online als {client.user}")

@tree.command(name="zitat", description="Füge ein Crewmate-Zitat hinzu")
@app_commands.describe(
    nachricht="Das Zitat",
    von_wem="Wer hat das gesagt? (optional, Standard: dein Name)",
    wann="Wann wurde das gesagt? (optional, z.B. 'gestern', '12.03.2026')"
)
async def zitat(
    interaction: discord.Interaction,
    nachricht: str,
    von_wem: str = None,
    wann: str = None
):
    # Fallback-Werte
    autor = von_wem if von_wem else interaction.user.display_name
    
    if wann:
        zeitpunkt_str = wann
    else:
        now = datetime.now()
        # Format: Sunday, March 15, 2026 5:50 PM
        zeitpunkt_str = now.strftime("%A, %B %d, %Y %-I:%M %p")

    # Embed bauen – gleicher Style wie im Screenshot
    embed = discord.Embed(
        color=0x9B59B6  # lila wie im Screenshot
    )

    embed.title = "💬  Zitat des Crewmates"
    embed.description = f'**"{nachricht}"**'

    embed.add_field(
        name="🧑 Gesagt von",
        value=f"@{autor}",
        inline=True
    )
    embed.add_field(
        name="📅 Zeitpunkt",
        value=zeitpunkt_str,
        inline=True
    )

    embed.set_footer(
        text=f"Zitat hinzugefügt von {interaction.user.display_name} • Among Us Server",
        icon_url=interaction.user.display_avatar.url if interaction.user.display_avatar else None
    )

    await interaction.response.send_message(embed=embed)


if __name__ == "__main__":
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        raise ValueError("DISCORD_TOKEN Umgebungsvariable nicht gesetzt!")
    client.run(token)
