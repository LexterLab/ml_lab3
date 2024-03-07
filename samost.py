import matplotlib.pyplot as plt
import numpy as np


def samost1_1():
    randomSet = {3, 54, 22, 3131, 10}
    print(randomSet.__contains__(3))
    randomSet.add(44)
    print(randomSet)
    randomSet.discard(3)
    print(randomSet)
    randomSet.pop()
    print(randomSet)
    print(randomSet.__len__())
    another_set = {22, 34242, 54, 3, 10}
    print(randomSet.__and__(another_set))
    another_set = randomSet.copy()
    print(another_set)
    andAnotherSet = {323232, 3, 22, 10, 55}
    print(another_set.difference(andAnotherSet))
    print(another_set.intersection(andAnotherSet))


def samost1_2():
    randomDict = {'Japan': 'Japanese', 'UK': 'English'}
    print(randomDict.__getitem__('Japan'))
    randomDict.setdefault('Macedonia', 'Gibberish')
    print(randomDict.get('Macedonia'))
    randomDict.popitem()
    print(randomDict)


def samost4():
    x = np.arange(-2., 2., 0.01)
    plt.plot(x, x ** 2, 'bs')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y = x**2')
    plt.show()


def samost3():
    text = "I love chocolate very much"

    with open("new.txt", "w") as f:
        for word in text.split(" "):
            f.write(word + "\n")

def main():
    samost4()

main()
