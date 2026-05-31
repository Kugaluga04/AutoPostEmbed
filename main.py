from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str, username: str) -> None:
    username =  (
        username
        .replace("\\", "\\\\")
        .replace("*", "\\*")
        .replace("_", "\\_")
        .replace("~", "\\~")
        .replace("`", "\\`")
        .replace("|", "\\|")
        .replace(">", "\\>")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("(", "\\(")
        .replace(")", "\\)")
    )
    
    if not user_message:
        print("Message empty")
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    if is_post := "/twitter.com/" in user_message or "/vxtwitter.com/" in user_message or "/x.com/" in user_message or "/instagram.com/" in user_message or "/www.instagram.com/" in user_message:
        await message.channel.purge(limit=1)
        user_message = user_message
    else:
        return
    
    try:
        if username == "artemiswuzhere" and "/vxtwitter.com/" in user_message:
            response: str = "Sent by " + username + "\n\nNo! Stop that!\n\n" + get_response(user_message)
            await message.author.send(response) if is_private else is_post and await message.channel.send(response)
        else:
            response: str = "Sent by " + username + "\n" + get_response(user_message)
            await message.author.send(response) if is_private else is_post and await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
# STEP 3: HANDLING
@client.event
async def on_ready() -> None:
    print(f'WE RISE')
        
@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = str(message.content)
    
    await send_message(message, user_message, username)
    
# STEP 4: MAIN
def main() -> None:
    client.run(token=TOKEN)
    
if __name__ == '__main__':
    main()