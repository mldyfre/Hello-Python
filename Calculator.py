# -*- coding: utf-8 -*-

import os, sys
import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter.font import Font

calculator = tkinter.Tk()		# 第一步，实例化object，建立窗口window
calculator.title('计算器')	# 第二步，给窗口的可视化起个名字
calculator.geometry('320x100')	# 第三步，设定窗口的大小（长 * 宽）  这里的乘是小x

jiguo=IntVar()
jiguo.set('输入后直接按 Enter 进行计算')

# 定义按钮功能
def jisuan():
	i = eval(entry_number.get())
	jiguo.set(i)
	print(i)
	
def jisuans(q):
	q = eval(entry_number.get())
	jiguo.set(q)
	print(q)
	
# 定义一个输入框
var_usr_name = tkinter.StringVar()
var_usr_name.set('')
entry_number = tkinter.Entry(calculator, textvariable=var_usr_name, font=('微软雅黑', 14))
entry_number.place(x=10, y=20)


# 改变按钮风格


# 定义一个按钮
Button(calculator, text='计算', width=7, height=1, command=jisuan).place(x=250, y=20)

entry_number.bind('<Key-Return>', jisuans)

# 显示结果
l = Label(calculator, text='计算结果：', width=8, height=2, ).place(x=10, y=55)
o = Label(calculator, textvariable=jiguo, width=27, height=2, ).place(x=75, y=55)

		
calculator.mainloop()