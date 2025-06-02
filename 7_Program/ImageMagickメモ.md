# ImageMagickの使い方
<br>

---
---

# インストールの確認
``` powershell
convert -version
```
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
