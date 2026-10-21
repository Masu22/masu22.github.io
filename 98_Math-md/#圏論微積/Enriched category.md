# Enriched category 

## Weighted Kan拡張

以下は**圏論 (特に加群や任意の閉対称モノイダル圏 $\mathcal V$ に値を取る ｢$\mathcal V$-強化圏
(enriched categories)｣)**での定義を意識した説明です｡ 必要に応じて普通の (Set-値) 場合の対応も示
します｡
---
1) まず：重み付き (weighted) 極限・余極限 (colimit / limit) の直感と定義
**重み (weight)** とは､ 図 $T: \mathcal D \to \mathcal C$ に対して ｢どのように合成するか｣ を指定する
$\mathcal V$-函手
$W: \mathcal D^{\mathrm{op}} \to \mathcal V$
のことです｡
(普通のSet値の場合､ 重み $W$ は $\mathcal D^{\mathrm{op}} \to \mathbf{Set}$ になります｡)
重み付き余極限 (weighted colimit) $W \star T$ は､ 対象 $c\in\mathcal C$ に対して次の普遍同型で特徴付
けられるものです：
$$\mathcal C(W \star T,\, c) \cong [\mathcal D^{\mathrm{op}},\mathcal V]\bigl(W,\; \mathcal
C(T(-),c)\bigr)$$

ここで右辺は ｢重み $W$ と各ホム函手 $\mathcal C(T-,c)$ との $\mathcal V$-函手の間の射｣ の集合 (または
$\mathcal V$-対象) です｡

直感的には：$W$ が各点に重みを与え､ これを $T$ の値に対して合成して得る余極限が $W \star T$ です｡
普通の (Set-enriched) 場合､ 重み付き余極限は**共積分 (coend)**の形で表せます：

$$W \star T \cong \int^{d\in\mathcal D} W(d)\;\otimes\; T(d),$$

(ここで $\otimes$ は $\mathcal V$ におけるテンソル｡)

---

2) Weighted Kan 拡張 の定義 (左 Kan 拡張 を先に)

状況：$\mathcal V$-函手 $K:\mathcal A\to\mathcal B$ と $F:\mathcal A\to\mathcal X$ があるとする｡

($\mathcal X$ は $\mathcal V$-圏､ 例えば $\mathcal V=\mathbf{Set}$ の普通の圏でもよい｡)

定義 (左重み付き Kan 拡張)  
左Kan拡張 (weighted left Kan extension) $\operatorname{Lan}_K F:\mathcal B\to\mathcal X$ は､各点 $b\in\mathcal B$ に対して

$$(\operatorname{Lan}_K F)(b) \;=\; \mathrm{colim}\bigl( \, \mathcal B(K-,\,b) \;\star\; F \,\bigr)$$

(つまり重み $\mathcal B(K-,b) : \mathcal A^{\mathrm{op}}\to \mathcal V$ による F の重み付き余極限) として存在することが多いです｡

この定義は普遍性で言うと次と同値です：  
任意の $\mathcal V$-函手 $G:\mathcal B\to\mathcal X$ に対して自然同型
$$\mathcal X\bigl(\operatorname{Lan}_K F,\; G\bigr) \;\cong\; \mathcal X\bigl(F,\; G\circ K\bigr)$$
が成り立つ｡ ここで $\mathcal X(-,-)$ は ｢函手間の自然変換全体｣ を示す表現です (enriched の場合は対応
する $\mathcal V$-対象)｡

---

3) 右 Kan 拡張 (weighted right Kan extension)

右 Kan 拡張 $\operatorname{Ran}_K F:\mathcal B\to\mathcal X$ は双対に対応します｡ 各 $b$ に対して

$$(\operatorname{Ran}_K F)(b) \;=\; \mathrm{lim}\bigl( \, [\mathcal B(b,\,K-),\; F(-)] \,\bigr)$$

もっと標準的には､ cotensor を用いて
$$(\operatorname{Ran}K F)(b) \cong \int{a\in\mathcal A} [\,\mathcal B(b,K a)\,,\; F(a)\,]$$
(ここで $[-, -]$ は $\mathcal V$ における内ホム (cotensor) を表します｡)

普遍性は
$$\mathcal X\bigl(G,\; \operatorname{Ran}_K F\bigr) \;\cong\; \mathcal X\bigl(G\circ K,\; F\bigr)$$
が任意の $G:\mathcal B\to\mathcal X$ に対して成り立つことです

---

4) Set-enriched (通常の圏) での分かりやすい公式
普通の圏 ($\mathcal V=\mathbf{Set}$) の場合､ 左・右 Kan は**共積分 (coend) ／積分 (end)**で次のよ
うに書けます：

• 左 Kan (点 $b$ に対して)：
$$(\operatorname{Lan}_K F)(b)\;\cong\;\int^{a\in\mathcal A} \mathcal B(K a,\, b)\times F(a)$$
(集合の共積分＝共等化子や共限極限の総称的な記述)

• 右 Kan：
$$(\operatorname{Ran}K F)(b)\;\cong\;\int{a\in\mathcal A} F(a)^{\mathcal B(b,\,K a)}$$

(指数関手を使った式)

また､ これらはcomma 圏を用いて書くと馴染みやすく､ 左 Kan は $b$ の上の圏 ($K\downarrow b$) による
普通の余極限 (colimit) としても表される：
$$(\operatorname{Lan}_K F)(b) \cong \operatorname{colim}\bigl( (K\downarrow b) \xrightarrow{\
\mathrm{proj}\ } \mathcal A \xrightarrow{\ F\ } \mathcal X \bigr)$$

---

5) 直感と用途 (丁寧な解説)
• 直感：Kan 拡張は ｢ある圏 $\mathcal A$ 上で定義されたデータ $F$ を､ 関手 $K:\mathcal
A\to\mathcal B$ に沿って $\mathcal B$ 上まで 『延長』 する最も普遍的な方法｣ です｡

重み付きの式を見ると､ 各点 $b$ のために $\mathcal A$ の各点 $a$ が ｢どれだけ寄与するか｣ をホ
ム値 $\mathcal B(K a,b)$(あるいはその重みによる) で測って合成しているイメージです｡

• なぜ重みが現れるか：$b$ に対する ｢代表的な寄与｣ は K a から b への射 (＝ホム) で表
されます｡ そのホム函手を重み $W=\mathcal B(K-,b)$ とみなすと､ weighted colimit の形
(共積分) でKan拡張が得られます｡ これにより､ 表現的で計算しやすい公式が得られます｡

• 用途：左 Kan はコリミット的操作 (左アダム／左導関手)､ 右 Kan はリミット的操作
(右導関手) で､ 層の押し出し､ 点検査､ 関手の延長・補完､ adjoint の存在証明や計算などに
広く使われます｡

---

6) 特別な場合 (代表性)

• K が包含関手や埋め込みなど特別な形の場合､ Kan 拡張は通常のコリミットや右随伴
(right adjoint) の計算に帰着します｡

• $K=\mathrm{id}\mathcal A$ のとき､ $\operatorname{Lan}{\mathrm{id}} F \cong F$
(自明)｡

---

7) まとめ (要点だけ)

• 左重み付きKan拡張 $\operatorname{Lan}_K F$ は点ごとに重み $\mathcal B(K-,b)$ を
用いた重み付き余極限で定義される：

$$(\operatorname{Lan}_K F)(b)\simeq \int^{a} \mathcal B(K a,b)\otimes F(a)$$ 

普遍性：
$$\mathcal X(\operatorname{Lan}_K F, G)\cong\mathcal X(F, G\circ K)$$

• 右重み付きKan拡張 $\operatorname{Ran}_K F$ は点ごとに重み $\mathcal B(b,K-)$
を用いた重み付き極限で定義される：

$$(\operatorname{Ran}K F)(b)\simeq \int{a} [\mathcal B(b,K a), F(a)]$$

普遍性：

$$\mathcal X(G,
\operatorname{Ran}_K F)\cong\mathcal X(G\circ K, F)$$

---

参考 (入門書)

• Saunders Mac Lane ｢Categories for the Working Mathematician｣— Kan 拡張の
基本的扱い (Set-enriched)｡

• G. M. Kelly ｢Basic Concepts of Enriched Category Theory｣— 重み付き極限・Kan 拡張の豊富な議論 (enriched)｡

---

もしよければ､ 具体例 (簡単な K,F を与えて実際に $\operatorname{Lan}_K F$ を計算する) を一つ作って丁
寧に計算して見せます｡ どのレベル (普通の集合圏での例／$\mathcal V$-enriched の一般例／comma圏を
使った説明) で見たいか教えてください｡

---
---

# enriched category

以下では $\mathcal V$-強化圏 (enriched category) と $\mathcal V$-関手 (enriched functor) を､ できる
だけ丁寧に・分かりやすく定義します｡

---

1. $\mathcal V$-強化圏 ($\mathcal V$-enriched category) の定義

前提：$\mathcal V$ は？

• $\mathcal V$ は 閉対称モノイド圏 (closed symmetric monoidal category) であ
る：

• 対象：$\mathrm{Ob}(\mathcal V)$

• モノイド積：$\otimes$ : $\mathcal V \times \mathcal V \to \mathcal V$

• 単位：$I\in \mathcal V$

• 内部ホム：$[-, -]$(closeness を保証)

典型例：

• $\mathcal V = \mathbf{Set}$ (普通の圏論に戻る)

• $\mathcal V = \mathbf{Ab}$ (アーベル群 enriched 圏)

• $\mathcal V = \mathbf{Vect}_k$ (線形圏＝k-線形圏)

• $\mathcal V = \mathbf{Cat}$
など｡

---

1.1 定義：$\mathcal V$-強化圏

$\mathcal V$-強化圏 (または $\mathcal V$-enriched category, $\mathcal V$-category)$\mathcal C$ とは､ 次のデータからなる：

(1) 対象の集合 (またはクラス)$\mathrm{Ob}(\mathcal C)$

(2) $\mathcal V$ の対象としての ｢ホム対象｣
任意の対象 $x,y\in\mathcal C$ に対し､
$\mathcal C(x,y) \in \mathrm{Ob}(\mathcal V)$
を与える｡

(普通の圏のホム集合が､ $\mathcal V$ の中の一般の対象に置き換えられたと思ってよい｡)

例：

• $\mathcal V = \mathbf{Vect}_k$ なら､ $\mathcal C(x,y)$ は k-ベクトル空間｡

• $\mathcal V = \mathbf{Ab}$ なら､ $\mathcal C(x,y)$ はアーベル群｡

• $\mathcal V = \mathbf{Set}$ なら､ これは通常のホム集合に一致する｡

(3) 合成 (composition)

各 $x,y,z\in\mathcal C$ に対して､ $\mathcal V$ の射として

$$\circ_{x,y,z} : \mathcal C(y,z) \otimes \mathcal C(x,y) \;\longrightarrow\; \mathcal C(x,z)$$

(4) 単位射 (identity)

各 $x \in \mathcal C$ に対して､ $\mathcal V$ の射

$$\mathrm{id}_x : I \longrightarrow \mathcal C(x,x)$$

(5) 公理 (普通の圏の結合法則・単位公理の $\mathcal V$ 版)

以下が可換になる：

• 結合律 (associativity)：

$$\begin{aligned}
&(\mathcal C(z,w)\otimes\mathcal C(y,z)) \otimes\mathcal C(x,y)
\xrightarrow{\alpha} \mathcal C(z,w)\otimes(\mathcal C(y,z)\otimes\mathcal C(x,y)) \\
&\xrightarrow{1\otimes\circ} \mathcal C(z,w)\otimes \mathcal C(x,z)
\xrightarrow{\circ} \mathcal C(x,w)
\end{aligned}$$

が

$$\begin{aligned}
&(\mathcal C(z,w)\otimes\mathcal C(y,z)) \otimes\mathcal C(x,y)
\xrightarrow{\circ\otimes 1} \mathcal C(y,w)\otimes\mathcal C(x,y) \\&\xrightarrow{\circ} \mathcal C(x,w)
\end{aligned}$$

に等しい｡

• 単位律 (unit laws)：

$$\mathcal C(x,y)
\cong I\otimes \mathcal C(x,y)
\xrightarrow{\mathrm{id}_y\otimes 1} \mathcal C(y,y)\otimes\mathcal C(x,y)
\xrightarrow{\circ} \mathcal C(x,y)$$

が恒等射になる｡
同様に右単位についても同じ｡

---

2. $\mathcal V$-関手 ($\mathcal V$-functor)

$\mathcal V$-圏 $\mathcal C,\mathcal D$ の間の $\mathcal V$-関手 (enriched functor)
$F:\mathcal C \longrightarrow \mathcal D$
とは､ 次のデータである：

(1) 対象の写像
$F : \mathrm{Ob}(\mathcal C) \to \mathrm{Ob}(\mathcal D)$

(2) ホム対象を $\mathcal V$ の射で送る
各 $x,y\in\mathcal C$ に対し､

$F_
{x,y} : \mathcal C(x,y) \longrightarrow \mathcal D(Fx, Fy)$ 
($\mathcal V$ の射)

(3) 公理 (合成・単位を保つ)

以下が可換：

• 合成を保つ：
$$\mathcal C(y,z)\otimes\mathcal C(x,y)
\xrightarrow{\circ} \mathcal C(x,z)
\xrightarrow{F} \mathcal D(Fx, Fz)$$
と
$$\mathcal C(y,z)\otimes\mathcal C(x,y)
\xrightarrow{F\otimes F} \mathcal D(Fy,Fz)\otimes\mathcal D(Fx,Fy)\xrightarrow{\circ} \mathcal D(Fx,Fz)$$
が一致する｡

• 単位を保つ：

$$I \xrightarrow{\mathrm{id}x} \mathcal C(x,x)
\xrightarrow{F} \mathcal D(Fx,Fx)
は
I\xrightarrow{\mathrm{id}{Fx}} \mathcal D(Fx,Fx)$$
に等しい｡

---

3. $\mathcal V=\mathbf{Set}$ のときは通常の圏・関手に戻る

• $\mathcal C(x,y)$ は単なる集合

• 合成は集合の写像

• 単位も要素 $1\in\mathcal C(x,x)$

• $\mathcal V$-関手は普通の関手

つまり enriched category は普通の圏の一般化｡

---
4. 例を見ると理解しやすい

例1：$\mathbf{Vect}_k$-圏 (線形圏)

• $\mathcal C(x,y)$ は k-ベクトル空間

• 合成は双線形写像

• 単位は線形写像 $k\to\mathcal C(x,x)$ で､ 単位元を恒等射に送る

例2：前順序集合 (preorder) は $\mathbf{Bool}$-圏

• $\mathcal V = \mathbf{Bool}=\{0,1\}$

• $x\le y$ を真偽値で表現

• 合成はAND

• enriched viewpoint で preorder の全体像がきれいに表現できる｡

---

要約 (やさしいまとめ)

• $\mathcal V$-強化圏

• ホム集合が $\mathcal V$ の対象に置き換わったもの

• 合成・単位が $\mathcal V$-射で与えられる

• 結合律・単位律が可換図式で課される｡

• $\mathcal V$-関手

• 対象の対応 $x\mapsto Fx$

• ホム対象の対応 $\mathcal C(x,y)\to\mathcal D(Fx,Fy)$

• 合成・単位を保つ｡

---

必要ならば

• enriched 自然変換 ($\mathcal V$-natural transformation)

• enriched limit/colimit

• enriched Kan extension
なども続けて説明できます｡ さらに例を見たい場合は言ってください！

---
---

# enriched natural transformation

了解！前回触れた

• $\mathcal V$-自然変換 (enriched natural transformation)

• $\mathcal V$-極限／余極限 (enriched limits / colimits)

• $\mathcal V$-Kan 拡張 (enriched Kan extension)

を 丁寧に 説明します｡
(必要なら例を追加しますので言ってください！)

---

1. $\mathcal V$-自然変換 (enriched natural transformation)

普通の自然変換より １段階強い構造 を持ちます｡

前提

• $\mathcal C,\mathcal D$ は $\mathcal V$-強化圏

• $F,G: \mathcal C \to \mathcal D$ は $\mathcal V$-関手

定義 (重要)

$\mathcal V$-自然変換 (または enriched natural transformation)

$\alpha : F \Rightarrow G$とは､ 各対象 $x\in\mathcal C$ に対して､ 
$\mathcal V$ の射

$\alpha_x : I \longrightarrow \mathcal D(Fx, Gx)$

を与え､ 次の図式が可換になるものです：

$$\begin{aligned}
\mathcal C(x,y)
&\xrightarrow{F} \mathcal D(Fx,Fy)
\xrightarrow{\alpha_y \circ -}
\mathcal D(Fx,Gy) \\
\mathcal C(x,y)
&\xrightarrow{G} \mathcal D(Gx,Gy)
\xrightarrow{-\circ \alpha_x}
\mathcal D(Fx,Gy)
\end{aligned}$$

直観的には：

普通の自然変換の ｢成分｣ が､ 集合の元ではなく $\mathcal V$ の射 
$I \to \mathcal D(Fx,Gx)$ に
なったもの｡

Set の場合との比較

• $\mathcal V=\mathbf{Set}$ なら
$(I=\{ * \})$､ 射 $I\to\mathcal D(Fx,Gx)$ は $\mathcal D(Fx,Gx)$ の元に対応
→ 普通の自然変換に完全に一致

---

2. $\mathcal V$-極限 / 余極限 (enriched limits / colimits)

2.1 enriched limit の定義 (普遍性で定義)

図
$F : \mathcal J \to \mathcal C$
に対して､ 対象 $L\in\mathcal C$ が $\mathcal V$-極限 (limit enriched in $\mathcal V$) であるとは：

$$\mathcal C(x, L)
\;\cong\;
[\mathcal J,\, \mathcal V]\bigl( \Delta(\mathcal C(x,-)), F \bigr)$$

が自然同型であること｡
もっと分かりやすく言うと：

enriched limit は
ホム対象 を使って普遍性を表す点が普通の極限と違う｡

2.2 enriched colimit

双対に：
$$\mathcal C(C, x)
\;\cong\;
[\mathcal J,\, \mathcal V]\bigl( W, \mathcal C(F(-),x) \bigr)$$

特に 重み付き余極限 (weighted colimit) は共積分 (coend)

$W \star F = \int^{j\in\mathcal J} W(j)\otimes F(j)$

で書かれる ($\mathcal V$ が十分よい場合)｡

Set の場合

$\mathcal V = \mathbf{Set}$ のとき､

• enriched limit = 普通の極限

• enriched colimit = 普通の余極限

に完全に一致する｡

---

3. $\mathcal V$-Kan 拡張 (enriched Kan extension)

普通の Kan 拡張を $\mathcal V$-圏で行ったもの｡

3.1 定義 (左 $\mathcal V$-Kan 拡張)

関手
$$K : \mathcal A \to \mathcal B,\qquad
F : \mathcal A \to \mathcal X$$
に対し､ $\mathcal V$-関手 $\operatorname{Lan}_K F : \mathcal B \to \mathcal X$ が
左 $\mathcal V$-Kan 拡張 とは：

$$\mathcal X\bigl(\operatorname{Lan}_K F, G\bigr)
\;\cong\;
\mathcal X\bigl(F, G\circ K\bigr)$$
が全 $\mathcal V$-関手 G について自然同型であること｡

点ごと (weighted colimit を使った) 公式良い場合 (特に $\mathcal X$ が $\mathcal V$-余完備) には
$$(\operatorname{Lan}_K F)(b)
\;=\;
\int^{a\in\mathcal A}
\mathcal B(K a, b) \otimes F(a)$$

つまり
ホム対象を重みとして使った重み付き余極限 (coend) である｡

3.2 右 $\mathcal V$-Kan 拡張

双対に
$$(\operatorname{Ran}K F)(b)
\;=\;
\int{a\in\mathcal A}
[\,\mathcal B(b,Ka),\, F(a)\,]$$

(内ホムを使った end)

---

4. 全体のまとめ

|概念 |enriched の定義| Set の場合|
|---|---|---|
|$\mathcal V$-自然変換| $I\to \mathcal D(Fx,Gx)$ の族 |普通の自然変換|
|$\mathcal V$-極限| ホム対象による普遍性| 普通の極限|
|$\mathcal V$-余極限| weighted colimit (coend)| 普通の余極限|
|$\mathcal V$-左Kan| weighted colimit| 普通の左 Kan|
|$\mathcal V$-右Kan| weighted limit| 普通の右 Kan|

---

5. もっと理解したい場合は？

• 具体例 (例：$Vect_k$-圏での enriched limit の計算)

• enriched natural transformation の図式 chasing

• コエンド・エンドの計算例

• enriched adjunction の定義

• enriched Kan 拡張の具体例など､ 必要なトピックを言ってください！

---
---

# Kan拡張まとめ

**｢普通の (Set-enriched) Kan 拡張｣**と
｢$\mathcal V$-強化 (enriched) weighted Kan 拡張｣
の 定義を “横に並べて” 比較しながら丁寧に説明します｡
これがもっとも理解しやすい構成です｡

---

0. 事前知識
• 普通の圏論→すべて Set-enriched の特別な場合
• enriched 圏論→ホム集合の代わりにホム対象 ($\mathcal V$ の対象)

---

1. 普通の Kan 拡張 (Set-enriched)

■ 1.1 左 Kan 拡張の定義 (普遍性)

関手
$K:\mathcal A \longrightarrow \mathcal B,\qquad
F:\mathcal A \longrightarrow \mathcal X$
に対し､
左 Kan 拡張 $\operatorname{Lan}_K F : \mathcal B\to \mathcal X$ は次の普遍性で定義される：

$$\operatorname{Nat}\bigl(\operatorname{Lan}_K F,\; G\bigr)
\;\cong\;
\operatorname{Nat}\bigl(F,\; G\circ K\bigr)
\qquad (\forall\, G:\mathcal B\to\mathcal X)$$

自然同型が

• すべての G で

• 自然に成り立つ｡

これが Kan 拡張の本質｡--- ■

1.2 点ごとの計算 (Set のときの公式)

$(\operatorname{Lan}K F)(b) \cong \mathop{\mathrm{colim}}{(a\to b)\in (K\downarrow b)} F(a)$

つまり
comma 圏 (K\downarrow b) 上の余極限
あるいは coend を使うと
$$(\operatorname{Lan}_K F)(b)
\cong
\int^{a\in\mathcal A}
\mathcal B(K a, b)\times F(a)$$

(重みはホム集合 $\mathcal B(K a,b)$｡)

--- ■

1.3 右 Kan 拡張 (双対)
$$(\operatorname{Ran}K F)(b)
\cong
\lim{(b\to Ka)\in (b\downarrow K)} F(a)$$

または end で：

$$(\operatorname{Ran}K F)(b)
\cong
\int{a}
F(a)^{\mathcal B(b,K a)}$$

---

2. enriched weighted Kan 拡張 ($\mathcal V$-Kan 拡張)

ここから一気に一般化します｡

■ 2.1 enriched 左 Kan 拡張の定義 (普遍性)

関手
$K:\mathcal A\to\mathcal B,\qquad F:\mathcal A\to\mathcal X$
で､ すべてが $\mathcal V$-圏・$\mathcal V$-関手であるとする｡

左 $\mathcal V$-Kan 拡張 $\operatorname{Lan}_K F$ は次の普遍性で定義される：

$$\mathcal X\bigl(\operatorname{Lan}_K F,\; G\bigr)
\;\cong\;
\mathcal X\bigl(F,\; G\circ K\bigr)
\qquad(\forall G:\mathcal B\to\mathcal X)$$

これは Set 版と完全に同じ形｡
ただし右辺・左辺のホムは
自然変換の集合
ではなく
enriched natural transformations の $\mathcal V$-対象
である点が違う｡

--- ■

2.2 enriched weighted の点ごとの公式

重要なコア公式：

$$(\operatorname{Lan}_K F)(b)
\;\;=\;\;
\int^{a\in\mathcal A}
\mathcal B(K a, b)\;\otimes\; F(a).$$

ここで

• 重み (weight) は $\mathcal B(Ka,b)\in \mathcal V$

• $\otimes$ は $\mathcal V$ のモノイド積

• $\int^{a}$ は enriched coend

つまり ｢ホム集合｣ を ｢ホム対象｣ に置き換えただけで
coend を使った形も完全に一致する！！

--- ■

2.3 enriched weighted 右 Kan 拡張双対：

$$(\operatorname{Ran}K F)(b)
\;\;=\;\;
\int{a\in\mathcal A}
[\mathcal B(b, K a),\, F(a)]$$

ここで $[ -, -]$ は $\mathcal V$ の 内部ホム (内ホム)｡

---

3. ｢普通 → enriched → weighted｣ の三段階比較

|レベル| 左 Kan 拡張| 特徴|
|---|---|---|
|普通 (Set)| $(\operatorname{Lan} F)(b)=\displaystyle\int^{a} \mathcal B(Ka,b)\times F(a)$| ホムは集合|
|enriched| $(\operatorname{Lan} F)(b)=\displaystyle\int^{a}\mathcal B(Ka,b)\otimes F(a)$| ホムは $\mathcal V$ の対象|
|weighted|$(W\star F)=\displaystyle\int^{a} W(a)\otimes F(a)$| 普通の重みを任意の W に置換|

そして enriched Kan は
重み $W=\mathcal B(K-,b)$ を特別な重みとして使うだけ｡

---

4. 一言まとめ

普通の Kan 拡張  
• 普遍性  
• comma 圏で計算できる  
• coend で書ける  
• 重み=\mathcal B(K-,b) は 集合  

enriched weighted Kan 拡張  
• 普遍性は同じ  
• ただしホムが $\mathcal V$ の対象  
• coend ($\mathcal V$-coend) で計算  
• 重み=$\mathcal B(K-,b)$ は $\mathcal V$ の対象  
• $\otimes$, 内ホム $[-,-]$ が登場---  

さらに理解したい場合  
• enriched coend の計算例  
• Vect_k-圏での enriched Kan 拡張  
• Set の場合に戻るとどうなるかの比較  
• diagram chasing で普遍性を実感する例  
なども作れます！  
必要なら､ 計算例をぜひ言ってください｡

