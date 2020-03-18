#!/usr/bin/env python
# coding: utf-8

# In[69]:



def game_core_v1(number):
    count = 0
    a=1
    b=100
    while a < b:
        count+=1
        mean=(a+b)//2
        if mean == number: 
            break
        if number < mean:
            b=mean
        else:
            a=mean
    return(count)
    
def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v1)


# In[ ]:




