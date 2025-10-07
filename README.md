
# 🤖 Telegram File Forwarder Bot

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![Telegram Bot](https://img.shields.io/badge/Telegram%20Bot-API-green.svg)](https://core.telegram.org/bots)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A sophisticated Telegram bot that allows users to upload files, add custom names as hashtags, and automatically forwards them to your designated group with professional formatting.

## ✨ Features

- 📁 **Multi-format Support**: Handles documents, photos, videos, and audio files
- 🏷️ **Custom Hashtags**: Users can add personalized names as #hashtags
- 💬 **Group Integration**: Seamlessly forwards files to your Telegram group
- 🔄 **Interactive Flow**: Guided conversation for file naming
- 🚫 **Cancel Operation**: Users can abort at any time with /cancel
- 🛡️ **Error Handling**: Comprehensive error messages and validation
- 📊 **Logging**: Detailed activity logging for monitoring

## 🚀 Setup Instructions

### 1. Create Telegram Bot
1. Open Telegram and search for **🤖 @BotFather**
2. Create a new bot using `/newbot` command
3. Follow the prompts to set bot name and username
4. Copy the **🔑 BOT TOKEN** provided by BotFather

### 2. Add Bot to Your Group
1. Create a new group or use an existing group
2. Add your bot as a **👥 member** of the group
3. Grant the bot permission to **📤 Send Messages**

### 3. Get Group ID
1. Add `@JsonDumpBot` to your group
2. Post any message in the group
3. The bot will reply with the group ID (format: `-100xxxxxxxxxx`)
4. Copy this numeric ID (it will be a negative number)

### 4. Configure the Bot
1. Clone this repository:
```bash
git clone https://github.com/xPOURY4/telegram-file-forwarder.git
cd telegram-file-forwarder
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Edit `config.py`:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # 🔑 From BotFather
GROUP_ID = -1001234567890  # 👥 Your group ID
```

### 5. Run the Bot
```bash
python bot.py
```

## 📖 How to Use

1. **📤 Send File**: Upload any file to the bot
2. **✏️ Name File**: When prompted, enter a name for the file
3. **🏷️ Hashtag Format**: The bot will format it as #YourName
4. **📤 Forward**: File appears in your group with the hashtag caption
5. **🚫 Cancel**: Use /cancel to abort at any time

## 🎮 Supported Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Welcome message and instructions | `/start` |
| `/help` | Usage instructions | `/help` |
| `/cancel` | Abort current operation | `/cancel` |

## 🛠️ Troubleshooting

| Issue | Solution | Emoji |
|-------|----------|-------|
| **"Failed to send file"** | Verify bot is group member with send permissions | 🔍 |
| **Bot not responding** | Check BOT_TOKEN and internet connection | 🌐 |
| **Invalid Group ID** | Use @RawDataBot to get correct ID | 🆔 |
| **Name not accepted** | Enter text after sending file | ✏️ |
| **Unsupported file type** | Send document, photo, video or audio | 📁 |

## 🔒 Security Notes

- 🔑 Never share your BOT_TOKEN publicly
- 🔐 Use environment variables for sensitive data in production
- 🔄 Regularly update dependencies: `pip install --upgrade -r requirements.txt`
- 📝 Monitor bot usage and logs for suspicious activity
- 🛡️ Keep your bot code private and secure

## 📄 License

This project is licensed under the MIT License - feel free to use and modify

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Contact the developer

---

Made with ❤️ by [xPOURY4](https://github.com/xPOURY4)
