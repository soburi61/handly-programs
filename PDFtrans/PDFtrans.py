# -*- coding: utf-8 -*-
"""
このプログラムの私用用途以外での改変を禁じます.
転載,配信,商用利用を禁じます.
Created on 2022/5/24
@author:@burisoburi
"""
import pyperclip
import re
import subprocess
import os
from pygments import highlight
from pygments.lexers.python import Python3Lexer
from pygments.formatters.html import HtmlFormatter
import time

path = './out.py'
path2 = './out.html'


# デバッグ用
def debug(s):
    s = " 義 あ apple pen\n    print \t a 1 01 あ 1 a "
    return s


def show(s, flag):
    print("---------------")
    print(s)
    if flag:
        print("---↑変換後↑---")
        print("変換した文字列をクリップボードコピーしました(ctrl+vで貼り付けて使用してください)")
    else:
        print("---↑変換前↑---")


while True:
    print("----------------------------------------------------")
    print("クリップボードから文字列を自動取得")
    print(">t →(PDFをコピペしたときに出てくる)不要な空白を削除&全角記号を半角記号に変換")
    print(">n →行番号を削除(改行のあとの半角数字を削除)")
    print(">r →置換モード(正規表現可)")
    print(">a →pythonコードの自動整形(autopep8)")
    print(">p2h →pythonコードをhtml変換")
    print(">h →詳細な仕様を表示")
    print(">q →終了")
    print("----------------------------------------------------")
    x = input(">")

    if x == "q":
        break

    elif x == "t":
        # 改行の除去と連結
        s = pyperclip.paste()
        #s = debug(s)
        show(s, False)
        s = s.splitlines()
        for i in range(len(s)):
            ss = s[i]
            ss = ss.replace("，", ",")
            ss = ss.replace("．", ".")
            ss = ss.replace("。", ".")
            ss = ss.replace("、", ",")
            ss = ss.replace("（", "(")
            ss = ss.replace("）", ")")
            ss = ss.replace("　", " ")
            ss = ss.replace("’", "'")
            ss = ss.replace("´", "'")
            # -----------------
            # 英数字と英数字に挟まれた空白以外を削除
            ss = re.sub(r"([あ-んア-ン一-龥ー]) ((?=[あ-んア-ン一-龥ー]))", r"\1\2", ss)
            ss = re.sub(r"([あ-んア-ン一-龥ー]) ((?=\w))", r"\1\2", ss)
            ss = re.sub(r"(\w) ((?=[あ-んア-ン一-龥ー]))", r"\1\2", ss)
            ss = re.sub(r"^ +((?=[あ-んア-ン一-龥ー]))", r"\1", ss)
            ss = re.sub(r" +$", "", ss)
            # -----------------
            s[i] = ss

        s = "\n".join(s)

    elif x == "n":
        s = pyperclip.paste()
        show(s, False)
        s = s.splitlines()  # 改行区切ってリストに
        s = [re.sub("^ *[0-9]+ ", "", i) for i in s]  # 先頭^の連続*した数字[0-9]を消去
        s = [re.sub("^ *[0-9]+", "", i) for i in s]
        s = [re.sub(" +$", "", i) for i in s]  # 末尾空白を消去
        s = "\n".join(s)

    elif x == "r":
        while True:
            s = pyperclip.paste()
            show(s, False)
            s = "\n".join(s.splitlines())
            a = input("置換元文字列>")
            b = input("置換先文字列>")
            a = re.compile(a)  # 正規表現に変換
            s = re.sub(a, b, s)
            pyperclip.copy(s)
            show(s, True)
            x = input("続けて置換しますか?(y/n)>")
            if x == 'n':
                break
        continue

    elif x == "h":
        f = open('readme.txt', "r", encoding="utf-8")
        s = f.read()
        print(s)
        f.close()
        print()
        continue

    elif x == "s":
        f = open('sorce.txt', "r", encoding="utf-8")
        s = f.read()
        print(s)
        f.close()
        print()
        continue

    elif x == "a":
        s = pyperclip.paste()
        s = s.splitlines()
        f = open(path, "w", encoding='utf-8')
        for i in s:
            f.write(i+"\n")
        f.close()
        s = "\n".join(s)
        show(s, False)
        subprocess.call('admin.bat', shell=True)
        time.sleep(0.5)
        f = open(path, "r", encoding='utf-8')
        s = f.read()
        f.close()

    elif x== "p2h":
        s = pyperclip.paste()
        s = s.splitlines()
        f = open(path, "w", encoding='utf-8')
        for i in s:
            f.write(i+"\n")
        f.close()
        s = "\n".join(s)
        show(s,False)
        subprocess.call('pygmentize -f html -l python -O full -o '+path2+' '+path, shell=True)
        time.sleep(0.5)
        f = open(path2, "r", encoding='utf-8')
        s = f.read()
        f.close()


    show(s, True)
    pyperclip.copy(s)
