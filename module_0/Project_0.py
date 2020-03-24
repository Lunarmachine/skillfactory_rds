import numpy as np
import math
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"¬аш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
def game_core(number):
    count = 0
    Top_bound = 100
    Bottom_bound = 1
    Predict = 50
    for count in range(1,100):
        if number == Predict: break    # выход из цикла, если угадали
        elif number > Predict: 
            Bottom_bound = Predict
            Predict = Bottom_bound + math.ceil((Top_bound - Bottom_bound) / 2)
        elif number < Predict: 
            Top_bound = Predict
            Predict = Bottom_bound + math.floor((Top_bound - Bottom_bound) / 2) 
    return(count)
score_game(game_core)