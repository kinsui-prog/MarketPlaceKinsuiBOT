import os
import telebot

# Mengambil token dari Environment Variables (nanti diatur di cloud)
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Respon saat bot dikirim /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Bot marketplace Anda sudah aktif dan online 24 jam! 🚀")

# Respon untuk pesan teks biasa
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Pesan diterima: {message.text}")

# Jalankan bot
print("Bot sedang berjalan...")
bot.infinity_polling()
