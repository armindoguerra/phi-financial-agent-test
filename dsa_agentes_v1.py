# Estudo de Caso - Deploy de Time de Agentes de IA com DeepSeek Para Análise de Inteligência de Mercado

# Imports
import os
import socket
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# Verificação antes de carregar variáveis de ambiente
if os.path.exists(".env"):
    load_dotenv()
    print("Variáveis de ambiente carregadas.")
else:
    print(
        "Arquivo .env não encontrado. Algumas configurações podem estar ausentes."
    )


# Função para verificar conexão com a internet
def verificar_conexao():
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        print("Conexão com a internet verificada.")
        return True
    except OSError:
        print(
            "Sem conexão com a internet! Algumas ferramentas podem não funcionar."
        )
        return False


# Executa a função
conexao_estabelecida = verificar_conexao()

# Criando Agentes de IA
print("Inicializando agentes...")

# Define o Agente Financeiro
agente_financeiro = Agent(
    name="Analista Financeiro",
    model=OpenAIChat(id="gpt-5.4"),
    tools=(
        [
            YFinanceTools(
                stock_price=True, analyst_recommendations=True, stock_fundamentals=True
            )
        ]
        if conexao_estabelecida
        else []
    ),  # Evita erro se não houver conexão
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Crie tabelas para comparações",
        "Gere os resultados com o idioma Português do Brasil",
    ],
)

print("Agente agente_financeiro inicializado com o modelo gpt-oss-120b")

# Define o Agente de Pesquisa
agente_pesquisa = Agent(
    name="Pesquisador Web",
    model=OpenAIChat(id="gpt-5.4"),
    tools=(
        [DuckDuckGo()] if conexao_estabelecida else []
    ),  # Evita erro se não houver conexão
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Inclua sempre as fontes das informações que você coleta",
        "Gere os resultados com o idioma Português do Brasil",
        "Use fontes confiáveis, você é um Analista de Pesquisa Sênior",
    ],
)

print("Agente agente_pesquisa inicializado com o modelo gpt-oss-120b")

# Define o Time de Agentes
time_agentes = Agent(
    team=[agente_financeiro, agente_pesquisa],
    model=OpenAIChat(id="gpt-5.4"),
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Inclua sempre a fonte das informações coletadas",
        "Crie tabelas para comparações",
        "Gere os resultados com o idioma Português do Brasil",
    ],
    debug_mode=True,
)

print("Time de agentes inicializados com o modelo gpt-5.4")

print("Agentes prontos para análise.")

# Executando a análise
print("Obtendo recomendações e informações sobre a Apple...")

# Executa o time de agentes
time_agentes.print_response(
    "Resumir as recomendações dos analistas sobre investimentos e compartilhar as informações mais recentes sobre a Apple."
)
