# encoding=gbk
import random
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

import SdkOcr
from ui.core import Ui_MainWindow


class my_ComboBox(Ui_MainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi(mainWindow)
        self.initUI()

    def initUI(self):

        self.pushButton_distinguishImage.clicked.connect(self.distinguishImage)
        self.pushButton_openImage.clicked.connect(self.openImage)

    def openImage(self):  # 选择本地图片上传
        global imgName  # 这里为了方便别的地方引用图片路径，我们把它设置为全局变量
        imgName, imgType = QFileDialog.getOpenFileName(self.centralwidget, "打开图片", "",
                                                       "*.jpg;;*.png;;All Files(*)")  # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        # 原始图片
        jpg = QtGui.QPixmap(imgName).scaled(self.label_image.width(),
                                            self.label_image.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长宽
        self.label_image.setPixmap(jpg)  # 在label控件上显示选择的图片

        print("" + imgName)

    def distinguishImage(self):

        self.label_txt.setText("")
        self.label_image1.setPixmap(QPixmap(""))
        self.label_image2.setPixmap(QPixmap(""))
        self.label_image3.setPixmap(QPixmap(""))
        self.label_image4.setPixmap(QPixmap(""))
        self.label_image5.setPixmap(QPixmap(""))

        list = SdkOcr.sdkocr(imgName)

        res = list[0]
        name = res.get("name")
        score = str(float(res.get("score")) * 100)
        baike = res.get("baike_info")

        if not bool(baike):
            description = "未收录该昆虫详细信息"
        else:
            description = baike.get("description")
        print("识别结果：" + name)
        print("准确度：" + score + '%')
        print("昆虫信息：" + description)
        if name == "非动物":
            self.label_txt.setText("<h1>当前图片中没有昆虫</h1>")
        else:
            path_circle = "picture\\p-circle.png"
            path_extend = "picture\\p-extend.png"
            path_leaf = "picture\\p-leaf.png"
            path_rect = "picture\\p-pherical.png"
            path_pherical = "picture\\p-rect.png"
            # 1
            jpg1 = QtGui.QPixmap(path_circle).scaled(self.label_image1.width(),
                                                     self.label_image1.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长宽
            self.label_image1.setPixmap(jpg1)  # 在label控件上显示选择的图片
            # 2
            jpg2 = QtGui.QPixmap(path_extend).scaled(self.label_image2.width(),
                                                     self.label_image2.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长宽
            self.label_image2.setPixmap(jpg2)  # 在label控件上显示选择的图片
            # 3
            jpg3 = QtGui.QPixmap(path_leaf).scaled(self.label_image3.width(),
                                                   self.label_image3.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长宽
            self.label_image3.setPixmap(jpg3)  # 在label控件上显示选择的图片
            # 4
            jpg4 = QtGui.QPixmap(path_rect).scaled(self.label_image4.width(),
                                                   self.label_image4.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长宽
            self.label_image4.setPixmap(jpg4)  # 在label控件上显示选择的图片
            # 5
            jpg5 = QtGui.QPixmap(path_pherical).scaled(self.label_image5.width(),
                                                       self.label_image5.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长宽
            self.label_image5.setPixmap(jpg5)  # 在label控件上显示选择的图片
            # self.label_txt.setWordWrap(True)

            self.label_txt.setText(
                "<h1>识别结果：" + name + '</h1>' + "<h2>准确度：" + score + '%' + '</h2>' + "<h4>昆虫信息：" + description + "</h4>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    form = my_ComboBox(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
