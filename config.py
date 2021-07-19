import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
admins = [
863325996
]
channels = [-1001543183452]
ip = os.getenv('ip')
monobank = '5375414129298500'





aiogram_redis = {
    'host': ip,
}

redis = {
    'adress': (ip, 6379),
    'encoding': 'utf'
}

PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')


