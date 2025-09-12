def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        value = 0
        try:
            if (isinstance(my_list_1[i], (int, float)) and
                    isinstance(my_list_2[i], (int, float))):
                value = my_list_1[i] / my_list_2[i]
            else:
                print("wrong type")
                value = 0
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except IndexError:
            print("out of range")
            value = 0
        finally:
            result.append(value)
    return result
