# Time de Agentes de IA para Inteligência de Mercado

Projeto em Python que demonstra a criação de um time de agentes de inteligência artificial para produzir análises de mercado sobre empresas. O exemplo incluído consulta informações financeiras e pesquisa na web para resumir recomendações de analistas e reunir informações recentes sobre a Apple.

O repositório contém duas implementações da mesma ideia, com provedores de modelos de linguagem diferentes.

## Objetivo

O projeto combina dois agentes especializados:

- **Analista Financeiro:** utiliza ferramentas do Yahoo Finance para consultar cotações, recomendações de analistas e fundamentos financeiros.
- **Pesquisador Web:** utiliza o DuckDuckGo para pesquisar informações na web e orientar a resposta com fontes.
- **Time de agentes:** coordena os dois agentes e consolida as informações em uma resposta em português do Brasil, com tabelas quando apropriado.

O exemplo executado pelos scripts solicita um resumo das recomendações dos analistas sobre investimentos e informações recentes sobre a Apple.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `dsa_agentes_v1.py` | Implementação que utiliza o modelo `gpt-5.4` por meio da integração com a OpenAI. |
| `dsa_agentes_v2.py` | Implementação que utiliza `deepseek-r1-distill-llama-70b` por meio da integração com a Groq. |

As duas versões usam a biblioteca Phidata/`phi` para definir os agentes, além das ferramentas DuckDuckGo e Yahoo Finance.

## Requisitos

- Python compatível com as versões instaladas das bibliotecas utilizadas.
- Acesso à internet para consultar as ferramentas externas.
- Chave de API da OpenAI para executar `dsa_agentes_v1.py`.
- Chave de API da Groq para executar `dsa_agentes_v2.py`.

## Instalação

1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   No Windows, ative o ambiente com:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

> Observação: a API e os nomes dos pacotes do ecossistema Phidata podem variar entre versões. Se houver erros de importação, consulte a documentação da versão utilizada e ajuste as dependências de acordo com ela.

## Configuração das credenciais

Crie um arquivo `.env` na raiz do projeto. Informe apenas a chave correspondente à versão que deseja executar:

Para `dsa_agentes_v1.py`:

```dotenv
OPENAI_API_KEY=sua_chave_openai
```

Para `dsa_agentes_v2.py`:

```dotenv
GROQ_API_KEY=sua_chave_groq
```

## Como executar

Com o ambiente virtual ativado e as credenciais configuradas, execute um dos scripts:

```bash
python dsa_agentes_v1.py
```

ou:

```bash
python dsa_agentes_v2.py
```

Os scripts verificam a existência do arquivo `.env`, tentam verificar a conexão com a internet e inicializam os agentes. As chamadas às ferramentas externas são configuradas de acordo com o resultado dessa verificação.

### Resultados

- **Versão 1 (`dsa_agentes_v1.py`):** envia a solicitação ao time de agentes e apresenta a resposta no terminal.
- **Versão 2 (`dsa_agentes_v2.py`):** coleta o conteúdo gerado e, se houver resposta não vazia, salva o relatório em `resultados.txt`.

O arquivo `resultados.txt` é criado no diretório de execução do script da versão 2.

## Fluxo de funcionamento

1. Carrega as variáveis de ambiente, se o arquivo `.env` existir.
2. Verifica a conectividade com a internet.
3. Configura o agente financeiro com ferramentas do Yahoo Finance.
4. Configura o agente de pesquisa com a ferramenta DuckDuckGo.
5. Cria um agente coordenador que reúne os dois especialistas.
6. Executa a solicitação de análise sobre a Apple.
7. Exibe a resposta e, na versão 2, grava o relatório em um arquivo de texto.

## Limitações e observações

- A verificação de conectividade utiliza uma conexão com `www.google.com` na porta 80. Ela é apenas um teste básico e não garante que todas as APIs e ferramentas externas estejam disponíveis.
- Se a conexão falhar, os scripts inicializam os agentes sem as ferramentas externas. Nesse caso, a análise pode ficar limitada ou não conter dados atuais.
- As informações financeiras e as recomendações de analistas podem mudar. Verifique os dados diretamente nas fontes antes de tomar decisões.
- O conteúdo gerado por modelos de linguagem pode conter erros, omissões ou referências imprecisas. O relatório deve ser tratado como apoio à pesquisa, não como recomendação financeira personalizada.
- Os scripts habilitam a exibição das chamadas de ferramentas para facilitar a observação do fluxo de execução. O modo de depuração também está ativado no agente coordenador.

## Segurança

- Armazene as chaves de API em variáveis de ambiente ou em um arquivo `.env` local.
- Não versione credenciais, dados pessoais ou outros segredos.
- Considere fixar as versões das dependências em um arquivo `requirements.txt` para tornar o ambiente reproduzível.

## Possíveis melhorias

- Tornar a empresa ou o ticker parâmetros de entrada, em vez de usar a Apple como exemplo fixo.
- Adicionar tratamento de exceções e mensagens de erro específicas para falhas de API.
- Registrar as fontes consultadas e os horários de coleta no relatório.
- Criar testes automatizados para a inicialização dos agentes e o processamento das respostas.
- Centralizar a configuração por variáveis de ambiente e documentar versões testadas das dependências.
- Comparar sistematicamente os resultados dos dois provedores usando as mesmas perguntas e critérios de avaliação.

## Aviso

Este projeto tem finalidade educacional e demonstrativa. Não constitui aconselhamento financeiro nem substitui a validação independente das informações obtidas.
