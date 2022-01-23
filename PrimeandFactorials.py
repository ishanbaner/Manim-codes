from manim import *

class TestScene1(Scene):
  def construct(self):
    p = Tex("There are infinitely many primes of the form $n!\pm 1$")
    p.scale(1)
    t = Tex("There are infinitely many primes of the form $\prod\limits_{p_i\leqslant p\,primes}^p p_i\pm 1$")
    t.scale(1)
    q = Tex("Open problem")
    q.scale(2)


    self.play(Write(p))
    self.play(p.animate.shift(UP*3),run_time=2)
    self.play(Write(t))
    self.play(t.animate.shift(UP*2),run_time=2)
    self.wait(12)
    self.play(Write(q))
    self.wait()
    self.wait(6)





from manim import *

class TestScene2(Scene):
  def construct(self):
      Name = Tex("Reo F. Fortune")
      Name.scale(2)
      eq1 = Tex("Least prime $ q > \prod p_i $")
      t = Tex("$ q - \prod p_i $ is a prime for all $ p $")

 
      self.play(Write(Name))
      self.wait(2)
      self.play(Name.animate.shift(DOWN*3,RIGHT*3),run_time=2)
      self.play(Write(eq1))
      self.play(eq1.animate.shift(UP*1))
      self.play(Write(t))
      self.wait(3)



from manim import *

class TestScene3(Scene):
  def construct(self):
      eq1 = Tex("If a prime $r\;|(q-\prod p_i)$, then $r>p$").shift(UP*2)
      name1 = Tex("Selfridge")
      name2 = Tex("Schinzel's formulation of Cramer's conjecture")
      name3 = Tex("$x>7.1374035$, there is always a prime between $x$ and $x+(\ln x)^2$")
      text4 = Tex("For $x>7.1374035$",color=BLUE).shift(DOWN*1)
      text5 = Tex("there is always a prime between $x$ and $(\ln x)^2$",color=BLUE).shift(DOWN*2)
      arrow1 = Arrow(start=DOWN,end=UP,color=GOLD).shift(UP+RIGHT*0.6)
      circle1 = Circle(radius=0.5).shift(UP*2+LEFT*0.8)
      pr = Tex("$2 \cdot 3\cdot 5\cdot 7\cdot 11\ldots p$",color=YELLOW).shift(UP+RIGHT*0.6)

      self.play(Write(eq1))
      self.wait(4)
      self.play(Write(circle1))
      self.wait(3)
      self.play(FadeOut(circle1),run_time=4)
      self.play(Write(arrow1))
      self.wait(3)
      self.play(Transform(arrow1,pr))
      self.wait(2)
      self.play(Write(name1))
      self.wait(3)
      self.play(Transform(name1,name2))
      self.wait(3)
      self.play(Write(text4))
      self.play(Write(text5))
      self.wait(8)


from manim import *

class TestScene4(Scene):
  def construct(self):
    text1 = Tex(r"$\lim\limits_{n \to \infty} \, sup \dfrac{p_{n+1}-p_n}{(\ln p_n)^2} = 1$",color=BLUE)
    text2 = Tex(":(",color = BLUE).shift(DOWN*1)

    self.wait(7)
    self.play(Write(text1))
    self.wait(3)
    self.play(Write(text2))
    self.wait(6)




from manim import *

class TestScene5(Scene):
  def construct(self):
    text1 = Tex("Erdos-Stewart's conjecture",color=YELLOW).shift(UP*2)
    text2 = Tex("$1!+1=2, 2!+1=3, 3!+1=7, 4!+1=25, 5!+1=121$").shift(UP*1)
    text3 = Tex("$n!+1=p_k^a\cdot p_{k+1}^b$",color=YELLOW)
    text4 = Tex("$p_{k-1}\leq n < p_k$",color=BLUE).shift(DOWN*1)
    p1    = Tex("$p_{k-1}$",color=BLUE).shift(LEFT*2)
    p2    = Tex("$p_k$",color=BLUE)
    p3    = Tex("$p_{k+1}$",color=BLUE).shift(RIGHT*2)
    p4    = Tex("n",color=YELLOW).shift(LEFT*1)
    p5    = Tex("$p_k^a$",color=BLUE).shift(DOWN*1)
    p6    = Tex("$p_{k+1}^b$",color=BLUE).shift(RIGHT*2+DOWN*1)
    p7    = Tex(r"$\times$").shift(RIGHT*1+DOWN*1)
    p8    = Tex("$=$").shift(DOWN*1+LEFT*0.5)
    p9    = Tex("$n!+1$",color=YELLOW).shift(LEFT*1.5+DOWN*1)
    line  = NumberLine(x_range=[-7, 7, 1],length=20, color=GREEN, include_numbers=False, include_tip=True).shift(UP*0.5)
    d1    = Dot(point=LEFT*2+UP*0.5)
    d2    = Dot(point=UP*0.5)
    d3    = Dot(point=RIGHT*2+UP*0.5)
    d4    = Dot(point=LEFT*1+UP*0.5)



    self.play(Write(text1))
    self.wait(3)
    self.play(Write(text2))
    self.wait()
    self.play(Write(text3))
    self.play(Write(text4))
    self.wait(2)
    self.play(FadeOut(text3))
    self.play(FadeOut(text4))
    self.play(Write(line))
    self.play(Write(d1))
    self.play(FadeIn(p1), shift=UP)
    self.play(Write(d2))
    self.play(FadeIn(p2), shift=UP)
    self.play(Write(d3))
    self.play(FadeIn(p3), shift=UP)
    self.wait()
    self.play(Write(d4))
    self.wait(1)
    self.play(d4.animate.shift(LEFT*1))
    self.play(d4.animate.shift(RIGHT*1.5))
    self.play(d4.animate.shift(LEFT*0.5))
    self.play(Write(p4))
    self.play(Transform(p4,p9))
    self.play(Transform(p2,p5))
    self.play(Transform(p3,p6))
    self.play(Write(p7))
    self.play(Write(p8))
    self.wait(10)

    
                
from manim import *

class TestScene6(Scene):
  def construct(self):
    text1 = Tex("$\exists$ infinitely many primes,$p$ such that",color=YELLOW).shift(UP*2)
    text2 = Tex("$p-k!$").shift(UP*1)
    text3 = Tex("(composite)",color=BLUE).shift(UP*1+RIGHT*2)
    text4 = Tex("$n$",color=BLUE)
    text5 = Tex("$l!<$",color=GREEN).shift(LEFT*1)
    text6 = Tex("$\leq (l+1)!$",color=GREEN).shift(RIGHT*2)
    text7 = Tex("$\prod p_i^{a_i}$",color=BLUE).shift(RIGHT*0.4)
    text8 = Tex("All $p_i>l$",color=GREEN).shift(DOWN*1)
    text9 = Tex("$n-k!,k\leq l$").shift(DOWN*2)
    text10= Tex("(Composite)",color=YELLOW).shift(DOWN*2+RIGHT*3)

    self.play(Write(text1))
    self.wait(1)
    self.play(Write(text2))
    self.wait(1)
    self.play(Write(text3))
    self.wait(10)
    self.play(Write(text4))
    self.play(Write(text5))
    self.play(Write(text6))
    self.wait(2)
    self.play(Transform(text4,text7))
    self.wait()
    self.play(Write(text8))
    self.wait()
    self.play(Write(text9))
    self.play(Write(text10))
    self.wait(10)
      


from manim import *

class TestScene7(Scene):
  def construct(self):
    text1 = Tex("Wilson's Theorem",color=YELLOW).shift(UP*1)
    text2 = Tex("$p|(p-1)!+1$",color=GREEN)
    text3 = Tex("$p^2|(p-1)!+1$?",color=BLUE)
    text4 = Tex("$5,13,563$").shift(DOWN*1)
    text5 = Tex("Atleast not below $5\cdot 10^8$",color=ORANGE).shift(DOWN*2)

    self.play(Write(text1))
    self.wait(1)
    self.play(Write(text2))
    self.wait(5)
    self.play(Transform(text2,text3))
    self.wait(6)
    self.play(Write(text4))
    self.wait(6)
    self.play(Write(text5))
    self.wait(10)


from manim import *

class TestScene(Scene):
  def construct(self):
    text = Tex("$e^{i\pi}$")
    self.play(Write(text),run_time=6)




















    
