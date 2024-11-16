import random
import re
import json
import os
from langchain.prompts import PromptTemplate

tarot_cards = [
    # Старшие Арканы
    "Шут (Дурак)", "Маг", "Верховная Жрица", "Императрица", "Император",
    "Иерофант (Жрец)", "Влюблённые", "Колесница", "Сила", "Отшельник",
    "Колесо Фортуны", "Справедливость", "Повешенный", "Смерть",
    "Умеренность", "Дьявол", "Башня", "Звезда", "Луна", "Солнце",
    "Суд", "Мир",
    
    # Младшие Арканы - Жезлы
    "Туз Жезлов", "Двойка Жезлов", "Тройка Жезлов", "Четвёрка Жезлов",
    "Пятёрка Жезлов", "Шестёрка Жезлов", "Семёрка Жезлов", "Восьмёрка Жезлов",
    "Девятка Жезлов", "Десятка Жезлов", "Паж Жезлов", "Рыцарь Жезлов",
    "Королева Жезлов", "Король Жезлов",
    
    # Младшие Арканы - Кубки
    "Туз Кубков", "Двойка Кубков", "Тройка Кубков", "Четвёрка Кубков",
    "Пятёрка Кубков", "Шестёрка Кубков", "Семёрка Кубков", "Восьмёрка Кубков",
    "Девятка Кубков", "Десятка Кубков", "Паж Кубков", "Рыцарь Кубков",
    "Королева Кубков", "Король Кубков",
    
    # Младшие Арканы - Мечи
    "Туз Мечей", "Двойка Мечей", "Тройка Мечей", "Четвёрка Мечей",
    "Пятёрка Мечей", "Шестёрка Мечей", "Семёрка Мечей", "Восьмёрка Мечей",
    "Девятка Мечей", "Десятка Мечей", "Паж Мечей", "Рыцарь Мечей",
    "Королева Мечей", "Король Мечей",
    
    # Младшие Арканы - Пентакли
    "Туз Пентаклей", "Двойка Пентаклей", "Тройка Пентаклей", "Четвёрка Пентаклей",
    "Пятёрка Пентаклей", "Шестёрка Пентаклей", "Семёрка Пентаклей", "Восьмёрка Пентаклей",
    "Девятка Пентаклей", "Десятка Пентаклей", "Паж Пентаклей", "Рыцарь Пентаклей",
    "Королева Пентаклей", "Король Пентаклей"
]

tarot_cards = [card.lower() for card in tarot_cards]


def parse_txt_files(folder_path: str) -> dict:
    """
    Считывает все txt файлы в папке и их содержимое,
    добавляя содержимое rules.txt ко всем другим файлам.
    
    Возвращает словарь с ключами - именами файлов и значениями - содержимым.
    """

    if not os.path.exists(folder_path):
        print('Указанная папка не найдена')
    
    prompts = {}
    rules_file_path = os.path.join(folder_path, 'rules.txt')

    try:
        with open(rules_file_path, 'r', encoding='utf-8') as file:
            rules_content = file.read()
    except FileNotFoundError as ex:
        print ('Файл rules.txt не найден')

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') and filename != 'rules.txt':
            key = os.path.splitext(filename)[0]
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except Exception as e:
                continue

            prompts[key] = rules_content + content

    return prompts





def process_tarot_data(raw_data: str) -> dict:
    """
    Функция для обработки строки с картами Таро, удаления символов, замены скобок и преобразования в JSON.

    :param raw_data: строка с данными карт Таро в формате с и квадратными скобками
    :return: возвращает обработанный JSON в виде словаря
    """
    processed_data = raw_data.replace("\n", "").replace("[", "{").replace("]", "}")

    pattern = r"{(.*)}"
    matches = re.findall(pattern, processed_data)

    if matches:
        json_data = "{" + matches[0] + "}"
        return json.loads(json_data)
    else:
        raise ValueError("Не удалось извлечь данные")
    

def draw_random_cards(tarot_list: list[str] = tarot_cards, N: int = 3) -> list[str]:
    """
    Функция для случайного выбора N карт из списка tarot_list.
    Карты могут повторяться.

    :param tarot_list: список карт Таро
    :param N: количество карт для выбора
    :return: список из N случайных карт
    """
    new_list = [random.choice(tarot_list) for _ in range(N)]

    result_list = [
        card + " перевёрнута" if random.random() < 0.25 else card
        for card in new_list
    ]
    return result_list


def get_tarot(model, data: dict, N: int = 3):
    """
    Функция для выдачи словаря с N картами и их описание
    """
    data = parse_txt_files('prompts/')
    tarot = draw_random_cards(tarot_list = tarot_cards, N = 3)


    prompt = PromptTemplate(
        template = data['tarot_description'],
        input_variables = ['tarot_list']
    ).format(
        tarot_list = tarot
    )

    tarot = process_tarot_data(model.invoke(prompt).content)
    return tarot