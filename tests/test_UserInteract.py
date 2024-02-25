import os
import pytest
from src.Vacancy import Vacancy
from src.UserInteract import create_vacancy_objects, create_empty_json_file

@pytest.fixture
def mock_vacancies_data():
    return [
        {
            "name": "Software Engineer",
            "area": {"name": "Moscow"},
            "salary": {"from": 50000, "to": 100000},
            "alternate_url": "https://example.com",
            "snippet": {"requirement": "Python, Java, SQL"},
            "experience": "Mid"
        },

    ]


def test_create_vacancy_objects(mock_vacancies_data):
    vacancies = create_vacancy_objects(mock_vacancies_data)
    assert len(vacancies) == len(mock_vacancies_data)
    assert isinstance(vacancies[0], Vacancy)


def test_create_empty_json_file(tmpdir):
    filename = os.path.join(tmpdir, "test.json")
    create_empty_json_file(filename)
    assert os.path.exists(filename)
    with open(filename, 'r') as file:
        data = file.read()
        assert data == '[]'