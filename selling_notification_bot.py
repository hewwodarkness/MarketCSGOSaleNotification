import requests
import time
from datetime import datetime
import json

API_KEY = "YOUR_API_KEY"
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
chat_id = "YOUR_TELEGRAM_GROUP"

while True:
  try:
    response = requests.get("https://market.csgo.com/api/v2/items?key=" + API_KEY)
    data = response.json()
    # print(data)
    if response.status_code == 200:
      items = data.get("items", [])
      for item in items:
        if item['status'] == '2' and float(item['price']) > 150:
          for _ in range(5):
            datetime_obj = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = (f"Статус змінено, передай боту: {item['market_hash_name']}\nЦіна: {item['price']} RUB\nЧас: {datetime_obj}")
            urltg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(urltg).json()
            time.sleep(1)
          
        elif item['status'] == '3' and float(item['price']) > 150:
          for _ in range(5):
            datetime_obj = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = (f"Статус змінено, чекаю: {item['market_hash_name']}\nЦіна: {item['price']} RUB\nЧас: {datetime_obj}")
            urltg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(urltg).json()
            time.sleep(1)

        elif item['status'] == '4' and float(item['price']) > 150:
          for _ in range(5):
            datetime_obj = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = (f"Статус змінено, повністю продано: {item['market_hash_name']}\nЦіна: {item['price']} RUB\nЧас: {datetime_obj}")
            urltg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(urltg).json()
            time.sleep(1)

      time.sleep(5)
      print('Checked. Time: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elif response.status_code != 200:
      print("Internet/Site problem.. Pass")
      pass
  except json.decoder.JSONDecodeError:
    print("JSONDecodeError.. Pass")
    pass