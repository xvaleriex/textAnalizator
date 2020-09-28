import string
separator = '-' * 30
greet_str = 'Welcome to the Text Analyzer App. Please log in:'
success = 'Successfully logged in!'
choose_text = 'There are 3 texts to be analyzed. \n Please select text number between 1 and 3: '

def process_registered_users():
    '''
    Function that processes the file with registered users and their passwords into a dict
    :return: a dictionary user: password
    '''
    result_dict = {}
    with open('registered_users.txt', 'r') as users_file:
        # we need to skip first 2 lines, they contain no useful info
        next(users_file)
        next(users_file)
        for line in users_file:
            #strip first and last | and split into list
            line_values_list = line.strip('|').split()
            # since input has same structure, positions of data
            # for username and pass will be always the same
            result_dict[line_values_list[0]] = line_values_list[2]
    # print(result_dict)
    return result_dict


def check_username(user):
    '''
    Function that checks if given user is in dictionary of registered users
    :param user: username to check
    :return: True if username is in dictionary, False otherwise
    '''
    if user in registeredUsers.keys():
        return True
    else:
        return False


def check_password(user, passw):
    '''
    Function that checks if for given username, password corresponds to the one given
    in parameters
    :param user: username to check the password for
    :param passw: password to check
    :return: True if password id correct, False otherwise
    '''
    if registeredUsers[user] == passw:
        return True
    else:
        return False


def process_text_source():
    text_string = ''
    with open('task_template.py', 'r') as texts_file:
        # we need to skip first 4 lines, they contain no useful info
        next(texts_file)
        next(texts_file)
        next(texts_file)
        next(texts_file)
        for line in texts_file:
            text_string += line.strip(']')
        text_list = text_string.split('\'\'\',\n\n\'\'\'', 2)
        for text in text_list:
            text = text.strip('\'')
            print(type(text))
    return text_list


def count_words(text):
    '''
    Count amount of different type of words in a selected text.
    Word can be numeric, alphabetic, titlecase,
    :param text: selected text as a string
    :return: list of words in this text that are being count,
    for future processing by other functions
    '''
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
    items = []
    # words_sum = sum([item.strip(string.punctuation)for item in text.split()])
    for item in text.split():
        # we could use string.punctuation, but then it would strip words like 'upper-case'
        # so we define custom set
        item = item.strip(r"""!"#$%&'()*+,./:;<=>?@[\]^_`{|}~""")
        if item.isalpha() or ('-' in item) or item.isnumeric():
            if item[0].isupper():
                title_count += 1
            if item.isnumeric():
                num_count += 1
            if item.isupper():
                upper_count += 1
            if item.islower():
                lower_count += 1
            items.append(item)
            all_count += 1
    print(f'There are {all_count} words in the selected text.')
    print(f'There are {num_count} numeric strings in the text.')
    print(f'There are {title_count} titlecase words')
    print(f'There are {upper_count} uppercase words')
    print(f'There are {lower_count} lowercase words')
    return items


def create_chart(words_list):
    letters_dict = {}
    for word in words_list:
        letters_dict[len(word)] = letters_dict.get(len(word), 0) + 1
    for key, value in letters_dict.items():
        stars = value * '*'
        print(f'{key} {stars} {value}')


def sum_numeric(items):
    s = 0
    s = 0
    for word in items:
        if word.isnumeric():
            s += int(word)
    print(f'If we sum up all the numbers in this text we will get {s}')

def analyze_text(num):
    '''
    Function that analyzes selected text
    :param text_num: index of text selected
    :return:
    '''
    text_list = process_text_source()
    items = count_words(text_list[num])
    print(separator)
    create_chart(items)
    print(separator)
    sum_numeric(items)



registeredUsers = process_registered_users()
print(separator)
print(greet_str)
print(separator)
username = input('USERNAME: ')
# checkusername - function that checks if username is between registered users
if (not check_username(username)):
    # returned false, user is not registered
    print('Sorry, you are not registered. Only registered users can use this cool app.')
else:
    # if returned true, proceed with password
    password = input('PASSWORD: ')
    # check that password for registered user is same as should be
    if (not check_password(username, password)):
        #returned false, password is not correct
        passwordCorrect = False
        while (not passwordCorrect):
            password = input ('Wrong password. Please try again! \nPASSWORD: ')
            passwordCorrect = check_password(username, password)
    print(success)
    print(separator)

    is_between_1_and_3 = False
    while not is_between_1_and_3:
        text_num = int(input(choose_text))
        if text_num in range(1, 4):
            is_between_1_and_3 = True
    print(separator)
    analyze_text(text_num - 1)








