import asyncio
import webbrowser

async def open_websites():
    """Open websites using Python's webbrowser module"""
    print("Opening websites...")
    
    # Open google.com
    print("\nOpening google.com...")
    webbrowser.open("https://google.com")
    
    # Wait a moment between navigations
    await asyncio.sleep(2)
    
    # Open makemytrip.com
    print("Opening makemytrip.com...")
    webbrowser.open("https://makemytrip.com")
    
    print("\nBoth websites should now be open in your default browser.")

if __name__ == "__main__":
    asyncio.run(open_websites())

