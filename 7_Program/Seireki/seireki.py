# 西暦か和暦を入力すると、他の一方に変換する！

import re

# 和暦の元号と対応する西暦の開始年
WAREKI_TO_SEIREKI = {
    "令和": 2019,
    "平成": 1989,
    "昭和": 1926,
    "大正": 1912,
    "明治": 1868,
}

def wareki_to_seireki(wareki: str) -> int:
    """和暦（例: '令和5年'）を西暦に変換"""
    match = re.match(r"(令和|平成|昭和|大正|明治)(\d+)年?", wareki)
    if match:
        era, year = match.groups()
        return WAREKI_TO_SEIREKI[era] + int(year) - 1
    else:
        raise ValueError("正しい和暦の形式で入力してください（例: '令和5年'）")

def seireki_to_wareki(seireki: int) -> str:
    """西暦を和暦に変換（例: 2023 → '令和5年'）"""
    for era, start in WAREKI_TO_SEIREKI.items():
        if seireki >= start:
            year = seireki - start + 1
            return f"{era}{year}年"
    raise ValueError("明治以前の年には対応していません")

def main():
    print("和暦⇔西暦 変換プログラム")
    print("和暦（例: '令和5年'）または西暦（例: '2023'）を入力してください。'exit' で終了。")

    while True:
        user_input = input("\n変換する年を入力: ").strip()

        if user_input.lower() == "exit":
            print("プログラムを終了します。")
            break

        # 和暦のパターンに一致するか判定
        if re.match(r"^(令和|平成|昭和|大正|明治)\d+年?$", user_input):
            try:
                seireki = wareki_to_seireki(user_input)
                print(f"→ 西暦: {seireki}年")
            except ValueError as e:
                print(f"エラー: {e}")
        
        # 西暦のパターンに一致するか判定
        elif user_input.isdigit():
            try:
                seireki = int(user_input)
                wareki = seireki_to_wareki(seireki)
                print(f"→ 和暦: {wareki}")
            except ValueError as e:
                print(f"エラー: {e}")
        
        else:
            print("入力が正しくありません。もう一度入力してください。")

# 直接読み込まれたときのみ実行する！！他からインポートされると、関数を読み込むのみ！
if __name__ == "__main__":
    main()
