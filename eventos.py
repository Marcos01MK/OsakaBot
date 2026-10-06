import discord
import re


GIF_OSAKA_CHOQUE = "https://media1.tenor.com/m/SiRpGBwmY4oAAAAC/azumanga-azumanga-daioh.gif"
GIF_OSAKA_CHORANDO = "https://media1.tenor.com/m/ODFy4zme6d4AAAAd/osaka-azumanga-daioh.gif"


# ============================================================
# MEMÓRIA TEMPORÁRIA DOS EVENTOS
# ============================================================

# Guarda usuários que acabaram de falar sobre o Saurus.
# Exemplo:
#
# usuario_id -> True
#
# Isso permite que a Osaka entenda:
#
# "Osaka, o Saurus morreu"
# "é verdade"
#
# como duas mensagens relacionadas.

saurus_eventos = {}


# ============================================================
# PALAVRAS RELACIONADAS
# ============================================================

PALAVRAS_SAURUS = [
    "saurus",
    "sauro",
    "saurinhos"
]

PALAVRAS_DOENTE = [
    "doente",
    "doença",
    "adoeceu",
    "mal",
    "passando mal"
]

PALAVRAS_MORTE = [
    "morreu",
    "morto",
    "morte",
    "falecido",
    "faleceu",
    "mataram",
    "matei",
    "morrer"
]

PALAVRAS_CONFIRMACAO = [
    "sim",
    "é verdade",
    "e verdade",
    "verdade",
    "isso",
    "é",
    "foi",
    "morreu mesmo",
    "ele morreu",
    "eu matei",
    "matei ele"
]


# ============================================================
# FUNÇÃO AUXILIAR
# ============================================================

def contem_alguma(texto, palavras):

    texto = texto.lower()

    return any(
        palavra in texto
        for palavra in palavras
    )


# ============================================================
# EVENTO DO SAURUS
# ============================================================

async def verificar_evento_saurus(
    message: discord.Message
):

    if message.author.bot:
        return False


    texto = message.content.lower().strip()


    # ========================================================
    # CONFIRMAÇÃO DE MORTE
    # ========================================================

    if message.author.id in saurus_eventos:

        estado = saurus_eventos[message.author.id]


        if estado == "morte_pendente":

            if contem_alguma(
                texto,
                PALAVRAS_CONFIRMACAO
            ):

                del saurus_eventos[
                    message.author.id
                ]

                await message.channel.send(
                    "いややぁぁぁ……！"
                    "ザウルス…いややぁぁぁ……！\n\n"
                    "抱っこすんの、めっちゃ好きやってん…\n\n"
                    "なんで最後の時に、"
                    "離れてなアカンかったんやろぅ……"
                    "うぅぅ……。",
                    file=await baixar_gif(
                        GIF_OSAKA_CHORANDO
                    )
                )

                return True


    # ========================================================
    # SAURUS + MORTE
    # ========================================================

    if (
        contem_alguma(texto, PALAVRAS_SAURUS)
        and
        contem_alguma(texto, PALAVRAS_MORTE)
    ):

        saurus_eventos[
            message.author.id
        ] = "morte_pendente"

        await message.channel.send(
            "NANI?????",
            file=await baixar_gif(
                GIF_OSAKA_CHOQUE
            )
        )

        return True


    # ========================================================
    # SAURUS + DOENTE
    # ========================================================

    if (
        contem_alguma(texto, PALAVRAS_SAURUS)
        and
        contem_alguma(texto, PALAVRAS_DOENTE)
    ):

        await message.channel.send(
            "NANI?????",
            file=await baixar_gif(
                GIF_OSAKA_CHOQUE
            )
        )

        return True


    return False


# ============================================================
# BAIXAR GIF
# ============================================================

async def baixar_gif(url):

    import aiohttp
    import io

    if not url or url.startswith("COLE_AQUI"):
        return None

    try:

        async with aiohttp.ClientSession() as session:

            async with session.get(url) as resposta:

                if resposta.status != 200:
                    return None

                dados = await resposta.read()

        return discord.File(
            io.BytesIO(dados),
            filename="osaka.gif"
        )

    except Exception as erro:

        print(
            f"❌ Erro ao baixar GIF: {erro}"
        )

        return None