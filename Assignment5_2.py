def IsVowel(ch1):
    vowels = "aeiou"
    if ch1 in vowels :
        print(ch1 + " is a vowel")
    else:
        print(ch1 + " is a consonant")

def main():
    ch = input("Enter a single character: ")

    if len(ch) >= 1 :
        print("Enter only single character.")
        return

    IsVowel(ch)

if __name__ == "__main__":
    main()
