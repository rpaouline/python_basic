def int_func(word: str) -> str:
    """
    The function capitalizes the word.
    :param word: word in lower case
    :return: word with first letter in upper case
    """
    if word:
        return word.upper()[0]+word.lower()[1:]

    return word


def int_func_exp(sentence: str) -> str:

    return ' '.join([int_func(word) for word in sentence.split(' ') if word])


print(int_func_exp(input("Input a sentence:\n")))
