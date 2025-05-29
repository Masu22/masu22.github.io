# tcolorboxのマニュアル
## https://texdoc.org/serve/tcolorbox.pdf/0

# texのインストール場所

TeX Live 2024 がインストールされているか探す方法は、使っているOSごとに以下の通りです。

---

## Windowsの場合

1. **コマンドプロンプトを開く**
   スタートメニューから「cmd」などで検索して起動。

2. **pdflatexの場所を調べる**

   ```
   where pdflatex
   ```

   これで pdflatex.exe のフルパスが出ます。例：

   ```
   C:\texlive\2024\bin\win32\pdflatex.exe
   ```

   と出れば、2024年版のTeX Liveが使われていることがわかります。

3. **環境変数PATHに入っているフォルダを確認**
   コマンドプロンプトで

   ```
   echo %PATH%
   ```

   と入力して、TeX Liveのbinディレクトリが2024年版かどうか確認。

---

## macOSの場合

1. **ターミナルを開く**

2. **pdflatexのパスを調べる**

   ```
   which pdflatex
   ```

   例）

   ```
   /usr/local/texlive/2024/bin/universal-darwin/pdflatex
   ```

   のように2024年版のパスが出ます。

3. **システムのPATH確認**

   ```
   echo $PATH
   ```

   でTeX Liveのbinディレクトリの場所を確認。

---

## Linuxの場合

1. **ターミナルを開く**

2. **pdflatexのパスを調べる**

   ```
   which pdflatex
   ```

   例）

   ```
   /usr/local/texlive/2024/bin/x86_64-linux/pdflatex
   ```

   のように出ます。

3. **PATH変数を確認**

   ```
   echo $PATH
   ```

---

## まとめ

* **pdflatexの場所を調べてみるのが一番早い**
* 出てきたパスに「2024」が含まれていればTeX Live 2024がインストール済みかつ環境変数に登録されています
* パスに見当たらない場合は、TeX Live 2024はインストールされていても環境変数に追加されていない可能性あり

---

もし場所が分かったら、実際にTeXのアップデートやコンパイルで使うバージョンを切り替える方法もお教えしますね。何かあれば教えてください！

---
---

# Lualatexのタイプセットを更新

はい、TeXworksでLuaLaTeXを2024年版のものに切り替えるには、**LuaLaTeX実行ファイルのパスを2024年版のものに設定し直す**のがポイントです。手順をわかりやすく説明しますね。

---

# TeXworksでLuaLaTeXをTeX Live 2024に切り替える手順

---

## 1. TeX Live 2024 の LuaLaTeX 実行ファイルのパスを確認する

まず、2024年版のLuaLaTeXがどこにあるかを調べます。

* Windows ならコマンドプロンプトで：

```cmd
where lualatex
```

* macOS/Linux ならターミナルで：

```bash
which lualatex
```

例えば、

```
C:\texlive\2024\bin\win32\lualatex.exe
```

や

```
/usr/local/texlive/2024/bin/x86_64-linux/lualatex
```

のようにパスが分かります。

---

## 2. TeXworksを開く

---

## 3. LuaLaTeX の設定を編集する

* メニューバーの **\[編集] > \[設定]** を開く
* 左側のタブで **「タイプセット」** を選択

---

## 4. LuaLaTeX の実行コマンドを修正する

* 「タイプセット」タブの「処理系」（Tools）一覧から「LuaLaTeX」を選ぶ
* 「プログラム」欄に LuaLaTeX の実行ファイルパスをフルパスで指定します

例：

* Windows の場合

  ```
  C:/texlive/2024/bin/win32/lualatex.exe
  ```
* macOS/Linux の場合

  ```
  /usr/local/texlive/2024/bin/x86_64-linux/lualatex
  ```

（TeXworksはパスの区切りにスラッシュ `/` が使えます）

---

## 5. 変更を保存して閉じる

---

## 6. LuaLaTeX を実行して動作確認

* TeXworksでLuaLaTeXを選択してタイプセット（ビルド）し、ちゃんとコンパイルされるか確認しましょう。
* バージョン確認もできます。ソースファイルに

```latex
\message{LuaLaTeX version: \pdftexbanner}
```

や、

```latex
\typeout{LuaLaTeX version: \directlua{tex.print(status.luatex_version)}}
```

を入れてログで確認してもOKです。

---

## 【補足】PATHを切り替える方法（環境変数を変える場合）

もしTeXworksのパスをいじらずに全体のLuaLaTeXを切り替えたい場合は、OSの環境変数`PATH`で先頭にTeX Live 2024のbinディレクトリを入れる方法もあります。ただしこちらはOSの設定変更が必要でやや上級者向けです。

---

## まとめ

| 手順 | 内容                                  |
| -- | ----------------------------------- |
| 1  | TeX Live 2024 の lualatex のフルパスを確認する |
| 2  | TeXworks の「編集」→「設定」→「タイプセット」を開く     |
| 3  | 「LuaLaTeX」のプログラム欄を2024年版のパスに書き換える   |
| 4  | 保存して閉じる                             |
| 5  | LuaLaTeXでコンパイルして動作確認                |

---

わからない点があれば遠慮なくどうぞ！

---
---
