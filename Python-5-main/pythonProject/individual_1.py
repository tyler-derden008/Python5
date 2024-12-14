#!/usr/bin/env python6
# -*- coding: utf-8 -*-

import sys


def is_sorted_ascending(tup):
    for i in range(len(tup) - 1):
        if tup[i] > tup[i + 1]:
            return False, i + 1  # Возвращаем False и индекс следующего элемента
    return True, None  # Если не найдено нарушений, возвращаем True

# Провел рассчет кортежа
tup = (1, 2, 3, 4, 5, 3, 7)

is_sorted, index = is_sorted_ascending(tup)

if is_sorted:
    print("Кортеж упорядочен по возрастанию.")
else:
    print(f"Кортеж не упорядочен по возрастанию. Нарушение на индексе: {index}")
