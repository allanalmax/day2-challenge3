def countvowels(my_string):
    vowels_in_string = set()
    my_vowels = ["a", "e", "o", "u"]
    for vowel in my_string:
        if vowel in my_vowels:
            vowels_in_string.add(vowel)

    dup_elements = set()
    for letter in my_string:
        dup_element_list = []
        for element in my_string:
            if element == letter:
                dup_element_list.append(letter)
        if len(dup_element_list) > 1 :
            dup_elements.add(letter)

    vowels_string = ",".join(vowels_in_string)
    duplicates_number = len(dup_elements)
    return (vowels_string, duplicates_number)

my_string = input("enter your string: ")
result = countvowels(my_string)
print(result)