# -*- coding: utf-8 -*-
import json
import requests

def isTaskUnique(srcData, checkObj):
    # В исходном списке в случае уникальности должен быть обнаружен только 1 элемент
    # Если элементов больше - он уже не уникален
    counter = 0
    for element in srcData:
        if element[ "title" ] == checkObj["title"]:
            counter += 1
        if counter > 1:
            return False
    return True

def main():
    # считываем ответ с сайта
    response = requests.get( "https://jsonplaceholder.typicode.com/todos" )
    data = json.loads( response.text )

    # сохраняем в файл
    with open( "response.txt", "w" ) as f:
        json.dump( data, f, indent=4 )

    # Сформируем структуру, в которой в каждом элементе будет храниться информация о количестве
    # уникальных задач и количестве завершенных уникальных задач
    users = {}

    for record in data:
        # Если такого пользователя нет, создать новую запись для него
        if record[ "userId" ] not in users.keys():
            users[ record[ "userId" ] ] = {}
            users[ record[ "userId" ] ][ "complete_tasks" ] = 0
            users[ record[ "userId" ] ][ "unique_tasks"   ] = 0

        # Проверяем на уникальность задачи
        if isTaskUnique( data, record ):
            users[ record[ "userId" ] ][ "unique_tasks" ] += 1
            # Проверяем равезрешнность задачи
            if record[ "completed" ] == True:
                users[ record[ "userId" ] ][ "complete_tasks" ] += 1

    for user in users:
        print( "\n" )
        print( "Текущий пользователь: ", user )
        print( "Оригинальных задач:   ", users[ user ][ "unique_tasks" ] )
        print( "Выполнено задач:      ", users[ user ][ "complete_tasks" ] )

    print( "\nКоличество уникальных пользователей: ", len( users.keys() ) )

if __name__ == "__main__":
    main()
