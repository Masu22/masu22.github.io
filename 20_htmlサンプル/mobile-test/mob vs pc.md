# 1つのディレクトリで、pcとスマホ版サイトを振り分け

GitHub Pages で **PC版とスマホ版のサイトをサブディレクトリで分ける方法** を、 **リポジトリの作成から公開まで** 丁寧に説明するね！  

---

## **手順 ① GitHub にリポジトリを作成**
1. [GitHub](https://github.com/) にアクセスしてログイン。  
2. **新しいリポジトリを作成** （例: `my-website`）。  
   - **Public（公開）** にする（GitHub Pages は無料プランでは Public のみ対応）。  
   - `README.md` のチェックは任意（あとで追加可能）。  
3. 作成後、リポジトリのページに移動。  

---

## **手順 ② PC版・スマホ版のファイルを用意**
ローカル環境で、以下のようなフォルダ構成を作る。  

```
/my-website
  ├── /pc/index.html  （PC版のトップページ）
  ├── /mobile/index.html  （スマホ版のトップページ）
  ├── /css/style.css  （共通のCSSファイル）
  ├── /js/script.js  （共通のJavaScriptファイル）
  ├── /images/  （画像フォルダ）
```

### **PC版の `index.html`**
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>PC版サイト</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h1>これはPC版のページです</h1>
    <p>PC用のデザインを適用。</p>
</body>
</html>
```

### **スマホ版の `index.html`**
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>スマホ版サイト</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <h1>これはスマホ版のページです</h1>
    <p>スマホ用のデザインを適用。</p>
</body>
</html>
```

### **共通の `css/style.css`**
```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 50px;
}
```

---

## **手順 ③ GitHub にアップロード**
### **方法 1: GitHub 上で直接アップロード**
1. GitHub のリポジトリページに移動。  
2. `Add file` → `Upload files` を選択。  
3. `pc/`、`mobile/`、`css/` フォルダごとアップロード。  
4. `Commit changes` で変更を確定。  

### **方法 2: Git コマンドを使う（推奨）**
ローカルに Git をインストール済みなら、以下の手順でアップロード。  

1. **リポジトリをクローン**
```bash
git clone https://github.com/あなたのユーザー名/my-website.git
cd my-website
```

2. **作成したファイルを追加**
```bash
git add .
git commit -m "PC版とスマホ版のサイトを追加"
```

3. **GitHub にプッシュ**
```bash
git push origin main
```

---

## **手順 ④ GitHub Pages で公開**
1. GitHub のリポジトリページに移動。  
2. `Settings` → `Pages` を開く。  
3. **「Branch: `main`」を選択し、「/（root）」を指定** → `Save` をクリック。  
4. しばらくすると、**サイトが公開される！**  

### **アクセスURL**
- **PC版**: `https://あなたのGitHubユーザー名.github.io/my-website/pc/`  
- **スマホ版**: `https://あなたのGitHubユーザー名.github.io/my-website/mobile/`  

---

## **手順 ⑤ 自動で振り分ける（オプション）**
もし **「1つのURLでPC/スマホを自動判別したい」** 場合は、トップページ（`index.html`）を作成し、JavaScript でリダイレクトする。

### **ルート (`index.html`)**
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>自動振り分けページ</title>
    <script>
        if (window.innerWidth <= 768) {
            window.location.href = "/my-website/mobile/";
        } else {
            window.location.href = "/my-website/pc/";
        }
    </script>
</head>
<body>
    <p>自動でPC版またはスマホ版にリダイレクトされます。</p>
</body>
</html>
```
これで、アクセス時に **スマホなら `mobile/`、PCなら `pc/` に自動で移動** する！

---

## **まとめ**
✅ **PC版とスマホ版を `/pc/` `/mobile/` に分ける**  
✅ **GitHub Pages を設定し、それぞれのURLでアクセス可能にする**  
✅ **トップページでリダイレクトすれば自動振り分けも可能**  

この方法なら、簡単に PC / スマホ版を分けて公開できるよ！