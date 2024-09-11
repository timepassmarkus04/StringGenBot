from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://devilkingp0404:HpFatXEgKjMUtxkW@cluster0.3yabl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", 6813000899))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TSS_Support_Group")
