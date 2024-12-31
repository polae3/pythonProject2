'''
파일명: Ex24-1-tkinter.py
'''

import tkinter as tk
from tkinter import ttk

from PIL.ImageOps import scale

root = tk.Tk()
# 레이블 위젯 생성
label = tk.Label(root, text='Hello, Tkinter!')
label.pack()

# 한줄 입력 위젯 생성
entry = tk.Entry(root)
entry.pack()

# 여러 줄 텍스트 입력 위젯 생성
text = tk.Text(root)
text.pack()

# 체크박스 변수 위젯 생성
checkbox_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text='Check me!', variable=checkbox_var)
checkbutton.pack()

# 라디오버튼 위젯 생성
radio_var = tk.StringVar()
radio_var.set('option1')
radiobutton1 = tk.Radiobutton(root, text='Option1', variable=radio_var, value='option1')
radiobutton2 = tk.Radiobutton(root, text='Option2', variable=radio_var, value='option2')
radiobutton1.pack()
radiobutton2.pack()


# 수평 슬라이더 위젯 생성
scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
scale.pack()

# 스핀 박스 위젯 생성
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# 콤보 박스(드랍다운 리스트) 위젯 배치
combo = ttk.Combobox(root, values=['Item1', 'Item2', 'Item3'])
# combo.current(0)
combo.set('Item1')
combo.pack()

def onClick():
    print('Button Click!')

    # 각 위젯의 현재값을 가져 오기
    s_entry = entry.get()   # 스테이 위젯의 입력값 가져오기
    s_text = text.get('1.0', tk.END)        # Text 위젯의 모든 퀘스트(1행 0열까지의 모든 택스트

    # 각 엔젤의 현재 값을 가져오기

    # 각 위젯의 현재 값을 가져오기
    i_checkbox = checkbox_var.get()
    s_radiobutton = radio_var.get()
    i_scale = scale.get()
    i_spinbox = spinbox.get()
    s_combo = combo.get()

    # 기재된 값들을 출력
    print(f's_entry: {s_entry}')
    print(f's_text: {s_text}')
    print(f'i_checkbox: {i_checkbox}')
    print(f's_radiobutton: {s_radiobutton}')
    print(f'i_scale: {i_scale}')
    print(f'i_spinbox: {i_spinbox}')
    print(f's_combo: {s_combo}')



# 버튼 위젯 생성
button = tk.Button(root, text='Click me!', command=onClick)
button.pack()




# 실행코드
if __name__ == '__main__': # main 코드
    root.mainloop()