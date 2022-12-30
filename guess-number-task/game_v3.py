"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = np.random.randint(1, 101)) -> int:
    """Компьютер или пользователь загадывает число

    Args:
        number (int, optional): Загаданное число. По умаолчанию рандом от 0 до 100

    Returns:
        int: Число попыток
    """
    count = 0
    
    # заготовим переменные для ограничения "отгадывателя"
    mx = 101 
    mn = 1

    while True:
        count += 1
        predict_number = np.random.randint(mn, mx)  # предполагаемое число
        if number < predict_number: # если предполагаемое число больше загаданного, то оно становится новым ограничением сверху
            mx = predict_number 
        elif number > predict_number: # если предполагаемое число меньше загаданного, то оно становится новым ограничением снизу
            mn = predict_number
        else:          
            break  # выход из цикла если угадали
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score