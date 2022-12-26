# PySide6-uic UIV1.ui -o ui.py
# from ui_demo import Ui_Demo
# https://gitee.com/laorange/DemoPyside6/blob/master

from threading import Thread
from ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Signal, QObject
import os
import utils

class BotSignal(QObject):
    setProgressBar = Signal(int)
    setButtorn = Signal(str, bool)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  # UI类的实例化()
        self.ui.setupUi(self)
        
        self.bot_signal = BotSignal()
        self.output_path = os.path.join(os.path.dirname(__file__), 'output')

        self.bind()
    
    def bind(self):
        self.ui.startButton.clicked.connect(self.handle_click)
        self.bot_signal.setProgressBar.connect(self.set_progress_bar)
        self.bot_signal.setButtorn.connect(self.set_button_status)

    def set_progress_bar(self, progress: int):
        self.ui.download_progressBar.setValue(progress)
        # self.ui.label.setText(f'下载进度：{progress}%')
    
    def set_button_status(self, text: str, enabled: bool):
        self.ui.startButton.setText(text)
        self.ui.startButton.setEnabled(enabled)
    
    def handle_click(self):
        
        def do_task():
            fid = self.ui.input_fid.text()
            cookie = self.ui.input_cookie.toPlainText()
            name = self.ui.input_name.text()
            pages = self.ui.input_pages.value()
            scale = self.ui.input_scale.value()

            self.bot_signal.setButtorn.emit(f'正在下载', False)

            if not os.path.exists(self.output_path):
                os.mkdir(self.output_path)
            
            try:
                for item_page in range(pages):    
                    utils.get_page(item_page, fid, cookie, name, scale, self.output_path)
                    progress = (item_page + 1) * 100 // pages
                    self.bot_signal.setProgressBar.emit(progress)
                    self.bot_signal.setButtorn.emit(f'正在下载: {item_page+1}/{pages}', False)
                self.bot_signal.setButtorn.emit(f'正在合并', False)
                utils.pic2pdf(name, self.output_path)

            except Exception as e:
                print(e)
                print("出错了")
            finally:
                self.bot_signal.setButtorn.emit(f'开始下载', True)
        Thread(target=do_task).start()

if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出


