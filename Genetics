from manim import *

class TestScene1(Scene):
  def construct(self):
      AlleleI = Tex("Allele",color=RED)
      Allele = Tex("Diiferent forms of gene representing a character")
      White = Tex(r"White $\to$ A ",color=WHITE)
      Red = Tex(r"Red $\to$ a",color=RED).shift(DOWN*1)
      Name = Tex("Hardy Weinberg Principle").shift(UP*3)
      Allele1 = Tex("A").shift(LEFT*2 , UP*1)
      Allele2 = Tex("a",color=RED).shift(LEFT*2)
      F1 = Tex("Frequency(A)").shift(UP*1)
      F2 = Tex("Frequency(a)",color=RED)
      FA = Tex("$=p$").shift(RIGHT*2 , UP*1)
      Fa = Tex("=q",color=RED).shift(RIGHT*2)

      self.play(Write(AlleleI))
      self.wait(3)
      self.play(Transform (AlleleI,Allele))
      self.wait(4)
      self.play(Transform(AlleleI , White))
      self.wait()
      self.play(FadeIn(Red))
      self.wait(2)
      self.play(FadeOut(AlleleI))
      self.wait()
      self.play(FadeOut(Red))
      self.wait(6)
      self.play(Write (Name))
      self.wait()
      self.play(Write (F1))
      self.wait()
      self.play(Write (F2))
      self.wait()
      self.play(Write (FA))
      self.wait()
      self.play(Write (Fa))
      self.wait(5)


from manim import *

class TestScene2(Scene):
  def construct(self):
    FAA = Tex("Frequency(AA)$=p^2$").shift(UP*1)
    FAa = Tex("Frequency(Aa)$=2pq$")
    Faa = Tex("Frequency(aa)$=q^2$").shift(DOWN*1)
    Note = Tex("We need a pair of alleles to represent a character").shift(DOWN*2)

    self.play(Write (FAA))
    self.wait()
    self.play(Write (FAa))
    self.wait()
    self.play(Write (Faa))
    self.wait(4)
    self.play(Write (Note))
    self.wait(10)


from manim import *

class TestScene3(Scene):
  def construct(self):
    Name = Tex("Bernstein's problem").shift(UP*3)
    Coordinate = Tex("$(x_1 , x_2 , \ldots x_n)$").shift(UP*2)
    Sum = Tex("$\sum\limits_{i=1}^n x_i=1\,\,\, x_i\geq 0$").shift(UP*1)
    Simplex = Tex(r"$S \to$ Set of all such subsets of $\mathbb{R}^n$")
    Vertices1 = Tex("Vertices $\Rightarrow$ Basis elements of $S$").shift(DOWN*1)
    Vertices2 = Tex("$\Rightarrow$ Different types of individuals in the population").shift(DOWN*2)
    Elements = Tex("$e_i$",color = YELLOW).shift(DOWN*2)

    self.play(Write (Name))
    self.wait(7)
    self.play(Write (Coordinate))
    self.wait(3)
    self.play(Write (Sum))
    self.wait(3)
    self.play(Write (Simplex))
    self.wait(4)
    self.play(Write (Vertices1))
    self.wait(2)
    self.play(Write (Vertices2))
    self.wait(2)
    self.play(Transform(Vertices2,Elements))
    self.wait(5)
    
    
    
    
from manim import *

class TestScene4(Scene):
  def construct(self):
      EI = Tex("$e_i$",color=RED).shift(UP*1,LEFT*1)
      EJ = Tex("$e_j$").shift(UP*1,RIGHT*1)
      EK = Tex("$e_k$",color=RED).shift(DOWN*1)
      arrow1 = Arrow(start=UP*1+LEFT*1,end=DOWN,color=RED)
      arrow2 = Arrow(start=UP*1+RIGHT*1,end=DOWN)
      prob = Tex("$\gamma_{ijk}$ or $\gamma_{jik}$").shift(DOWN*2)

      self.play(Write(EI))
      self.play(Write(EJ))
      self.play(Write(arrow1))
      self.play(Write(arrow2))
      self.play(Write(EK))
      self.wait()
      self.play(Write(prob))
      self.wait(5)
      
      

from manim import *

class TestScene5(Scene):
  def construct(self):      
      SUM = Tex("$\sum\limits_{k=1}^{n}\gamma_{ijk}=1\,\,(i,j=1,2,\ldots n)$")
      Qo = Tex(r"$V:S \to S$").shift(DOWN*1)
      op = Tex("$V^2=V$").shift(DOWN*1)

      self.play(Write(SUM))
      self.wait(9)
      self.play(Write(Qo))
      self.wait(2)
      self.play(Transform(Qo,op))
      self.wait(7)


from manim import *

class TestScene6(Scene):
  def construct(self):
    WBasis = Tex("What is a Basis ?").shift(UP*3)
    Reals = Tex("$\mathbb{R}^n$", color = RED).shift(UP*2)
    Basis = Tex("$v_1, v_2, \ldots v_n$")
    Lincomb = Tex("$a_1v_1 + a_2v_2, \ldots a_nv_n = r \in \mathbb{R}$")
    LI = Tex("Linearly Independent",color =YELLOW).shift(DOWN*1)
    Linind = Tex("$a_1v_1 + a_2v_2, \ldots a_nv_n = 0$").shift(DOWN*1)
    Zero = Tex("$a_1=a_2=\ldots=a_n=0$").shift(DOWN*2)

    self.play(Write(WBasis))
    self.wait(2)
    self.play(Write(Reals))
    self.wait(6)
    self.play(Write(Basis))
    self.wait()
    self.play(Transform(Basis , Lincomb))
    self.wait(5)
    self.play(Write(LI))
    self.wait(2)
    self.play(Transform(LI , Linind))
    self.wait(1)
    self.play(Write(Zero))
    self.wait(5)


from manim import *

class TestScene7(Scene):
  def construct(self):
    EV = Tex("Evolution algebra").shift(UP*2)
    Basis = Tex("$G_1,G_2,\ldots G_n $",color=YELLOW).shift(UP*1)
    Multiply1 = Tex(r"$G_i \cdot G_j = 0$ if $i\neq j$",color=BLUE)
    Multiply2 = Tex("$G_i \cdot G_i = \sum\limits_{j}p_{ij}G_j$",color=BLUE).shift(DOWN*1)

    self.play(Write(EV))
    self.wait(6)
    self.play(Write(Basis))
    self.wait(11)
    self.play(Write(Multiply1))
    self.wait(5)
    self.play(Write(Multiply2))
    self.wait(10)

from manim import *

class TestScene8(Scene):
  def construct(self):
    Train = Tex("Train Algebra").shift(UP*2)
    K = Tex("$K$",color=RED).shift(LEFT*1 , UP*1)
    W = Tex("$w$",color=YELLOW).shift(RIGHT*1 , UP*1)
    Elem = Tex("$c_1,c_2,\ldots c_n \in K$")
    Sum = Tex("$c_1+c_2+\ldots c_n = 0$")
    Trapol = Tex("$a^n + c_1 w(a) a^{n-1} + c_2 w(a)^2 a^{n-2} + \ldots c_n w(a)^n = 0 $").shift(DOWN*1)
    B = Tex("$a \in B$",color=BLUE).shift(DOWN*2)

    self.play(Write(Train))
    self.wait(8)
    self.play(Write(K))
    self.wait(3)
    self.play(Write(W))
    self.wait(2)
    self.play(Write(Elem))
    self.wait(3)
    self.play(Transform(Elem,Sum))
    self.wait(5)
    self.play(Write(Trapol))
    self.wait(5)
    self.play(Write(B))
    self.wait(12)


from manim import *

class TestScene9(Scene):
  def construct(self):
    genetics1 = Tex("\"Genetics is where we come from.",color=BLUE).shift(UP*1)
    genetics2 = Tex("It is deeply natural to want to know\"",color=BLUE)
    author = Tex("~Ellen Ullman").shift(DOWN*1)

    self.play(Write(genetics1))
    self.play(Write(genetics2))
    self.wait()
    self.play(Write(author))
    self.wait()


from manim import *

class TestScene10(Scene):
  def construct(self):
    genetics = Tex("Genetics")
    algebra = Tex("Genetic Algebra",color=BLUE)

    self.play(Write(genetics))
    self.wait(10)
    self.play(Transform(genetics,algebra))
    self.wait(5)


from manim import *

class TestScene11(Scene):
  def construct(self):
    Text1 = Tex("Don't get misleaded").shift(UP*1)
    Text2 = Tex("Genetic algebra is a lot huge")
    Text3 = Tex("And indeed a beautiful subject to work on").shift(DOWN*1)

    self.play(Write(Text1))
    self.wait()
    self.play(Write(Text2))
    self.wait()
    self.play(Write(Text3))
    self.wait()


from manim import *

class TestScene12(Scene):
  def construct(self):
    profile = Tex("$e^{i\pi}$")

    self.play(Write(profile , run_time=3))
    
      
      
