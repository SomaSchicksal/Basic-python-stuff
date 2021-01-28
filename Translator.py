def translate (phrase):
    translation=""
    for vowel in phrase:
        if vowel in "AEIOUaeiou":
            translation= translation  + "g"
        else:
            translation= translation + vowel

    return translation

print(translate(input("Enter a phrase:")))

