; Kindle用 自動保存スクリプト：右キーを押したら自動でスクリーンショット保存
; 右キーを押したときに動作（必要ならPageDownにも対応可能）

$Right::
    FormatTime, timestamp,, yyyyMMdd_HHmmss
    FilePath := "C:\Users\NARUTO\Downloads\Kindle\kindle_" . timestamp . ".png"

    ; スクリーンショット取得
    Send, {PrintScreen}
    Sleep, 300

    ; ペイントで保存（シンプルな方法）
    Run, mspaint
    WinWaitActive, 無題 - ペイント
    Send, ^v
    Sleep, 300
    Send, ^s
    Sleep, 300
    SendInput, %FilePath%
    Send, {Enter}
    Sleep, 300
    Send, ^w  ; 閉じる

    ; 最後にキーを送信してページを進める（元のRightキーを送る）
    Send, {Right}
return
