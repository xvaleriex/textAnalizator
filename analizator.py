from task_template import TEXTS

SEPARATOR = '-' * 30
SEPARATOR_CHAR = '*'
GREET = 'Welcome to the Text Analyzer App. Please log in:'
SUCCESS = 'Successfully logged in!'
CHOOSE_TEXT = 'There are 3 texts to be analyzed. \n Please select text number between 1 and 3: '
NOT_REGISTERED = 'Sorry, you are not registered. Only registered users can use this cool app.'
WRONG_PASSWORD = 'Wrong password. Try Again.'
REGISTERED_USERS_FILE = 'registered_users.txt'


def process_registered_users(file) -> dict:
    """
    Function that processes the file with registered users and their passwords into a dict
    :return: a dictionary user: password
    """
    result_dict = {}
    with open(file, 'r') as users_file:
        # we need to skip first 2 lines, they contain no useful info
        next(users_file)
        next(users_file)
        for line in users_file:
            # strip first and last | and split into list
            line_values_list = line.strip('|').split()
            # since input has same structure, positions of data
            # for username and pass will be always the same
            result_dict[line_values_list[0]] = line_values_list[2]
    # print(result_dict)
    return result_dict


def check_username(user) -> bool:
    """
    Function that checks if given user is in dictionary of registered users
    :param user: username to check
    :return: True if username is in dictionary, False otherwise
    """
    return user in registeredUsers.keys()


def check_password(user, passw) -> bool:
    """
    Function that checks if for given username, password corresponds to the one given
    in parameters
    :param user: username to check the password for
    :param passw: password to check
    :return: True if password id correct, False otherwise
    """
    if registeredUsers[user] == passw:
        return True
    else:
        return False


def process_text_source() -> list:
    text_list = []
    for text in TEXTS:
        text_list.append(text.strip('\''))
    return text_list


def count_words(text: str) -> list:
    """
    Count amount of different type of words in a selected text.
    Word can be numeric, alphabetic, titlecase,
    :param text: selected text as a string
    :return: list of words in this text that are being count,
    for future processing by other functions
    """
    # counter for all words
    all_count = 0
    # counter for numeric words
    num_count = 0
    # counter for words that start with upper case
    title_count = 0
    # counter for upper case words
    upper_count = 0
    # counter for lower case words
    lower_count = 0
    # for sum of all numbers
    numbers_sum = 0
    items = []
    # words_sum = sum([item.strip(string.punctuation)for item in text.split()])
    for item in text.split():
        # we could use string.punctuation, but then it would strip words like 'upper-case'
        # so we define custom set
        item = item.strip(r"""!"#$%&'()*+,./:;<=>?@[\]^_`{|}~""")
        # word can be numeric, can have - character in them, or be numbers
        if not item.isalpha() and not item.isnumeric() and '-' not in item:
            continue

        # then count uppercase, lowercase, titlecase words, numeric strings separately
        if item[0].isupper():
            title_count += 1
        if item.isnumeric():
            num_count += 1
            numbers_sum += int(item)
        if item.isupper():
            upper_count += 1
        if item.islower():
            lower_count += 1
        items.append(item)
    print(f'There are {len(items)} words in the selected text.')
    print(f'There are {num_count} numeric strings in the text.')
    print(f'There are {title_count} titlecase words')
    print(f'There are {upper_count} uppercase words')
    print(f'There are {lower_count} lowercase words')
    print(f'If we sum up all the numbers in this text we will get {numbers_sum}')
    return items


def create_chart(words_list):
    """
    Function to create chart that represents amount or words of different lengths
    """
    letters_dict = {}
    for word in words_list:
        letters_dict[len(word)] = letters_dict.get(len(word), 0) + 1
    for key, value in letters_dict.items():
        stars = value * SEPARATOR_CHAR
        print(f'{key} {stars} {value}')


def analyze_text(num):
    """
    Function that analyzes selected text
    :param num: index of text selected
    :return:
    """
    text_list = process_text_source()
    items = count_words(text_list[num])
    print(SEPARATOR)
    create_chart(items)
    print(SEPARATOR)

if __name__ == '__main__':
    registeredUsers = process_registered_users(REGISTERED_USERS_FILE)
    print(SEPARATOR)
    print(GREET)
    print(SEPARATOR)
    username = input('USERNAME: ')
    # checkusername - function that checks if username is between registered users
    if not check_username(username):
        # returned false, user is not registered
        print(NOT_REGISTERED)
        exit(1)

    # if returned true, proceed with password
    # check that password for registered user is same as should be
    while not check_password(username, input('PASSWORD: ')):
        print(WRONG_PASSWORD)

    print(SUCCESS)
    print(SEPARATOR)

    text_num = -1
    while text_num not in range(1, len(TEXTS)+1):
        text_num = int(input(CHOOSE_TEXT))

    print(SEPARATOR)
    analyze_text(text_num - 1)
