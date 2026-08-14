sentence = input("Enter your string: ")

vowels = "aeiouAEIOU"
count_vowel = 0

for char in sentence:
    if char in vowels:
        count_vowel += 1

print("Number of vowels:", count_vowel)
