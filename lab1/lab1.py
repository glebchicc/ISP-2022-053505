from statistics import mean, median

text_data =  """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

words = {}
def count_words(text_data):
    #создадим словарь, где будем считать количество слов
    for word_from_text in text_data.split():
        word = word_from_text.strip(',.!?;:').lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

#выводим словарь на экран, где до двоеточия указывается слово, а после двоеточия - частота его появления в тексте
def print_dict(dictionary):
    for k, v in dictionary.items():
        print(f'{k}:{v}')

#создаем список, который хранит число слов в предложениях текста
sentence_words = []
def count_sentence_words(text_data):
    for i in filter(None, text_data.split('.')):
        sentence_words.append(len(i.split()))

#создаем словарь для n-грам
ngrams = {}
def k_of_n(text_data, k, n) :
    for word_from_text in text_data.split():
        word_from_text = word_from_text.strip(',.!?;:').lower()
        for i in range(len(word_from_text) - n + 1):
            gram = word_from_text[i:n+i]
            if gram in ngrams:
                ngrams[gram] += 1
            else:
                ngrams[gram] = 1
    sorted_dict = dict(sorted(ngrams.items(), reverse = True, key = lambda x: x[1]))
    sorted_dict = dict(list(sorted_dict.items())[0: k])
    return sorted_dict

print("Введите k")
k = int(input())
print("Введите n")
n = int(input())

#выводим число слов
print("Words count:")
count_words(text_data)
print_dict(words)

#считаем и выводим среднее арифметическое и медианное количество слов
count_sentence_words(text_data)
print("\nAverage number of words in sentences:")
print(int(mean(sentence_words)))
print("\nMedian number of words in sentences:")
print(int(median(sentence_words)))

count_sentence_words(text_data)
print("\nN-grams:")
print_dict(k_of_n(text_data, k, n))