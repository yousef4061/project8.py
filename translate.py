def read_from_file():
    global words_bank
    words_bank = []
    try:
        f = open("Translate.txt", "r")
        words = []
        for line in f:
            words.append(line,strip())
        temp = f.read().split("\n")
        for i in range(0, len(temp)-1, 2):
            my_dict = {"en": temp[i], "fa": temp[i+1]}
            words_bank.append(my_dict)
        f.close()
    except FileNotFoundError:
        print("file not found! please create translate.txt first.")
        exit()

def translate_english_to_persian():
    user_txt = input("enter your english text: ")
    user_words = user_txt.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"] + " "
                break
        else:
            output = output + user_word + " "

    print(output)

def translate_persian_to_english():
    user_txt = input("enter your persian text: ")
    user_words = user_txt.split(" ")
    output = ""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                output = output + word["en"] + " "
                break
        else:
            output = output + user_word + " "
    print(output)

def add_new_word():
    en_word = input("enter english word: ")
    fa_word = input("enter persian word: ")
    with open ("translate.txt", "a") as f:
        f.write(f"{en_word} {fa_word}\n")
        print("word added!")
    
def show_menu():
    print("welcome to my translate")
    print("1- translate english to persian")
    print("2- translate persian to english")
    print("3- add a new word to database")
    print("4- exit")

read_from_file()

while True:
    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()
    elif choice == 3:
        add_new_word()
    elif choice == 4:
        exit(0)
