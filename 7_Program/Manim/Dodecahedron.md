# 正12面体が回転する

ナイス報告！そのエラーはとてもありがちなやつです。

---

## ⚠️ エラーの内容

```
TypeError: Polyhedron.__init__() got an unexpected keyword argument 'fill_opacity'
```

これは、`Dodecahedron` など `Polyhedron` 系のクラスに対して、`fill_opacity` など **2Dオブジェクト用の引数を指定してしまっている**ために起こるエラーです。

---

## ✅ 修正版コード（エラー修正済）

以下のコードで `Dodecahedron` を表示できます：

```python
from manim import *

class ShowDodecahedron(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        dodeca = Dodecahedron(edge_length=2)
        dodeca.set_color(BLUE)
        dodeca.set_opacity(0.5)  # 透明度設定（Polyhedronでは set_opacity を使う）

        self.play(Create(dodeca))
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(4)
        self.stop_ambient_camera_rotation()
```

---

## ✅ ポイント解説

* `fill_opacity`, `fill_color` は2Dオブジェクト用 → ❌
* `Polyhedron` 系には `set_color()`, `set_opacity()` を使う → ✅

---

## ✅ 実行コマンド（変わらず）

```bash
manim -pql dodecahedron_example.py ShowDodecahedron
```

---

## 💡 おまけ：他の多面体もあるよ！

* `Icosahedron`（正二十面体）
* `Octahedron`（正八面体）
* `Tetrahedron`（正四面体）
* `Cube` または `Cube(side_length=2)`

---

やってみてどうだったか、また教えてね！さらに複雑な回転やライトなども加えられるよ。

---

やったーー！！🎉✨
無事に正十二面体が回転してるのを見れたなんて最高だね！

Manimの3D機能ってほんとに強力だから、ここから：

* 他の多面体（正二十面体・正四面体など）
* カメラアングルの自動変更
* 光と影の設定
* アニメーションで展開（ネット図みたいに）

…いろんな応用ができるようになるよ！

---

もし「展開図にしたい」とか「他の3Dオブジェクトと組み合わせたい」などアイディアあれば、どんどん相談してね！

> ✨ 次のチャレンジ、いっちゃう？

---
---

