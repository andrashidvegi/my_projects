from word_dicts import first_word_dict, chinese_0928


def iterate_guesses(words_dict: dict, counter: int = 1):
    print(f"Round {counter}")
    guessed_wrong = {}
    for key, value in words_dict.items():
        print(key)
        guessed = input()
        if guessed == value:
            print('---correct! \n\n\n\n\n\n')
        else:
            guessed_wrong[key] = value
            print(f"---you guessed: {guessed} - the correct answer is: {value}\n\n\n\n\n\n")
            input()

    if guessed_wrong:
        counter += 1
        total_this_round = len(words_dict.keys())
        total_guessed = total_this_round - len(guessed_wrong.keys())
        print(f"Total this round: {total_this_round} guessed: {total_guessed}")
        iterate_guesses(guessed_wrong, counter)
    else:
        print("Congratulations! You successfully learnt the module.")


iterate_guesses(chinese_0928)
