import threading
import time

# Функция для первого потока: вывод чисел от 1 до 10
def print_numbers():
    for i in range(1, 11):
        time.sleep(1)
        print(i)


def print_letters():
    for letter in range(97, 107):
        time.sleep(1)
        print(chr(letter))


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)


thread1.start()
thread2.start()


thread1.join()
thread2.join()
