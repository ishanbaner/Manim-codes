from manim import *
class intro(Scene):
    def construct(self):
        topog=Tex("Topological group",color=GREEN).shift(UP*1+LEFT*2.4)
        topom=Tex("(Topological manifold)",color=BLUE).shift(UP*1+RIGHT*2.4)
        iso=Tex("$\cong$")
        lie=Tex("Lie Group",color=YELLOW).shift(DOWN*1)
        self.play(Write(topog),run_time=1)
        self.wait()
        self.play(Write(topom),run_time=1)
        self.play(Write(iso))
        self.play(Write(lie))
        self.wait(30)

class topogro(Scene):
    def construct(self):
        gro=VGroup()
        topog=Tex("Topological group",color=GREEN).shift(UP*1+LEFT*2.4)
        topom=Tex("(Topological manifold)",color=BLUE).shift(UP*1+RIGHT*2.4)
        iso=Tex("$\cong$")
        lie=Tex("Lie Group",color=YELLOW).shift(DOWN*1)
        gro.add(topog,topom,iso,lie)
        wh=Tex("Topological Group?",color=GREEN)
        g=Tex("$G$",color=GREEN)
        gg=MathTex(r"(G,\tau_G)",color=BLUE)
        pr=Tex("$(x,y)\mapsto xy$")
        inv=Tex("$x \mapsto x^{-1}$").shift(DOWN*1)
        self.add(gro)
        self.play(Transform(topog,wh),FadeOut(topom,iso,lie))
        self.wait(2)
        self.play(Transform(topog,g))
        self.wait()
        self.play(Transform(topog,gg))
        self.wait(3)
        self.play(topog.animate.shift(UP*1),Write(pr))
        self.wait()
        self.play(Write(inv))
        self.wait(5)

class topoman(Scene):
    def construct(self):
        gro=VGroup()
        topog=Tex("Topological group",color=GREEN).shift(UP*1+LEFT*2.4)
        topom=Tex("(Topological manifold)",color=BLUE).shift(UP*1+RIGHT*2.4)
        iso=Tex("$\cong$")
        lie=Tex("Lie Group",color=YELLOW).shift(DOWN*1)
        gro.add(topog,topom,iso,lie)
        topo=Tex("Topological manifold?",color=BLUE)
        x=Tex("$X$",color=RED)
        loc=Tex("Locally resembles a Euclidean space").shift(DOWN*0.5)
        sp=Circle()
        d=Dot().shift(RIGHT*0.2)
        ssp=Circle().scale(0.4).shift(RIGHT*0.2)
        sp.set_fill(RED,opacity=0.5)
        ssp.set_fill(GREEN,opacity=0.5)
        ssp.set_stroke(color=GREEN,width=0.1)
        sspc=Circle().scale(0.4).shift(RIGHT*0.2)
        sspc.set_fill(GREEN,opacity=0.5)
        sspc.set_stroke(color=GREEN,width=0.1)
        sspcc=Circle().scale(0.7).shift(RIGHT*2.7)
        sspcc.set_fill(BLUE,opacity=0.5)
        sspcc.set_fill(color=BLUE)
        sspcc.set_stroke(color=BLUE,width=0.1)
        ax=Axes().scale(0.4).shift(RIGHT*2.5)
        g1=VGroup()
        g1.add(sp,ssp,d,sspc)
        self.add(gro)
        self.wait()
        self.play(Transform(topom,topo),FadeOut(topog,iso,lie))
        self.wait()
        self.play(Transform(topom,x))
        self.wait()
        self.play(FadeIn(loc))
        self.wait(8)
        self.play(FadeOut(loc,topom))
        self.play(FadeIn(sp))
        self.play(Write(d))
        self.play(FadeIn(ssp))
        self.wait(2)
        self.play(g1.animate.shift(LEFT*1),FadeIn(ax),Transform(sspc,sspcc))
        self.wait(5)

class Lie(Scene):
    def construct(self):
        gro=VGroup()
        topog=Tex("Topological group",color=GREEN).shift(UP*1+LEFT*2.4)
        topom=Tex("(Topological manifold)",color=BLUE).shift(UP*1+RIGHT*2.4)
        iso=Tex("$\cong$")
        lie=Tex("Lie Group",color=YELLOW).shift(DOWN*1)
        gro.add(topog,topom,iso,lie)
        liec=Tex("Lie Group?",color=YELLOW)
        sm=Tex("Smooth Manifold")
        self.add(gro)
        self.wait()
        self.play(Transform(lie,liec),FadeOut(topog,topom,iso))
        self.wait(1)
        self.play(Transform(lie,sm))
        self.wait()

class smooth(Scene):
    def construct(self):
        sp=Circle()
        d=Dot().shift(RIGHT*0.2)
        ssp=Circle().scale(0.4).shift(RIGHT*0.2)
        sp.set_fill(RED,opacity=0.5)
        ssp.set_stroke(color=GREEN,width=0.1)
        ssp.set_fill(GREEN,opacity=0.5)
        sspc=Circle().scale(0.4).shift(RIGHT*0.2)
        sspc.set_fill(GREEN,opacity=0.5)
        sspc.set_stroke(color=GREEN,width=0.1)
        sspcc=Circle().scale(0.7).shift(RIGHT*2.7)
        sspcc.set_fill(BLUE,opacity=0.5)
        sspcc.set_fill(color=BLUE)
        sspcc.set_stroke(color=BLUE,width=0.1)
        ax=Axes().scale(0.4).shift(RIGHT*2.5)
        u=Tex("$U$").shift(LEFT*1.6)
        ph=Tex(r"$\phi$").shift(UP*1+RIGHT*1)
        arr=Arrow(start=d.get_center()+LEFT*1,end=sspcc.get_center()+LEFT*0.3).shift(UP*0.3)
        pair=Tex("$(U,\phi)$")
        ch=Tex("Chart").shift(DOWN*1)
        g1=VGroup()
        g1.add(sp,ssp,d,sspc)
        self.add(g1)
        self.wait()
        self.play(g1.animate.shift(LEFT*1),FadeIn(ax),Transform(sspc,sspcc))
        self.wait()
        self.play(Write(u))
        self.wait()
        self.play(Write(arr))
        self.wait()
        self.play(Transform(arr,ph))
        self.wait()
        self.play(Transform(arr,pair),Transform(u,pair),FadeOut(g1,ax,sspcc))
        self.wait()
        self.play(Write(ch))
        self.wait()

class comp(Scene):
    def construct(self):
        heart=VGroup()
        a1=Arc(angle=PI,color=RED)
        a2=Arc(angle=PI,color=RED).shift(RIGHT*2)
        b1=Line(start=LEFT*1,end=DOWN*2+RIGHT*1,color=RED)
        b2=Line(start=RIGHT*3,end=DOWN*2+RIGHT*1,color=RED)
        heart.add(a1,a2,b1,b2)
        heart.shift(LEFT*1+UP*0.5).scale(0.25)
        c1=Tex("$(U,\phi)$").shift(LEFT*1.5)
        c2=Tex("$(V,\psi)$").shift(RIGHT*1.5)
        f1=Tex(r"$\phi\circ\psi^{-1}:\psi(U\cap V)\to\phi(U\cap V)$").shift(UP*0.5)
        f2=Tex(r"$\psi\circ\phi^{-1}:\phi(U\cap V)\to\psi(U\cap V)$").shift(DOWN*0.5)
        u=Circle().shift(RIGHT*0.4)
        v=Circle().shift(LEFT*0.4)
        phuv=Circle().scale(0.5).shift(LEFT*3)
        psuv=Circle().scale(0.5).shift(RIGHT*3)
        phuv.set_fill(ORANGE,opacity=0.5)
        psuv.set_fill(YELLOW,opacity=0.5)
        u.set_fill(RED,opacity=0.4)
        v.set_fill(BLUE,opacity=0.4)
        inter=Intersection(u,v,color=GREEN)
        inter1=Intersection(u,v,color=GREEN)
        ar1=Arrow(start=phuv.get_center(),end=u.get_center()).shift(LEFT*0.1)
        ar2=Arrow(start=v.get_center(),end=psuv.get_center()).shift(RIGHT*0.1)
        a11=Arrow(end=phuv.get_center(),start=u.get_center()).shift(LEFT*0.1)
        a21=Arrow(end=v.get_center(),start=psuv.get_center()).shift(RIGHT*0.1)
        self.play(Write(c1),Write(c2))
        self.wait(2)
        self.play(Write(heart))
        self.wait(5)
        self.play(FadeOut(c1,c2,heart))
        self.play(Write(f1))
        self.play(Write(f2))
        self.wait(2)
        self.play(FadeOut(f1,f2))
        self.wait()
        self.play(Write(u))
        self.play(Write(v))
        self.wait(6)
        self.play(Transform(inter,phuv))
        self.wait(4)
        self.play(Transform(inter1,psuv))
        self.wait()
        self.play(Write(ar1),Write(ar2))
        self.wait()
        self.play(Transform(ar1,a11),Transform(ar2,a21))
        self.wait(5)

class atlas(Scene):
    def construct(self):
        at=Tex(r"$\{(U_{\alpha},\phi_{\alpha})\}$")
        union=Tex(r"$M=\bigcup_{\alpha}U_{\alpha}$").shift(DOWN*0.5)
        atlas=Tex("Atlas on $M$",color=RED).shift(DOWN*1.5)
        maximal=Tex("$A$")
        s=Tex(r"$A\subseteq A_1$")
        s1=Tex("$A=A_1$")
        man=Tex("$(M,A)$")
        self.play(Write(at))
        self.wait()
        self.play(at.animate.shift(UP*0.5))
        self.wait(3)
        self.play(Write(union))
        self.wait(2)
        self.play(Write(atlas))
        self.wait(2)
        self.play(FadeOut(at,union,atlas))
        self.wait(3)
        self.play(Write(maximal))
        self.play(Transform(maximal,s))
        self.wait(1)
        self.play(Transform(maximal,s1))
        self.wait(3)
        self.play(Transform(maximal,man))
        self.wait(20)

class Liereturn(Scene):
    def construct(self):
        state=Tex("Lie Group",color=YELLOW)
        g=Tex("$G$",color=YELLOW)
        mult=Tex(r"$(x,y)\to xy$")
        inv=Tex(r"$x\to x^{-1}$").shift(DOWN*1)
        self.play(Write(state))
        self.wait(2)
        self.play(Transform(state,g))
        self.wait(5)
        self.play(state.animate.shift(UP*1))
        self.play(Write(mult))
        self.play(Write(inv))
        self.wait(10)

class results(Scene):
    def construct(self):
        pr=Tex("Progress")
        y1=Tex("1933").shift(UP*1)
        j=Tex("John von Neumann")
        com=Tex("Compact groups",color=GREEN).shift(DOWN*1)
        y2=Tex("1934").shift(UP*1)
        l=Tex("Lev Pontryagin")
        lcom=Tex("Locally compact abelian groups",color=GREEN).shift(DOWN*1)
        y3=Tex("1950").shift(UP*1)
        gmz=Tex("Gleason-Montgomery-Zippin")
        res=Tex("Topological group (manifold)$ \cong $ Lie Group",color=GREEN).shift(DOWN*1)
        y4=Tex("1953").shift(UP*1)
        h=Tex("Hidehiko Yamabe")
        g=Tex("$G$")
        sp=Circle(color=BLUE)
        sp.set_fill(color=BLUE,opacity=0.5)
        unit=Dot()
        sp2=Circle().scale(0.5)
        sp2.set_stroke(color=GREEN,width=0.1)
        sp2.set_fill(color=GREEN,opacity=0.5)
        sp3=Circle().scale(0.7)
        sp3.set_fill(color=YELLOW,opacity=0.5)
        sp3.set_stroke(color=YELLOW,width=0.1)
        sp4=Circle().scale(0.25)
        sp4.set_fill(color=RED,opacity=0.5)
        sp4.set_stroke(color=RED,width=0.1)
        g1=Tex("$G'$").shift(RIGHT*1.5)
        n=Tex("$N$").shift(LEFT*1.5)
        gn=Tex("$G'/N$")
        iso=Tex("$\cong $ Lie Group").shift(DOWN*0.5)
        self.play(Write(pr))
        self.wait(1)
        self.play(FadeOut(pr))
        self.wait()
        self.play(Write(y1))
        self.wait(2)
        self.play(Write(j))
        self.wait()
        self.play(Write(com))
        self.wait(2)
        self.play(Transform(y1,y2),FadeOut(j,com))
        self.wait()
        self.play(Write(l))
        self.wait()
        self.play(Write(lcom))
        self.wait(4)
        self.play(Transform(y1,y3),FadeOut(l,lcom))
        self.wait()
        self.play(Write(gmz))
        self.wait()
        self.play(Write(res))
        self.wait(15)
        self.play(FadeOut(gmz,res),Transform(y1,y4))
        self.wait(1)
        self.play(Write(h))
        self.wait(14)
        self.play(FadeOut(y1),Transform(h,g))
        self.wait()
        self.play(Transform(h,sp))
        self.wait()
        self.play(Write(unit))
        self.wait(2)
        self.play(Write(sp2))
        self.wait(3)
        self.play(Write(sp3))
        self.wait(2)
        self.play(Write(sp4))
        self.wait()
        self.play(Transform(sp3,g1))
        self.wait()
        self.play(Transform(sp4,n))
        self.wait()
        self.play(FadeOut(h,unit,sp2),Transform(sp3,gn),Transform(sp4,gn))
        self.wait()
        self.play(sp3.animate.shift(UP*0.5),sp4.animate.shift(UP*0.5),Write(iso))
        self.wait(10)

class notuni(Scene):
    def construct(self):
        topog=Tex("Topological group",color=GREEN).shift(UP*1+LEFT*2.4)
        topom=Tex("(Topological manifold)",color=BLUE).shift(UP*1+RIGHT*2.4)
        iso=Tex("$\cong$")
        lie=Tex("Lie Group",color=YELLOW).shift(DOWN*1)
        nu=Tex("Not a unique statement",color=RED).shift(DOWN*2+RIGHT*2)
        self.play(Write(topog),run_time=1)
        self.wait()
        self.play(Write(topom),run_time=1)
        self.play(Write(iso))
        self.play(Write(lie))
        self.wait()
        self.play(Write(nu))
        self.wait(5)

