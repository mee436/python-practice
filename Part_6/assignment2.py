def count_vowels(word):
    count = 0
    for character in word.lower():
        if character in "aeiou":
            count += 1
    
    return count

vowel_count = count_vowels("Hello Motoo")
print(vowel_count)