import telepot
import os
from telepot.loop import MessageLoop
import time

# Fetch tokens from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_PAT = os.getenv('GITHUB_PAT')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']

        if command == '/start':
            bot.sendMessage(chat_id, "Hello! I'm your bot. Use /pull to update the repository.")
        
        elif command == '/pull':
            updating_message = bot.sendMessage(chat_id, "Updating... Please wait.")
            try:
                # Change to your repository directory
                os.chdir('/home/Ankit/web/mycsmtp.com/public_html')

                # Set the remote URL (only needed once, can be omitted after the first run)
                os.system(f'git remote set-url origin https://{GITHUB_USERNAME}:{GITHUB_PAT}@github.com/Harshit403/mycsmtp.git')

                # Pull the latest changes
                result = os.popen('git pull').read()

                # Edit the updating message with the result
                bot.editMessageText((chat_id, updating_message['message_id']), f"Result of `git pull`:\n{result}")
            except Exception as e:
                bot.editMessageText((chat_id, updating_message['message_id']), f"Error: {str(e)}")

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

print('Listening ...')

# Keep the program running
while True:
    time.sleep(10)
