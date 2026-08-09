import random
import sys
import time
from typing import Dict, Tuple

STOP_WORD = 'СТОП'


def load_words(filename):
    dictionary = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 2:
                    continue
                key, value = parts[0].strip(), parts[1].strip()
                dictionary[key] = value
    except FileNotFoundError:
        print(f'Файл {filename} не найден.')
        sys.exit(1)

    return dictionary


def print_statistics(score, total_time):
    pass


def ask_and_check(word, correct):
    pass


def start_game(words):

    if not words:
        print('Словарь пуст. Добавьте слова перед началом игры.')
        return

    print(
        'Начинаем игру! Введите перевод слова. Чтобы закончить, введите СТОП'
    )

    total_time = 0
    score = 0
    answer_count = 0

    key_list = list(words.keys())

    while True:
        random_key = key_list[random.randint(0, len(key_list) - 1)]

        start_time = time.time()

        print(f'Переведите слово: {random_key}')

        user_answer = input('Ваш ответ: ')

        if user_answer.strip().upper() == STOP_WORD:
            average_time_message = ''

            if answer_count > 0:
                average_time_message = (
                    f' (Среднее время ответа:'
                    f'{total_time / answer_count:.2f} секунд)'
                )

            print(
                f'Игра окончена.\nВаш счет: {score}.\n'
                f'Общее время: {total_time:.2f} секунд{average_time_message}.'
            )

            break

        answer_time = time.time() - start_time
        total_time += answer_time
        answer_count += 1

        if user_answer.strip().lower() == words[random_key].strip().lower():
            score += 1

            print(f'Верно! Время ответа: {answer_time:.2f} секунд')

        else:
            print(
                f'Неверно! Правильный ответ: {words[random_key]}.\n'
                f'Время ответа: {answer_time:.2f} секунд'
            )


def train_until_mistake(words):
    pass


def add_words(words):

    print('Чтобы закончить, введите СТОП')

    while True:
        input_word = input('Введите слово: ')

        if input_word.strip().upper() == STOP_WORD:
            break

        input_translation = input('Введите перевод: ')

        if input_translation.strip().upper() == STOP_WORD:
            break

        words[input_word.strip()] = input_translation.strip()


def show_all_words(words):
    all_words = []

    for key, value in words.items():
        all_words.append(f'{key} - {value}')

    print('; '.join(all_words))


def save_words(words, filename='words.txt'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for key, value in words.items():
                file.write(f'{key},{value}\n')

        print(f'Было сохранено {len(words)} слов в файл {filename}')

    except Exception as e:
        print(f'Ошибка при сохранении слов: {e}')


def main():
    while True:
        menu = '''Меню:
        1. Начать игру
        2. Добавить слова
        3. Тренировка до первой ошибки
        4. Вывод всех слов
        5. Выход
        '''
        print(menu)
        menu_choice = input('Пункт меню: ')


if __name__ == '__main__':
    main()
