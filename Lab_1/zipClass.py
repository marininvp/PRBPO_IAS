import os #удаление файла
import zipfile #zip
class task5():
    items = []
    def __init__(self,name):
        self.name=name
        self.typeFile=""
        task5.items.append(self)
    def nameFileIn(self,nameFile, typeFile):
        self.nameFile=nameFile
        self.typeFile = typeFile
    #5.1 Создать архив в формате zip:
    def create_zip_archive(self, data):
        with zipfile.ZipFile(data, 'w') as zipf:
            pass

    #5.2 Добавить файл, выбранный пользователем, в архив
    def add_file_to_zip(self, file_to_add):
        with zipfile.ZipFile(self.name, 'a') as zipf:
            zipf.write(file_to_add, os.path.basename(file_to_add))

    #5.3 Разархивировать файл и вывести данные о нем
    def extract_zip_file(self):
        with zipfile.ZipFile(self.name, 'r') as zipf:
            zipf.extractall()
            for file_info in zipf.infolist():
                print(f"Имя файла: {file_info.filename}")
                print(f"Размер файла: {file_info.file_size} bytes")

    #5.4 Удалить файл из архива
    def remove_file_from_zip(self):
        with zipfile.ZipFile(self.name, 'a') as zipf:
            # Создаем новый архив, исключая файл, который нужно удалить
            with zipfile.ZipFile('temp.zip', 'w') as temp_zip:
                for item in zipf.infolist():
                    if item.filename != self.nameFile:
                        # Копируем файлы, кроме того, который нужно удалить
                        data = zipf.read(item.filename)
                        temp_zip.writestr(item, data)

        # Заменяем оригинальный архив временным архивом без файла
        os.remove(self.name)
        os.rename('temp.zip', self.name)

        print(f"Файл '{self.nameFile}' удален из архива '{self.name}'.")

    # 5.5 Удалить сам архив

    def delete_file(self):
        if os.path.exists(self.name):
            os.remove(self.name)
            print(f"Файл {self.name} удален.")
        else:
            print(f"Файл {self.name} не найден.")