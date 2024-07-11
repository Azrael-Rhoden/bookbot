def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count_func = word_count(file_contents)
        count_char = char_count(file_contents)
        converted_list = convert_list(count_char)
        converted_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count_func} words found in the document \n")
        for item in converted_list:
            print(f"The '{item['letter']}' character was found {item['num']} times")
        print("--- End report ---")
        


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

def convert_list(word_dict):
    list_of_dicts = []
    for key, value in word_dict.items():
        if key.isalpha():
            list_of_dicts.append({'letter': key, 'num': value})    
    return list_of_dicts

def sort_on(list_of_dicts):
    return list_of_dicts['num']

main()