# インストール説明サイト
## https://www.python.jp/install/anaconda/windows/install.html

---

# インストールの確認

いいですね！Anaconda が正しくインストールされたかどうかを確認する方法を、OS別（Windows / macOS / Linux）にわかりやすくご案内します。

---

## ✅ Anacondaインストール確認方法（共通編）

まずターミナル（または Anaconda Prompt）を開いて、以下のコマンドを入力してみてください：

```bash
conda --version
```

🔍 出力例（バージョン番号が出ればOK）：

```
conda 24.1.2
```

→ 上記のように「conda ○○」と表示されれば、Anaconda（の中核である conda）が正しくインストールされています！

---

## 🪟 Windows の場合

1.「スタートメニュー」を開いて
 「Anaconda Navigator」や「Anaconda Prompt」があるかを確認
2.「Anaconda Prompt」を開いて、次のコマンドを入力：

```bash
conda info
```

出力例（一部）：

```
active environment : base
base environment : C:\Users\yourname\anaconda3
...
```

✅ このように「base environment」などが表示されれば OK！

---

## 🍎 macOS / Linux の場合

ターミナルを開いて次のように確認します：

```bash
which conda
```

出力例：

```
/Users/yourname/anaconda3/bin/conda
```

✅ これが表示されればインストール済みです！

補足：もし「command not found」と出た場合は、インストールに失敗しているか、PATH（環境変数）が通っていない可能性があります。

---

## ✅ さらに試す：Jupyter Notebookが使えるか

Jupyter Notebook を起動できるか試すのも、Anaconda確認の定番です：

```bash
jupyter notebook
```

ブラウザが開いて、Jupyterの画面（ファイル一覧）が表示されれば完璧！

---

## ✨ おまけ：Anaconda Navigatorで確認

GUI（画面操作）で確認したい場合は：

1. Anaconda Navigator を起動（スタートメニューやLaunchpadから）
2. 画面が開き、「Jupyter Notebook」や「VS Code」などのアイコンが見える

→ これでも「ちゃんと入ってる」と確認できます！

---

ご不明な点があれば、コマンドの出力を教えていただければ診断できます！どこまで試されましたか？😊

---
---
