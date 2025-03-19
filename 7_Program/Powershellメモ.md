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
