from src.ABCClass import AbstractJobApi
import requests


class HHApi(AbstractJobApi):
    def __init__(self, access_token):
        self.access_token = access_token
        self.per_page = 100

    def get_vacancies(self, keyword, page=0):
        if not self.access_token:
            raise ValueError("Access token is not specified.")

        vacancies_url = "https://api.hh.ru/vacancies"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {"text": keyword, "area": 113, "currency": "RUR", "per_page": self.per_page, "page": page}

        response = requests.get(vacancies_url, headers=headers, params=params)
        if response.status_code != 200:
            print("Error:", response.status_code)
            print("Response:", response.text)
            return None

        vacancies_data = response.json().get("items", [])
        return vacancies_data