import asyncio
import json
from EdgeGPT import Chatbot, ConversationStyle


async def givenTranscription(transcription):
    bot = Chatbot(cookiePath='cookies.json')
    response = await bot.ask(prompt=f"""What can you say about the following: {transcription}
                             """, conversation_style=ConversationStyle.creative)
    await bot.close()
    return response['item']['messages'][1]['text']