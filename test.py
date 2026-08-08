from main import load_words, save_words

result = load_words('words.txt')

print(result)

words = {
    'cat': 'кот',
    'dog': 'собака',
    'bird': 'птица'
}

save_words(words, 'test_words.txt')