from jobs.updater import update_dynu_dns
import threading,logging
from jobs.telegram import TelegramBot

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

update_dynu_dns('ZX444b3443XTb3dT4c4d464Wd3WU6gUW', 'heisenberglabs.mywire.org') # API_KEY,HOSTNAME

TelegramBot("7239184567:AAFKIzHdHqQJYZPrFoDh-bVwgSCbOwDFmM8")  # Replace with your actual token

