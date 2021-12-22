
# Сортировка вставками
def sorted_list(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


# Бинарный поиск искомого элемента
def binary_search(arr_in, element, left, right):
    if left > right:
        return None
    middle = (right + left) // 2
    if arr_in[middle] == element:
        return middle
    elif element < arr_in[middle]:
        return binary_search(arr_in, element, left, middle - 1)
    else:
        return binary_search(arr_in, element, middle + 1, right)


# Преобразование типа введённого числа из строки в число с плавающей точкой
def float_verify(str_input):
    try:
        str_to_float = float(str_input)
        return str_to_float
    except ValueError:
        print(f'Значение {str_input} невозможно преобразовать в число')
        exit()


input_nums_set = input("Введите последовательность чисел через пробел: ")

input_nums_list = list(map(float_verify, input_nums_set.split()))

if len(input_nums_list) < 2:
    print("Введено недостаточное количество чисел")
    exit()
else:
    print(f'Сортировка списка по возрастанию в нём элементов: {sorted_list(input_nums_list)}')

input_num = float_verify(input("Введите любое число, которое бы входило в данный список: "))

# Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.
if input_nums_list[0] >= input_num or input_nums_list[-1] < input_num:
    print("Введённое число не входит в данный список")
else:
    for i in range(int(input_num), int(input_nums_list[0] - 1), -1):
        idx = binary_search(input_nums_list, i, 0, len(input_nums_list))
        if idx is not None:
            print(f'Искомое число занимает позицию номер [{idx}] в списке')
            break
