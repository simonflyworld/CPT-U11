#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 15 17:41:06 2019

@author:    Simon Li
"""

import PIL
from tkinter import *
from tkinter.dialog import *
from tkinter import simpledialog
from tkinter import filedialog
import pytesseract
import cv2
import numpy as np
import math
import re


def take_picture(camra_choose):

    int_value = int(camra_choose)

    cam_input = cv2.VideoCapture(int_value)

    while True:

        (ret, frame) = cam_input.read()

        cv2.imshow('Take a picture', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):

            cv2.imwrite('image.jpg', frame)

            break

    cam_input.release()

    cv2.destroyAllWindows()

    pass


def identification():

    img = cv2.imread('image.jpg')

    resized = cv2.resize(img, (600, 400))

    # convert to gray

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # threshold the gray

    (ret, thresh) = cv2.threshold(gray, 110, 0xFF, cv2.THRESH_TRUNC)

    # apply closing to fill in holes

    kernel = np.ones((5, 5), dtype=np.uint8)

    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    cv2.imwrite('onecolor.png', closing)

    letter_in_image = \
        pytesseract.image_to_string(PIL.Image.open('onecolor.png'))

    # print(letter_in_image)

    return letter_in_image


def init_action(expression):
    """

    # initialization

    :param expression: "-1-20*-3"

    :return: res   ['-1', '-', '20', '*', '-3']

    """

    res = []

    tag = False

    char = ''

    for i in expression:

        if i.isdigit():

            tag = True

            char += i
        else:

        # not an number it's a symbol.

            if tag:

                # It's a symbol ，and have number before

                if i == '.':

                    # solve decimal

                    char += i
                else:

                    res.append(char)

                    char = ''

                    res.append(i)

                    tag = False
            else:

                # it's a symbol ，No number before it.

                if i == '-':

                    char = i
                else:

                    res.append(i)

                pass

    if len(char) > 0:

        res.append(char)

    return res


def delete_space(expression):

    res = ''

    for i in expression:

        if i == ' ':

            continue

        res += i

    pass

    return res


def priority(exp, opt_list):
    """

    判断优先级

    :param exp:  symbol in now

    :param opt_list:   符号栈

    :return:">" 当前符号优先级大于栈顶元素优先级

            "<"  当前符号优先级小于栈顶元素优先级

             "=" : 当前符号优先级等于栈顶元素优先级

    """

    laval1 = ['+', '-']

    laval2 = ['*', '/']

    if exp in laval1:

        if opt_list[-1] in laval1:

            # it's  + —  same level

            return '='
        else:

            return '<'

    if exp in laval2:

        if opt_list[-1] in laval2:

            return '='
        elif opt_list[-1] in laval1:

            return '>'


def compute(num1, opt, num2):
    """

    count 

    param num1: first process number

    param opt: operator

    param num2: second process number

    return:

    """

    if opt == '+':

        return num1 + num2
    elif opt == '-':

        return num1 - num2
    elif opt == '*':

        return num1 * num2
    elif opt == '/':

        return num1 / num2
    else:

        return None


def calculate(exp_list):

    number_list = []

    opt_list = []

    symbol_list = [
        '+',
        '-',
        '*',
        '/',
        '(',
        ')',
        ]

    tag = False

    for exp in exp_list:

        if exp not in symbol_list:

            # it's number

            exp = float(exp)

            if not tag:

                number_list.append(exp)
            else:

                tag = False

                num2 = exp

                num1 = number_list.pop()

                opt = opt_list.pop()

                result = compute(num1, opt, num2)

                # print("result111  : %s"%result)

                # print("num1  : %s" % num1)

                # print("opt  : %s" % opt)

                # print("num2  : %s" % num2)

                number_list.append(result)
        else:

            # it's symbol

            if len(opt_list) == 0:

                opt_list.append(exp)
            else:

                if priority(exp, opt_list) == '=' or priority(exp,
                        opt_list) == '<':

                    # Can count

                    num1 = 0

                    num2 = 0

                    opt = opt_list.pop()

                    if len(number_list) >= 2:

                        num2 = number_list.pop()

                        num1 = number_list.pop()

                        result = compute(num1, opt, num2)

                        # print("result : %s"%result)

                        number_list.append(result)

                        opt_list.append(exp)
                    else:

                        # error

                        return None
                elif priority(exp, opt_list) == '>':

                    tag = True

                    opt_list.append(exp)

    # print("number_list : %s"%number_list)

    # print("opt_list : %s" % opt_list)

    if len(number_list) == 2 and len(opt_list) == 1:

        pass

        num2 = number_list.pop()

        num1 = number_list.pop()

        opt = opt_list.pop()

        return compute(num1, opt, num2)
    else:

        # "The input expression is incorrect and cannot be evaluated."

        return None


def count_main(letter):

    # expression = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

    # expression = "-1 + 2-3 + 4 + 5+8"

    # expression = "2*2+3*4-22*6+4"

    # expression = "2*2+(3*(4-22)*6)*2+(4+5)-4"

    expression = letter.strip()

    expression = delete_space(expression)

        # print("expression : %s"%expression)

    while True:

        match = re.search(r'\([^()]+\)', expression)

        if not match:

            break
        else:

            exp = match.group()

            exp_list = init_action(exp[1:-1])

                # print("exp_list : %s"%exp_list)

            cal_result = calculate(exp_list)

                # print("cal_result:%s"%cal_result)

            tmp = expression.replace(exp, str(cal_result))

            expression = tmp

                # print("expression: %s"%expression)

        # print("expression--22  : %s"%expression)

    exp_list = init_action(expression)

        # print("exp_list : %s"%exp_list)

    cal_result = calculate(exp_list)

    return cal_result


def main():

    def zeropg():
        global root0
        root0 = Tk()

        # 登陆名字密码判断

        def reg():
            password=['a','b']
            myAccount = a_entry.get()
            myPassword = p_entry.get()
            a_len = len(myAccount)
            p_len = len(myPassword)
            if myAccount == 'a' and myPassword in password:
                msg_label['text'] = 'well down'
                firstpg()
            elif myAccount == 'a' and myPassword not in password:

                msg_label['text'] = 'password errow'
                p_entry.delete(0, p_len)
            else:
                msg_label['text'] = 'name errow'
                a_entry.delete(0, a_len)
                p_entry.delete(0, p_len)

        # 第二页登陆界面

        root0.title('Login')
        root0.geometry('1920x1080')
        root0.resizable(width=True, height=True)
        root0.configure(bg='MediumOrchid1')

        # 名字输入

        a_label = Label(root0, text='username:')
        a_label.grid(row=0, column=0, sticky=W)
        a_entry = Entry(root0)
        a_entry.grid(row=0, column=1, sticky=E)

        # 密码

        p_label = Label(root0, text='password:')
        p_label.grid(row=1, column=0, sticky=W)
        p_entry = Entry(root0)
        p_entry['show'] = '*'
        p_entry.grid(row=1, column=1, sticky=E)

        # 三收钱图片

        photo = PhotoImage(file='picweisar.png')
        lbl = Label(image=photo)
        lbl.image = photo
        lbl.grid(column=100, row=80)

        # 二收钱图片

        photo = PhotoImage(file='picweier.png')
        lbl = Label(image=photo)
        lbl.image = photo
        lbl.grid(column=200, row=80)

        # pay for us

        L_title = Label(root0,
                        text='It is not free, please pay us to get licence! '
                        )
        L_title.config(font='Helvetica -50 bold', bg='green', fg='red')
        L_title.place(x=900, y=900, anchor='center')

        # 登录按钮

        btn = Button(root0, text='login', command=reg)
        btn.grid(row=2, column=1, sticky=E)

        # 提示

        msg_label = Label(root0, text='')
        msg_label.grid(column=1,row=5)

    def firstpg():
        root0.destroy()
        global root1
        root1 = Tk()

        root1.title('Wecome')
        root1.geometry('1920x1080')
        root1.resizable(width=True, height=True)

        # 图片

        photo = PhotoImage(file='welcome.png')
        lbl = Label(image=photo)
        lbl.image = photo
        lbl.grid(column=0, row=0)

        # 标签

        L_title = Label(root1, text='Vision calculator')
        L_title.config(font='Helvetica -50 bold', bg='blue4', fg='red')
        L_title.place(x=950, y=200, anchor='center')

        L_title = Label(root1,
                        text='about us : please visit "https://docs.google.com/document/d/1q5qVvbdpkswktQKYdEsMGA3xBCi3_el3K9IjyY29ACA/edit"'
                        )
        L_title.config(font='Helvetica -20 bold', fg='white', bg='blue4'
                       )
        L_title.place(x=980, y=1000, anchor='center')

        B_0 = Button(
            root1,
            text='start',
            command=secondpg,
            width=28,
            height=3,
            bg='blue4',
            fg='white',
            )
        B_0.place(x=590, y=700)
        B_1 = Button(
            root1,
            text='cancel',
            command=root1.destroy,
            width=28,
            height=3,
            bg='blue4',
            fg='white',
            )
        B_1.place(x=1160, y=700)

    def secondpg():
        root1.destroy()
        global root2
        root2 = Tk()

        root2.title('cam choose')
        root2.geometry('1920x1080')
        root2.resizable(width=True, height=True)
        root2.configure(bg='green')

        # 标题

        L_title = Label(root2, text='please give a camera number')
        L_title.config(font='Helvetica -50 bold', bg='green', fg='red')
        L_title.place(x=500, y=100, anchor='center')

        # 报错

        L_title = Label(root2,
                        text='input is your camera port number(usually onbord camera is 0, if your computer did not have your input camera number,we will auto use 0)'
                        )
        L_title.config(font='Helvetica -27 bold', bg='green', fg='red')
        L_title.place(x=950, y=800, anchor='center')

        # 输入按钮

        cam_choose = Entry(root2)  # 输入框赋值在e变量
        cam_choose.pack(padx=50, pady=300)

        def takein():

            cram_choose = cam_choose.get()
            root2.destroy
            campg(cram_choose)

        b1 = Button(root2, text='next', width=15, height=2,
                    command=takein)
        b1.pack()

    def campg(cram_choose):
        root2.destroy()
        while True:
            try:
                take_picture(cram_choose)
            except:
                cram_choose = 0
            else:
                break

        letter_in_image = identification()
        answer = count_main(letter_in_image)
        fourthpg(answer)

    def fourthpg(answer):
        global root4
        root4 = Tk()

        root4.title('answer')
        root4.geometry('1920x1080')
        root4.resizable(width=True, height=True)

        photo = PhotoImage(file='wixp.png')
        lbl = Label(image=photo)
        lbl.image = photo
        lbl.grid(column=0, row=0)

        L_title = Label(root4, text='answer:')
        L_title.config(font='Helvetica -40 bold', fg='blue')
        L_title.place(x=200, y=100, anchor='center')
        out_answer = str(answer)
        L_title = Label(root4, text=out_answer)
        L_title.config(font='Helvetica -40 bold', fg='blue')
        L_title.place(x=500, y=100, anchor='center')

        B_5 = Button(root4, text='exit', command=root4.destroy,
                     width=30, height=5)
        B_5.place(x=1500, y=900)

    zeropg()
    root0.mainloop()
    cv2.destroyAllWindows()


def test():
    assert count_main('1+1') == 2, 'answer error 1+1 == 2'
    assert count_main('2-2') == 0, 'answer error 2-2 == 0'
    assert count_main('2*2') == 4, 'answer error 2*2 == 4'
    assert count_main('4/2') == 2, 'answer error 4/2 == 2'
    assert count_main('15+1') == 16, 'answer error 15+1 == 16'
    assert count_main('(2+2)*8') == 32, 'answer error (2+2)*8 == 4'
    
    print ('pass all test!')


test()
main()
