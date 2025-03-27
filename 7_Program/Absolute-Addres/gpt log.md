# 相対アドレスに、先頭アドレスを付けて、絶対アドレスをつくる！

Pythonで相対アドレスのリストがある`input.txt`を読み込み、指定した先頭のアドレス（例えば`/home/user/`）を追加して、新しいテキストファイルに保存するスクリプトを作成できます。  

### 例:  
`input.txt`（元のファイル）:
```
docs/report.pdf
images/photo.jpg
music/song.mp3
```
  
追加する先頭アドレス: `/home/user/`  

`output.txt`（出力ファイル）:
```
/home/user/docs/report.pdf
/home/user/images/photo.jpg
/home/user/music/song.mp3
```

---

### Pythonスクリプト:
```python
# 先頭に付けるアドレス（ここを好きなものに変更）
prefix = "/home/user/"

# 入力ファイルと出力ファイル
input_file = "input.txt"
output_file = "output.txt"

# ファイルを読み込んで変換
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        # 空行を無視し、先頭のアドレスを追加
        new_line = prefix + line.strip() + "\n"
        outfile.write(new_line)

print("変換完了！出力ファイル:", output_file)
```

このスクリプトを実行すれば、`input.txt`の各行の前に`/home/user/`を追加し、新しいファイル`output.txt`に書き込むことができます！ 🚀

---
---

# ソートも行うバージョン

相対アドレス一覧を処理し、指定した先頭アドレスを追加した後にソートして出力するPythonスクリプトを作成しました！  

---

### 例:  
**`input.txt`（元のファイル）**
```
images/photo.jpg
docs/report.pdf
music/song.mp3
```

追加する先頭アドレス: `/home/user/`  

**`output.txt`（ソート後の出力ファイル）**
```
/home/user/docs/report.pdf
/home/user/images/photo.jpg
/home/user/music/song.mp3
```

---

### ソート機能付きPythonスクリプト
```python
# 先頭に付けるアドレス
prefix = "/home/user/"

# 入力・出力ファイル
input_file = "input.txt"
output_file = "output.txt"

# ファイルを読み込んで変換
with open(input_file, "r", encoding="utf-8") as infile:
    lines = [prefix + line.strip() for line in infile if line.strip()]  # 空行を除去し、前にアドレスを付加

# ソート
lines.sort()

# 結果をファイルに書き込む
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("\n".join(lines) + "\n")  # 改行を入れて書き込み

print("変換 & ソート完了！出力ファイル:", output_file)
```

これを実行すれば、各行に`/home/user/`を付け加えた後、辞書順でソートしたものを`output.txt`に出力できます！ 🚀

---
---
