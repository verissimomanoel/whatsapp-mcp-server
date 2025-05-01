import json
import logging
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("waha-mcp-server")


@mcp.tool()
async def send_message(phone_number: str, message: str) -> Dict[str, Any]:
    """
    Envia uma mensagem para um número de WhatsApp usando a API Z-API.io

    Args:
        phone_number: Número de telefone no formato completo (com código do país)
        message: Texto da mensagem a ser enviada

    Returns:
        Resposta da API em formato JSON
    """
    instance = os.environ["INSTANCE"]
    token = os.environ["TOKEN"]
    client_token = os.environ["CLIENT_TOKEN"]

    url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-text"

    payload = json.dumps({
        "phone": phone_number,
        "message": message
    })

    headers = {
        'Client-Token': client_token,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.exception(f"Falha ao enviar mensagem para o cliente: telefone={phone_number}")
        return {"success": False, "error": str(e)}


def read_contacts_file(uri: str) -> Dict[str, str]:
    """
    Lê o arquivo de contatos e retorna como dicionário

    Args:
        uri: Caminho do arquivo de contatos

    Returns:
        Dicionário com os contatos
    """
    with open(uri) as f:
        return json.load(f)


@mcp.resource("file://data/contacts.json")
async def read_resource() -> Dict[str, str]:
    """
    Use o conteúdo deste arquivo para obter os contatos a serem usados como phone_number

    Returns:
        Dicionário com os contatos no formato {"nome": "telefone", ...}
    """
    try:
        return read_contacts_file("data/contacts.json")
    except Exception as e:
        logging.exception(f"Erro ao ler arquivo de contatos: {str(e)}")
        return {}  # Retorna um dicionário vazio em caso de erro


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')