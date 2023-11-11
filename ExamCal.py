import tkinter as tk

win = tk.Tk()
win.title('examcalculate')
win.geometry('600x500')
win.resizable(False, False)

def calc():
    if check_value(korVal.get()) == False:
        return

    if check_value(engVal.get()) == False:
        return

    if check_value(mathVal.get()) == False:
        return

    total = int(korVal.get()) + int(engVal.get()) + int(mathVal.get())
    average = total/3

    sumVal.set(total)
    avgVal.set(f'{average:.2f}')

def init():
    nameVal.set('')
    korVal.set('')
    engVal.set('')
    mathVal.set('')
    sumVal.set('')
    avgVal.set('')

def check_value(value):
    cnt = 0

    for ch in value:
        if not (ord('0') <= ord(ch) <= ord('9')):
            cnt += 1

    if cnt == 0:
        return True
    else:
        return False

# 이름
name_lb = tk.Label(win, text='이름', font=('', 25))
name_lb.grid(row=0, column=0)

nameVal = tk.StringVar()
name_ent = tk.Entry(win, font=('', 25), width=10, textvariable=nameVal)
name_ent.grid(row=0, column=1)

# 국어
kor_lb = tk.Label(win, text='국어', font=('', 25))
kor_lb.grid(row=1, column=0)

korVal = tk.StringVar()
kor_ent = tk.Entry(win, font=('', 25), width=10, textvariable=korVal)
kor_ent.grid(row=1, column=1)

# 영어
eng_lb = tk.Label(win, text='영어', font=('', 25))
eng_lb.grid(row=2, column=0)

engVal = tk.StringVar()
eng_ent = tk.Entry(win, font=('', 25), width=10, textvariable=engVal)
eng_ent.grid(row=2, column=1)

# 수학
math_lb = tk.Label(win, text='수학', font=('', 25))
math_lb.grid(row=3, column=0)

mathVal = tk.StringVar()
math_ent = tk.Entry(win, font=('', 25), width=10, textvariable=mathVal)
math_ent.grid(row=3, column=1)

# 총점
sum_lb = tk.Label(win, text='총점', font=('', 25))
sum_lb.grid(row=4, column=0)

sumVal = tk.StringVar()
sum_ent = tk.Entry(win, font=('', 25), width=10, textvariable=sumVal, state='readonly')
sum_ent.grid(row=4, column=1)

# 평균
avg_lb = tk.Label(win, text='평균', font=('', 25))
avg_lb.grid(row=5, column=0)

avgVal= tk.StringVar()
avg_ent = tk.Entry(win, font=('', 25), width=10, textvariable=avgVal, state='readonly')
avg_ent.grid(row=5, column=1)


# 계산
cal_btn = tk.Button(win, text='계산', font=('', 25), command=calc)
cal_btn.grid(row=6, column=0)

# 초기화
reset_btn = tk.Button(win, text='초기화', font=('', 25), command=init)
reset_btn.grid(row=6, column=1)

win.mainloop()