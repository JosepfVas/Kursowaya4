import os
from src.HHApi import HHApi
from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy


def create_vacancy_objects(vacancies_data):
    vacancies = []
    for vacancy_data in vacancies_data:
        title = vacancy_data.get("name")
        city = vacancy_data.get("area").get("name")
        salary_info = vacancy_data.get("salary", {})
        salary_from = salary_info.get("from") if salary_info else 0
        salary_to = salary_info.get("to") if salary_info else 0
        link = vacancy_data.get("alternate_url")
        description = vacancy_data.get("snippet", {}).get("requirement", "")
        experience = vacancy_data.get("name")

        vacancy = Vacancy(title, city, salary_from, salary_to, link, description, experience)
        vacancies.append(vacancy)
    return vacancies


def create_empty_json_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write('[]')
    else:
        with open(filename, 'w') as file:
            file.write('[]')


def interact_with_user():
    access_token = "USERGMNFVG3IMPO9OUTIACEHLTOP4ME3VHTI2AP3THN4QU2819MN1S6T5BPDLKKD"
    api = HHApi(access_token)
    create_empty_json_file("vacancies.json")
    saver = JSONSaver("vacancies.json")

    while True:
        profession = str(input("Введите профессию на английском: ")).lower()
        if not profession.isalpha():
            print("Некорректный ввод. Профессия должна содержать только буквы.")
            continue

        city = str(input("Введите город на русском: ")).lower()
        if not city.isalpha():
            print("Некорректный ввод. Город должен содержать только буквы.")
            continue

        salary = input("Введите желаемую зарплату: ")
        if not salary.isdigit():
            print("Некорректный ввод. Зарплата должна быть числом.")
            continue

        salary = int(salary)

        query = f"{profession} {city} {salary}"
        vacancies_data = api.get_vacancies(query)
        if vacancies_data is not None:
            vacancies = create_vacancy_objects(vacancies_data)
            if vacancies:
                user_all_vacancies = input("Вывести все найденные вакансии, или продолжить сортировку?\n 1.Вывести "
                                           "все вакансии\n 2.Продолжить сортировку\n >>>")
                if user_all_vacancies == "1":
                    for index, vacanci in enumerate(vacancies, start=1):
                        print(f"{index}. {vacanci}")
                else:
                    pass

                top_n = input("Введите количество вакансий для отображения: ")
                if not top_n.isdigit():
                    print("Некорректный ввод. Количество вакансий должно быть целым числом.")
                    continue

                top_n = int(top_n)

                filtered_vacancies = [v for v in vacancies if v.salary_from is not None and v.salary_from >= salary]

                # Сортируем отфильтрованные вакансии по зарплате
                sorted_vacancies = sorted(filtered_vacancies,
                                          key=lambda x: x.salary_to if x.salary_to is not None else float('inf'),
                                          reverse=True)

                # Выводим топ N вакансий
                print(f"Топ {min(top_n, len(sorted_vacancies))} вакансий по зарплатам:")
                for index, vacancy in enumerate(sorted_vacancies[:top_n], start=1):
                    print(f"{index}. {vacancy}")

                while True:
                    user_save = input("Сохранить ваш ТОП вакансий в JSON файл?\n 1.Да\n 2.Нет\n >>>")
                    if user_save in ('1', '2'):
                        break
                    else:
                        print("Некорректный ввод. Пожалуйста, введите '1' для сохранения или '2' для отмены.")

                if user_save == '1':
                    for vacancy in sorted_vacancies[:top_n]:
                        saver.add_vacancy(vacancy)
                    print("Вакансии сохранены в JSON файл.")
                elif user_save == '2':
                    print("Вакансии не сохранены.")

                break

            else:
                print("По вашему запросу вакансий не найдено.")
        else:
            print("Не удалось получить вакансии. Пожалуйста, попробуйте другой поисковый запрос.")
