def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_char_count(text):
    text = text.lower()
    words = text.split()

    char_count = {}

    for word in words:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def sort_on(dict):
    return dict["count"]

def sort_chars_count(chars_count):
    chars = []
    for char in chars_count:
        item = {}
        item["char"] = char
        item["count"] = chars_count[char]

        chars.append(item)

    chars.sort(reverse=True, key=sort_on)    

    return chars    

# chars = get_char_count("deaba aba Abc")
# print(sort_chars_count(chars))