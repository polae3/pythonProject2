'''
파일명: Ex24-3-Tkinter.py


'''

import tkinter as tk

root = tk.Tk()
root.geometry('500x300')    # 넓이 500, 높이 300 설정

'''
# pack() - 위젯들을 상자안에 쌓듯이 배치한다
label1 = tk.Label(root, text='Hello World')
label1.pack()
label2 = tk.Label(root, text='This is a sample program!')
label2.pack()
'''


'''
# grid() - 위젯을 격자 모양으로 배치한다. - row 와 column으로 위치 지정한다.

label1 = tk.Label(root, text='Hello World')
label1.grid(row=0, column = 0)
label2 = tk.Label(root, text='This is a sample program!')
label2.grid(row=1, column = 1)
'''

# place() - 위젯을 지정된 좌표에 배치한다. x, y 좌표를 지정
label1 = tk.Label(root, text='Hello World')
label1.place(x=10, y=10)
label2 = tk.Label(root, text='This is a sample program!')
label2.place(x=10, y=50)

root.mainloop()
