class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def my_replace(text):
        punctuation = [',', '.', '=', '!', '?', ';', ':']
        for punct in punctuation:
            text = line.replace(punct, '')
            line = line.replace(' - ', ' ')
        return text

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = self.my_replace(text)
                all_words[file_name] = text.split()
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        counters = {}
        for file_name, words in self.get_all_words().items():
            words_count = words.count(word.lower())
            counters[file_name] = words_count
        return counters
