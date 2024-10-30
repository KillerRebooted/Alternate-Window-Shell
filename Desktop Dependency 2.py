import os
import sys
import ctypes
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets
from PyQt5 import QtWinExtras
ctypes.windll.shell32.ExtractIconW.restype = ctypes.c_size_t

def displayIcon(path: str, index=0):
    hicon = ctypes.windll.shell32.ExtractIconW(0, path, index)
    qpixmap = QtWinExtras.QtWin.fromHICON(hicon)
    ctypes.windll.user32.DestroyIcon(ctypes.c_void_p(hicon))
    name = f'{os.path.basename(path)}.ico'
    qpixmap.save(name, 'ICO')
    qimg = qpixmap.toImage()
    width, height = qimg.width(), qimg.height()
    ptr = qimg.bits()  # qimg.constBits(), # bgra
    ptr.setsize(qimg.byteCount())
    img = np.array(ptr).reshape(height, width, 4)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    plt.imshow(img)
    plt.title(name)
    plt.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    print(sys.executable)
    #displayIcon(sys.executable)
    #displayIcon(r'C:\Windows\System32\shell32.dll', 3)
    displayIcon(r'C:\Windows\System32\imageres.dll', 11)

    for i in range(1000):
        displayIcon(r'C:\Windows\System32\shell32.dll', i)
        print(i)