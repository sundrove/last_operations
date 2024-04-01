import json
import re
from datetime import datetime


def open_json_file(filename):
    """Считывает файл json"""
    with open(filename) as json_file:
        return json.load(json_file)


def filter_list(data):
    """фильтрует, оставляя только выполненные операции"""
    filtred_list = []
    for operation in data:
        if operation.get('state') == "EXECUTED":
            filtred_list.append(operation)
    return filtred_list


def sort_operation_list(operations_data: list[dict]) -> list[dict]:
    """сортирует список по дате"""
    sorted_list = sorted(operations_data, key=lambda x: x['date'], reverse=True)
    return sorted_list


def date_converting(date):
    """преобразует дату в нужный формат
    """
    newdate = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return newdate.strftime("%d.%m.%Y")


def hide_from(from_):
    """Маскирует часть номера счета, откуда был перевод, и выводит в нужном формате"""
    if from_ is not None:
        card_numbers = ' '.join(re.findall("\d{4}", from_))
        letters = ''.join(re.findall("\D", from_))
        return f'{letters}{card_numbers[:-12]}** **** {card_numbers[-4:]}'


def hide_to(to_):
    """Маскирует часть номера счета, куда был перевод, и выводит в нужном формате"""
    if to_ is not None:
        numbers = ''.join(re.findall("\d", to_))
        letters = ''.join(re.findall("\D", to_))
        return f'{letters}**{numbers[-4:]}'
