import os
import traceback
from loguru import logger
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY") 
openai_client = OpenAI(
            api_key=openai_api_key,
            timeout=60,
            max_retries=3
        )


def get_bot_response(message : str,previous_messages : list):
    """
    This function generates a response from a medical assistant chatbot based on a given user message and previous conversation history.

    Parameters:
    message (str): The user's message for which the chatbot needs to provide a response.
    previous_messages (list): A list of previous messages in the conversation.

    Returns:
    str: The chatbot's response to the user's message.
    """
    try:

        messages = []
        previous_messages_string = "\n".join(previous_messages)

        system_content = f"""You are a medical assistant who helps users with their medical needs. Below is the user's message for which you need to provide a response. Please do not include any personal information.

Previous message history: {previous_messages_string}"""

        messages.extend([
            {"role": "system", "content": system_content},
            {"role": "user", "content": message}
        ])

        bot_response = openai_client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo-1106",
        )

        bot_response = bot_response.choices[0].message.content
        if bot_response is None:
            bot_response = "No response from the bot"
        else:
            logger.info(
                f"Bot response successfully generated: {bot_response[0:15]}")

    except Exception as e:
        error_message = f"An error occured in processing message.\nTraceback: {traceback.format_exc()}\nError: {e}"
        logger.exception(error_message)



