# WAHA MCP Server

[![Linguagem](https://img.shields.io/badge/linguagem-Python-blue.svg)](https://www.python.org/)

Servidor MCP (Message Control Protocol) que interage com uma instância do [WAHA (WhatsApp HTTP API)](https://github.com/devlikeapro/waha) para enviar mensagens do WhatsApp e ler uma lista de contatos de um arquivo local.

## Funcionalidades Principais ✨

*   **Envio de Mensagens via WAHA:** Expõe uma ferramenta (`send_message`) que permite enviar mensagens de texto para números de WhatsApp através de uma API WAHA local.
*   **Leitura de Contatos:** Expõe um recurso (`read_resource`) que lê um arquivo JSON local (`data/contacts.json`) para fornecer uma lista de contatos.
*   **Integração com FastMCP:** Construído sobre o framework `FastMCP` para expor ferramentas e recursos.

## Tecnologias Utilizadas 🛠️

*   **Linguagem:** Python 3
*   **Framework MCP:** `FastMCP` (do pacote `mcp-server`)
*   **Comunicação HTTP:** Biblioteca `requests` (para interagir com a API WAHA)
*   **Dependência Externa:** WAHA (WhatsApp HTTP API) - **Não incluído neste projeto, deve estar rodando separadamente.**

## Pré-requisitos 📋

Antes de começar, você precisará ter instalado em sua máquina:

*   Python (recomendado 3.7+)
*   `pip` (gerenciador de pacotes Python)
*   Uma instância do **WAHA (WhatsApp HTTP API)** rodando e acessível em `http://localhost:3000`.
    *   Consulte a documentação do WAHA para instalação e configuração.
    *   Certifique-se de que uma sessão do WhatsApp (nomeada `default` neste código) esteja ativa e conectada no WAHA.
*   Git (para clonar o repositório, se aplicável)