import os
import json
import pytest
from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy
@pytest.fixture
def json_saver(tmp_path):
    filename = tmp_path / "test.json"
    saver = JSONSaver(str(filename))
    return saver


def test_add_vacancy(json_saver):
    vacancy = Vacancy("Software Engineer", "Moscow", 50000, 100000, "https://example.com", "Python developer", "Junior")
    json_saver.add_vacancy(vacancy)
    with open(json_saver.filename, 'r') as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]["title"] == "Software Engineer"
        assert data[0]["city"] == "Moscow"
        assert data[0]["salary_from"] == 50000
        assert data[0]["salary_to"] == 100000
        assert data[0]["link"] == "https://example.com"
        assert data[0]["description"] == "Python developer"
        assert data[0]["experience"] == "Junior"




