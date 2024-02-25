import pytest
from src.Vacancy import Vacancy

@pytest.fixture
def vacancy_data():
    return {
        "title": "Software Engineer",
        "city": "Moscow",
        "salary_from": 100000,
        "salary_to": 150000,
        "link": "https://example.com",
        "description": "Python, SQL",
        "experience": "2 years"
    }


def test_vacancy_creation(vacancy_data):
    vacancy = Vacancy(**vacancy_data)
    assert vacancy.title == vacancy_data["title"]
    assert vacancy.city == vacancy_data["city"]
    assert vacancy.salary_from == vacancy_data["salary_from"]
    assert vacancy.salary_to == vacancy_data["salary_to"]
    assert vacancy.link == vacancy_data["link"]
    assert vacancy.description == vacancy_data["description"]
    assert vacancy.experience == vacancy_data["experience"]


def test_to_dict(vacancy_data):
    vacancy = Vacancy(**vacancy_data)
    vacancy_dict = vacancy.to_dict()
    assert vacancy_dict == {
        "title": vacancy_data["title"],
        "city": vacancy_data["city"],
        "salary_from": vacancy_data["salary_from"],
        "salary_to": vacancy_data["salary_to"],
        "link": vacancy_data["link"],
        "description": vacancy_data["description"],
        "experience": vacancy_data["experience"]
    }


def test_repr(vacancy_data):
    vacancy = Vacancy(**vacancy_data)
    expected_repr = (
        f"{vacancy_data['title']}, {vacancy_data['city']}, "  
        f"зарплата от - {vacancy_data['salary_from']}руб., "
        f"зарплата до - {vacancy_data['salary_to']}руб., "
        f"ссылка на вакансию '{vacancy_data['link']}', "  
        f"описание работы: {vacancy_data['description']}, "  
        f"опыт: {vacancy_data['experience']}"
    )
    assert repr(vacancy) == expected_repr
