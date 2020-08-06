
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:43:45 2020

@author: 1002
"""
import tkinter as tk

from tkinter import ttk

from CaesarCiper import CaesarCiper


window=tk.Tk()
window.title('Caesar Cipher')  #窗口名字  
window.geometry('800x600')   #窗口size
'''
# Entry的第一个参数是父窗口，即这里的window
# *表示输入的文本变为星号，在Entry不可见内容，若为None则表示为输入文本以原形式可见
e=tk.Entry(window,show='*')
e.pack()
'''

#文本输入
inputTxt=tk.Text(window,height=10)  
inputTxt.pack(side = 'top')

optCode = CaesarCiper()


def encode():
    var = inputTxt.get('0.0','end')
    k = process_combobox()
    codeText = optCode.encoder(var,k)
    var = "out>>"+codeText
    resultTxt.insert('insert',var)

    
def decode():
    var = inputTxt.get('0.0','end')
    decodeText = optCode.decoder(var)
    var = "out>>"+decodeText
    resultTxt.insert('end',var)
    
def clear_input():
    inputTxt.delete('0.0','end')

def process_combobox():
    varCom  = com.get()
    if varCom == "下拉选择移动key值":
        key = 0
        resultTxt.insert('end',"（warning,没有选择key,默认key为0）")
        return 0
    else:
        key = int(varCom)
        return key
    
        
#这里的end表示插入在结尾，可以换为1.2，则插入在第一行第二位后面
b1=tk.Button(window,text='凯撒加密',width=15,height=2,command=encode)
b1.pack()

b1=tk.Button(window,text='凯撒解密',width=15,height=2,command=decode)
b1.pack()

b2=tk.Button(window,text='清空',width=15,height=2,command=clear_input)
b2.pack()

#文本输出
resultTxt=tk.Text(window,height=30)     #这里设置文本框高，可以容纳两行
resultTxt.pack(side = 'left')

#下拉框
cv= tk.StringVar()
com=ttk.Combobox(window,text='key',textvariable=cv)
com.pack()
#设置下拉数据
com["value"]=("下拉选择移动key值","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26")
#设置默认值
com.current(0)

key =0

window.mainloop()