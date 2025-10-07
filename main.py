import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from config import BOT_TOKEN, GROUP_ID

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

WAITING_FOR_NAME = 1

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        "👋 Welcome! Send me any file and I'll ask for a name to add as a hashtag.\n\n"
        "Supported formats: Documents, photos, videos, audio files\n\n"
        "Files will be forwarded to our group with your custom hashtag.\n\n"
        "Use /help for more information."
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "📖 Help:\n"
        "1. Send any file to this bot\n"
        "2. I'll ask you to enter a name for the file\n"
        "3. The file will be sent to the group with #YourName as caption\n"
        "4. Supported types: Documents, images, videos, audio\n"
        "5. Use /cancel to abort the operation"
    )

def cancel(update: Update, context: CallbackContext) -> int:
    """Cancel the conversation."""
    update.message.reply_text("❌ Operation cancelled. Send a new file to start again.")
    return ConversationHandler.END

def receive_file(update: Update, context: CallbackContext) -> int:
    """Handle file uploads and ask for a name."""
    if update.message.document:
        context.user_data['file_id'] = update.message.document.file_id
        context.user_data['file_type'] = 'document'
    elif update.message.photo:
        context.user_data['file_id'] = update.message.photo[-1].file_id
        context.user_data['file_type'] = 'photo'
    elif update.message.video:
        context.user_data['file_id'] = update.message.video.file_id
        context.user_data['file_type'] = 'video'
    elif update.message.audio:
        context.user_data['file_id'] = update.message.audio.file_id
        context.user_data['file_type'] = 'audio'
    else:
        update.message.reply_text("❌ Unsupported file type. Please send a document, photo, video or audio.")
        return ConversationHandler.END
    
    update.message.reply_text(
        "📝 Please enter a name for this file. I'll add it as a hashtag (#YourName) in the group.\n\n"
        "Example: if you enter 'ProjectX', the caption will be #ProjectX\n\n"
        "Use /cancel to abort."
    )
    return WAITING_FOR_NAME

def receive_name(update: Update, context: CallbackContext) -> int:
    """Handle the name input and send file to group."""
    name = update.message.text.strip()
    if not name:
        update.message.reply_text("❌ Name cannot be empty. Please enter a valid name.")
        return WAITING_FOR_NAME
    hashtag = f"#{name.replace(' ', '_')}"
    
    try:
        file_id = context.user_data.get('file_id')
        file_type = context.user_data.get('file_type')
        
        if not file_id or not file_type:
            update.message.reply_text("❌ Error: File information lost. Please try again.")
            return ConversationHandler.END
        if file_type == 'document':
            context.bot.send_document(
                chat_id=GROUP_ID,
                document=file_id,
                caption=hashtag
            )
        elif file_type == 'photo':
            context.bot.send_photo(
                chat_id=GROUP_ID,
                photo=file_id,
                caption=hashtag
            )
        elif file_type == 'video':
            context.bot.send_video(
                chat_id=GROUP_ID,
                video=file_id,
                caption=hashtag
            )
        elif file_type == 'audio':
            context.bot.send_audio(
                chat_id=GROUP_ID,
                audio=file_id,
                caption=hashtag
            )
        
        update.message.reply_text(f"✅ Success! File sent to the group with caption: {hashtag}")
        logger.info(f"File sent to group with caption: {hashtag}")
        
    except Exception as e:
        logger.error(f"Error sending file: {e}")
        update.message.reply_text("❌ Failed to send file. Please make sure the bot is a member of the group.")
    context.user_data.clear()
    return ConversationHandler.END

def main() -> None:
    """Start the bot."""
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(
            Filters.document | Filters.photo | Filters.video | Filters.audio,
            receive_file
        )],
        states={
            WAITING_FOR_NAME: [MessageHandler(Filters.text & ~Filters.command, receive_name)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
        per_message=False
    )

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    logger.info("Bot started successfully!")
    updater.idle()

if __name__ == '__main__':
    main()
