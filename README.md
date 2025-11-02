# MCP Demo

A Python demo application showcasing the Model Context Protocol (MCP) with LangChain and Groq. This project demonstrates how to build an interactive AI agent that can interact with multiple MCP servers for enhanced capabilities like web search and Airbnb listings.

## Features

- 🤖 **Interactive AI Chat Agent** - Powered by Groq's Llama 3.1 70B model via LangChain
- 🔌 **MCP Server Integration** - Seamlessly integrates with multiple MCP servers:
  - **Airbnb MCP Server** - Search and browse Airbnb listings
  - **DuckDuckGo Search** - Perform web searches
- 💾 **Memory-Enabled Conversations** - Maintains conversation context across interactions
- 🔧 **Easy Configuration** - Simple JSON-based MCP server configuration

## Prerequisites

- Python 3.13 or higher
- Node.js and npm (for MCP servers that use npx)
- A Groq API key ([Get one here](https://console.groq.com/))

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mcpdemo
   ```

2. **Install dependencies using uv** (recommended)
   ```bash
   uv sync
   ```
   
   Or using pip:
   ```bash
   pip install langchain-groq langchain-openai mcp-use python-dotenv
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Configuration

The MCP servers are configured in `browser_mcp.json`. By default, it includes:

- **Airbnb MCP Server** - For searching Airbnb listings
- **DuckDuckGo Search MCP Server** - For web searches

You can modify this file to add or remove MCP servers as needed.

## Usage

Run the interactive chat application:

```bash
python app.py
```

Or using uv:

```bash
uv run app.py
```

### Interactive Commands

- **Chat** - Simply type your message and press Enter
- **`exit`** or **`quit`** - Exit the chat application
- **`clear`** - Clear the conversation history/memory

### Example Interactions

```
You: Search for Airbnb listings in Paris for 2 adults

Assistant: [The agent will use the Airbnb MCP server to search and return results]

You: What's the weather like today?

Assistant: [The agent will use DuckDuckGo search to find current weather information]
```

## Project Structure

```
mcpdemo/
├── app.py              # Main interactive chat application
├── main.py             # Simple hello world entry point
├── open_websites.py    # Utility script for opening websites
├── browser_mcp.json    # MCP server configuration
├── pyproject.toml      # Project dependencies and metadata
└── README.md          # This file
```

## Dependencies

- **langchain-groq** - LangChain integration for Groq LLM
- **langchain-openai** - LangChain OpenAI integration
- **mcp-use** - MCP client and agent utilities
- **python-dotenv** - Environment variable management

## How It Works

1. The application initializes an MCP client from the configuration file
2. Creates an MCP agent with the Groq LLM (Llama 3.1 70B)
3. The agent can use tools from connected MCP servers to:
   - Search the web
   - Browse Airbnb listings
   - Perform other actions available through configured MCP servers
4. Conversation memory is maintained throughout the session

## Troubleshooting

### Common Issues

**"Error initializing MCP client"**
- Ensure Node.js and npm are installed
- Check that your `browser_mcp.json` file is valid JSON
- Verify you have internet connection for npx commands

**"API Key Error"**
- Make sure your `.env` file exists and contains `GROQ_API_KEY`
- Verify your Groq API key is valid

**MCP Server Issues**
- Some MCP servers require internet access to download via npx
- Check that the MCP server packages are correctly specified in `browser_mcp.json`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license here]

## Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Powered by [Groq](https://groq.com/)
- Uses [MCP (Model Context Protocol)](https://modelcontextprotocol.io/)

