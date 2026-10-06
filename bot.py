import discord
from discord.ext import commands
from discord import app_commands

from config import (
    TOKEN,
    GUILD_ID,
    COR_OSAKA
)

from tickets import (
    TicketView,
    FecharTicketView,
    enviar_painel_ticket
)

from eventos import verificar_evento_saurus

from reacoes import verificar_reacoes

intents = discord.Intents.default()

intents.guilds = True
intents.members = True
intents.message_content = True


bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.tree.command(
    name="ticket",
    description="Enviar o painel de atendimento"
)

@app_commands.guilds(
    discord.Object(
        id=GUILD_ID
    )
)

async def ticket(
    interaction: discord.Interaction
):
    if interaction.user.id != __import__(
        "config"
    ).OWNER_ID:

        await interaction.response.send_message(
            "❌ Apenas o responsável pode "
            "enviar o painel de tickets.",
            ephemeral=True
        )

        return

    await enviar_painel_ticket(
        interaction
    )

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    await verificar_evento_saurus(
        message
    )
    await verificar_reacoes(
        message
    )
    await bot.process_commands(
        message
    )

@bot.event
async def on_ready():

    print(
        f"🌸 Osaka-san online como {bot.user}"
    )

    try:

        synced = await bot.tree.sync(
            guild=discord.Object(
                id=GUILD_ID
            )
        )

        print(
            f"✅ {len(synced)} comando(s) sincronizado(s)."
        )

    except Exception as e:

        print(
            f"❌ Erro ao sincronizar comandos: {e}"
        )

bot.run(
    TOKEN
)