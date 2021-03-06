from typing import List, Dict, Union, Generator
import random
import string

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter
    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for x in data:
        if 'name' in x:
            x['name'] = x['name'].capitalize()
    return data

def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value
    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for x in data:
        for key in redundant_keys:
            if key in x:
                del x[key]
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    return [d for d in data if value in d.values()]

def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    if data:
        x = data[0]
        for i in data:
            if i < x:
                x = i
        return x

def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    li = list(map(str, data))
    try:
        return min(li, key=len)
    except:
        return None

def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:
    """
    list = [i for i in data if i.get('age', 0)]
    return min(list, key=lambda x: x.get('age'))

def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    return max([i for list in data for i in list])

def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    l=0
    for x in data:
        l+=x
    return l



def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text
    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532
    """
    sum = 0
    for x in text:
        sum +=ord(x)
    return sum


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    for x in range(2, 200):
        if all(x % i != 0 for i in range(2, x)):
            yield x

def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet
    """
    li = [random.choice(string.ascii_lowercase) for x in range(20)]
    return li