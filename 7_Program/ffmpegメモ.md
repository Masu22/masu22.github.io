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

