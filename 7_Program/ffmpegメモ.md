# ffmpegバージョンの確認
``` sh
ffmpeg -version
```
<br>

---
<br>

# mp4の動画と映像を一つに！
``` sh
ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac -strict experimental output.mp4
```
<br>

-c:v copy  
動画を再エンコードせずにコピー  

-c:a aac -strict experimental  
音声をAACに変換  
<br>

---
<br>

# powershellで、フォルダの中の動画(mp4)と音声(mp4形式)が１組だけのとき、探して一体化させる！
``` powershell
# 動画ファイルと音声ファイルを探す
$video_file = $null
$audio_file = $null

# カレントディレクトリ内の mp4 ファイルを取得
$files = Get-ChildItem -Filter "*.mp4"

foreach ($file in $files) {
    if ($file.Name -match "-") {
        $audio_file = $file.Name
    } else {
        $video_file = $file.Name
    }
}

# 両方のファイルが見つかった場合、ffmpeg を実行
if ($video_file -and $audio_file) {
    $output_file = "output.mp4"
    Write-Host "動画: $video_file"
    Write-Host "音声: $audio_file"
    
    ffmpeg -i "$video_file" -i "$audio_file" -c:v copy -c:a aac -strict experimental "$output_file"

    Write-Host "Output file created: $output_file"
} else {
    Write-Host "動画ファイルまたは音声ファイルが見つかりません。"
}
```
<br>

---
---
<br>

# ffmpegでmp4の動画の再生時間を調べる

`ffmpeg` または `ffprobe` を使うと、MP4動画の\*\*再生時間（duration）\*\*を簡単に調べることができます。

---

### ✅ 方法1：`ffprobe` を使う（おすすめ）

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 input_video.mp4
```

#### 出力例：

```
123.456000
```

（単位は**秒**です。上の例だと 123.456 秒 ≒ 2分3秒）

---

### ✅ 方法2：`ffmpeg` で情報を見る（`ffprobe`がない場合）

```bash
ffmpeg -i input_video.mp4
```

#### 出力例（一部）：

```
Duration: 00:02:03.45, start: 0.000000, bitrate: 543 kb/s
```

このように `Duration: 00:02:03.45` という情報が表示されます。

> ⚠️ 注意：この方法だと情報は\*\*標準エラー出力（stderr）\*\*に出るので、スクリプトで処理するには少し面倒です。正確に取得したい場合は `ffprobe` を使うのがベストです。

---

### おまけ：人間に読みやすい形式で `ffprobe` を使いたい場合

```bash
ffprobe -i input_video.mp4 -show_format -v quiet | grep duration
```

---

必要に応じて、これをシェルスクリプトで使って処理を自動化することもできます。興味があればお手伝いしますよ！

---
---

<br>

# ffmpegで、mp4から画像フレームを抽出

`ffmpeg`を使って動画から特定の間隔で画像のフレームを取り出す方法を説明します。例えば、1秒おきにフレームを取り出す場合、次のコマンドを使用します。

### コマンド例（1秒おきに画像を抽出）

```bash
ffmpeg -i input_video.mp4 -vf "fps=1" output_frame_%04d.png
```

### コマンドの説明：

* `-i input_video.mp4` ： 動画ファイルの入力を指定します（ここでは `input_video.mp4`）。
* `-vf "fps=1"` ： フィルターオプションで、1秒おきにフレームを抽出します。`fps=1` は1秒あたり1フレームを意味します。
* `output_frame_%04d.png` ： 出力ファイル名のパターン。`%04d` はフレーム番号を4桁の数字で付けるフォーマットです。例えば、`output_frame_0001.png`、`output_frame_0002.png` といった具合です。

### 例: 2秒おきに画像を抽出したい場合

```bash
ffmpeg -i input_video.mp4 -vf "fps=0.5" output_frame_%04d.png
```

ここで `fps=0.5` は、0.5フレーム/秒、つまり2秒おきにフレームを抽出します。

#### その他のオプション：

* `-t` オプションで、抽出する時間範囲を指定することもできます。

  * 例: 最初の30秒間だけフレームを抽出する場合

    ```bash
    ffmpeg -i input_video.mp4 -t 30 -vf "fps=1" output_frame_%04d.png
    ```


---
---

<br>