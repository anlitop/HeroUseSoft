from PyQt5.QtCore import pyqtSignal,QThread
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QMessageBox
from Ui_main import Ui_MainWindow
from sys import exit,argv
import HeroUse as hu
from os import path,startfile
from json import dumps,load
from webbrowser import open_new_tab,get


class App(QMainWindow,Ui_MainWindow):
       
    def __init__(self,parent=None):
        super(App,self).__init__(parent)
        self.setupUi(self)
        self.workthread=WorkThread(self)
        self.workthread.trigger.connect(self.Callback)
        self.chose_data_btn.clicked.connect(self.onClick_data_btn)
        self.chose_file_btn.clicked.connect(self.onClick_file_btn)
        self.start_handle_btn.clicked.connect(self.onClick_start_btn)
        self.copy_sql_btn.clicked.connect(self.onclick_copy_btn)
        self.open_link_btn.clicked.connect(self.onclick_open_link)
        self.read_path="C:/"
        self.save_path="D:"
        self.sql_str=""
        self.load_dict={}
        self.control_btns=[self.chose_data_btn,self.chose_file_btn,self.start_handle_btn,self.data_path_line,self.save_path_line]
        self.read_config()
        self.cb=QApplication.clipboard()
    def onClick_data_btn(self):
        '''设置data文件的路径'''
        path=self.check_file_path(self.data_path_line,"read_path")
        fname,ok=QFileDialog.getOpenFileName(self,"选择文件",path,'csv files(*.csv)')
        if ok :
            self.data_path_line.setText(str(fname))
            self.read_path=self.data_path_line.text()
    def onClick_file_btn(self):
        '''设置保存文件的路径'''
        path=self.check_file_path(self.save_path_line,"save_path")
        fname=QFileDialog.getExistingDirectory(self,"选择文件",path)        
        self.save_path_line.setText(str(fname))
        self.save_path=self.save_path_line.text()
    def onClick_start_btn(self):
        #判定合法
        if path.isfile(self.read_path) and path.isdir(self.save_path):
            #开始工作
            self.workthread.start()
            #self.start_work()
        else:
            QMessageBox.critical(self,"警告","非法路径")
    def check_file_path(self,l_edit,key_name):
        '''如果lineedit中有路径，就返回路径'''
        if path.isfile(l_edit.text()):
            return l_edit.text()
        else:
            return self.config[key_name]   
    def handle_file_btns(self,open):
        '''处理按钮的禁用与启用'''
        for btn in self.control_btns:
            btn.setEnabled(open)
    def Callback(self,i):
        '''设置进度条'''
        if i==0:
            self.handle_file_btns(False)
        if i==100 and self.handle_file_progress.value()!=100:
            startfile(self.save_path)
            self.handle_file_btns(True)
            self.workthread.wait()
        self.handle_file_progress.setValue(i)        
    def read_config(self):
        with open("Data/config.json",'r')as f:
            self.config=load(f)            
        with open("Data/sql.csv",'r') as f:
            self.sql_str=f.read()         
    def onclick_copy_btn(self):
        self.cb.clear()
        self.cb.setText(self.sql_str)
        reply=QMessageBox.information(self,"复制成功","复制成功是否前往网站进行查询",QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply==QMessageBox.Ok:
            self.onclick_open_link()
    def onclick_open_link(self):
        try:
            get("chrome").open_new_tab(self.config["tga_url"])
        except Exception as e:
            open_new_tab(self.config["tga_url"])
    def update_config(self):        
        self.config['read_path']=self.read_path
        self.config['save_path']=self.save_path
        res=dumps(self.config)
        with open("Data/config.json",'w') as f:
            f.write(res)
    def open_dir(self):
        '''打开路径'''
        pass
    def start_work(self):
        #user_data
        user_data={
            'level':16,
            'col_name':'段位',
            'file_name':'/段位使用率.xlsx',
            'level_type':'pvp_level'
        }
        hu.handle_file(self.read_path,self.save_path,self,user_data)
        #不管怎么样，结束时进度条设定为100
        
        user_data={
        'level':15,
        'col_name':'主城',
        'file_name':'/主城使用率.xlsx',
        'level_type':'pve_level'}
        hu.handle_file(self.read_path,self.save_path,self,user_data)
        

class WorkThread(QThread):
    trigger=pyqtSignal(int)
    
    def __init__(self,ui):
        super(WorkThread,self).__init__()
        self.ui=ui


    def run(self):
        #开始处理线程
        self.trigger.emit(0)
        #更新一下config
        self.ui.update_config()
        #处理数据
        if self.ui.gen_pve_level_btn.isChecked():
            max_sum_count=200
        else:
            max_sum_count=100
        #user_data
        user_data={
            'level':16,
            'col_name':'段位',
            'file_name':'/段位使用率.xlsx',
            'level_type':'pvp_level',
            'max_sum_count':max_sum_count
        }
        hu.handle_file(self.ui.read_path,self.ui.save_path,self,user_data)
        #不管怎么样，结束时进度条设定为100
        if self.ui.gen_pve_level_btn.isChecked():
            user_data={
            'level':15,
            'col_name':'主城',
            'file_name':'/主城使用率.xlsx',
            'level_type':'pve_level',
            'max_sum_count':max_sum_count
            
        }
            hu.handle_file(self.ui.read_path,self.ui.save_path,self,user_data)
        self.trigger.emit(100)
        
if __name__ == "__main__":
     
    app=QApplication(argv)
    myapp=App()
    myapp.show()
    exit(app.exec_())