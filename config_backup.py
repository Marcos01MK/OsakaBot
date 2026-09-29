import discord
from config import (
    GUILD_ID,
    TICKET_CATEGORY_ID,
    OWNER_ID,
    COR_OSAKA
)


# ============================================================
# CONTADOR DOS TICKETS
# ============================================================

ticket_counter = 0


# ============================================================
# VERIFICAR DONO
# ============================================================

def is_owner(user):

    return user.id == OWNER_ID


# ============================================================
# BOTÃO DE FECHAR
# ============================================================

class FecharTicketView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=None
        )


    @discord.ui.button(
        label="🔒 Fechar Ticket",
        style=discord.ButtonStyle.red,
        custom_id="fechar_ticket_osaka"
    )
    async def fechar(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if not is_owner(
            interaction.user
        ):

            await interaction.response.send_message(

                "❌ Apenas o responsável pelo servidor "
                "pode fechar este ticket.",

                ephemeral=True
            )

            return


        await interaction.response.send_message(

            "🔒 Este ticket será fechado em 5 segundos..."
        )

        import asyncio

        await asyncio.sleep(5)

        await interaction.channel.delete()


# ============================================================
# CRIAR TICKET
# ============================================================

async def criar_ticket(
    interaction: discord.Interaction
):

    global ticket_counter

    guild = interaction.guild
    usuario = interaction.user


    # --------------------------------------------------------
    # PEGAR CATEGORIA
    # --------------------------------------------------------

    categoria = guild.get_channel(
        TICKET_CATEGORY_ID
    )


    if categoria is None:

        await interaction.response.send_message(

            "❌ A categoria de tickets não foi encontrada.",

            ephemeral=True
        )

        return


    # --------------------------------------------------------
    # VERIFICAR SE JÁ POSSUI TICKET
    # --------------------------------------------------------

    for canal in categoria.channels:

        if canal.topic:

            if (
                f"Ticket de {usuario.id}"
                in canal.topic
            ):

                await interaction.response.send_message(

                    f"❌ Você já possui um ticket: "
                    f"{canal.mention}",

                    ephemeral=True
                )

                return


    # --------------------------------------------------------
    # CONTADOR
    # --------------------------------------------------------

    ticket_counter += 1

    numero = ticket_counter


    # --------------------------------------------------------
    # NOME DO CANAL
    # --------------------------------------------------------

    nome = f"ticket-{numero:04d}"


    # --------------------------------------------------------
    # PERMISSÕES
    # --------------------------------------------------------

    overwrites = {

        guild.default_role:
            discord.PermissionOverwrite(
                view_channel=False
            ),

        usuario:
            discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                read_message_history=True
            )
    }


    # Você sempre terá acesso
    dono = guild.get_member(
        OWNER_ID
    )


    if dono:

        overwrites[dono] = (
            discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                read_message_history=True,
                manage_messages=True
            )
        )


    # --------------------------------------------------------
    # CRIAR CANAL
    # --------------------------------------------------------

    canal = await guild.create_text_channel(

        name=nome,

        category=categoria,

        overwrites=overwrites,

        topic=(
            f"Ticket de {usuario.id} | "
            f"Pedido #{numero:04d}"
        )
    )


    # --------------------------------------------------------
    # EMBED
    # --------------------------------------------------------

    embed = discord.Embed(

        title="🌸 Osaka-san",

        description=(

            f"Olá, {usuario.mention}!\n\n"

            "Seu ticket foi aberto com sucesso.\n\n"

            "Explique aqui o que você precisa "
            "e aguarde o atendimento."
        ),

        color=discord.Color(
            COR_OSAKA
        )
    )


    embed.add_field(

        name="🎫 Ticket",

        value=f"#{numero:04d}",

        inline=True
    )


    embed.add_field(

        name="👤 Cliente",

        value=usuario.mention,

        inline=True
    )


    embed.set_footer(

        text="Osaka-san • Sistema de Atendimento"
    )


    # --------------------------------------------------------
    # ENVIAR MENSAGEM
    # --------------------------------------------------------

    await canal.send(

        content=usuario.mention,

        embed=embed,

        view=FecharTicketView()
    )


    # --------------------------------------------------------
    # RESPONDER AO USUÁRIO
    # --------------------------------------------------------

    await interaction.response.send_message(

        f"🎫 Seu ticket foi criado: {canal.mention}",

        ephemeral=True
    )


# ============================================================
# PAINEL DE TICKET
# ============================================================

class TicketView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=None
        )


    @discord.ui.button(

        label="🎫 Abrir Ticket",

        style=discord.ButtonStyle.primary,

        custom_id="abrir_ticket_osaka"
    )
    async def abrir(

        self,

        interaction: discord.Interaction,

        button: discord.ui.Button

    ):

        await criar_ticket(
            interaction
        )


# ============================================================
# ENVIAR PAINEL
# ============================================================

async def enviar_painel_ticket(
    interaction: discord.Interaction
):

    embed = discord.Embed(

        title="🎫 Atendimento",

        description=(

            "Precisa de ajuda?\n\n"

            "Clique no botão abaixo para abrir "
            "um ticket privado com a equipe.\n\n"

            "🌸 **Osaka-san estará esperando por você!**"
        ),

        color=discord.Color(
            COR_OSAKA
        )
    )


    embed.set_footer(

        text="Osaka-san • Sistema de Atendimento"
    )


    await interaction.response.send_message(

        embed=embed,

        view=TicketView()
    )