import discord

from config import (
    TICKET_CATEGORY_ID,
    OWNER_ID,
    COR_OSAKA,
    BANNER_URL,
    THUMBNAIL_URL,
    PAINEL_TITULO,
    PAINEL_DESCRICAO,
    PAINEL_RODAPE,
    TICKET_TITULO,
    TICKET_DESCRICAO,
    TICKET_RODAPE,
    TIPOS_TICKET,
    STAFF_ROLE_1_ID,
    STAFF_ROLE_2_ID
)



ticket_counter = 0


def is_owner(user):
    return user.id == OWNER_ID


class FecharTicketView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="🔒 Fechar Ticket",
        style=discord.ButtonStyle.red,
        custom_id="osaka_fechar_ticket"
    )
    async def fechar(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if not is_owner(interaction.user):

            await interaction.response.send_message(
                "❌ Apenas o responsável pelo servidor "
                "pode fechar este ticket.",
                ephemeral=True
            )

            return

        await interaction.response.send_message(
            "🔒 Ticket será fechado em 5 segundos..."
        )

        import asyncio

        await asyncio.sleep(5)

        try:
            await interaction.channel.delete()

        except discord.NotFound:
            pass

class TipoTicketSelect(discord.ui.Select):

    def __init__(self):

        options = []

        for chave, dados in TIPOS_TICKET.items():

            options.append(
                discord.SelectOption(
                    label=dados["label"],
                    description=dados["descricao"][:100],
                    value=chave
                )
            )

        super().__init__(
            placeholder="🎫 Escolha o tipo de atendimento...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="osaka_tipo_ticket"
        )

    async def callback(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.defer(
            ephemeral=True
        )

        await criar_ticket(
            interaction,
            self.values[0]
        )

class TicketView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=None
        )

        self.add_item(
            TipoTicketSelect()
        )

async def criar_ticket(
    interaction: discord.Interaction,
    tipo: str
):

    global ticket_counter

    guild = interaction.guild
    usuario = interaction.user


    if tipo not in TIPOS_TICKET:

        await interaction.followup.send(
            "❌ Tipo de ticket inválido.",
            ephemeral=True
        )

        return

    dados = TIPOS_TICKET[tipo]


    # ========================================================
    # CATEGORIA
    # ========================================================

    categoria = guild.get_channel(
        TICKET_CATEGORY_ID
    )

    if categoria is None:

        await interaction.followup.send(
            "❌ Categoria de tickets não encontrada.",
            ephemeral=True
        )

        return


    # ========================================================
    # TICKET EXISTENTE
    # ========================================================

    for canal in categoria.channels:

        if canal.topic and f"Ticket de {usuario.id}" in canal.topic:

            await interaction.followup.send(
                f"❌ Você já possui um ticket: {canal.mention}",
                ephemeral=True
            )

            return


    # ========================================================
    # NÚMERO
    # ========================================================

    ticket_counter += 1

    numero = ticket_counter


    nome_canal = f"{dados['nome']}-{numero:04d}"



    overwrites = {

        # @everyone não vê
        guild.default_role: discord.PermissionOverwrite(
            view_channel=False
        ),

        # Cliente vê e escreve
        usuario: discord.PermissionOverwrite(
            view_channel=True,
            send_messages=True,
            read_message_history=True
        )
    }

    bot_member = guild.me

    if bot_member:

        overwrites[bot_member] = discord.PermissionOverwrite(
            view_channel=True,
            send_messages=True,
            read_message_history=True,
            embed_links=True,
            attach_files=True,
            manage_messages=True
        )


    dono = guild.get_member(
        OWNER_ID
    )

    if dono:

        overwrites[dono] = discord.PermissionOverwrite(
            view_channel=True,
            send_messages=True,
            read_message_history=True,
            manage_messages=True
        )


    staff_1 = guild.get_role(
        STAFF_ROLE_1_ID
    )

    if staff_1:

        overwrites[staff_1] = discord.PermissionOverwrite(
            view_channel=True,
            send_messages=True,
            read_message_history=True
        )

    staff_2 = guild.get_role(
        STAFF_ROLE_2_ID
    )

    if staff_2:

        overwrites[staff_2] = discord.PermissionOverwrite(
            view_channel=True,
            send_messages=True,
            read_message_history=True
        )


    canal = await guild.create_text_channel(
        name=nome_canal,
        category=categoria,
        overwrites=overwrites,
        topic=(
            f"Ticket de {usuario.id} | "
            f"Tipo: {tipo} | "
            f"Pedido #{numero:04d}"
        )
    )


    descricao = TICKET_DESCRICAO.format(
        usuario=usuario.mention
    )

    embed = discord.Embed(
        title=TICKET_TITULO,
        description=descricao,
        color=discord.Color(COR_OSAKA)
    )


    if THUMBNAIL_URL:

        embed.set_thumbnail(
            url=THUMBNAIL_URL
        )


    if BANNER_URL:

        embed.set_image(
            url=BANNER_URL
        )


    embed.add_field(
        name="🎫 Ticket",
        value=f"#{numero:04d}",
        inline=True
    )

    embed.add_field(
        name="📂 Atendimento",
        value=dados["label"],
        inline=True
    )

    embed.add_field(
        name="👤 Cliente",
        value=usuario.mention,
        inline=True
    )

    embed.add_field(
        name="📋 Sobre",
        value=dados["descricao"],
        inline=False
    )


    embed.set_footer(
        text=TICKET_RODAPE
    )


    mencoes = []

    if staff_1:

        mencoes.append(
            staff_1.mention
        )

    if staff_2:

        mencoes.append(
            staff_2.mention
        )


    mensagem_osaka = (
        f"{usuario.mention}\n\n"
        f"{' '.join(mencoes)}\n\n"
        "So ya... Osaka-san já entrou em contato "
        "com a Chiyo-chan, ela vai chamar os ADMs! 🌸"
    )


    await canal.send(
        content=mensagem_osaka,
        embed=embed,
        view=FecharTicketView()
    )


    await interaction.followup.send(
        f"🎫 Seu ticket foi criado: {canal.mention}",
        ephemeral=True
    )

async def enviar_painel_ticket(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title=PAINEL_TITULO,
        description=PAINEL_DESCRICAO,
        color=discord.Color(COR_OSAKA)
    )


    if THUMBNAIL_URL:

        embed.set_thumbnail(
            url=THUMBNAIL_URL
        )



    if BANNER_URL:

        embed.set_image(
            url=BANNER_URL
        )


    embed.set_footer(
        text=PAINEL_RODAPE
    )


    await interaction.response.send_message(
        embed=embed,
        view=TicketView()
    )