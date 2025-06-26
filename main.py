import os
import discord
from discord.ext import commands
from discord import ButtonStyle, Interaction
from discord.ui import View, button
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
BUTTON_CHANNEL_ID = int(os.getenv("BUTTON_CHANNEL_ID"))
MESSAGE_CHANNEL_ID = int(os.getenv("MESSAGE_CHANNEL_ID"))
ROLLE_ID = int(os.getenv("ROLLE_ID"))

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

class ÖffnungsView(View):
    @button(label="📢 Öffnen", style=ButtonStyle.success, custom_id="open")
    async def öffnen(self, interaction: Interaction, button: discord.ui.Button):
        if not any(role.id == ROLLE_ID for role in interaction.user.roles):
            await interaction.response.send_message("❌ Du hast keine Berechtigung.", ephemeral=True)
            return

        kanal = bot.get_channel(MESSAGE_CHANNEL_ID)
        if kanal:
            await kanal.send("📢 Wir haben jetzt geöffnet!")
        await interaction.response.send_message("✅ Meldung gesendet.", ephemeral=True)

    @button(label="🔒 Schließen", style=ButtonStyle.danger, custom_id="close")
    async def schließen(self, interaction: Interaction, button: discord.ui.Button):
        if not any(role.id == ROLLE_ID for role in interaction.user.roles):
            await interaction.response.send_message("❌ Du hast keine Berechtigung.", ephemeral=True)
            return

        kanal = bot.get_channel(MESSAGE_CHANNEL_ID)
        if kanal:
            await kanal.send("🔒 Wir schließen jetzt.")
        await interaction.response.send_message("✅ Meldung gesendet.", ephemeral=True)

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")
    kanal = bot.get_channel(BUTTON_CHANNEL_ID)
    if kanal:
        await kanal.send("🕒 Öffnungsstatus steuern:", view=ÖffnungsView())

keep_alive()
bot.run(MTM4Nzg3NDk5MDUzOTU0MjY3OQ.GP-NiJ.YG8TQHLQFhidYsXk--NGSUAGTJA-C6VH8zAM2Q)
