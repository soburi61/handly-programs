"""
Created on Sun Jun  4 00:29:54 2023
coding: utf-8
import all files modules
"""
import os

# カレントディレクトリ内の全てのファイルを取得します
file_list = os.listdir()

# Pythonファイルの拡張子(.py)を持つファイルのみを抽出します
python_files = [file for file in file_list if file.endswith('.py')]

# 各Pythonファイルから要素をワイルドカードでインポートします
for file in python_files:
    module_name = os.path.splitext(file)[0]  # 拡張子(.py)を除いたモジュール名を取得します
    try:
        module = __import__(module_name)
        globals().update(vars(module))
    except ImportError:
        print(f"Failed to import module: {module_name}")

