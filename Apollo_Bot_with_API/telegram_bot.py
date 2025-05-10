from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from automation import search_apollo_person, log_to_sheet
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send me a person's name to look up.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    result = search_apollo_person(query)
    log_to_sheet(query, result)

    if 'error' in result:
        await update.message.reply_text(result['error'])
    else:
        reply = (
            f"🔍 *Result:*\n"
            f"👤 Name: {result['name']}\n"
            f"💼 Title: {result['title']}\n"
            f"🏢 Company: {result['company']}\n"
            f"📧 Email: {result['email']}\n"
            f"🔗 LinkedIn: {result['linkedin']}"
        )
        await update.message.reply_text(reply, parse_mode='Markdown')

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
