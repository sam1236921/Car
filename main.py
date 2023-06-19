# -*- coding: utf-8 -*-
#謝昇宏
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_main import Ui_Form
from error import Ui_Dialog
import cv2
import sys
import os
from shutil import copy
import numpy as np
from PIL import ImageGrab


class error(QDialog):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Dialog()
        # 初始化界面
        self.ui.setupUi(self)      

class DraggableLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.draggable = True

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.draggable:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.draggable:
            self.move(self.mapToParent(event.pos() - self.offset))

# 自定义代理模型
class FileIconDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_icon = QIcon("icon.png")
        self.icon_provider = QFileIconProvider()
    
    def paint(self, painter, option, index):
        if index.column() == 0:
            # 获取文件信息
            model = index.model()
            file_info = model.fileInfo(index)
            file_path = file_info.filePath()
            is_folder = file_info.isDir()
            file_name = file_info.fileName()

            # 绘制图标和文件名
            painter.save()
            rect = option.rect
            icon_size = rect.height() - 4  # 调整图标大小
            icon_rect = QRect(rect.left() + 2, rect.top() + 2, icon_size, icon_size)

            if is_folder:
                folder_icon = self.icon_provider.icon(QFileIconProvider.Folder)
                folder_icon.paint(painter, icon_rect, Qt.AlignmentFlag.AlignCenter, QIcon.Mode.Normal, QIcon.State.Off)
            else:
                self.file_icon.paint(painter, icon_rect, Qt.AlignmentFlag.AlignCenter, QIcon.Mode.Normal, QIcon.State.Off)
            
            text_rect = QRect(icon_rect.right() + 4, rect.top(), rect.width() - icon_rect.width() - 4, rect.height())
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, file_name)

            painter.restore()
        else:
            # 默认绘制其他列
            super().paint(painter, option, index)

            

class Stats(QLabel):
    global imgpath
    imgpath=0
    
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)   
        
        self.setup_control()
        self.path()

        self.flag=False
        self.isShow=False
        self.point_type=0 #0-左键前景点,1-右键背景点
        self.clk_pos=None
        self.x=None
        self.y=None

    def setup_control(self):
        self.ui.tabWidget.lower()
        self.ui.horizontalSliderD.setRange(0,255)
        self.ui.horizontalSliderL.setRange(0,255)
        self.ui.horizontalSliderD.setTickPosition(2)
        self.ui.horizontalSliderL.setTickPosition(2)          # 下加入刻度線
        self.ui.horizontalSliderD.setTickInterval(10)
        self.ui.horizontalSliderL.setTickInterval(10)
        self.ui.checkBox.toggled.connect(self.check)
        self.ui.horizontalSliderD.valueChanged.connect(self.getslidervalueD)
        self.ui.horizontalSliderL.valueChanged.connect(self.getslidervalueL)
        self.ui.toolButton_1.clicked.connect(self.open_folder1)
        self.ui.toolButton_2.clicked.connect(self.open_folder2)
        self.ui.toolButton_3.clicked.connect(self.open_folder3)
        self.ui.pushButton_7.clicked.connect(self.save_of)
        self.ui.pushButton_4.clicked.connect(self.rst)
        self.ui.pushButton_8.clicked.connect(self.showNewWindow)
        self.ui.pushButton.clicked.connect(self.saveimg)

        self.closeEvent(self.close)
        if imgpath !=0:
            self.ui.img2.mouseDoubleClickEvent = self.get_clicked_position
            self.ui.checkBox.setEnabled(True)

        else:
            self.ui.checkBox.setEnabled(False)

        global width,height
        width=250
        height=200

        label_geometry = self.ui.img2.geometry()
        self.ui.img2.setAlignment(Qt.AlignCenter)

        # 创建可拖拽的 label
        self.img1 = DraggableLabel(self.ui.img2)
        self.img1.setGeometry(label_geometry.x(), label_geometry.y(), width, height)
        self.img1.setAlignment(Qt.AlignCenter)
        # 将原有 QLabel 的位置和大小设置为不可见，用 DraggableLabel 替代显示
        # self.setGeometry(0, 0, 0, 0)


        
    def open_next_file(self,):
        folder_path = r'C:\Users\Home\car\image'  # 更改为实际的文件夹路径

        file_list = os.listdir(folder_path)
        if b in file_list:
            folder_index = file_list.index(b)
            print("Folder Index:", folder_index)
        else:
            print("File not found in the folder.")
                        
    def open_previous_file(self):
        if hasattr(self, 'selected_index'):
            model = self.selected_index.model()
            current_row = self.selected_index.row()
            current_column = self.selected_index.column()
            previous_index = model.index(current_row - 1, current_column, self.selected_index.parent())
            if previous_index.isValid():
                bb = model.fileName(previous_index)
                self.ui.img2.mouseDoubleClickEvent = self.get_clicked_position
        
                c=[".jpg",".png",".JPG",".PNG"]
                for i in range(4):
                    if c[i] in bb:
                        
                        path=os.listdir(r'C:\Users\Home\car')
                        pathimg=os.listdir(r'C:\Users\Home\car\image')
                        topath=r'C:\Users\Home\car\image'
                        imgpath=topath+'\\'+bb
                        
                        # if not os.path.isdir(topath):
                        #     os.makedirs(topath)
                        # if b not in pathimg:
                        #     copy(a,topath)
                        # else:
                        #     print('已存在檔案')
                        
                        self.paint0()
                        self.img1.hide()
                
    def closeEvent(self, event):
        QApplication.closeAllWindows()
    def sort_treeview_children(self,tree_view, parent_index):
        model = tree_view.model()
        num_children = model.rowCount(parent_index)

        if num_children > 0:
            file_indexes = []
            folder_indexes = []

            # 分類子項為檔案和資料夾
            for i in range(num_children):
                child_index = model.index(i, 0, parent_index)
                is_dir = model.isDir(child_index)
                if is_dir:
                    folder_indexes.append(child_index)
                else:
                    file_indexes.append(child_index)

            # 根據資料夾內的索引進行排序
            sorted_folder_indexes = sorted(folder_indexes, key=lambda x: model.fileName(x))
            sorted_file_indexes = sorted(file_indexes, key=lambda x: model.fileName(x))

            # 更新TreeView的順序
            for i, folder_index in enumerate(sorted_folder_indexes):
                model.moveRow(parent_index, i, parent_index, i)
            for i, file_index in enumerate(sorted_file_indexes):
                model.moveRow(parent_index, len(sorted_folder_indexes) + i, parent_index, i + len(sorted_folder_indexes))

            # 遞迴處理子目錄
            for folder_index in sorted_folder_indexes:
                self.sort_treeview_children(tree_view, folder_index)
    def path(self):
        self.model = QFileSystemModel()
        self.model.setFilter(QDir.AllDirs | QDir.Files)
        self.model.setRootPath(QDir.rootPath())
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(QDir.rootPath()))
        if self.ui.lineEdit_1.text() !="":
            self.ui.treeView.setRootIndex(self.model.index(self.ui.lineEdit_1.text()))
        
        # 隐藏"Size"列
        self.ui.treeView.setColumnHidden(1, True)
        self.ui.treeView.setColumnHidden(2, True)
        self.ui.treeView.setColumnHidden(3, True)


        self.ui.treeView.setColumnWidth(0, 250)
        self.ui.treeView.setAnimated(True)
        self.ui.treeView.setIndentation(20)
        # self.ui.treeView.setSortingEnabled(True)
        self.ui.treeView.setSelectionMode(QTreeView.SingleSelection)

        # 设置过滤器，仅显示指定目录下的数据
        directory = 'C:\\'  # 指定目录的路径
        if self.ui.lineEdit_1.text() !="":
            directory=self.ui.lineEdit_1.text()

        directory_index = self.model.index(directory)
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)
        self.ui.treeView.setRootIndex(directory_index)
        
        self.ui.treeView.expandAll()
        self.ui.treeView.doubleClicked.connect(self.file_name)
        
        self.ui.pushButton_6.clicked.connect(self.open_next_file)
        self.ui.pushButton_5.clicked.connect(self.open_previous_file)

        # 设置自定义代理模型
        delegate = FileIconDelegate(self.ui.treeView)
        self.ui.treeView.setItemDelegate(delegate)
        self.sort_treeview_children(self.ui.treeView, self.ui.treeView.rootIndex())

    def file_name(self,Qmodelidx):
        global imgpath,b
        a=self.model.filePath(Qmodelidx) #输出文件的地址。
        b=self.model.fileName(Qmodelidx) #输出文件名
        self.ui.img2.mouseDoubleClickEvent = self.get_clicked_position
        
        c=[".jpg",".png",".JPG",".PNG"]
        for i in range(4):
            if c[i] in b:
                cccc=""
                ccc=a.split("/")[:-1]
                d=ccc[-1]
                for f in ccc:
                    cccc+=f+'\\'
                print(cccc)                
                topath=cccc
                imgpath=topath+b
                # if self.ui.lineEdit_2.text !=None:
                #     path=os.listdir(self.ui.lineEdit_2)
                #     pathimg=os.listdir(self.ui.lineEdit_2+d)
                #     topath=self.ui.lineEdit_2+d
                #     imgpath=topath+'\\'+b
                
                # if not os.path.isdir(topath):
                #     os.makedirs(topath)
                # if b not in pathimg:
                #     copy(a,topath)
                # else:
                #     print('已存在檔案')
                
                self.paint0()
                self.img1.hide()
                # self.img1.setPixmap(QPixmap.fromImage(self.qimg))
                
    # def itemtext(self):
    #     self.er = error()
    #     c=[1,2,3,4,5]
    #     AllItems = [self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())]
    #     print(AllItems)
    #     for i in range(c.__len__()): 
    #         self.item = QListWidgetItem(str(c[i]))
    #         self.er.ui.listWidget.addItem(self.item)
    #     self.er.show()  
    def showNewWindow(self):
        self.er = error()       # 連接新視窗
        #setup
        self.er.ui.XX.clicked.connect(self.er.close)
        self.er.ui.ADD.clicked.connect(self.itemtext)
        self.er.show()              # 顯示新視窗

    def saveimg(self):
        if self.ui.lineEdit_2.text()!='':
            # 创建一个QPixmap对象，与label的大小相同
            pixmap = QPixmap(self.ui.img2.size())
            pixmap.fill(Qt.transparent)  # 设置透明背景

            # 创建一个QPainter对象，并将其与QPixmap关联
            painter = QPainter(pixmap)
            self.ui.img2.render(painter)  # 在pixmap上绘制label的内容
            painter.end()  # 结束绘制过程
            save_path = self.ui.lineEdit_2.text()+"//" +"Finish_"+ b
            # 保存pixmap中的图像到文件
            pixmap.save(save_path)
            #输出文件名 b


    def rstt(self):
        if imgpath !=0:
            self.img = cv2.imread(imgpath)
            height0, width0, channel = self.img.shape
            bytesPerline = 3 * width0
            self.qimg0 = QImage(self.img.data, width0, height0, bytesPerline, QImage.Format_RGB888).rgbSwapped()
            self.qimg=QPixmap.fromImage(self.qimg0)
            self.ui.img2.setPixmap(self.qimg)
            self.ui.img2.setScaledContents(True)
            self.img1.hide()

    def check(self):
        try:
            if self.ui.checkBox.isChecked():
                self.ui.horizontalSliderD.setEnabled(True)
                self.ui.horizontalSliderL.setEnabled(True)
                self.getslidervalueD()
                self.paint0()
                self.paint1()

            else:
                self.ui.horizontalSliderD.setEnabled(False)
                self.ui.horizontalSliderL.setEnabled(False)

                self.rstt()

            #img1圖
                
                qpainter = QPainter()
                qpainter.begin(self.qimg)
                qpainter.setPen(QPen(QColor('#ff0000'), 10))

                xx=norm_x*self.qimg.width()-(width/2)
                yy=norm_y*self.qimg.height()-(height/2)
                
                rect=QRect(xx,yy,width,height)
                qpainter.drawRect(rect)
                self.ui.img2.setPixmap(self.qimg)
                self.ui.img2.setScaledContents(True)

                pixmap = self.ui.img2.pixmap()

                # 截取绘制区域的图像
                captured_image = pixmap.toImage().copy(rect)

                # 保存截图（可根据需要进行处理）
                # captured_image.save("captured_image.jpg")
                captured_pixmap = QPixmap.fromImage(captured_image)
                # 显示裁剪后的图像
                self.img1.setPixmap(captured_pixmap)
                self.img1.setScaledContents(True)

                self.img1.show()    

                qpainter.end()
                        
                
                
        except:
            print('XX')
        
    def rst(self):
        self.ui.horizontalSliderD.setEnabled(False)
        self.ui.horizontalSliderL.setEnabled(False)
        self.ui.checkBox.setChecked(False)
        self.ui.horizontalSliderD.setValue(0)
        self.ui.horizontalSliderL.setValue(0)
        self.paint0()
        self.paint1()

    
    def getslidervalueD(self): 
        self.paint0()
        self.paint1()
        self.ui.horizontalSliderD.setValue(self.ui.horizontalSliderD.value())
    def getslidervalueL(self):    
        self.paint0()
        self.paint1()
        self.ui.horizontalSliderL.setValue(self.ui.horizontalSliderL.value())
    

 
    def get_clicked_position(self, event):
        global norm_x,norm_y
        # index = event.pos.y()*self.ui.img2.size().width()+event.pos().x() #像素位置
        self.isShow=True
        if event.buttons() == QtCore.Qt.LeftButton:
            # print("左键按下")
            self.point_type=0
        # elif event.buttons() == QtCore.Qt.RightButton:
        #     print("右键按下")
        #     self.point_type=1
        global x,y
        x = event.pos().x()
        y = event.pos().y() 
        norm_x = x/self.ui.img2.width()
        norm_y = y/self.ui.img2.height()
        # print(f"(x, y) = ({x}, {y}), normalized (x, y) = ({norm_x}, {norm_y})")
        # if self.isShow==True:
        #     self.update()
        self.paint1()
    
    def paint0(self):
        if imgpath !=0:
            self.ui.checkBox.setEnabled(True)
        else:
            self.ui.checkBox.setEnabled(False)

        self.img = cv2.imread(imgpath)
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width

        contrast = self.ui.horizontalSliderD.value()
        brightness = self.ui.horizontalSliderL.value()
        output = self.img * (contrast/127 + 1) - contrast + brightness
        output = np.clip(output, 0, 255)
        output = np.uint8(output)

        self.qpixmap = QPixmap.fromImage(QImage(output.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped())
        self.ui.img2.setPixmap(self.qpixmap)
        self.ui.img2.setScaledContents(True)
        
        
            
    def paint1(self):  
        if imgpath !=0:
            self.paint0()
            qpainter = QPainter()
            qpainter.begin(self.qpixmap)
            qpainter.setPen(QPen(QColor('#ff0000'), 10))

            xx=norm_x*self.qpixmap.width()-(width/2)
            yy=norm_y*self.qpixmap.height()-(height/2)
            try:
                if self.point_type==0:
                    rect=QRect(xx,yy,width,height)
                    qpainter.drawRect(rect)
                    
                    self.ui.img2.setPixmap(self.qpixmap)
                    pixmap = self.ui.img2.pixmap()

                    # 截取绘制区域的图像
                    captured_image = pixmap.toImage().copy(rect)

                    # 保存截图（可根据需要进行处理）
                    # captured_image.save("captured_image.jpg")
                    captured_pixmap = QPixmap.fromImage(captured_image)
                    # 显示裁剪后的图像
                    self.img1.setPixmap(captured_pixmap)
                    self.img1.show()
                    
            except:
                qpainter.drawRect(100,100,width,height)
            
            qpainter.end()
            
    
            
    #目錄設置
    def save_of(self):
         self.ui.lineEdit_1.setPlaceholderText(self.ui.lineEdit_1.text())
         self.ui.lineEdit_2.setPlaceholderText(self.ui.lineEdit_2.text())
         self.ui.lineEdit_3.setPlaceholderText(self.ui.lineEdit_3.text())
         self.path()

    def open_folder1(self):
        folder_path = QFileDialog.getExistingDirectory(self,
                  "開啟資料夾",
                  "./")                 # start path
        self.ui.lineEdit_1.setText(folder_path)
    def open_folder2(self):
        folder_path = QFileDialog.getExistingDirectory(self,
                  "開啟資料夾",
                  "./")                 # start path    
        self.ui.lineEdit_2.setText(folder_path)
    def open_folder3(self):
        folder_path = QFileDialog.getExistingDirectory(self,
                  "開啟資料夾",
                  "./")                 # start path
        self.ui.lineEdit_3.setText(folder_path)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    stats = Stats()   
    stats.showMaximized() 
    stats.show()
    sys.exit(app.exec_())

    
