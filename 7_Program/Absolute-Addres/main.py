# 先頭に付けるアドレス
prefix = "/home/user/"

# 入力・出力ファイル
input_file = "input.txt"
output_file = "output.txt"

# ファイルを読み込んで変換
with open(input_file, "r", encoding="utf-8") as infile:
    lines = [prefix + line.strip() for line in infile if line.strip()]  # 空行を除去し、前にアドレスを付加

# ソート
lines.sort()

# 結果をファイルに書き込む
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("\n".join(lines) + "\n")  # 改行を入れて書き込み

print("変換 & ソート完了！出力ファイル:", output_file)
