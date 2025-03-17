# 和暦と西暦の変換

Python で和暦（例えば「令和5年」）と西暦（例えば「2023年」）を相互に変換するプログラムを作るには、以下の方法があります。

### 方法
1. 和暦の各元号と対応する西暦の開始年を辞書で定義する。
2. 文字列の解析を行い、和暦から西暦へ変換する。
3. 逆に、西暦から和暦へ変換する。

---

### サンプルコード

```python
import re

# 和暦の元号と対応する西暦の開始年
WAREKI_TO_SEIREKI = {
    "令和": 2019,
    "平成": 1989,
    "昭和": 1926,
    "大正": 1912,
    "明治": 1868,
}

def wareki_to_seireki(wareki: str) -> int:
    """和暦（例: '令和5年'）を西暦に変換"""
    match = re.match(r"(令和|平成|昭和|大正|明治)(\d+)年", wareki)
    if match:
        era, year = match.groups()
        return WAREKI_TO_SEIREKI[era] + int(year) - 1
    else:
        raise ValueError("正しい和暦の形式で入力してください（例: '令和5年'）")

def seireki_to_wareki(seireki: int) -> str:
    """西暦を和暦に変換（例: 2023 → '令和5年'）"""
    for era, start in WAREKI_TO_SEIREKI.items():
        if seireki >= start:
            year = seireki - start + 1
            return f"{era}{year}年"
    raise ValueError("明治以前の年には対応していません")

# 使用例
print(wareki_to_seireki("令和5年"))  # 2023
print(seireki_to_wareki(2023))       # 令和5年
print(wareki_to_seireki("平成30年")) # 2018
print(seireki_to_wareki(1989))       # 平成1年
```

---

### 説明
1. **和暦 → 西暦**
   - `re.match()` を使って「元号 + 数字 + '年'」の形式を解析。
   - 辞書 `WAREKI_TO_SEIREKI` から元号の開始年を取得し、`(開始年 + 和暦の年数 - 1)` で西暦を計算。

2. **西暦 → 和暦**
   - `WAREKI_TO_SEIREKI` を新しい元号から順に調べて、該当する元号を見つける。
   - `(西暦 - 開始年 + 1)` で和暦の年数を計算。

---

### 拡張
- `datetime` モジュールを使って `datetime.date.today().year` を取得し、現在の年を和暦で表示する機能を追加できる。
- `input()` を使って対話的に変換できるようにする。
- 「令和元年」などの特殊な表記に対応する。

もしカスタマイズしたい部分があれば教えてね！

---
---

# 対話型に
対話的に和暦と西暦を相互変換できるプログラムを作ってみたよ！  
ユーザーが入力した和暦または西暦を自動判別して変換するようにしている。

---

### **対話型プログラム**

```python
import re

# 和暦の元号と対応する西暦の開始年
WAREKI_TO_SEIREKI = {
    "令和": 2019,
    "平成": 1989,
    "昭和": 1926,
    "大正": 1912,
    "明治": 1868,
}

def wareki_to_seireki(wareki: str) -> int:
    """和暦（例: '令和5年'）を西暦に変換"""
    match = re.match(r"(令和|平成|昭和|大正|明治)(\d+)年?", wareki)
    if match:
        era, year = match.groups()
        return WAREKI_TO_SEIREKI[era] + int(year) - 1
    else:
        raise ValueError("正しい和暦の形式で入力してください（例: '令和5年'）")

def seireki_to_wareki(seireki: int) -> str:
    """西暦を和暦に変換（例: 2023 → '令和5年'）"""
    for era, start in WAREKI_TO_SEIREKI.items():
        if seireki >= start:
            year = seireki - start + 1
            return f"{era}{year}年"
    raise ValueError("明治以前の年には対応していません")

def main():
    print("和暦⇔西暦 変換プログラム")
    print("和暦（例: '令和5年'）または西暦（例: '2023'）を入力してください。'exit' で終了。")

    while True:
        user_input = input("\n変換する年を入力: ").strip()

        if user_input.lower() == "exit":
            print("プログラムを終了します。")
            break

        # 和暦のパターンに一致するか判定
        if re.match(r"^(令和|平成|昭和|大正|明治)\d+年?$", user_input):
            try:
                seireki = wareki_to_seireki(user_input)
                print(f"→ 西暦: {seireki}年")
            except ValueError as e:
                print(f"エラー: {e}")
        
        # 西暦のパターンに一致するか判定
        elif user_input.isdigit():
            try:
                seireki = int(user_input)
                wareki = seireki_to_wareki(seireki)
                print(f"→ 和暦: {wareki}")
            except ValueError as e:
                print(f"エラー: {e}")
        
        else:
            print("入力が正しくありません。もう一度入力してください。")

if __name__ == "__main__":
    main()
```

---

### **プログラムの動作**
- `令和5年` と入力すると `→ 西暦: 2023年` と変換。
- `2023` と入力すると `→ 和暦: 令和5年` と変換。
- `exit` と入力するとプログラム終了。

---

### **実行例**
```
和暦⇔西暦 変換プログラム
和暦（例: '令和5年'）または西暦（例: '2023'）を入力してください。'exit' で終了。

変換する年を入力: 令和5年
→ 西暦: 2023年

変換する年を入力: 2018
→ 和暦: 平成30年

変換する年を入力: 昭和50年
→ 西暦: 1975年

変換する年を入力: exit
プログラムを終了します。
```

---

### **ポイント**
1. **和暦 or 西暦の判定**
   - `re.match(r"^(令和|平成|昭和|大正|明治)\d+年?$", user_input)` で和暦の形式をチェック。
   - `user_input.isdigit()` で西暦の整数かどうかを判定。

2. **入力のバリデーション**
   - 間違った入力をすると「エラー」として表示。

3. **ループ処理**
   - `while True:` で無限ループし、`exit` を入力すると終了。

---

このプログラムをターミナルやコマンドプロンプトで実行すると、和暦・西暦を自由に変換できる！  
もっと機能を追加したい場合は、希望を教えてね！

---
---

# 最後の２行の意味は？
プログラムの最後にある以下の2行は、Python スクリプトの実行方法を制御するためのものだよ。  

```python
if __name__ == "__main__":
    main()
```

---

### **このコードの意味**
1. `__name__` は Python の特別な変数で、スクリプトが**直接実行された場合**は `"__main__"` になる。
2. `if __name__ == "__main__":` は「このスクリプトが直接実行されたときのみ `main()` を実行する」という意味。

---

### **なぜ必要？**
このスクリプトを**直接実行するとき**は `main()` を実行するが、**モジュールとして他のスクリプトからインポートされたとき**には `main()` を実行しないようにするため。

#### **① 直接実行した場合**
```sh
$ python wareki_converter.py
```
この場合、`__name__` は `"__main__"` なので `main()` が実行される。

#### **② モジュールとしてインポートされた場合**
```python
import wareki_converter  # このときは main() は実行されない
```
この場合、`__name__` は `"wareki_converter"` になるため、`main()` は実行されない。

---

### **まとめ**
- **スクリプトを直接実行するとき** `main()` を動かす。
- **他のファイルからインポートされたとき** `main()` を実行しないようにする。
- これにより、コードの再利用性が向上する。

この書き方は Python のスクリプトを書くときの基本だから、覚えておくと便利だよ！

---
---

# 他ファイルからインポートされた場合は、実行されない！
そう！ 他のファイルからインポートされたときは、関数や変数、クラスなどが**定義されるだけ**で、`main()` は実行されないんだ。  

---

### **具体的な動作を確認しよう**
例えば、今のプログラムを `wareki_converter.py` というファイルに保存して、別の Python スクリプトから使ってみる。

#### **① `wareki_converter.py`（モジュール側）**
```python
import re

WAREKI_TO_SEIREKI = {
    "令和": 2019, "平成": 1989, "昭和": 1926, "大正": 1912, "明治": 1868,
}

def wareki_to_seireki(wareki: str) -> int:
    match = re.match(r"(令和|平成|昭和|大正|明治)(\d+)年?", wareki)
    if match:
        era, year = match.groups()
        return WAREKI_TO_SEIREKI[era] + int(year) - 1
    else:
        raise ValueError("正しい和暦の形式で入力してください（例: '令和5年'）")

def seireki_to_wareki(seireki: int) -> str:
    for era, start in WAREKI_TO_SEIREKI.items():
        if seireki >= start:
            year = seireki - start + 1
            return f"{era}{year}年"
    raise ValueError("明治以前の年には対応していません")

def main():
    print("和暦⇔西暦 変換プログラム")
    print(wareki_to_seireki("令和5年"))  # 2023
    print(seireki_to_wareki(2023))       # 令和5年

if __name__ == "__main__":
    main()  # 直接実行された場合のみ動く
```

---

#### **② `test.py`（別のファイルでインポート）**
```python
import wareki_converter  # ここでは main() は実行されない

# 定義されている関数を使う
print(wareki_converter.wareki_to_seireki("平成30年"))  # 2018
print(wareki_converter.seireki_to_wareki(1989))        # 平成1年
```

---

#### **③ 実行結果**
```sh
$ python test.py
2018
平成1年
```
**`main()` の内容は実行されていない** ことがわかる！

---

### **まとめ**
- `import wareki_converter` すると、`wareki_to_seireki` や `seireki_to_wareki` の関数は**定義される**けど、`main()` は実行されない。
- `if __name__ == "__main__":` を入れることで、「このスクリプトが直接実行されたときだけ `main()` を動かす」という制御ができる。

つまり、**インポートされたときは、関数や変数だけが読み込まれ、処理（`main()`）は実行されない** ということだね！

---
---

Yes, exactly! When you import the script into another file, only the functions, classes, and variables are loaded. The `main()` function will not run automatically because it’s inside the check `if __name__ == "__main__":`. This is a common practice in Python, as it
