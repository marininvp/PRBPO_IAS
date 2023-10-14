import psutil #о дисках

#1.Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы.
def print_info():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Имя диска: {partition.device}")
        print(f"Метка тома: {partition.mountpoint}")
        disk_usage = psutil.disk_usage(partition.mountpoint)
        print(f"Размер диска: {disk_usage.total / (1024 ** 3):.2f} GB")
        print(f"Тип файловой системы: {partition.fstype}\n")