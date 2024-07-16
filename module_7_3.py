class WordsFinder:
    __file_names = ()

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                info = file.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' -']:
                    info = info.replace(sym, '')
                all_words[name] = info.split()

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                print(f'{word} found in {name}')

w = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
w.get_all_words()
print(w.get_all_words())