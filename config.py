import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# TOKEN
# ============================================================

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("❌ TOKEN não encontrado no arquivo .env")


# ============================================================
# ID DO SERVIDOR
# ============================================================

GUILD_ID = 1541218856163352666

# ID DA CATEGORIA ONDE OS TICKETS SERÃO CRIADOS
TICKET_CATEGORY_ID = 1541247952704639076

# SEU ID
OWNER_ID = 839137533496918036


# ============================================================
# IDENTIDADE VISUAL DA OSAKA
# ============================================================

# Rosa #FF1493
COR_OSAKA = 0xFF1493


# ============================================================
# IMAGENS
# ============================================================

# Banner grande da Osaka
BANNER_URL = (
    "https://i.pinimg.com/originals/"
    "c1/e9/62/c1e9624717b88515e6f16d7b67437c40.png"
)

# Imagem pequena no canto superior direito
THUMBNAIL_URL = (
    "https://encrypted-tbn0.gstatic.com/images?"
    "q=tbn:ANd9GcQhISjLKOnR0mvvUeiSUdv6y6JutQFfl5ZffexVCF0uicRyNT71-41TOEE"
    "&s=10"
)


# ============================================================
# TEXTO DO PAINEL PRINCIPAL
# ============================================================

PAINEL_TITULO = (
    "🌸 Osaka-san • Central de Atendimento"
)

PAINEL_DESCRICAO = (
    "So ya... Bem-vindo ao nosso sistema de atendimento!\n\n"
    "Selecione abaixo o tipo de atendimento que você deseja.\n\n"
    "Nossa equipe estará disponível para ajudá-lo.\n\n"
    "SATA ANDAGI!"
)

PAINEL_RODAPE = (
    "Osaka-san • Central de Atendimento"
)


# ============================================================
# TEXTO QUE APARECE DENTRO DO TICKET
# ============================================================

TICKET_TITULO = (
    "🌸 Osaka-san"
)

TICKET_DESCRICAO = (
    "Olá, {usuario}!\n\n"
    "Seu atendimento foi aberto com sucesso.\n\n"
    "Explique detalhadamente o que você precisa "
    "e aguarde a nossa equipe."
)

TICKET_RODAPE = (
    "Osaka-san • Sistema de Atendimento"
)


# ============================================================
# TIPOS DE ATENDIMENTO
# ============================================================

TIPOS_TICKET = {

    "suporte": {
        "label": "🛠️ Suporte",
        "descricao": (
            "Precisa de ajuda com alguma coisa?"
        ),
        "nome": "suporte"
    },

    "compras": {
        "label": "🛒 Compras",
        "descricao": (
            "Dúvidas sobre compras ou pedidos."
        ),
        "nome": "compras"
    },

    "parcerias": {
        "label": "🤝 Parcerias",
        "descricao": (
            "Entre em contato para parcerias."
        ),
        "nome": "parceria"
    },

    "outros": {
        "label": "❓ Outros",
        "descricao": (
            "Outro tipo de atendimento."
        ),
        "nome": "outros"
    },

    "denuncia": {
        "label": "🚨 Denúncias",
        "descricao": (
            "Realizar uma denúncia."
        ),
        "nome": "denuncia"
    }
}


# ============================================================
# CARGOS DA EQUIPE
# ============================================================

# Primeiro cargo da equipe
STAFF_ROLE_1_ID = 1541235613208940624

# Segundo cargo da equipe
STAFF_ROLE_2_ID = 1541237646683144303