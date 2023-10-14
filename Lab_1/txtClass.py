import os #удаление файла

class task2():
    items = []
    def __init__(self,name):
        self.name=name
        task2.items.append(self)

    # 2.1 Создать файл
    def create_file(self,file_name):
        with open(file_name, 'w') as file:
            pass

    # 2.2 Записать в файл строку, введённую пользователем
    def write_to_file(self,text):
        with open(self.name, 'w') as file:
            file.write(text)

    # 2.3 Прочитать файл в консоль
    def read_file(self):
        with open(self.name, 'r') as file:
            content = file.read()
            print(content)

    # 2.4 Удалить файл
    def delete_file(self):
        if os.path.exists(self.name):
            os.remove(self.name)
            print(f"Файл {self.name} удален.")
        else:
            print(f"Файл {self.name} не найден.")