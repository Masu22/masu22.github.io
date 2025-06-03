# ImageMagickの使い方
<br>

---
---

# インストールと確認
ImageMagick のインストールとバージョン確認方法は、使用している OS によって異なります。以下に各プラットフォームごとの手順をまとめます。

---

## 🐧 Linux (Ubuntu/Debian など)

### 🔧 インストール

```bash
sudo apt update
sudo apt install imagemagick
```

### 🔍 バージョン確認

```bash
convert -version
# または
magick -version
```

---

## 🍏 macOS

### 🔧 インストール（Homebrew 使用）

```bash
brew install imagemagick
```

### 🔍 バージョン確認

```bash
magick -version
# または
convert -version
```

※ `convert` コマンドは macOS に元々ある別のツールと衝突する場合があるため、`magick` の使用がおすすめです。

---

## 🪟 Windows

### 🔧 インストール手順

1. 公式サイトからインストーラーをダウンロード：[https://imagemagick.org/script/download.php](https://imagemagick.org/script/download.php)
2. Windows 用バイナリを選び、インストール中に「Add to PATH」オプションを有効にする

### 🔍 バージョン確認（コマンドプロンプトまたは PowerShell）

```powershell
magick -version
```

---

## ✅ 出力例（ImageMagick 7 の場合）

```text
Version: ImageMagick 7.1.1-32 Q16-HDRI x86_64  https://imagemagick.org
Copyright: © 1999-2025 ImageMagick Studio LLC
License: https://imagemagick.org/script/license.php
Features: Cipher DPC HDRI Modules OpenMP(4.5)
Delegates (built-in): bzlib cairo fontconfig freetype heic jng jp2 jpeg lcms lqr lzma openexr pangocairo png ps raw tiff webp xml zlib
```

---

問題があれば、実行結果を見せてくれたらサポートします！
<br>

---
---

# webpをjpgに変換する
``` powershell
convert input.webp output.jpg
```
<br>

---
---

# カレントフォルダにある.webpをすべてpngに変換する

ImageMagick を使って、特定のフォルダ内にある `.webp` 形式の画像ファイルをすべて `.png` に変換するには、以下のようなコマンドを使います。

---

### ✅ 1. 前提条件

* ImageMagick がインストールされていること（`convert` または `magick` コマンドが使える）
* ターミナル（macOS/Linux）または PowerShell（Windows）で実行

---

### 🖥️ 2. Linux/macOS の場合

```bash
mkdir -p output_pngs  # 出力用フォルダ（任意）
for file in *.webp; do
    convert "$file" "output_pngs/${file%.webp}.png"
done
```

または ImageMagick 7 以降なら：

```bash
mkdir -p output_pngs
for file in *.webp; do
    magick "$file" "output_pngs/${file%.webp}.png"
done
```

---

### 🪟 3. Windows PowerShell の場合

```powershell
New-Item -ItemType Directory -Path .\output_pngs -Force
Get-ChildItem -Filter *.webp | ForEach-Object {
    magick $_.FullName ("output_pngs\" + ($_.BaseName + ".png"))
}
```

---

### 📌 補足

* `output_pngs` フォルダは出力用です。上書きしたくない場合に使ってください。
* `.webp` がサブフォルダにある場合は、再帰的に処理するようなスクリプトに変更できます。

---

必要であれば、サブフォルダ対応バージョンも作成します。お使いの OS を教えてもらえると、もっと正確に案内できます！

---
---
