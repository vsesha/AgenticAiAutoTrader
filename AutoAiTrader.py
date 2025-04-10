import os
from dotenv import load_dotenv
import logging
from agents import  Runner
from AgentOrchestractor import orchestrator_agent
import asyncio
import json
#import Sales_FileVector

# Configure logging
logger = logging.getLogger("FinancialAnalyst")

# Load environment variables to get OPENAI API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# This function, `conversationMemory`, updates the conversation history by 
# appending the user's new input to the existing result. If `result` is not `None`, it converts it into a list and adds the new input; otherwise, it returns the new input as is.

def conversationMemory(result, new_input):
    if result !=None:
        new_input = result.to_input_list() + [{'content': new_input, 'role': 'user'}]
    else:
        new_input = new_input
    return new_input


async def main():

    result = None
    new_prompt = input("\nWelcome to SMART analyst! I can help you with the following:\n"
                        "* Discounted vehicles for sale in my Inventory\n"
                        "* Sales Analysis and forecast\n"
                        "* Executive Email assistant, who can help you with crafting and send emails.\n"
                        "* Also, you can ask me about the JSON file details. \n"
                        "* All powered by OpenAI's Agentic AI\n What do you like me to work on?: ")
    
    while new_prompt != "quit":

        new_input = conversationMemory(result, new_prompt)
        result = await Runner.run(orchestrator_agent, new_input)

        print(result.final_output)
        new_prompt = input()


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())