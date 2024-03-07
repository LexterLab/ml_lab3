# This is a sample Python script.
from __future__ import print_function

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = 111


def function(answer, count=5, text='Text'):
    while 1:
        yesno = input(answer)
        if yesno in ('Да', 'да'): return 1
        if yesno in ('Не', 'не'): return 0
        count = count - 1
        if count < 0: raise IOError('Довиждане')
        print(text)


def function2(parameter=x):
    print(parameter)


def function3(x, y=[]):
    y.append(x)
    return y


def function4(x, y=None):
    if y is None:
        y = []
    y.append(x)
    return y


def sendMessage(sender, recipient='World', greeting='Hello', question='How have you been?', sendoff='Best wishes'):
    print(greeting, recipient, question, sendoff, sender)


def fun(a):
    print("Hello world")


def showRanking(*arguments, **keywords):
    print(arguments)
    print(keywords)


def main():
    x = {3, 1, 2, 5, 5}
    print(x)  # primer 1

    A = {1, 2, 3}
    B = {2, 1, 4}
    print(A | B)  # primer2
    print(A & B)  # primer 3
    print(A - B)  # PRIMER 4
    print(A ^ B)  # PRIMER 5

    C = {1, 2}
    print(A > C)  # PRIMER 6

    lang = {'USA': 'English', 'Bulgaria': 'Bulgarian'}
    print(lang)  # primer 7
    print('USA' in lang)  # primer 8
    print('English' in lang)  # primer 9
    print(lang.keys())  # primer 10
    print(lang.values())  # primer 11
    print(lang.items())  # primer 12

    lang['Russia'] = 'Russian'
    print(lang)  # primer 13

    del lang['Russia']
    print(lang)  # primer 14
    print(sorted(lang))  # primer 15
    print(dict(USA='English', Bulgaria='Bulgarian'))  # primer 16
    print(dict([('USA', 'English'), ('Bulgaria', 'Bulgarian')]))  # primer 17

    x = [1, 2, 3]
    print(type(x))  # primer 18

    y = 1
    print(type(y))  # primer 19

    print(list({1, 2, 3}))  # primer 20
    print(list((1, 2, 3)))  # primer 21
    print(tuple([1, 2, 3]))  # primer 22
    print(tuple({1, 2, 3}))  # primer 23
    print(set((1, 2, 3)))  # primer 24
    print(set([1, 2, 3]))  # primer 25

    # print(function("Да"))  # primer 26
    function2()  # primer 27
    print(function3(1))
    print(function3(2))
    print(function3(3))  # primer 28
    print(function4(1))
    print(function4(2))  # primer 29 i samost 2
    print(function4(3))

    sendMessage("Skynet")  # primer 30
    sendMessage(greeting='Dear Mr/Ms', sender='Random Internet Person')  # primer 31
    sendMessage('Me', sendoff='Regards')  # primer 32
    sendMessage('Your mom', 'Ron', 'What did you do with the car?')  # primer 33
    # sendMessage()
    # sendMessage('Me', sender=' you')
    # sendMessage(city='Sofia')    primer 34 errors

    # fun(0, a = 0) primer 35 error
    showRanking('Skiing', 'Bobsled', 'Triathlon', first='Bulgaria', second='Romania', third='Macedonia')  # primer 36
    showRanking(22, 'Bobsled', 30.50, Johnny='Bravo', Dexter='Laboratory', Popeye='Sailor')

    file = open("testfile.txt", "r")
    print(file.read())  # primer 37

    file = open("testfile.txt", "r")
    print(file.readline())  # primer 38

    file = open("testfile.txt", "r")
    print(file.readlines())  # primer 39

    file = open("testfile.txt", "r")
    for line in file:
        print(line)  # primer 40

    file = open("testfile.txt", "w")
    file.write("Some text 1")
    file.write("Some text 2")
    file.write("\nSome text 3")
    file.close()  # primer 41

    with open("testfile.txt") as f:
        for line in f:
            print(line)  # primer 42

    with open("123.txt", "w") as f:  # primer 43
        f.write("hello\n")
        f.write("1234567\n")
        f.write("abcdefgh\n")

    with open("123.txt") as f:  # primer 44
        data = f.readlines()
        print(data)

    with open("123.txt", "r") as f:  # primer 45
        data = f.readlines()
    for line in data:
        words = line.split()
        print(words)

    str = 'I love banana, orange and kiwi smoothie'
    print(str.split(','))  # primer 46

    plt.plot([1, 2, 1, 2, 3, 2, 4])
    plt.ylabel('some numbers')
    plt.show()  # primer 47

    plt.plot([1, 2, 3, 4], [1, 4, 1, 16])
    plt.show()  # primer 48

    plt.plot([1, 2, 3, 4], [1, 4, 1, 16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()  # primer 49

    t = np.arange(0., 5., 0.2)
    print(t)  # primer 50

    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
    plt.show()  # primer 51

    plt.figure(1)
    plt.subplot(211)
    plt.plot([3, 1, 7])
    plt.figure(2)
    plt.plot([4, 2, 8])

    plt.figure(1)
    plt.subplot(211)
    plt.title('Easy as 1, 2, 3')
    plt.show()  # primer 52

    x = np.random.randn(10000)
    plt.hist(x)
    plt.title("Gaussian Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()  # primer 53

    ax = plt.subplot(111)
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    line = plt.plot(t, s)
    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black'))
    plt.ylim(-2, 2)
    plt.show()  # primer 54

    city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
    population = pd.Series([852469, 1015785, 485199])
    print(pd.DataFrame({'City name': city_names, 'Population': population}))  # primer 55

    california_housing_datafrane = pd.read_csv("https://download.mlcc.google.com/mledu-datasets"
                                               "/california_housing_train.csv", sep=",")
    print(california_housing_datafrane.describe())  # primer 56
    print(california_housing_datafrane.head())  # primer 57
    print(california_housing_datafrane.hist("housing_median_age"))  # primer 58

    cities = pd.DataFrame({'City name': city_names, 'Population': population})
    print(type(cities['City name']))
    print(cities['City name'])  # primer 59
    print((type(cities['City name'][1])))
    print(cities['City name'][1])  # primer 60
    print(type(cities[0:2]))
    print(cities[0:2])  # primer 61
    print(population / 1000)
    print(pd.DataFrame({'City name': city_names, 'Population': population / 1000}))  # primer 62
    print(np.log(population))  # primer 63
    print(population.apply(lambda val: val > 1000))     # primer 64
    cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
    cities['Population density'] = cities['Population'] / cities['Area square miles']
    print(cities)   # primer 65
    print(cities.reindex([2, 0, 1]))    # primer 66
    print(cities.reindex(np.random.permutation(cities.index)))  # primer 67


main()
