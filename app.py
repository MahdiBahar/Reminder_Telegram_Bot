import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

token = "8110934779:AAEL1-v3BqBV-ISozqhvKnWpAIQyWlcPOp8"


import logging
logging.basicConfig(level=logging.DEBUG)


import httpx
import asyncio

async def test_connection():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.telegram.org')
        print(response.status_code, response.text)

asyncio.run(test_connection())






# # Enable logging for debugging purposes
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a welcome message when the /start command is issued."""
#     await update.message.reply_text(
#         'Hi! I am your reminder bot. Use /remind <seconds> <message> to set a reminder.'
#     )

# async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Handles the /remind command to set a reminder."""
#     try:
#         # Extract delay and reminder message from the command arguments
#         delay = int(context.args[0])
#         reminder_message = ' '.join(context.args[1:])
        
#         # Schedule a job to send the reminder after the specified delay
#         context.job_queue.run_once(
#             callback=send_reminder,
#             when=delay,
#             chat_id=update.effective_chat.id,
#             data=reminder_message
#         )
        
#         await update.message.reply_text(
#             f"Reminder set! I will remind you in {delay} seconds."
#         )
#     except (IndexError, ValueError):
#         await update.message.reply_text("Usage: /remind <seconds> <reminder message>")

# async def send_reminder(context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Callback function that sends the reminder message."""
#     job_data = context.job.data  # This holds the reminder message
#     await context.bot.send_message(
#         chat_id=context.job.chat_id,
#         text=f"Reminder: {job_data}"
#     )

# def main():

#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token(token).build()

#     # Add command handlers
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("remind", remind))
    
#     # Run the bot until the user sends a signal with Ctrl-C
#     application.run_polling()

# if __name__ == '__main__':
#     main()
