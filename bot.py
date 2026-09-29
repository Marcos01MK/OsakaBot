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


# ============================================================
# INTENTS
# ============================================================

intents = discord.Intents.default()

intents.guilds = True
intents.members = True

# Necessário para a Osaka conseguir ler mensagens
intents.message_content = True


# ============================================================
# BOT
# ============================================================

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# ============================================================
# COMANDO /TICKET
# ============================================================

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

    # Somente você pode enviar o painel
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


# ============================================================
# EVENTO DE MENSAGENS
# ============================================================

@bot.event
async def on_message(message):

    # Ignora mensagens de bots
    if message.author.bot:
        return

    # ========================================================
    # EVENTO DO SAURUS
    # ========================================================

    await verificar_evento_saurus(
        message
    )

    # ========================================================
    # REAÇÕES DA OSAKA
    # ========================================================

    await verificar_reacoes(
        message
    )

    # ========================================================
    # MANTÉM OS COMANDOS FUNCIONANDO
    # ========================================================

    await bot.process_commands(
        message
    )


# ============================================================
# READY
# ============================================================

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


# ============================================================
# INICIAR
# ============================================================

bot.run(
    TOKEN
)