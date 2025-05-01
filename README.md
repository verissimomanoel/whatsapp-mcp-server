# WhatsApp MCP Server

A FastMCP server implementation that provides WhatsApp messaging capabilities using the Z-API.io service. This server allows you to send WhatsApp messages programmatically through a simple interface.

## Features

- Send WhatsApp messages using Z-API.io
- Contact management through JSON file
- Asynchronous message handling
- Error logging and handling

## Prerequisites

- Python 3.x
- Access to Z-API.io service
- Valid Z-API.io credentials (Instance ID, Token, and Client Token)

## Installation

1. Clone the repository:

2. Install dependencies using UV:## Configuration

The server requires the following environment variables:

- `INSTANCE`: Your Z-API.io instance ID
- `TOKEN`: Your Z-API.io token
- `CLIENT_TOKEN`: Your Z-API.io client token

You can set these variables in your environment or use a `.env` file.

## Contact List Configuration

Create a `data/contacts.json` file with your contacts in the following format:

```json
{
    "contact_name": "phone_number",
    "john": "5511999999999"
}
```python waha_mcp_server.pypython waha_mcp_server.pyThis README provides a comprehensive overview of your WhatsApp MCP server project, including setup instructions, configuration requirements, and usage examples. You may want to customize it further by:

1. Adding the actual repository URL
2. Including specific license information
3. Adding more detailed contribution guidelines
4. Including any specific deployment instructions
5. Adding troubleshooting guides
6. Including any additional features or functionalities you plan to add

Would you like me to modify any section or add more specific information to the README?