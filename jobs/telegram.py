import telebot, logging
from jobs.updater import get_public_ip, update_dynu_dns  # Ensure these are defined in jobs.updater
from telebot.types import BotCommand, MenuButtonCommands

class TelegramBot:
  def __init__(self, token):
    self.bot = telebot.TeleBot(token)
    self.setup_commands()
    self.initialize_handlers()
    self.start_bot()

  def setup_commands(self):
    """Set up bot commands and menu button."""
    commands = [
    BotCommand(command='start', description='Start the Bot'),
    BotCommand(command='get_ip', description='Get Public IP'),
    BotCommand(command='update_ip', description='Update IP')]
    self.bot.set_my_commands(commands)
    self.bot.set_chat_menu_button(menu_button=MenuButtonCommands(type='commands'))

  def initialize_handlers(self):
    """Initialize command handlers."""
    @self.bot.message_handler(commands=['start'])
    def handle_start(message):
      self.bot.send_message(message.chat.id,"Welcome to the bot! Use /get_ip to get the public IP or /update_ip to update the IP.")

    @self.bot.message_handler(commands=['get_ip'])
    def handle_get_ip(message):
      self.bot.send_message(message.chat.id, f"Public IP: {get_public_ip()}")

    @self.bot.message_handler(commands=['update_ip'])
    def handle_update_ip(message):
      status = update_dynu_dns('ZX444b3443XTb3dT4c4d464Wd3WU6gUW', 'heisenberglabs.mywire.org')
      self.bot.send_message(message.chat.id, f"Update Status: {status}")

  def start_bot(self):
    logging.info("Bot is Initiated...")
    self.bot.infinity_polling()

