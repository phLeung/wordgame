import os
common_words_path = os.environ['HOME'] + "/Projects/gre_word_game/words/common.txt"
basic_words_path = os.environ['HOME'] + "/Projects/gre_word_game/words/basic.txt"
advanced_words_path = os.environ['HOME'] + "/Projects/gre_word_game/words/advanced.txt"

def sort_words(file_path):
    with open(file_path, 'r+') as f:
        words = f.readlines()
        words = [word.strip() for word in words]
        words.sort()
    return words

def write_common_sorted(file_path):
    assert(os.path.isfile(file_path))
    words_sorted = sort_words(file_path)
    with open(file_path,"w") as f:
        for word in words_sorted:
            f.write(word)
            f.write("\n")


        
write_common_sorted(common_words_path)
