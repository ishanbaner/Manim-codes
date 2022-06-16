from manim import *
class intro(Scene):
    def construct(self):
        bos=Tex(r"$Z_{open}^{bos}=\dfrac{1}{\eta (q)^4}=\dfrac{(q^{\frac{-1}{24}})^{24}}{\prod\limits_{m=1}^{\infty}(1-q^m)^{24}}$").scale(0.5).shift(UP*1)
        black=Tex("$S_{Cardy}=4\pi\sqrt{\dfrac{cE}{6}}$").scale(0.5)
        q=Tex("$\chi_0=q^-1/60G(q)$").scale(0.5).shift(DOWN*1+LEFT*1)
        q1=Tex("$\chi_{1/5}=q^11/60H(q)$").scale(0.5).shift(DOWN*1+RIGHT*1)
        intr=Tex("An introduction to q-series and Ramanujan's theta functions",color=RED)
        self.play(Write(bos))
        self.play(Write(black))
        self.play(Write(q))
        self.play(Write(q1))
        self.wait(10)
        self.play(FadeOut(bos,black,q,q1))
        self.play(Write(intr))
        self.wait(10)

class notation(Scene):
    def construct(self):
        nota=Tex("Notations",color=RED)
        aq=Tex("$(a;q)_n=(1-a)(1-aq)(1-aq^2)\ldots(1-aq^{n-1})$")
        aqn=Tex("$(a)_n=(1-a)(1-aq)(1-aq^2)\ldots(1-aq^{n-1})$")
        z=Tex("$(a;q)_0=1$")
        inf=Tex("$(a;q)_{\infty}=\prod\limits_{k=0}^{\infty}(1-aq^k)$ where $|q|<1$").shift(DOWN*1)
        self.play(Write(nota))
        self.wait(5)
        self.play(nota.animate.shift(UP*2))
        self.play(Write(aq))
        self.wait(6)
        self.play(Transform(aq,aqn))
        self.wait()
        self.play(aq.animate.shift(UP*1))
        self.wait(2)
        self.play(Write(z))
        self.wait(1)
        self.play(Write(inf))
        self.wait(10)

class qseries(Scene):
    def construct(self):
        q=Tex("What is a q-series?")
        a=Tex("$(a;q)_n$")
        the=Tex("Theta function",color=GREEN)
        theta=Tex(r"$f(a,b):=\sum\limits_{n=-\infty}^{\infty}a^{\frac{n(n+1)}{2}}b^{\frac{n(n-1)}{2}}$ where $|ab|<1$")
        self.play(Write(q))
        self.wait(3)
        self.play(Transform(q,a))
        self.wait(11)
        self.play(Transform(q,the))
        self.wait(5)
        self.play(q.animate.shift(UP*2))
        self.play(Write(theta))
        self.wait(10)

class cases3(Scene):
    def construct(self):
        spe=Tex("3 special cases",color=RED)
        phi=Tex("$\phi(q):=f(q,q)=\sum\limits_{n=-\infty}^{\infty}q^{n^2}$").scale(0.7).shift(UP*1)
        psi=Tex(r"$\psi(q):=f(q,q^3)=\sum\limits_{n=0}^{\infty}q^{\frac{n(n+1)}{2}}$").scale(0.7)
        f=Tex(r"$f(-q):=f(-q,-q^2)=\sum\limits_{n=-\infty}^{\infty}(-1)^nq^{\frac{n(3n-1)}{2}}$").scale(0.7).shift(DOWN*1)
        self.play(Write(spe))
        self.wait(5)
        self.play(spe.animate.shift(UP*2))
        self.play(Write(phi))
        self.play(Write(psi))
        self.play(Write(f))
        self.wait(10)

class the1(Scene):
    def construct(self):
        fun=Tex("Some Fundamental Theorems",color=RED)
        qana=Tex("q-analogue of binomial theorem",color=GREEN)
        summ=Tex("$\sum\limits_{n=0}^{\infty}\dfrac{(a)_n}{(q)_n}z^n=\dfrac{(az)_{\infty}}{(z)_{\infty}}$")
        such=Tex("where $|q|,|z|<1$").shift(DOWN*2)
        summ2=Tex(r"$\lim\limits_{q\to 1}\dfrac{(q^a)_n}{(q)_n}=\lim\limits_{q\to 1}\dfrac{\prod\limits_{k=0}^{n-1}(1-q^{a+k})}{\prod\limits_{k=0}^{n-1}(1-q^{1+k})}$")
        summ3=Tex(r"$\lim\limits_{q\to 1}\dfrac{(q^a)_n}{(q)_n}=\dfrac{a(a+1)(a+2)\ldots (a+n-1)}{n!}$")
        summ4=Tex("$\sum\limits_{k=0}^{\infty}\dfrac{a(a+1)(a+2)\ldots (a+n-1)}{n!}z^n$").shift(LEFT*2)
        summ5=Tex("$=\dfrac{(az)_{\infty}}{(z)_{\infty}}$").shift(RIGHT*3.1)
        summ6=Tex("$=\prod\limits_{k=0}^{a-1}\dfrac{1}{1-z}$").shift(RIGHT*3.2)
        summ7=Tex("$=(1-z)^{-a}$").shift(RIGHT*3.2)
        self.play(Write(fun))
        self.wait(7)
        self.play(FadeOut(fun))
        self.play(Write(qana))
        self.play(qana.animate.shift(UP*2))
        self.play(Write(summ))
        self.play(Write(such))
        self.wait(7)
        self.play(FadeOut(qana,summ,such))
        self.play(Write(summ2))
        self.wait(5)
        self.play(Transform(summ2,summ3))
        self.wait(2)
        self.play(FadeOut(summ2))
        self.play(Write(summ4))
        self.play(Write(summ5))
        self.play(Transform(summ5,summ6))
        self.play(Transform(summ5,summ7))
        self.wait(10)

class corollary(Scene):
    def construct(self):
        cor1=Tex("$\sum\limits_{n=0}^{\infty}\dfrac{z^n}{(q)_n}=\dfrac{1}{(z)_{\infty}}$ , $|z|<1$").shift(UP*2)
        cor2=Tex("$\sum\limits_{n=0}^{\infty}\dfrac{(-z)^nq^{n(n-1)/2}}{(q)_n}=(z)_{\infty}$, $|z|<\infty$")
        self.play(Write(cor1))
        self.play(Write(cor2))
        self.wait(15)

class Jacobi(Scene):
    def construct(self):
        jac=Tex("Jacobi's triple product identity",color=RED)
        exp=Tex("$\sum\limits_{n=-\infty}^{\infty}z^nq^{n^2}=(-zq:q^2)_{\infty}(-q/z:q^2)_{\infty}(q^2:q^2)_{\infty}$")
        exp2=Tex("$f(a,b)=(-a;ab)_{\infty}(-b:ab)_{\infty}(ab,ab)_{\infty}$")
        self.wait(10)
        self.play(Write(jac))
        self.wait(3)
        self.play(jac.animate.shift(UP*2))
        self.wait(2)
        self.play(Write(exp))
        self.wait(3)
        self.play(Transform(exp,exp2))
        self.wait(10)

class Proof(Scene):
    def construct(self):
        cor2=Tex("$\sum\limits_{n=0}^{\infty}\dfrac{(-z)^nq^{n(n-1)/2}}{(q)_n}=(z)_{\infty}$",color=GREEN)
        exp1=Tex("$\sum\limits_{n=0}^{\infty}\dfrac{(zq)^nq^{n(n-1)}}{(q^2;q^2)_n}=(-zq;q^2)_{\infty}$",color=GREEN)
        exp11=Tex("$\sum\limits_{n=0}^{\infty}\dfrac{(zq)^nq^{n(n-1)}}{(q^2;q^2)_n}=(-zq;q^2)_{\infty}$",color=GREEN).scale(0.5).shift(UP*2)
        exp2=Tex("$\sum\limits_{n=0}^{\infty}\dfrac{z^nq^{n^2}}{(q^2;q^2)_n}=(-zq;q^2)_{\infty}$",color=GREEN)
        exp3=Tex("$\dfrac{1}{(q^2;q^2)_{\infty}}\sum\limits_{n=-\infty}^{\infty}z^nq^{n^2}(q^{2n+2};q^2)_{\infty}=(-zq;q^2)_{\infty}$",color=GREEN)
        note=Tex("$(q^{2n+2};q^2)_{\infty}=0$ if $n$ is negative").shift(DOWN*2)
        note2=Tex("$\prod\limits_{k=0}^{\infty}(1-q^{2n+2}q^{2k})$").shift(DOWN*2)
        box=Rectangle(width=3,height=1,color=YELLOW).shift(RIGHT*0.6)
        exp4=Tex("$\dfrac{1}{(q^2;q^2)_{\infty}}\sum\limits_{n=-\infty}^{\infty}z^nq^{n^2}\sum\limits_{r=0}^{\infty}\dfrac{(-1)^rq^{(2n+2)r+r^2-r}}{(q^2;q^2)_r}=(-zq;q^2)_{\infty}$",color=GREEN)
        box1=Rectangle(width=4,height=1,color=YELLOW).shift(UP*2)
        exp5=Tex("$\dfrac{1}{(q^2;q^2)_{\infty}}\sum\limits_{r=0}^{\infty}\dfrac{(-1)^rz^{-r}q^r}{(q^2;q^2)_r}\sum\limits_{n=-\infty}^{\infty}z^{n+r}q^{(n+r)^2}=(-zq;q^2)_{\infty}$",color=GREEN)
        exp6=Tex(r"$\dfrac{1}{(q^2;q^2)_{\infty}}\sum\limits_{r=0}^{\infty}\dfrac{\left(\dfrac{-q}{z}\right)^r}{(q^2;q^2)_r}\sum\limits_{n=-\infty}^{\infty}z^{n+r}q^{(n+r)^2}=(-zq;q^2)_{\infty}$",color=GREEN)
        exp7=Tex(r"$\dfrac{1}{(q^2;q^2)_{\infty}}\sum\limits_{r=0}^{\infty}\dfrac{\left(\dfrac{-q}{z}\right)^r}{(q^2;q^2)_r}\sum\limits_{m=-\infty}^{\infty}z^{m}q^{(m)^2}=(-zq;q^2)_{\infty}$",color=GREEN)
        cor3=Tex("$\sum\limits_{n=-\infty}^{\infty}\dfrac{z^n}{(q)_n}=\dfrac{1}{(z)_n}$",color=YELLOW).shift(UP*2)
        exp8=Tex(r"$\dfrac{1}{(q^2;q^2)_{\infty}(\frac{-q}{z};q^2)_{\infty}}\sum\limits_{m=-\infty}^{\infty}z^{m}q^{(m)^2}=(-zq;q^2)_{\infty}$",color=GREEN)
        box3=Rectangle(width=3,height=2.7,color=YELLOW).shift(LEFT*1.9)
        exp9=Tex(r"$\sum\limits_{m=-\infty}^{\infty}z^{m}q^{(m)^2}=(-zq;q^2)_{\infty}(q^2;q^2)_{\infty}(\frac{-q}{z};q^2)_{\infty}$",color=GREEN)
        self.play(Write(cor2))
        self.wait(10)
        self.play(Transform(cor2,exp1))
        self.wait(4)
        self.play(Transform(exp1,exp11))
        self.wait(2)
        self.play(Transform(cor2,exp2))
        self.wait(2)
        self.play(Transform(cor2,exp3))
        self.wait(23)
        self.play(Write(note))
        self.wait(5)
        self.play(Transform(note,note2))
        self.wait(10)
        self.play(FadeOut(note))
        self.play(Write(box))
        self.wait(4)
        self.play(Write(box1))
        self.wait(2)
        self.play(FadeOut(box))
        self.play(Transform(cor2,exp4),FadeOut(box1,exp1))
        self.wait(2)
        self.play(Transform(cor2,exp5))
        self.wait(3)
        self.play(Transform(cor2,exp6))
        self.wait(3)
        self.play(Transform(cor2,exp7))
        self.wait(2)
        self.play(Write(cor3))
        self.wait(2)
        self.play(Write(box3))
        self.wait(2)
        self.play(FadeOut(box3,cor3))
        self.wait(2)
        self.play(Transform(cor2,exp8))
        self.wait(2)
        self.play(Transform(cor2,exp9))
        self.wait(2)
        self.play(FadeOut(cor2))
        self.wait(10)

class warning(Scene):
    def construct(self):
        warn=Tex("WARNING",color=RED).shift(UP*1.5)
        wa=Tex("To much notations ahead")
        self.play(Write(warn))
        self.play(Write(wa))
        self.play(FadeOut(warn,wa))        

class image(Scene):
    def construct(self):
        aq=Tex("$(a;q)_n$").scale(2)
        self.add(aq)