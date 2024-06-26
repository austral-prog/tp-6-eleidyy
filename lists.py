# Replace the "ANSWER HERE" with your answer

def remove_elements(lst):
    indices_to_remove = [0, 4, 5]
    result = [item for i, item in enumerate(lst) if i not in indices_to_remove]
    return result

# Ejemplo de uso:
sample_input = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
output = remove_elements(sample_input)
print(output)  # Output: ['Green', 'White', 'Black']


def add_elements(lst):
    lst.insert(0, 'Pink')  # Agrega 'Pink' al principio de la lista
    lst.append('Yellow')   # Agrega 'Yellow' al final de la lista
    return lst

# Ejemplo de uso:
sample_input = ['Red', 'Green', 'White', 'Black']
output = add_elements(sample_input)
print(output)  # Output: ['Pink', 'Red', 'Green', 'White', 'Black', 'Yellow']

    
def is_empty(lst):
    return len(lst) == 0

# Ejemplo de uso:
sample_list1 = []
sample_list2 = ['Red', 'Green', 'Blue']

print(is_empty(sample_list1))  # Output: True
print(is_empty(sample_list2))  # Output: False

def check_lists(lst1, lst2):
    if len(lst1) >= 3 and len(lst2) >= 3:
        return lst1[2] == lst2[2]
    else:
        return False

# Ejemplo de uso:
sample_list1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
sample_list2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
output1 = check_lists(sample_list1, sample_list2)
print(output1)  # Output: True

sample_list3 = ['Black', 'Pink', 'Green', 'White']
sample_list4 = ['Red', 'Green', 'Yellow', 'Black', 'Pink']
output2 = check_lists(sample_list3, sample_list4)
print(output2)  # Output: False

def list_of_lists(original_list):
    
    return [
        original_list[0][:2],  # First sublist, take first 2 elements
        original_list[1][1:4],  # Second sublist, take elements from index 1 to 3
        original_list[2][-2:]  # Third sublist, take last 2 elements
    ]

sample_list = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
print(list_of_lists(sample_list))  # Output: [[1, 2], [5, 6, 7], [11, 12]]
