import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем значения переменных окружения
TOKEN = os.getenv('TOKEN')
DATABASE = os.getenv('DATABASE')
