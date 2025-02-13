# VscodeとGitHubの連携について
## 参考になるサイト:  
- https://zenn.dev/ojk/books/github-vscode/viewer/vscode-git  
- このアカウントのchat gpt  

# ローカルリポジトリを作成  
### **1. ローカルリポジトリにしたいフォルダを作成する**
### **2. Gitリポジトリを初期化**  
   ```bash
   git init
   ```
   → `.git/` という隠しフォルダが作成され、Gitリポジトリになります。  

### **3. 既存のリポジトリをコピーしたい場合はcloneする**  
```bash
git clone https://github.com/your-username/your-repo.git
```

### **4. 次の手順で、アカウントやリモートリポジトリを設定する。**  

---
---

# アカウントを変更(別のアカウントのリポジトリと連携する場合)  

もともとあった古い情報を削除して、認証し直す必要あり。それから、リモートリポジトリのurlを再設定する！　　

---

## **1. 現在のユーザー情報を確認**
まず、現在設定されているGitのユーザー情報を確認しましょう。

```bash
git config --global user.name
git config --global user.email
```

もし古いユーザー情報が表示されるなら、次の手順で修正します。

---

## **2. ユーザー名とメールアドレスを変更**
Gitのグローバル設定を新しいユーザー情報に変更します。

```bash
git config --global user.name "新しいGitHubのユーザー名"
git config --global user.email "新しいGitHubのメールアドレス"
```

設定が正しく変更されたか確認：
```bash
git config --global user.name
git config --global user.email
```

---

## **3. リポジトリごとにユーザーを変更**
特定のリポジトリだけ設定を変更したい場合は、リポジトリのディレクトリ内で以下を実行：

```bash
git config --local user.name "新しいユーザー名"
git config --local user.email "新しいメールアドレス"
```

ローカル設定を確認：
```bash
git config --local user.name
git config --local user.email
```

---

## **4. 認証情報をリセット**
古い認証情報が残っている場合、それを削除して新しいアカウントで再認証します。

### **Windowsの場合**
1. **「資格情報マネージャー」を開く**
2. **「Windows資格情報」タブを選択**
3. **「github.com」のエントリを削除**
4. **VSCodeを再起動し、`git push` を実行（新しいGitHubアカウントでログイン）**  
認証の仕方については、一番上に書いた、参考urlが手助けになる!!  

---

## **6. リモートURLを変更**
リモートURLが古いアカウントのものになっているなら、修正します。あたらしく作る場合は、新しいリモートリポジトリを設定する。

### **現在のリモートURLを確認**
```bash
git remote -v
```

### **HTTPSの場合**
```bash
git remote set-url origin https://github.com/new-user/repository.git
```

変更後、再度 `git remote -v` で正しいアカウントになっているか確認してください。

---

## **7. `git push` を再試行**
ユーザー情報と認証を修正したら、もう一度 `push` を試してみます。

```bash
git push origin main
```
---
---
# はじめてのプッシュをしてみる
## 1. **ファイルを追加**
   ```bash
   echo "# My Project" > README.md
   git add .
   ```
## 2. **コミットする**
   ```bash
   git commit -m "Initial commit"
   ```
## 3. **リモートにプッシュ（必要なら）**
   ```bash
   git push -u origin main
   ```


### **まとめ**
| やりたいこと | コマンド |
|-------------|---------|
| 空のリポジトリを作る | `git init` |
| 既存のリポジトリをコピー | `git clone [URL]` |
| 最初のコミット | `git add . && git commit -m "Initial commit"` |
| リモートを追加 | `git remote add origin [URL]` |

これで新しいローカルリポジトリを作成できます！ 🚀
