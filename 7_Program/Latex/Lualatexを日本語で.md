# Lualatexで日本語を使う方法

LuaLaTeXで日本語を使うには、主に以下のポイントを押さえる必要があります。

---

## 1. 日本語フォント設定には `luatexja` パッケージを使う

LuaLaTeXは元々英語向けなので、日本語組版には専用のパッケージが必要です。
代表的なのは `luatexja` パッケージです。

```latex
\usepackage{luatexja}
```

---

## 2. フォントは `fontspec` で指定する

LuaLaTeXはUnicode対応なので、好きな日本語フォントを直接指定できます。

```latex
\usepackage{fontspec}
\setmainfont{IPAexMincho} % 好きな日本語フォント名に変える
```

---

## 3. 簡単な日本語のサンプル

```latex
\documentclass{article}
\usepackage{luatexja}       % 日本語処理用
\usepackage{fontspec}       % フォント設定用

\setmainfont{IPAexMincho}   % ここで日本語フォント指定（要インストール済み）

\begin{document}

こんにちは、LuaLaTeXで日本語を使っています。

\end{document}
```

---

## 4. 日本語フォントが無い場合は

* Windowsなら「MS 明朝」や「Yu Gothic」などを指定可能
* Macなら「Hiragino Mincho Pro」など
* LinuxならIPAフォント（IPAex明朝・ゴシック）などをインストール推奨

---

## 5. 注意点

* LuaLaTeXはTeX LiveやMiKTeXで標準サポートされている（2015年以降のバージョン推奨）
* 古いTeX環境だと`luatexja`の挙動が変な場合があるので、最新環境を使うのがおすすめ

---

もし具体的な環境（Windows/Mac/Linux）やフォントの設定例が欲しかったら教えてね！
