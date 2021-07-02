import matplotlib.pyplot as plt
import numpy as np


def run():
    x = np.linspace(0, np.pi*2*2.0, int(np.pi*3*10))
    plt.plot(x, np.sin(x),'o-')
    plt.plot(x, np.cos(x),'o-')
    plt.legend(['sin(x)','cos(x)'])
    plt.ylabel('y')
    plt.xlabel('x')
    plt.title("Test plot.")
    plt.show()


if __name__=="__main__":
    run()