def concate_sub_lst(lst):
    """
    Понижает уровень хранения данных на 1 объединяя данные на одном уровне.
    Пример: [[1,2], [3,4]] => [1,2,3,4]
    """
    res = []
    for sub_lst in lst:
        for item in sub_lst:
            res.append(item)
    return res

def is_exist_index(lst, index):
    """
    Проверяет наличие индекса в списке
    """
    return index >= 0 and index < len(lst)