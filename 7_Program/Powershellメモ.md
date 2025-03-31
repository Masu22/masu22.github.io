# フォルダ内のテキストを全て、結合して出力
``` powershell
Get-Content *.txt | Set-Content combined.txt
```
---
---
<br>
<br>

# 重複行をなくして、アルファベット順にして出力！
```powershell
get-content xyz.txt | Sort-object -unique >> out.txt
```
<br>

💡 **応用編！**  
もし **大文字・小文字を区別せず** 重複を省きたい場合は、
```powershell
get-content xyz.txt | Sort-Object -Unique -CaseInsensitive >> out.txt
```

他にも、
```powershell
get-content xyz.txt | Sort-Object Length -Unique >> out.txt
```
なら **文字数順** でソートもできます。


---
---
<br>
<br>

# テキスト結合＋ソートして出力

PowerShellを使って複数のテキストファイルを結合し、さらにソートする方法を紹介します。  

### 手順：
1. **複数のテキストファイルを結合**
2. **内容をソート**
3. **結果を新しいファイルに保存**

---

## **方法 1：基本的な方法（シンプルなソート）**
```powershell
Get-Content *.txt | Sort-Object | Set-Content merged_sorted.txt
```
- `Get-Content *.txt` → カレントディレクトリ内のすべての`.txt`ファイルを取得
- `Sort-Object` → 内容をソート
- `Set-Content merged_sorted.txt` → `merged_sorted.txt` に保存

---

## **方法 2：重複を削除してソート**
```powershell
Get-Content *.txt | Sort-Object -Unique | Set-Content merged_sorted_unique.txt
```
- `-Unique` オプションを使うと、**重複行を削除** できます。

---

## **方法 3：ソート基準を指定（昇順・降順）**
```powershell
Get-Content *.txt | Sort-Object { $_ } -Descending | Set-Content merged_sorted_desc.txt
```
- `-Descending` を指定すると **降順** でソート

---

## **方法 4：数値データを正しくソート**
文字列ではなく、**数値の大小で正しく並べる** 場合：
```powershell
Get-Content *.txt | Sort-Object {[int]$_} | Set-Content merged_sorted_numbers.txt
```
- `[int]$_` を指定すると、数値としてソート

---

## **補足**
- `Get-Content` はすべてのテキストファイルを **行単位** で取得する。
- ファイルが大量にある場合、`Add-Content` を使うと効率的。

**大量のファイルを処理する場合**
```powershell
$files = Get-ChildItem -Filter "*.txt"
$files | ForEach-Object { Get-Content $_ } | Sort-Object | Set-Content merged_sorted.txt
```

この方法で、すべてのファイルの内容を結合し、ソートして保存できます！

---
---
<br>
<br>

# アドレス一覧を読み込み、アドレスの末尾を出力
PowerShellで、アドレス一覧が書かれているテキストファイルを読み込み、各アドレスの末尾部分（ドメインや特定の部分）を抽出し、新しいファイルに書き出すスクリプトを作成します。

### 例:
#### `input.txt`（入力ファイル）
```
user1@example.com
user2@test.org
user3@sample.net
```
#### `output.txt`（出力ファイル）
```
example.com
test.org
sample.net
```

---

### PowerShell スクリプト:
```powershell
# 入力ファイルと出力ファイルの指定
$inputFile = "input.txt"
$outputFile = "output.txt"

# ファイルを読み込み、アドレスの末尾を抽出
$domains = Get-Content $inputFile | ForEach-Object {
    ($_ -split "/")[-1]  # @で分割し、末尾（ドメイン）を取得
}

# 抽出したデータを新しいファイルに書き出し
$domains | Set-Content $outputFile

Write-Output "処理が完了しました。出力ファイル: $outputFile"
```

---

### スクリプトの説明:
1. `Get-Content $inputFile` で `input.txt` を読み込む。
2. `ForEach-Object` で各行を処理し、`-split "@"` で `@` の後ろ（末尾部分）を取得。
3. `Set-Content` で `output.txt` に書き出す。
4. `Write-Output` で完了メッセージを表示。

**このスクリプトをPowerShellで実行すれば、アドレスの末尾（ドメイン部分）のみが `output.txt` に保存されます！**

---
---
<br>
<br>

# 末尾がハイフンで終わる行を取得

PowerShell で `-`（ハイフン）で終わる行を検索するには、正規表現を使うと便利です。以下のコマンドを試してみてください。

### 例: `Select-String` を使う
```powershell
Get-Content "ファイル名.txt" | Select-String -Pattern '-$'
```
このコマンドの意味:
- `Get-Content "ファイル名.txt"`: 指定したファイルの内容を取得
- `Select-String -Pattern '-$'`: `-` で終わる (`-$`) 行を検索

### 例: `Where-Object` を使う
```powershell
Get-Content "ファイル名.txt" | Where-Object { $_ -match '-$' }
```
この方法でも同じように `-` で終わる行を取得できます。

どちらでもOKですが、`Select-String` の方が検索専用なのでシンプルに書けます。

---
---
<br>
<br>

