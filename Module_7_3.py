class WordsFinder:
    file_names = []
    def __init__(self,names):
        self.file_names.append(names)
        self.names = names


    def get_all_words(self):
        all_words = {}
        new_str = []
        with open (self.names,'r',encoding = 'utf-8') as file:
            str_ = (file.read()).lower().split(sep=None, maxsplit=-1)
            for i in str_:
                i = i.replace(',', '')
                i = i.replace('.', '')
                i = i.replace('=', '')
                i = i.replace('!', '')
                i = i.replace('?', '')
                i = i.replace(';', '')
                i = i.replace(':', '')
                i = i.replace( ' - ', '')
                new_str.append(i)
            all_words[self.names] = new_str
        return all_words

    def find(self, word):
        answer_find = {}
        find_ = WordsFinder.get_all_words(self)
        all_list = find_[self.names]
        count_ : int = 0
        for i in all_list:
            count_ += 1
            if i == word.lower():
                break
        answer_find[self.names] = count_
        return answer_find


    def count(self, word):
        answer_count = {}
        num_count : int = 0
        count_ =  WordsFinder.get_all_words(self)
        all_list_for_count = count_[self.names]
        for i in all_list_for_count:
            if i == word.lower():
                num_count += 1
        answer_count[self.names] = num_count
        return answer_count


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print('finder2.get_all_words() = ',finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
