# 実行コマンド ： manim -pql dodecahedron_example.py ShowDodecahedron

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
