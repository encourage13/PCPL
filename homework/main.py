import requests
import logging


RAPIDAPI_KEY = "-_-"
RAPIDAPI_HOST = "-_-"



def search_hotels(entity_id, checkin_date, checkout_date, currency="USD"):
	url = "https://sky-scanner3.p.rapidapi.com/hotels/search"
	headers = {
		"x-rapidapi-key": RAPIDAPI_KEY,
		"x-rapidapi-host": RAPIDAPI_HOST
	}

	params = {
		"entityId": entity_id,
		"checkin": checkin_date,
		"checkout": checkout_date,
		"currency": currency,
		"adults": 1,
		"rooms": 1,
		"limit": 100
	}

	try:
		response = requests.get(url, headers=headers, params=params)
		response.raise_for_status()
		data = response.json()


		hotels = data.get("data", {}).get("results", {}).get("hotelCards", [])
		if hotels:
			logging.info(f"Найдено {len(hotels)} отелей.")
			return hotels
		logging.warning("Отели не найдены.")
		return []
	except requests.exceptions.RequestException as e:
		logging.error(f"Ошибка при запросе отелей: {e}")
		return []



def get_city_entity_id(city_name):
	url = "https://sky-scanner3.p.rapidapi.com/hotels/auto-complete"
	headers = {
		"x-rapidapi-key": RAPIDAPI_KEY,
		"x-rapidapi-host": RAPIDAPI_HOST
	}
	params = {"query": city_name}

	try:
		response = requests.get(url, headers=headers, params=params)
		response.raise_for_status()
		data = response.json()


		for item in data.get('data', []):
			if item.get('entityType') == 'city':
				logging.info(f"Найден город: {item['entityName']} с ID {item['entityId']}")
				return item['entityId']

		logging.warning("Город не найден.")
		return None
	except requests.exceptions.RequestException as e:
		logging.error(f"Ошибка при запросе Entity ID города: {e}")
		return None


def get_hotel_details(hotel_id):
	url = f"https://sky-scanner3.p.rapidapi.com/hotels/{hotel_id}"
	headers = {
		"x-rapidapi-key": RAPIDAPI_KEY,
		"x-rapidapi-host": RAPIDAPI_HOST
	}

	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()
		hotel_data = response.json()


		price = hotel_data.get("price", {}).get("total", "Цена не указана")
		address = hotel_data.get("address", "Адрес не указан")
		return price, address
	except requests.exceptions.RequestException as e:
		logging.error(f"Ошибка при запросе данных отеля {hotel_id}: {e}")
		return "Цена не указана", "Адрес не указан"

def main():
	city_name = input("Введите название города: ")
	checkin_date = input("Введите дату заезда (ГГГГ-ММ-ДД): ")
	checkout_date = input("Введите дату выезда (ГГГГ-ММ-ДД): ")


	entity_id = get_city_entity_id(city_name)
	if not entity_id:
		print(f"Не удалось найти город: {city_name}")
		return


	hotels = search_hotels(entity_id, checkin_date, checkout_date)
	if hotels:
		print("Доступные отели:")
		for hotel in hotels:
			name = hotel.get("name", "Без названия")
			price = hotel.get("price", {}).get("total", "Цена не указана")
			address = hotel.get("address", "Адрес не указан")
			print(f"{name} - {price} - {address}")
	else:
		print("Нет доступных отелей для указанных дат.")


if __name__ == "__main__":
	main()

