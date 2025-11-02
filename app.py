import asyncio

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from mcp_use import MCPAgent, MCPClient
import os

async def run_memory_chat():
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    config_file = "browser_mcp.json"
    
    print("Starting Chat with Browser MCP...")
    
    try:
        client = MCPClient.from_config_file(config_file)
        llm = ChatGroq(model="llama-3.1-70b-versatile")
        
        agent = MCPAgent(
            llm=llm,
            client=client,
            max_steps=15,
            memory_enabled=True,
        )
        
        print("\n==== Interactive MCP Chat ==== ")
        print("Type 'exit' to end the chat.")
        print("Type 'clear' to clear the memory.")
        print("================================\n")
        
        try:
            while True:
                try:
                    user_input = input("\n You: ")
                except (EOFError, KeyboardInterrupt):
                    print("\n\nExiting chat...")
                    break
                
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print("Exiting chat...")
                    break
                
                if user_input.lower() == "clear":
                    agent.clear_conversation_history()
                    print("Conversation history cleared.")
                    continue
                
                print("\n Assistant: ", end="", flush=True)
                
                try:
                    response = await agent.run(user_input)
                    print(response)
                except Exception as e:
                    print(f"\nError: {e}")
        finally:
            if client and hasattr(client, 'sessions') and client.sessions:
                await client.close_all_sessions()
    except Exception as e:
        print(f"\nError initializing MCP client: {e}")
        print("Please check:")
        print("1. Your browser_mcp.json configuration file")
        print("2. That all required MCP servers are properly installed")
        print("3. That you have an internet connection for npx commands")
        raise
            
if __name__ == "__main__":
    asyncio.run(run_memory_chat())