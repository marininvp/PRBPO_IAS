import os #удаление файла
import json #json

class task3():
    items = []
    def __init__(self,name):
        self.name=name
        task3.items.append(self)

    # 3.2 Создать новый объект. Выполнить сериализацию объекта в формате JSON и записать в файл.
    def create_and_write_json(self, data):
        with open(self.name, 'w') as json_file:
            json.dump(data, json_file)

    # 3.3 Прочитать файл в консоль
    def read_json(self):
        with open(self.name, 'r') as json_file:
            data = json.load(json_file)
            for attribute, value in data.items():
                print(f"{attribute}: {value}")

    # 3.4 Удалить файл
    def delete_file(self):
        if os.path.exists(self.name):
            os.remove(self.name)
            print(f"Файл {self.name} удален.")
        else:
            print(f"Файл {self.name} не найден.")