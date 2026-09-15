from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_char = {}
    for char in word:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    return count_char


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
