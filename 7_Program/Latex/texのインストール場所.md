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
