def get_vowels(input_string):
    vowel_counts = {}
    lowercase = input_string.lower()
    for vowel in "aeiou":
        count = lowercase.count(vowel)
        vowel_counts[vowel] = count
    counts = vowel_counts.values()
    total_vowels = sum(counts)
    return [total_vowels, vowel_counts]

vowels = get_vowels('aeiou')
print(vowels[1])
print(vowels[0])

