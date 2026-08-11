import random
import sys
import time
from typing import Dict, Tuple

STOP_WORD = 'СТОП'


def load_words(filename: str) -> Dict[str, str]:
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


def ask_and_check(word: str, correct: str) -> Tuple[bool, bool, float]:
    print(f'Переведите слово: {word}')

    start_time = time.time()

    answer = input('Ваш ответ: ')

    if answer.strip().upper() == STOP_WORD:
        return True, False, 0.0

    answer_time = time.time() - start_time

    is_correct = answer.strip().lower() == correct.strip().lower()

    return False, is_correct, answer_time


def start_game(words: Dict[str, str]):

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
        random_key = random.choice(key_list)
        correct_answer = words[random_key]

        is_stop, is_correct, answer_time = ask_and_check(
            random_key,
            correct_answer,
        )

        if is_stop:
            average_time_message = ''
            if answer_count > 0:
                average_time_message = (
                    f'Среднее время ответа: '
                    f'{total_time / answer_count:.2f} сек.'
                )
            print(
                f'Спасибо за игру!'
                f'Ваш итоговый счет: {score}\n'
                f'Время игры: {total_time:.2f} секунд'
                f' {average_time_message}'
            )
            break

        total_time += answer_time
        answer_count += 1

        if is_correct:
            score += 1
            print(f'Верно! Время ответа: {answer_time:.2f} секунд')

        else:
            print(
                f'Неверно! Правильный ответ: {correct_answer}.\n'
                f'Время ответа: {answer_time:.2f} секунд'
            )


def train_until_mistake(words: Dict[str, str]):
    pass


def add_words(words: Dict[str, str]):

    print('Чтобы закончить, введите СТОП')

    while True:
        input_word = input('Введите слово: ')

        if input_word.strip().upper() == STOP_WORD:
            break

        input_translation = input('Введите перевод: ')

        if input_translation.strip().upper() == STOP_WORD:
            break

        words[input_word.strip()] = input_translation.strip()


def show_all_words(words: Dict[str, str]):
    all_words = []

    for key, value in words.items():
        all_words.append(f'{key} - {value}')

    print('; '.join(all_words))


def save_words(words: Dict[str, str], filename: str = 'words.txt'):
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

        if menu_choice == '1':
            words = load_words('words.txt')
            start_game(words)

        elif menu_choice == '2':
            words = load_words('words.txt')
            add_words(words)
            save_words(words, 'words.txt')

        elif menu_choice == '3':
            words = load_words('words.txt')
            train_until_mistake(words)

        elif menu_choice == '4':
            words = load_words('words.txt')
            show_all_words(words)

        elif menu_choice == '5':
            print('До свидания!')
            break


if __name__ == '__main__':
    main()
