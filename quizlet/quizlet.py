from random import shuffle

from word_dicts import chinese_0410


def iterate_guesses(words_dict: dict, counter: int = 1):
    dict_items = list(words_dict.items())
    shuffle(dict_items)
    print(f"Round {counter}, number of words: {len(words_dict.keys())}")
    guessed_wrong = {}
    for key, value in dict_items:
        print(key)
        guessed = input()
        if guessed == value:
            print('---correct! \n\n\n\n\n\n')
        else:
            print(f"---you guessed: {guessed} - the correct answer is: {value}\n\n\n\n\n\n")
            second = input()
            if not second == 'i was right':
                guessed_wrong[key] = value

    if guessed_wrong:
        counter += 1
        total_this_round = len(words_dict.keys())
        total_guessed = total_this_round - len(guessed_wrong.keys())
        print(f"Total this round: {total_this_round} guessed: {total_guessed}")
        iterate_guesses(guessed_wrong, counter)
    else:
        print(f"Congratulations! You successfully learnt the module in {counter} rounds.")


iterate_guesses(chinese_0410)
