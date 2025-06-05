# カレントディレクトリの全ての.webpを.pngに変換する

Get-ChildItem *.webp | ForEach-Object {
  magick $_.Name ($_.BaseName + ".png")
}
