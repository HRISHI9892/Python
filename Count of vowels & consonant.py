def count(word):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonant_count =0
    for char in word:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonant_count += 1
    print("Number of vowels : ", vowels_count)
    print("Number of consonant : ", consonant_count)

user_word = input("Enter a word : ")
count(user_word)
