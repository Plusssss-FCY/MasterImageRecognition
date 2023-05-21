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

    def openImage(self):  # ѡ�񱾵�ͼƬ�ϴ�
        global imgName  # ����Ϊ�˷����ĵط�����ͼƬ·�������ǰ�������Ϊȫ�ֱ���
        imgName, imgType = QFileDialog.getOpenFileName(self.centralwidget, "��ͼƬ", "",
                                                       "*.jpg;;*.png;;All Files(*)")  # ����һ���ļ�ѡ��򣬵�һ������ֵimgName��¼ѡ�е��ļ�·��+�ļ������ڶ�������ֵimgType��¼�ļ�������
        # ԭʼͼƬ
        jpg = QtGui.QPixmap(imgName).scaled(self.label_image.width(),
                                            self.label_image.height())  # ͨ���ļ�·����ȡͼƬ�ļ���������ͼƬ����Ϊlabel�ؼ��ĳ���
        self.label_image.setPixmap(jpg)  # ��label�ؼ�����ʾѡ���ͼƬ

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
            description = "δ��¼��������ϸ��Ϣ"
        else:
            description = baike.get("description")
        print("ʶ������" + name)
        print("׼ȷ�ȣ�" + score + '%')
        print("������Ϣ��" + description)
        if name == "�Ƕ���":
            self.label_txt.setText("<h1>��ǰͼƬ��û������</h1>")
        else:
            path_circle = "picture\\p-circle.png"
            path_extend = "picture\\p-extend.png"
            path_leaf = "picture\\p-leaf.png"
            path_rect = "picture\\p-pherical.png"
            path_pherical = "picture\\p-rect.png"
            # 1
            jpg1 = QtGui.QPixmap(path_circle).scaled(self.label_image1.width(),
                                                     self.label_image1.height())  # ͨ���ļ�·����ȡͼƬ�ļ���������ͼƬ����Ϊlabel�ؼ��ĳ���
            self.label_image1.setPixmap(jpg1)  # ��label�ؼ�����ʾѡ���ͼƬ
            # 2
            jpg2 = QtGui.QPixmap(path_extend).scaled(self.label_image2.width(),
                                                     self.label_image2.height())  # ͨ���ļ�·����ȡͼƬ�ļ���������ͼƬ����Ϊlabel�ؼ��ĳ���
            self.label_image2.setPixmap(jpg2)  # ��label�ؼ�����ʾѡ���ͼƬ
            # 3
            jpg3 = QtGui.QPixmap(path_leaf).scaled(self.label_image3.width(),
                                                   self.label_image3.height())  # ͨ���ļ�·����ȡͼƬ�ļ���������ͼƬ����Ϊlabel�ؼ��ĳ���
            self.label_image3.setPixmap(jpg3)  # ��label�ؼ�����ʾѡ���ͼƬ
            # 4
            jpg4 = QtGui.QPixmap(path_rect).scaled(self.label_image4.width(),
                                                   self.label_image4.height())  # ͨ���ļ�·����ȡͼƬ�ļ���������ͼƬ����Ϊlabel�ؼ��ĳ���
            self.label_image4.setPixmap(jpg4)  # ��label�ؼ�����ʾѡ���ͼƬ
            # 5
            jpg5 = QtGui.QPixmap(path_pherical).scaled(self.label_image5.width(),
                                                       self.label_image5.height())  # ͨ���ļ�·����ȡͼƬ�ļ���������ͼƬ����Ϊlabel�ؼ��ĳ���
            self.label_image5.setPixmap(jpg5)  # ��label�ؼ�����ʾѡ���ͼƬ
            # self.label_txt.setWordWrap(True)

            self.label_txt.setText(
                "<h1>ʶ������" + name + '</h1>' + "<h2>׼ȷ�ȣ�" + score + '%' + '</h2>' + "<h4>������Ϣ��" + description + "</h4>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    form = my_ComboBox(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
