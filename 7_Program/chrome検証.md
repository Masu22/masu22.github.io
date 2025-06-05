# chromeで開ける画像の拡張子を調べる

その画像の\*\*本当の拡張子（ファイル形式）\*\*を調べる方法はいくつかあります。
Chromeで開けるということは、画像フォーマット自体はサポートされているもの（PNG, JPEG, WEBP, GIFなど）でしょう。

---

## ✅ 方法①：Chromeのデベロッパーツールで確認

1. Chromeでその画像を開く
2. 右クリック → **「検証」**（または `F12` キー）
3. 上部のタブで **「Network（ネットワーク）」** をクリック
4. ページをリロード（`F5`）して画像を再読み込み
5. Network内に表示されるその画像の行をクリック
6. **右側の「Headers（ヘッダー）」** → `Content-Type` を確認

### 例：

* `Content-Type: image/jpeg` → JPEG形式（.jpg）
* `Content-Type: image/png` → PNG形式（.png）
* `Content-Type: image/webp` → WebP形式（.webp）

---

## ✅ 方法②：ファイルの中身から判別（ファイルヘッダ解析）

画像ファイルには最初の数バイトに「マジックナンバー（シグネチャ）」という識別情報があります。

ターミナルやコマンドプロンプトで以下のように確認できます：

### 🔹 macOS / Linux：

```bash
file 画像ファイル名
```

例：

```bash
file unknown-image
# 出力: unknown-image: PNG image data ...
```

### 🔹 Windows（PowerShell）：

PowerShellには直接 `file` コマンドはないので、代わりに以下のようなスクリプトでバイナリの先頭を見ます。

```powershell
Get-Content .\画像ファイル名 -Encoding Byte -TotalCount 8
```

この結果を元に、以下のマジックナンバーを照合します：

| 形式   | 16進マジックナンバー（先頭バイト）                   |
| ---- | ------------------------------------ |
| PNG  | `89 50 4E 47 0D 0A 1A 0A`            |
| JPEG | `FF D8 FF`                           |
| GIF  | `47 49 46 38`                        |
| WebP | `52 49 46 46`（= "RIFF"） + 中間に `WEBP` |

---

## ✅ 方法③：画像ビューワやアプリを使う

* **IrfanView**（Windows）
* **XnView**
* **ExifTool**（詳細情報含む）

---

## ✅ 方法④：オンラインサービス

下記のようなサイトにファイルをアップロードして調べることも可能です：

* [https://checkfiletype.com/](https://checkfiletype.com/)
* [https://www.get-metadata.com/](https://www.get-metadata.com/)

> ⚠️ センシティブな画像はアップロード前にプライバシーに注意してください。

---

必要であれば、画像ファイルをアップロードしていただければ、こちらでも解析可能です！
