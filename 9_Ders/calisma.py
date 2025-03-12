# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     return fib(n-1) + fib(n-2)
#
# my_result = fib(38)
# print(my_result)
import time

my_dict={0:1, 1:1}
def fib(n):
    global my_dict
    if n in my_dict:
        return my_dict[n]

    my_dict[n] = fib(n-1) + fib(n-2)
    return my_dict[n]
t1=time.time()
print(fib(49))
t2=time.time()
print(f"fibo ilk çalışmada {t2-t1}")
print(fib(50))
t3=time.time()
print(f"fibo ilk çalışmada {t3-t2}")


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib_list = [0, 1]  # İlk iki Fibonacci sayısını listeye ekledik
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])  # Yeni Fibonacci sayısını ekliyoruz

    return fib_list[n]  # n'inci Fibonacci sayısını döndürüyoruz

t1=time.time()
print(fib(49))
t2=time.time()
print(f"fibo ilk çalışmada {t2-t1}")
print(fib(50))
t3=time.time()
print(f"fibo ilk çalışmada {t3-t2}")