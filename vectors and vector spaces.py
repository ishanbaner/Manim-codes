from manim import *

class TestScene1(Scene):
  def construct(self):
      vector = Tex("Vector").shift(UP*3)
      head = Tex("Head").shift(UP*1+LEFT*1)
      tail = Tex("Tail").shift(DOWN*2+RIGHT*3)
      arrow1 = Arrow(start = DOWN*2+RIGHT*2 , end = UP*1+LEFT*2)
      arrow2 = Arrow(start = DOWN*2+RIGHT*1.8 , end = UP*1+RIGHT*4 , color = RED)
      arrow3 = Arrow(start = DOWN*2+RIGHT*2 , end = UP*4+LEFT*1 , color = GREEN)
      arrow4 = Arrow(start = DOWN*2+RIGHT*2 , end = UP*4+LEFT*6)
      arrow5 = Arrow(start = UP*2+LEFT*3 , end = DOWN*2+RIGHT*2)
      V1 = Tex("$V_1$").shift(RIGHT*5)
      V1c = Tex("$V_1$").shift(RIGHT*5)
      V2 = Tex("$V_1+V_2$").shift(RIGHT*5)
      Mult1 = Tex(r"$3 \times V_1$").shift(RIGHT*5)
      Mult2 = Tex(r"$-1 \times V_1$").shift(RIGHT*5)

      self.play(Write(vector))
      self.wait(5)
      self.play(Write(arrow1))
      self.wait()
      self.play(Write(tail))
      self.wait()
      self.play(Write(head))
      self.wait(3)
      self.play(FadeOut(head),FadeOut(tail),FadeOut(arrow1),FadeOut(vector))
      self.wait(3)
      self.play(Write(arrow1),Write(V1))
      self.wait(3)
      self.play(Write(arrow2))
      self.wait()
      self.play(Write(arrow3),Transform(V1,V2))
      self.wait()
      self.play(FadeOut(arrow2),FadeOut(arrow3),Transform(V1,V1c))
      self.wait(2)
      self.play(Transform(arrow1,arrow4),Transform(V1,Mult1))
      self.wait()
      self.play(Transform(arrow1,arrow5),Transform(V1,Mult2))
      self.wait(10)

class Graph1(Scene):
    def construct(self):
        
        plane = NumberPlane( axis_config={"include_numbers": False},)
        arrow1 = Arrow(start=DOWN,end=UP*2.4+RIGHT*2.3,color=GOLD).shift(UP*0.8+LEFT*0.18)
        coord = Matrix([[2],[3]]).shift(UP*2.9+RIGHT*2.5)
        d = Dot(point=LEFT*0+UP*0,color=YELLOW)

        self.play(Write(plane))
        self.play(Write(arrow1))
        self.wait(3)
        self.play(Write(coord))
        self.wait(10)
        self.play(Write(d))
        self.play(d.animate.shift(RIGHT*2))
        self.wait()
        self.play(d.animate.shift(UP*3))
        self.wait(25)

class Graph2(Scene):
    def construct(self):

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
        line = Line(START,END,color=YELLOW);
        vec1 = Arrow(START1,END1,color=YELLOW)
        vec2 = Arrow(START1,END2,color=YELLOW)
        vec3 = Arrow(START2,END3,color=YELLOW)
        vec4 = Arrow(START2,END4,color=YELLOW)
        vec5 = Arrow(START2,END1,color=RED)
        vec6 = Arrow(START2,END3,color=BLUE)
        vec7 = Arrow(START2,END5,color=GREEN)
        vec8 = Arrow(START3,END4,color=GREEN)
        origin = Tex("$(0,0)$").shift(RIGHT*0.5+DOWN*0.5)
        vs = Tex("Vector Space")
        
        

        self.play(Write(plane))
        self.play(Write(line))
        self.wait()
        self.play(Write(vec1))
        self.play(Write(vec2))
        self.play(Write(vec3))
        self.play(Write(vec4))
        self.wait(5)
        self.play(FadeOut(vec1),FadeOut(vec2),FadeOut(vec3),FadeOut(vec4))
        self.wait()
        self.play(Write(vec5))
        self.wait()
        self.play(Write(vec6))
        self.wait()
        self.play(Transform(vec5,vec7),FadeOut(vec6))
        self.wait()
        self.play(Transform(vec5,vec8))
        self.wait(6)
        self.play(Write(origin))
        self.wait(2)
        self.play(FadeOut(origin,vec5))
        self.wait(14)
        self.play(Transform(line,vs),FadeOut(plane))
        self.wait(10)

class Addition(Scene):
    def construct(self):
      comm = Tex("$v+w=w+v$").shift(UP*2)
      zero = Tex("$0_V$").shift(UP*1)
      identity = Tex("$v+0_V=0_V+v=v$")
      inv = Tex("$v+(-v)=(-v)+v=0_V$").shift(DOWN*1)
      assoc = Tex("$u+(v+w)=(u+v)+w$").shift(DOWN*2)

      self.play(Write(comm))
      self.wait(5)
      self.play(Write(zero))
      self.wait(3)
      self.play(Write(identity))
      self.wait(6)
      self.play(Write(inv))
      self.wait(5)
      self.play(Write(assoc))
      self.wait(10)



class Multiplication(Scene):
    def construct(self):
      dis1 = Tex("$c\cdot(v+w)=c\cdot w+c\cdot v$").shift(UP*2)
      dis2 = Tex("$(c+d)\cdot v = c\cdot v + d \cdot v$").shift(UP*1)
      assoc = Tex(r"$c\cdot (d\cdot v) = (c\times d)\cdot v$")
      one= Tex("$1\cdot v = v\cdot 1 = v$").shift(DOWN*1)
      field = Tex("$V(\mathbb{F})$")
      real = Tex("$\mathbb{R}$")
      comp = Tex("$\mathbb{C}$")
      
      self.play(Write(dis1))
      self.play(Write(dis2))
      self.wait(3)
      self.play(Write(assoc))
      self.wait(2)
      self.play(Write(one))
      self.wait(4)
      self.play(FadeOut(dis1,dis2,assoc,one))
      self.wait()
      self.play(Write(real))
      self.wait(2)
      self.play(Transform(real,comp))
      self.wait(10)
      self.play(Transform(real,field))
      self.wait(10)


class Examples(Scene):
    def construct(self):
      r2 = Tex("$\mathbb{R}^2$").shift(LEFT*1)
      rn = Tex("$\mathbb{R}^n$").shift(RIGHT*1)
      p4 = Tex("$ax^4+bx^3+cx^2+dx+e$").shift(DOWN*1+LEFT*1)
      matr = Matrix([[1,4],[5,8]]).shift(DOWN*3)

      self.play(Write(r2))
      self.wait(5)
      self.play(Write(rn))
      self.wait(3)
      self.play(Write(p4))
      self.wait(1)
      self.play(Write(matr))
      self.wait(10)





      
        

        












      
      
