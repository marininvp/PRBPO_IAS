import os #удаление файла
import xml.etree.ElementTree as ET #xml
class task4():
    items = []
    def __init__(self,name):
        self.name=name
        task4.items.append(self)

    #4.2 Записать в файл новые данные из консоли xml.
    def create_and_write_xml(self, data):
        # Создаем корневой элемент
        root = ET.Element("root")
        for key, value in data.items():
            element = ET.Element(key)
            element.text = str(value)
            root.append(element)
        # Создаем объект ElementTree для записи в файл
        tree = ET.ElementTree(root)
        tree.write(self.name)

    #4.3 Прочитать файл в консоль.
    def read_xml(self):
        tree = ET.parse(self.name)
        root = tree.getroot()
        for element in root.iter():
            print(f"{element.tag}: {element.text}")

    # 4.4 Удалить файл.

    def delete_file(self):
        if os.path.exists(self.name):
            os.remove(self.name)
            print(f"Файл {self.name} удален.")
        else:
            print(f"Файл {self.name} не найден.")