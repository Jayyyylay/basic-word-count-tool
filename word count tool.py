def main():
    again = True
    while again:
        print("\nWelcome to Word count tool\n")
        enter = input("Enter a sentence or a paragraph: ")
        word_list = enter.split()
        num_word = len(word_list)
        print(f"THERE ARE {num_word} WORDS ")

main()
