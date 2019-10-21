import os
from typing import List, Dict


def word_split(phrase, list_of_words, output=None):
    if not output:
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
    return output


def reverse_string(string):
    if len(string) <= 1:
        return string
    return reverse_string(string[1:]) + string[0]


def permutation(s):
    output = []
    if len(s) == 1:
        output = [s]
    else:
        for index, data in enumerate(s):
            for perm in permutation(s[:index] + s[index + 1:]):
                print('data is {} and perm is {}'.format(data, perm))
                output += [data + perm]
                print('output is', output)
    return output


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_memoization(n):
    temp = [0] * (n + 1)
    temp[0] = 0
    temp[1] = 1
    for i in range(2, n + 1):
        temp[i] = temp[i - 1] + temp[i - 2]
    return temp[n]


def rec_coin(target, coins):
    min_of_coins = target
    if target in coins:
        return 1
    else:
        for c in [coin for coin in coins if coin <= target]:
            num_of_coins = 1 + rec_coin(target - c, coins)
            if num_of_coins < min_of_coins:
                min_of_coins = num_of_coins
    return min_of_coins


# returns minimum from list of numbers.
def rec_max(num_list):
    if not num_list:
        return 0
    if len(num_list) == 1:
        return num_list[0]
    else:
        max_value = num_list[0]
        max_value = max(max_value, rec_max(num_list[1:]))
    return max_value


def print_reverse_number(n):
    if n == 0:
        print(0)
    else:
        print(n)
        print_reverse_number(n - 1)


def reverse_string_concat(string):
    raise NotImplementedError
    # if len(string) <= 1:
    #     return string
    # return reverse_string_concat(string[1:]) + reverse_string_concat(string[:-1])


def flatten_list(a, result=None):
    """Flattens a nested list.

        # >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
        [1, 2, 3, 4, 5, 6, 7]
    """
    if result is None:
        result = []

    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)

    return result


def flatten_dict(a, result=None, sub_directory=None):
    if not result:
        result = {}
    for key, value in a.items():
        if isinstance(value, dict):
            flatten_dict(a=value, result=result, sub_directory=key)
        else:
            if sub_directory:
                result[f'{sub_directory}.{key}'] = value
            else:
                result[key] = value
    return result


def un_flatten_dict(a):
    # if not result:
    #     result = {}
    # for key, value in a.items():
    #     if '.' in key:
    #         # you know it has sub directory.
    #         sub_directory = key.split('.')[0]
    #         if sub_directory not in result:
    #             result[sub_directory] = {}
    #             temp = {key.split('.')[1]: value}
    #             un_flatten_dict(sub_directory=sub_directory, result=result, a=temp)
    #         else:
    #             temp = {key.split('.')[1]: value}
    #             un_flatten_dict(sub_directory=sub_directory, result=result, a=temp)
    #     elif sub_directory:
    #         result[sub_directory][key] = value
    #     else:
    #         result[key] = value
    # return result
    result = {}
    for key in a.keys():
        if "." in key:
            parent, child = key.split(".", 1)
            if parent in result.keys():
                result[parent].update(un_flatten_dict({child: a[key]}))
            else:
                result.update({parent: un_flatten_dict({child: a[key]})})
        else:
            result.update({key: a[key]})
    return result


def tree_map(func, list_of_numbers):
    result = []
    for number in list_of_numbers:
        if isinstance(number, list):
            result.append(tree_map(func, number))
        else:
            result.append(func(number))
    return result


def tree_reverse(list_of_numbers):
    result = []
    for number in list_of_numbers:
        if isinstance(number, list):
            result.insert(0, tree_reverse(number))
        else:
            result.insert(0, number)
    return result


#
# def dir_tree(file_path, is_dir=None):
#     all_files_and_folder_with_path = [os.path.join(file_path, file) for file in os.listdir(file_path)]
#     for files in all_files_and_folder_with_path:
#         if os.path.isdir(files):
#             print(f'|-- {files.split("/")[-1]}/')
#             dir_tree(files, True)
#         elif is_dir:
#             print(f'|   |-- {files.split("/")[-1]}')
#         else:
#             print(f'|-- {files.split("/")[-1]}')


if __name__ == '__main__':
    # print(word_split('themanran', ['the', 'ran', 'man']))
    # print(reverse_string('hello'))
    # print(permutation('abc'))
    # print(fib(10))
    # print(fib_memoization(10))
    # print(rec_coin(15, [1, 5, 10]))
    # print(rec_max([123, 243, 1245, 21, 234, 0, 1235354, 2343565, 898767465675]))
    # print_reverse_number(10)
    # print(reverse_string_concat('jenil'))
    # print(flatten_list([[1, 2, [3, 4]], [5, 6], 7]))
    # print(flatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
    # print(un_flatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
    # print(tree_map(lambda x: x * x, [1, 2, [3, 4, [5]]]))
    # print(tree_reverse([[1, 2], [3, [4, 5]], 6]))
    # path = os.path.join(os.path.dirname(__file__), '..')

    # print(dir_tree(os.path.dirname(os.getcwd())))
    pass
