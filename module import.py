
import os #импорт модуля целиком

from os import mkdir #импортирование отдельных функций

from os import rmdir as remover

from os import * #импортируем модуль целиком

#remover('test')
mkdir('test')
remover('test')

print(getcwd())

print(list(walk(getcwd())))



