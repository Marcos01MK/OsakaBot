import discord
import os


PASTA_AUDIOS = "audios"


async def enviar_audio(
    message: discord.Message,
    nome_audio: str,
    nome_personagem: str
):
    caminho_audio = os.path.join(
        PASTA_AUDIOS,
        nome_audio
    )

    # Verifica se o arquivo existe
    if not os.path.isfile(caminho_audio):
        print(
            f"⚠️ Áudio não encontrado: {caminho_audio}"
        )

        await message.channel.send(
            f"⚠️ Eu procurei meu áudio de "
            f"{nome_personagem}, mas não achei ele 😭"
        )

        return

    try:
        await message.channel.send(
            file=discord.File(
                caminho_audio,
                filename=nome_audio
            )
        )

        print(
            f"🌸 Reação '{nome_personagem}' "
            f"ativada por {message.author}"
        )

    except Exception as e:
        print(
            f"❌ Erro ao enviar "
            f"{nome_personagem}: {e}"
        )


# ============================================================
# SATA ANDAGI
# ============================================================

async def verificar_reacao_sata_andagi(
    message: discord.Message
):

    if message.author.bot:
        return

    texto = message.content.lower()

    frases_sata = [
        "sata andagi",
        "sata-andagi",
        "sataandagi"
    ]

    if not any(
        frase in texto
        for frase in frases_sata
    ):
        return

    await enviar_audio(
        message,
        "sata_andagi.mp3",
        "SATA ANDAGI"
    )


# ============================================================
# AMERICA YA
# ============================================================

async def verificar_reacao_america(
    message: discord.Message
):

    if message.author.bot:
        return

    texto = message.content.lower()

    frases = [
        "america ya",
        "americaia",
        "america ya!"
    ]

    if not any(
        frase in texto
        for frase in frases
    ):
        return

    await enviar_audio(
        message,
        "america_ya.mp3",
        "AMERICA YA"
    )


# ============================================================
# AAAAAAAA
# ============================================================

async def verificar_reacao_aaaa(
    message: discord.Message
):

    if message.author.bot:
        return

    texto = message.content.lower()

    # Detecta sequências grandes de "a"
    if "aaaa" not in texto:
        return

    await enviar_audio(
        message,
        "aaaa.mp3",
        "AAAAAAAA"
    )


# ============================================================
# HEYCHU
# ============================================================

async def verificar_reacao_heychu(
    message: discord.Message
):

    if message.author.bot:
        return

    texto = message.content.lower()

    frases = [
        "você está doente",
        "voce esta doente",
        "está doente",
        "esta doente",
        "você tá doente",
        "voce ta doente",
        "tá doente",
        "ta doente",
        "está gripada",
        "esta gripada",
        "tá gripada",
        "ta gripada",
        "está gripado",
        "esta gripado",
        "tá gripado",
        "ta gripado",
        "gripada?",
        "gripado?"
    ]

    if not any(
        frase in texto
        for frase in frases
    ):
        return

    await enviar_audio(
        message,
        "heychu.mp3",
        "HEYCHU"
    )


# ============================================================
# MERRY CHRISTMAS
# ============================================================

async def verificar_reacao_merry_christmas(
    message: discord.Message
):

    if message.author.bot:
        return

    texto = message.content.lower()

    frases = [
        "merry christmas",
        "merry christmasu",
        "feliz natal"
    ]

    if not any(
        frase in texto
        for frase in frases
    ):
        return

    await enviar_audio(
        message,
        "merry_christmas.mp3",
        "MERRY CHRISTMASUUUUUUUUU"
    )


# ============================================================
# YAMAPIKAYA
# ============================================================

async def verificar_reacao_yamapikaya(
    message: discord.Message
):

    if message.author.bot:
        return

    texto = message.content.lower()

    frases = [
        "yamapikaya",
        "yamapikayaa",
        "yamapikayaaaa",
        "yamapikayaaaaaaaa"
    ]

    if not any(
        frase in texto
        for frase in frases
    ):
        return

    await enviar_audio(
        message,
        "yamapikayaaaa.mp3",
        "YAMAPIKAYAAAAAAAAAAAAA"
    )


# ============================================================
# OMAIGAAAA
# ============================================================

async def verificar_reacao_omaigaaaa(
    message: discord.Message
):

    if message.author.bot:
        return

    texto = message.content.lower()

    frases = [
        "omaigaa",
        "omaigaaaa",
        "omaigaaaaa",
        "oh my god",
        "oh my gaa",
        "OMAIGAAA",
        "OMAIGAA",
        "OMAIGA",
        "omaiga",
        "mds",
        "MDS",
        "Meu Deus"
    ]

    if not any(
        frase in texto
        for frase in frases
    ):
        return

    await enviar_audio(
        message,
        "omaigaaaa.mp3",
        "OMAIGAAAA"
    )


# ============================================================
# CENTRAL DE REAÇÕES
# ============================================================

async def verificar_reacoes(
    message: discord.Message
):

    if message.author.bot:
        return

    await verificar_reacao_sata_andagi(message)

    await verificar_reacao_america(message)

    await verificar_reacao_aaaa(message)

    await verificar_reacao_heychu(message)

    await verificar_reacao_merry_christmas(message)

    await verificar_reacao_yamapikaya(message)

    await verificar_reacao_omaigaaaa(message)