from main import load_words, save_words, show_all_words, add_words

result = load_words('words.txt')

print('===Тест load_words===')
print(result)

words = {
    'cat': 'кот',
    'dog': 'собака',
    'bird': 'птица',
}

print('\n===Тест save_words===')
save_words(words, 'test_words.txt')

print('\n===Тест show_all_words===')
show_all_words(words)

print('\n===Тест add_words===')
add_words(words)
