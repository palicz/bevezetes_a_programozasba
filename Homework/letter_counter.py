# coding: utf-8

def main():
    # Input
    sentence = input("Adjon meg egy mondatot: \n")

    # Count the letters in sentence
    letter_counter = {}
    for i in sentence:
        letter = letter_counter.keys()
        if i in letter:
            letter_counter[i] += 1
        else:
            letter_counter[i] = 1
    print(letter_counter)

    # Print the sentence reversed
    reversed_sentence = sentence[::-1]
    print("Fordítva: ", reversed_sentence)

    # Print the words of sentence in a list (Split the sentence)
    print("Listába rendezve szavanként: ", sentence.split())


if __name__ == "__main__":
    main()