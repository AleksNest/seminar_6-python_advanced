'''
Задача 2
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка
8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
 каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь. .
'''

'''
Задача 3
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''

from my_pacage.homework_queen import successful_position, is_queen_beat

if __name__ == '__main__':
    print(is_queen_beat([[1, 1], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7], [4, 8]]))  #функция определяет успешно или нет расставлены ферзи на доске 8*8
    successful_position(4)                                                                  # функция вывода n успешных расстановок ферзей на доске 8*8


'''
вывод  функции successful_position(4):
[[5, 2], [3, 5], [8, 3], [2, 7], [4, 8], [6, 4], [1, 1], [7, 6]]  iter = 31591340
[[2, 4], [7, 3], [1, 7], [8, 5], [4, 8], [6, 1], [5, 6], [3, 2]]  iter = 41559817
[[8, 3], [7, 6], [3, 7], [6, 8], [2, 2], [1, 4], [5, 1], [4, 5]]  iter = 44096729
[[8, 5], [1, 2], [7, 7], [2, 4], [3, 6], [5, 3], [6, 1], [4, 8]]  iter = 96825221
'''
