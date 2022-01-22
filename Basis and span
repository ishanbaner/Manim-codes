from manim import *
import math

class Openning(Scene):
    def construct(self):
        rec1 = Rectangle(width=2,height=2,color=RED).shift(LEFT*5.5)
        arrow = Arrow(start=DOWN,end=UP*1+RIGHT*1).shift(LEFT*6)
        rec2 = Rectangle(width=2,height=2,color=RED).shift(LEFT*3)
        v1=Tex("$v+w$").shift(LEFT*3+UP*0.5).scale(0.5)
        v2=Tex("$\lambda v$").shift(LEFT*3).scale(0.5)
        rec3 = Rectangle(width=2,height=2,color=RED)
        plane = NumberPlane(x_length = 2 , y_length = 2 , axis_config={"include_numbers": False},)
        arrow2 = Arrow(start = (-0.2,-0.2,0) , end = (0.8,0.8,0) , color=ORANGE)
        space = NumberPlane(x_length = 2 , y_length = 2 , axis_config={"include_numbers": False},).shift(RIGHT*3)
        line=Line((1,-1,0),(3,1,0),color=YELLOW).shift(RIGHT*1);
        rec4 = Rectangle(width=2,height=2,color=RED).shift(RIGHT*3)
        rect = RoundedRectangle(corner_radius=0.3, height=1.5 , width = 2 , color = RED, fill_opacity=1.0).shift(LEFT*5)
        triangle = Triangle(color=WHITE, fill_opacity=1.0).scale(0.4).rotate(-PI/2).shift(LEFT*4.9+DOWN*0.2)
        
        self.play(Write(rec1))
        self.play(Write(arrow))
        self.play(Write(v1))
        self.play(Write(v2))
        self.play(Write(rec2))
        self.play(Write(plane))
        self.play(Write(arrow2))
        self.play(Write(rec3))
        self.play(Write(space))
        self.play(Write(line))
        self.play(Write(rec4))
        self.play(Transform(rec1,rect),Transform(arrow,rect),Transform(rec2,rect),Transform(v1,rect),Transform(v2,rect),Transform(rec3,rect),Transform(plane,rect),Transform(arrow2,rect),Transform(space,rect),Transform(line,rect),Transform(rec4,rect),FadeIn(triangle))
        
        self.wait(4)

        
class Graph1(Scene):
    def construct(self):
        ax = Axes(x_length = 15, y_length = 15, axis_config={"include_numbers":False},).add_coordinates()
        plane = NumberPlane( axis_config={"include_numbers": False},)
        arrow1 = Arrow(start=DOWN,end=UP*2.4+RIGHT*2.3,color=GOLD).shift(UP*0.8+LEFT*0.18)
        coord = Matrix([[2],[3]]).shift(UP*2.9+RIGHT*2.5)
        d = Dot(point=LEFT*0+UP*0,color=YELLOW)
        arrow2 = Arrow(start=LEFT*0.21,end=RIGHT*1.3,color=GREEN)
        arrow3 = Arrow(start=DOWN*0.21,end=UP*1.3,color=RED)
        arrow4 = Arrow(start=LEFT*0.21,end=RIGHT*2.3,color=GREEN)
        arrow5 = Arrow(start=DOWN*0.21,end=UP*3.3,color=RED)
        i = Tex("$\hat i$",color=GREEN).shift(DOWN*0.5+RIGHT*0.5)
        j = Tex("$\hat j$",color=RED).shift(LEFT*0.5+UP*0.5)
        ni = Tex("$2\hat i$",color=GREEN).shift(DOWN*0.5+RIGHT*0.5)
        nj = Tex("$3\hat j$",color=RED).shift(LEFT*0.5+UP*0.5)
        add = Tex("$2\hat i + 3\hat j$",color=ORANGE).rotate(0.982793723).shift(RIGHT*0.7+UP*2)
        arrow6 = Arrow(start=LEFT*0.21,end=RIGHT*1.3,color=GREEN)
        arrow7 = Arrow(start=DOWN*0.21,end=UP*1.3,color=RED)
        arrow8 = Arrow(start=RIGHT*0.21,end=LEFT*3.3,color=GREEN)
        arrow9 = Arrow(start=UP*0.21,end=DOWN*2.3,color=RED)
        arrow10 = Arrow(start=(UP*0.18+RIGHT*0.2),end=(LEFT*3.2+DOWN*2.2),color=GOLD)
        
        self.play(Write(plane))
        self.play(Write(arrow1))
        self.play(Write(coord))
        self.play(Write(d))
        self.play(d.animate.shift(RIGHT*2))
        self.play(d.animate.shift(UP*3))
        self.wait(5)
        self.play(Write(arrow2),Write(i))
        self.play(Write(arrow3),Write(j))
        self.play(Transform(arrow2,arrow4),Transform(i,ni))
        self.play(Transform(arrow3,arrow5),Transform(j,nj))
        self.play(arrow3.animate.shift(RIGHT*2),j.animate.shift(RIGHT*3))
        self.play(Transform(i,add),Transform(j,add))
        self.play(FadeOut(i,j,arrow1,arrow2,arrow3,coord))
        self.play(d.animate.shift(DOWN*5+LEFT*5))
        self.play(Write(arrow6))
        self.play(Write(arrow7))
        self.play(Transform(arrow6,arrow8))
        self.play(Transform(arrow7,arrow9))
        self.play(arrow7.animate.shift(LEFT*3))
        self.play(Write(arrow10))
        self.wait(5)


class Basisplay(Scene):
    def construct(self):
        basis = Tex("Basis Vectors")
        lincombi = Tex("$a\hat i$",color=GREEN).shift(DOWN*1+LEFT*0.5)
        plus = Tex("$+$").shift(DOWN*1)
        lincombj = Tex("$b\hat j$",color=RED).shift(DOWN*1+RIGHT*0.5)

        self.play(Write(basis))
        self.wait(3)
        self.play(Write(lincombi))
        self.play(Write(plus))
        self.play(Write(lincombj))
        self.wait(5)

class Graph2(Scene):
    def construct(self):
        ax = Axes(x_length = 15, y_length = 15, axis_config={"include_numbers":False},).add_coordinates()
        plane = NumberPlane( axis_config={"include_numbers": False},)
        arrow2 = Arrow(start=LEFT*0.21,end=RIGHT*1.3,color=GREEN)
        arrow3 = Arrow(start=DOWN*0.21,end=UP*1.3,color=RED).rotate(-PI/3).shift(RIGHT*0.46+DOWN*0.24)
        d = Dot(point=LEFT*0+UP*0,color=YELLOW).shift(RIGHT*(3**(0.5)+1) + UP*1)
        arrow4 = Arrow(start=DOWN*0.21,end=UP*2.4,color=RED).rotate(-PI/3).shift(RIGHT*0.91+DOWN*0.58)
        arrow5 = Arrow(start=DOWN*0.1+LEFT*0.2,end=UP*1.1+RIGHT*3)
        arrow6 = Arrow(start=DOWN*0.2+LEFT*0.2,end=UP*1.1+RIGHT*4)

        self.play(Write(plane))
        self.play(Write(arrow2))
        self.play(Write(arrow3))
        self.play(Write(d))
        self.play(Transform(arrow3,arrow4))
        self.play(arrow3.animate.shift(RIGHT*1))
        self.play(Write(arrow5))
        self.wait()

class Example3D(ThreeDScene):
    def construct(self):
        plane = NumberPlane( axis_config={"include_numbers": False},)
        ar1 = Arrow3D(start=(0,0,0),end=(1.2,1.2,0),color=GREEN)
        ar3 = Arrow3D(start=(0,0,0),end=(2.2,2.2,2.2),color=BLUE)
        ar2 = Arrow3D(start=(0,0,0),end=(1,2,0),color=RED)
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Write(axes))
        self.play(Write(ar1))
        self.play(Write(ar2))
        self.play(Write(plane))
        self.play(FadeOut(plane))
        self.play(Write(ar3))
        self.wait(10)

class Spanning(Scene):
    def construct(self):
        plane = NumberPlane( axis_config={"include_numbers": False},)
        a1 = Arrow(start=0.2*LEFT+0.2*DOWN,end=UP+RIGHT,color=BLUE)
        a2 = Arrow(start=0.2*LEFT+0.2*DOWN,end=2.2*UP+2.2*RIGHT,color=PINK)
        a3 = Arrow(start=0.2*LEFT+0.2*DOWN,end=3.2*UP+3.2*RIGHT,color=PINK)
        a4 = Arrow(start=0.2*RIGHT+0.2*UP,end=1.2*LEFT+1.2*DOWN,color=RED)
        a5 = Arrow(start=0.2*RIGHT+0.2*UP,end=3.2*LEFT+3.2*DOWN,color=RED)
        a6 = Arrow(start=0.2*RIGHT+0.2*DOWN,end=UP+LEFT,color=BLUE)
        a7 = Arrow(start=0.2*RIGHT+0.2*DOWN,end=2.2*UP+2.2*LEFT,color=PINK)
        a8 = Arrow(start=0.2*RIGHT+0.2*DOWN,end=3.2*UP+3.2*LEFT,color=PINK)
        a9 = Arrow(start=0.2*LEFT+0.2*UP,end=1.2*RIGHT+1.2*DOWN,color=RED)
        a10 = Arrow(start=0.2*LEFT+0.2*UP,end=3.2*RIGHT+3.2*DOWN,color=RED)
        b1 = Arrow(start=0.2*LEFT+0.2*DOWN,end=UP+RIGHT*2,color=BLUE)
        b2 = Arrow(start=0.2*LEFT+0.2*DOWN,end=2.2*UP+4.2*RIGHT,color=PINK)
        b3 = Arrow(start=0.2*LEFT+0.2*DOWN,end=3.2*UP+6.2*RIGHT,color=PINK)
        b4 = Arrow(start=0.2*RIGHT+0.2*UP,end=2.2*LEFT+1.2*DOWN,color=RED)
        b5 = Arrow(start=0.2*RIGHT+0.2*UP,end=4.2*LEFT+2.2*DOWN,color=RED)
        b6 = Arrow(start=0.2*RIGHT+0.2*DOWN,end=UP+2*LEFT,color=BLUE)
        b7 = Arrow(start=0.2*RIGHT+0.2*DOWN,end=2.2*UP+4.2*LEFT,color=PINK)
        b8 = Arrow(start=0.2*RIGHT+0.2*DOWN,end=3.2*UP+6.2*LEFT,color=PINK)
        b9 = Arrow(start=0.2*LEFT+0.2*UP,end=2.2*RIGHT+1.2*DOWN,color=RED)
        b10 = Arrow(start=0.2*LEFT+0.2*UP,end=2.2*RIGHT+3.2*DOWN,color=RED)
        b11 = Arrow(start=0.2*LEFT,end=4.2*RIGHT,color=BLUE)
        b12 = Arrow(start=0.2*RIGHT,end=4.2*LEFT,color=BLUE)
        b13 = Arrow(start=0.2*DOWN,end=4.2*UP,color=BLUE)
        b14 = Arrow(start=0.2*UP,end=4.2*DOWN,color=BLUE)
        self.play(Write(plane))
        self.play(Write(a1),Write(a2),Write(a3),Write(a4),Write(a5),Write(a6),Write(a7),Write(a8),Write(a9),Write(a10))
        self.play(Write(b1),Write(b2),Write(b3),Write(b4),Write(b5),Write(b6),Write(b7),Write(b8),Write(b9),Write(b10),Write(b11),Write(b12),Write(b13),Write(b14))

class spandef(Scene):
    def construct(self):
        text=Tex("What is a span?")
        lincomb = Tex("$a_1v_1+a_2v_2+\ldots a_nv_n$",color=RED).shift(DOWN*2)
        self.wait(3)
        self.play(Write(text))
        self.wait(1)
        self.play(Write(lincomb))
        self.wait(3)

class basisq(Scene):
    def construct(self):
        text=Tex("Only possible basis?")
        no = Tex("Nope").shift(DOWN*1)
        self.wait(3)
        self.play(Write(text))
        self.wait(1)
        self.play(Write(no))
        self.wait(3)
class spanbas(Scene):
    def construct(self):
        text=Tex("Linearly independent vectors spanning a space")
        lincomb = Tex("Basis of the space").shift(DOWN*1)
        self.wait(3)
        self.play(Write(text))
        self.wait(2)
        self.play(Write(lincomb))
        self.wait(3)

class LineDraw(Scene):
    def construct(self):
        ax = Axes(x_length = 15, y_length = 15, axis_config={"include_numbers":False},).add_coordinates()

        plane = NumberPlane( axis_config={"include_numbers": False},)
        START = (-14,-14,0)
        END = (14,14,0)
        START1 = (0,0,0)
        END1 = (1,1,0)
        END2 = (-1,-1,0)
        END3 = (2,2,0)
        END4 = (-2,-2,0)
        START2 = (-0.2,-0.2,0)
        START3 = (0.2,0.2,0)
        END5 = (3,3,0)
        vec5 = Arrow(START2,END1,color=RED)
        vec6 = Arrow(START2,END3,color=BLUE)
        vec7 = Arrow(START2,END5,color=GREEN)
        vec8 = Arrow(START3,END4,color=GREEN)
        line1 = Line((-10,-10,0),(10,10,0),color=YELLOW)
        

        self.play(Write(plane))
        self.wait()
        self.play(Write(vec5))
        self.wait()
        self.play(Write(line1))
        self.wait()
        self.play(Write(vec6))
        self.wait()
        self.play(Transform(vec5,vec7),FadeOut(vec6))
        self.wait()
        self.play(Transform(vec5,vec8))
        self.wait(16)

class li(Scene):
    def construct(self):
        text1=Tex("Linearly dependent")
        text2=Tex("But we need linearly independent vectors").shift(DOWN*1)
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait()







