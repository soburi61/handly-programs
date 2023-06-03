def euclidean_algorithm(a, b):
    # aとbの大きさを比較して、aがbより小さい場合は入れ替える
    if a < b:
        a, b = b, a

    # ユークリッドの互除法の計算過程を表示
    print(f"{a} &= {a // b} \\times {b} + {a % b}\\\\")

    while b != 0:
        # aをbで割った商と余りを計算
        quotient = a // b
        remainder = a % b

        # ユークリッドの互除法の計算過程を表示
        print(f"{b} &= {a} - {quotient} \\times {b}\\\\")
        print(f"{a} &= {quotient} \\times {b} + {remainder}\\\\")

        # aにはbの値を、bには余りの値を代入
        a = b
        b = remainder

    # 最大公約数を返す
    return a

if __name__=='__main__':
    # テスト
    result = euclidean_algorithm(3251, 90830)
    print(f"\n最大公約数: {result}")
