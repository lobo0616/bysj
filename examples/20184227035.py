def sort(data_list):
    length = len(data_list)

    for i in range(0, length):
        min = i        
        for j in range(i+1, length):
            if data_list[j] < data_list[min]:
                min = j        
        data_list[min], data_list[i] = data_list[i], data_list[min]
    return data_list


def two_sum(str1, str2):
    return int(str1) + int(str2)
