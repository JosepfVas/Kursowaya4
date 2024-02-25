import pytest
from src.HHApi import HHApi


@pytest.fixture
def hh_api():
    access_token = "USERGMNFVG3IMPO9OUTIACEHLTOP4ME3VHTI2AP3THN4QU2819MN1S6T5BPDLKKD"
    return HHApi(access_token)


def test_get_vacancies_success(hh_api):
    keyword = "python"
    vacancies = hh_api.get_vacancies(keyword)
    assert isinstance(vacancies, list)
    assert len(vacancies) > 0


def test_get_vacancies_no_access_token():
    access_token = None
    hh_api = HHApi(access_token)
    with pytest.raises(ValueError):
        hh_api.get_vacancies("python")