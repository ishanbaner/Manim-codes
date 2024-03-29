from manim import *

class Intro(Scene):
    def construct(self):
        p1=[-5,-0.5,0]
        p2=[1,-0.5,0]
        p3=[2,-0.5,0]
        p4=[5,-0.5,0]
        ques=Tex("$a^3+(a+1)^3+\ldots+(a+6)^3=b^4+(b+1)^4$")
        lbr=BraceBetweenPoints(p1,p2)
        rbr=BraceBetweenPoints(p3,p4)
        seven=Tex("divisible by $7$").shift(DOWN*1+LEFT*2)
        nseven=Tex("not divisible by $7$").shift(DOWN*1+RIGHT*3)
        eq=Tex("$a^k+b^k=c^k$").shift(UP*1)
        st=Tex("Does not have integer solutions for $a,b,c$ for any integer $k>2$")
        neq=Tex("$a^k+b^k=c^k\,\,(mod\,\,p)$").shift(UP*1)
        st1=Tex("Does the same idea hold?")
        st2=Tex("For a certain $n$ and for $p>n$ solution exists !")
        no=Tex("Nope",color=RED).shift(DOWN*1)
        self.play(Write(ques))
        self.wait(8)
        self.play(Write(lbr))
        self.wait()
        self.play(Transform(lbr,seven))
        self.wait(1)
        self.play(Transform(lbr,rbr))
        self.wait()
        self.play(Transform(lbr,nseven))
        self.wait()
        self.play(FadeOut(lbr))
        self.wait(9)
        self.play(FadeOut(ques))
        self.play(Write(eq))
        self.play(Write(st))
        self.wait()
        self.play(Transform(eq,neq),FadeOut(st))
        self.wait()
        self.play(Write(st1))
        self.wait(4)
        self.play(Write(no))
        self.wait(3)
        self.play(FadeOut(no,st1))
        self.play(Write(st2))
        self.wait(15)

class Ramsey(Scene):
    def construct(self):
        k=Tex("$k\in \mathbb{N}$").shift(LEFT*1)
        c=Tex("$c$ colors").shift(RIGHT*1)
        triangle=VGroup()
        d1=Dot(point=UP*1)
        d2=Dot(point=LEFT*1.5)
        d3=Dot(point=RIGHT*1.5)
        d4=Dot(point=DOWN*1.5+LEFT*1)
        d5=Dot(point=DOWN*1.5+RIGHT*1)
        p1=d1.get_center()
        p2=d2.get_center()
        p3=d3.get_center()
        p4=d4.get_center()
        p5=d5.get_center()
        l1=Line(p1,p2,color=RED)
        l2=Line(p1,p3,color=BLUE)
        l3=Line(p1,p4,color=RED)
        l4=Line(p1,p5,color=BLUE)
        l5=Line(p2,p3,color=RED)
        l6=Line(p2,p4,color=BLUE)
        l7=Line(p2,p5,color=RED)
        l8=Line(p3,p4,color=BLUE)
        l9=Line(p3,p5,color=RED)
        l10=Line(p4,p5,color=BLUE)
        ll5=Line(p2,p3,color=RED)
        ll7=Line(p2,p5,color=RED)
        ll9=Line(p3,p5,color=RED)
        b2=Dot(point=LEFT*1.5)
        b3=Dot(point=RIGHT*1.5)
        b5=Dot(point=DOWN*1.5+RIGHT*1)
        n=Tex("$n$")
        nn=Tex("Say $n=5$").shift(UP*2+LEFT*2)
        triangle.add(ll5,ll7,ll9,b2,b3,b5)
        self.play(Write(k))
        self.play(Write(c))
        self.wait(2)
        self.play(FadeOut(k,c),Write(n))
        self.wait(2)
        self.play(Transform(n,nn),Write(l1),Write(l2),Write(l3),Write(l4),Write(l5),Write(l6),Write(l7),Write(l8),Write(l9),Write(l10),Write(d1),Write(d2),Write(d3),Write(d4),Write(d5))
        self.wait()
        self.play(triangle.animate.shift(RIGHT*3.5))
        self.wait(15)

class number(Scene):
    def construct(self):
        c=Tex("$c\in \mathbb{N}$ colors").shift(UP*1)
        n=Tex("There exists $n\in \mathbb{N}$")
        one=Tex("$1$",color=RED).shift(LEFT*2)
        two=Tex("$2$",color=BLUE).shift(LEFT*1)
        dotdot=Tex("$\ldots$")
        n1=Tex("$n-1$",color=GREEN).shift(RIGHT*1.5)
        fn=Tex("$n$",color=BLUE).shift(RIGHT*2.5)
        x=Tex("$x$",color=GREEN).shift(LEFT*1+DOWN*1)
        y=Tex("$y$",color=GREEN).shift(DOWN*1)
        z=Tex("$z$",color=GREEN).shift(RIGHT*1+DOWN*1)
        p=Tex("$+$").shift(LEFT*0.5).shift(DOWN*1)
        e=Tex("$=$").shift(RIGHT*0.5).shift(DOWN*1)
        sch=Tex("Schur's Theorem",color=RED).shift(UP*1)
        elem=VGroup()
        elem1=Tex("$\ldots$")
        elem.add(x,y,z)
        self.play(Write(c))
        self.wait(2)
        self.play(Write(n))
        self.wait()
        self.play(FadeOut(c,n))
        self.play(Write(one),Write(two),Write(dotdot),Write(n1),Write(fn))
        self.wait()
        self.play(Transform(elem1,elem))
        self.wait(1)
        self.play(Write(p),Write(e))
        self.wait()
        self.play(Write(sch))
        self.wait(10)

class finalclass(Scene):
    def construct(self):
        nk=Tex("$n$ as mentioned with $k$ colors")
        p=Tex("$p>n$")
        modp=Tex("$\{1,2,\ldots p-1\}$")
        a=Tex("$a$")
        ag=Tex("$a=g^{m_a}$").shift(DOWN*1)
        ag2=Tex("$a=g^{ki_a+j_a}$").shift(DOWN*1)
        circ=Circle(radius=0.25).shift(DOWN*0.9+RIGHT*1)
        rang=Tex("$0\leq j_a \leq k-1$",color=RED).shift(DOWN*1+RIGHT*2.5).scale(0.75)
        one=Tex("$1$",color=RED).shift(LEFT*2)
        two=Tex("$2$",color=BLUE).shift(LEFT*1)
        dotdot=Tex("$\ldots$")
        n1=Tex("$p-2$",color=GREEN).shift(RIGHT*1.5)
        fn=Tex("$p-1$",color=BLUE).shift(RIGHT*3)
        x=Tex("$g^{i_ak+j}$",color=GREEN).shift(LEFT*2+DOWN*1)
        y=Tex("$g^{i_bk+j}$",color=GREEN).shift(DOWN*1)
        z=Tex("$g^{i_ck+j}$",color=GREEN).shift(RIGHT*2+DOWN*1)
        pl=Tex("$+$").shift(LEFT*1).shift(DOWN*1)
        e=Tex("$=$").shift(RIGHT*1).shift(DOWN*1)
        x1=Tex("$g^{i_ak}$",color=GREEN).shift(LEFT*2+DOWN*1)
        y1=Tex("$g^{i_bk}$",color=GREEN).shift(DOWN*1)
        z1=Tex("$g^{i_ck}$",color=GREEN).shift(RIGHT*2+DOWN*1)
        x11=Tex("$a^{k}$",color=GREEN).shift(LEFT*2+DOWN*1)
        y11=Tex("$b^{k}$",color=GREEN).shift(DOWN*1)
        z11=Tex("$c^{k}$",color=GREEN).shift(RIGHT*2+DOWN*1)
        g=Tex("$g$",color=GREEN).shift(LEFT*2)
        self.play(Write(nk))
        self.wait(2)
        self.play(nk.animate.shift(UP*1.5))
        self.play(Write(p))
        self.wait()
        self.play(Transform(p,modp))
        self.wait(19)
        self.play(Write(g))
        self.wait(3)
        self.play(a.animate.shift(DOWN*1))
        self.play(Transform(a,ag))
        self.wait(3)
        self.play(Transform(a,ag2))
        self.wait(3)
        self.play(Write(circ))
        self.wait(4)
        self.play(Transform(circ,rang))
        self.wait(6)
        self.play(FadeOut(circ,a,nk,p,g))
        self.wait()
        self.play(Write(one),Write(two),Write(dotdot),Write(n1),Write(fn))
        self.wait()
        elem=VGroup()
        elem2=VGroup()
        elem3=VGroup()
        elem1=Tex("$\ldots$")
        elem.add(x,y,z)
        elem2.add(x1,y1,z1)
        elem3.add(x11,y11,z11)
        self.play(Transform(elem1,elem))
        self.play(Write(pl),Write(e))
        self.wait(7)
        self.play(Transform(elem1,elem2))
        self.wait(2)
        self.play(Transform(elem1,elem3))
        self.play(FadeOut(one,two,dotdot,n1,fn),elem1.animate.shift(UP*1),pl.animate.shift(UP*1),e.animate.shift(UP*1))
        self.wait(10)
