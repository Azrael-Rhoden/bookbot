def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(word_count(file_contents))
        print(char_count(file_contents))


def word_count(f):
    count = 0
    words = f.split()
    for i in words:
        count += 1
    return count

def char_count(f):
    lowered_f = f.lower()
    word_dict = {}
    for i in lowered_f:
        if i not in word_dict:
            word_dict[i] = 0
        word_dict[i] += 1
    
    return word_dict
main()