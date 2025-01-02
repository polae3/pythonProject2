'''
파일명: Ex24-7-Tkinter-TAB.py

Tkinter 간단한 TAB
'''

import tkinter as tk
from cProfile import label
from tkinter import ttk
import sv_ttk
from PIL.ImageOps import expand


class SimpleNotebookApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('간단한 노트북 예제')
        self.root.geometry('400x300')

        sv_ttk.set_theme('dark')   # dark or light
        self.setup_ui()

    def setup_ui(self):

        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill='both', expand=True)

        # 노트북 생성
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill='both', expand=True)

        # 첫번째 탭
        tab1 = ttk.Frame(notebook)
        label1 = ttk.Label(tab1, text='첫 번째 탭의 내용입니다.')
        label1.pack(padx=20, pady=20)
        notebook.add(tab1, text='탭 1')

        # 두번째 탭
        tab1 = ttk.Frame(notebook)
        label1 = ttk.Label(tab1, text='두 번째 탭의 내용입니다.')
        label1.pack(padx=20, pady=20)
        notebook.add(tab1, text='탭 2')

        # 세번째 탭
        tab1 = ttk.Frame(notebook)
        label1 = ttk.Label(tab1, text='세 번째 탭의 내용입니다.')
        label1.pack(padx=20, pady=20)
        notebook.add(tab1, text='탭 3')

    def run(self):
        self.root.mainloop()


# 실행코드
app = SimpleNotebookApp()
app.run()

