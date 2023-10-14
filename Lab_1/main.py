from systemInfo import *
from serializeClass import *
from verifyData import *
from txtClass import *
from jsonClass import *
from xmlClass import *
from zipClass import *

if __name__ == "__main__":
    print("1.Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы.")
    print("2.1 Создать файл")
    print("2.2 Записать в файл строку, введённую пользователем")
    print("2.3 Прочитать файл в консоль")
    print("2.4 Удалить файл")
    print("3.2 Создать новый объект. Выполнить сериализацию объекта в формате JSON и записать в файл.")
    print("3.3 Прочитать файл в консоль")
    print("3.4 Удалить файл")
    print("4.2 Создать и записать в файл новые данные из консоли xml.")
    print("4.3 Прочитать файл в консоль.")
    print("4.4 Удалить файл.")
    print("5.1 Создать архив в формате zip")
    print("5.2 Добавить файл, выбранный пользователем, в архив")
    print("5.3 Разархивировать файл и вывести данные о нем")
    print("5.4 Удалить файл из архива")
    print("5.5 Удалить сам архив")
    data=input("Введите номер команды из представленного списка или 0, если хотите завершить выполнение программы: ")
    while data not in ("0","1","2.1","2.2","2.3","2.4","3.2", "3.3", "3.4","4.2","4.3","4.4","5.1","5.2","5.3","5.4", "5.5"):
        data = input("Введён некорректный номер задачи, попробуйте снова: ")
    while data!="0":
        if(data=="1"):
            # 1.Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы.
            print_info()
        elif(data=="2.1"):
            # 2.1 Создать файл
            name=input("Введите название файла: ")
            while len(name)==0 or len(name)>255:
                name = input("Введите название файла заново, количество символов некорректно: ")
            newObj=task2(name+".txt")
            newObj.create_file(name+".txt")
        elif (data == "2.2"):
            # 2.2 Записать в файл строку, введённую пользователем
            if len(task2.items)!=0:
                user_input = input("Введите текст для записи в файл: ")
                while len(user_input)==0 or len(user_input)>255:
                    user_input = input("Введите текст для записи в файл заново, количество символов некорректно: ")
                newObj.write_to_file(user_input)
            else:
                print("Вы не создали файл, для этого вам нужно обратиться к команде 2.1")
        elif(data=="2.3"):
            # 2.3 Прочитать файл в консоль
            if len(task2.items)!=0:
                newObj.read_file()
            else:
                print("Вы не создали файл, для этого вам нужно обратиться к команде 2.1")
        elif (data == "2.4"):
            # 2.4 Удалить файл
            if len(task2.items)!=0:
                newObj.delete_file()
            else:
                print("Вы не создали файл, для этого вам нужно обратиться к команде 2.1")
        elif (data == "3.2"):
            # 3.2 Создать новый объект. Выполнить сериализацию объекта в формате JSON и записать в файл        .
            newToSerialize = toSerialize(data_verify())
            nameJSON = input("Введите название файла JSON: ")
            while len(nameJSON) == 0 or len(nameJSON) > 255:
                nameJSON = input("Введите название файла заново, количество символов некорректно: ")
            newObj3 = task3(nameJSON+".json")
            newObj3.create_and_write_json(newToSerialize.__dict__)
        elif (data == "3.3"):
            # 3.3 Прочитать файл в консоль
            if len(task3.items)!=0:
                newObj3.read_json()
            else:
                print("Вы не создали файл, для этого вам нужно обратиться к команде 3.2")
        elif (data == "3.4"):
            # 3.4 Удалить файл
            if len(task3.items)!=0:
                newObj3.delete_file()
            else:
                print("Вы не создали файл, для этого вам нужно обратиться к команде 3.2")
        elif (data == "4.2"):
            # 4.2 Записать в файл новые данные из консоли xml.
            newToSerialize2 = toSerialize(data_verify())
            nameXML = input("Введите название файла XML: ")
            while len(nameXML) == 0 or len(nameXML) > 255:
                nameXML = input("Введите название файла заново, количество символов некорректно: ")
            newObj4 = task4(nameXML+".xml")
            newObj4.create_and_write_xml(newToSerialize2.__dict__)
        elif (data == "4.3"):
            # 4.3 Прочитать файл в консоль.
            if len(task4.items)!=0:
                newObj4.read_xml()
            else:
                print("Вы не создали файл, для этого вам нужно обратиться к команде 4.2")
        elif (data == "4.4"):
            # 4.4 Удалить файл.
            if len(task4.items)!=0:
                newObj4.delete_file()
            else:
                print("Вы не создали файл, для этого вам нужно обратиться к команде 4.2")
        elif (data == "5.1"):
            # 5.1 Создать архив в формате zip:
            nameZIP = input("Введите название файла ZIP: ")
            while len(nameZIP) == 0 or len(nameZIP) > 255:
                nameZIP = input("Введите название файла заново, количество символов некорректно: ")
            newObj5 = task5(nameZIP+".zip")
            newObj5.create_zip_archive(nameZIP+".zip")
        elif (data == "5.2"):
            # 5.2 Добавить файл, выбранный пользователем, в архив
            if len(task5.items)!=0:
                number=0
                while True:
                    try:
                        number = int(input("Если вы хотите добавить в архив txt-файл, то нажмите 1. Если json, нажмите 2. Если xml, нажмите 3: "))
                        break
                    except:
                        print("Введено некорректное значение, нажмите 1, 2, 3: ")
                while number not in (1,2,3):
                    number = int(input("Введите 1, 2 или 3: "))
                if number==1:
                    if len(task2.items)!=0:
                        newObj5.add_file_to_zip(newObj.name)
                        newObj5.nameFileIn(newObj.name,"txt")
                    else:
                        print("Вы не создали TXT файл, для этого вам нужно обратиться к команде 2.1")
                elif number==2:
                    if len(task3.items)!=0:
                        newObj5.add_file_to_zip(newObj3.name)
                        newObj5.nameFileIn(newObj3.name,"json")
                    else:
                        print("Вы не создали JSON файл, для этого вам нужно обратиться к команде 3.2")
                else:
                    if len(task4.items)!=0:
                        newObj5.add_file_to_zip(newObj4.name)
                        newObj5.nameFileIn(newObj4.name,"xml")
                    else:
                        print("Вы не создали XML файл, для этого вам нужно обратиться к команде 4.2")
            else:
                print("Вы не создали архив, для этого вам нужно обратиться к команде 5.1")
        elif (data == "5.3"):
            # 5.3 Разархивировать файл и вывести данные о нем
            if len(task5.items)!=0:
                if newObj5.typeFile=="":
                    print("Вы не внесли файл в архив, для этого вам нужно обратиться к команде 5.2")
                else:
                    newObj5.extract_zip_file()
            else:
                print("Вы не создали архив, для этого вам нужно обратиться к команде 5.1")
        elif (data == "5.4"):
            # 5.4 Удалить файл из архива
            if len(task5.items)!=0:
                if newObj5.typeFile == "":
                    print("Вы не внесли файл в архив, для этого вам нужно обратиться к команде 5.2")
                else:
                    newObj5.remove_file_from_zip()
            else:
                print("Вы не создали архив, для этого вам нужно обратиться к команде 5.1")
        else:
            # 5.5 Удалить сам архив
            if len(task5.items)!=0:
                newObj5.delete_file()
            else:
                print("Вы не создали архив, для этого вам нужно обратиться к команде 5.1")
        data = input("Введите номер команды из представленного списка или 0, если хотите завершить выполнение программы: ")
        while data not in ("0", "1", "2.1", "2.2", "2.3", "2.4", "3.2", "3.3", "3.4", "4.2", "4.3", "4.4", "5.1", "5.2", "5.3", "5.4","5.5"):
            data = input("Введён некорректный номер задачи, попробуйте снова: ")
    print("Выполнение программы завершено")