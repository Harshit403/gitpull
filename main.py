import telepot
import os
from telepot.loop import MessageLoop

# Fetch tokens from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_PAT = os.getenv('GITHUB_PAT')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']

        if command == '/pull':
            try:
                # Change to your repository directory
                os.chdir('/home/Harshit11/domains/mycamtp.com/public_html')

                # Set the remote URL (only needed once, can be omitted after the first run)
                os.system(f'git remote set-url origin https://{GITHUB_USERNAME}:{GITHUB_PAT}@github.com/Harshit403/mycamtp.git')

                # Pull the latest changes
                result = os.popen('git pull').read()

                # Send the result back to the user
                bot.sendMessage(chat_id, f"Result of `git pull`:\n{result}")
            except Exception as e:
                bot.sendMessage(chat_id, f"Error: {str(e)}")

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

print('Listening ...')

# Keep the program running
import time
while True:
    time.sleep(10)
