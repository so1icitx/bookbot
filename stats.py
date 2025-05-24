def book_len(book):
    book = book.split()
    return book



def count_char(book):
    main_dict={}
    for word in book:
        for char in word:
            char = char.lower()
            if char in main_dict:def book_len(book):
    book = book.split()
    return book



def count_char(book):
    main_dict={}
    for word in book:
        for char in word:
            char = char.lower()
            if char in main_dict:
                main_dict[char] += 1
            else:
                main_dict[char] = 1
    return main_dict



def sort_d(dict1):

    def none(dict):
        return dict["num"]
    

    placeholder_dict = {}
    sorted_list = []

    for key in dict1:

        placeholder_dict['char'] = key
        placeholder_dict['num'] = dict1[key]
        sorted_list.append(placeholder_dict)
        placeholder_dict = {}

    sorted_list.sort(reverse=True, key = none)
    return sorted_list
                main_dict[char] += 1
            else:
                main_dict[char] = 1
    return main_dict



def sort_d(dict1):

    def none(dict):
        return dict["num"]
    

    placeholder_dict = {}
    sorted_list = []

    for key in dict1:

        placeholder_dict['char'] = key
        placeholder_dict['num'] = dict1[key]
        sorted_list.append(placeholder_dict)
        placeholder_dict = {}

    sorted_list.sort(reverse=True, key = none)
    return sorted_list
