# MCP Client & Server Example


## Prerequisites

- Python 3.12 or higher
- uv (Python package installer and environment manager)
- Environment variables set up in `.env` file (for Anthropic API key)

## Installation

1. Clone the repository

2. Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Create and activate a new environment:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

4. Install dependencies using uv:
```bash
uv pip install -e .
```
5. Configure .env by copying `.env.example` to `.env` and filling in your Anthropic API key:


## Project Structure

- Simple client and server
    - `weather_server.py` - MCP server implementation with weather service endpoints
- [Client example](https://modelcontextprotocol.io/quickstart/client) and [Server example](https://modelcontextprotocol.io/quickstart/server)
    - `weather_example.py` - Example implementation using the National Weather Service API
    - `client_example.py` - Interactive client with Claude AI integration
