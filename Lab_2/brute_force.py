import itertools
import hashlib
import time
import threading

def brute_force(hash_value, num_threads):
    start_time = time.time()
    found = False

    # Составляем все возможные комбинации пяти строчных букв английского алфавита ASCII
    passwords = [''.join(p) for p in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=5)]
    # Разделяем список паролей на равные части для каждого потока
    chunk_size = len(passwords) // num_threads
    chunks = [passwords[i:i + chunk_size] for i in range(0, len(passwords), chunk_size)]

    # Функция, выполняемая в каждом потоке
    def check_passwords(passwords):
        nonlocal found
        # Пробуем каждый пароль в сформированном списке
        for password in passwords:
            # Вычисляем хеш от пароля
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            # Если хеш совпадает с заданным значением, выводим пароль и завершаем поиск
            if hashed_password == hash_value:
                found = True
                print("Хэш:",hash_value,"Пароль найден: ", password)
                # Выводим затраченное время на подбор пароля
                elapsed_time = time.time() - start_time
                print("Затраченное время: {:.2f} секунд".format(elapsed_time))
                break

    # Создаем и запускаем потоки
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=check_passwords, args=(chunks[i],))
        thread.start()
        threads.append(thread)

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

    if not found:
        print("Пароль не найден")

if __name__ == "__main__":
    hash_value = input("Введите хеш: ")
    while len(hash_value) == 0 or len(hash_value) > 255:
        country = input("Введите хеш, количество символов некорректно: ")
    while True:
        try:
            num_threads = int(input("Введите количество потоков (от 1 до 4): "))
            break
        except:
            print("Значение количества потоков должно быть от 1 до 4")

    brute_force(hash_value, num_threads)
