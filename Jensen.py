from manim import *

class App(Scene):
    def construct(self):
        app=Tex("A ton of applications").scale(1).shift(UP*1)
        con=Tex("A rather easy to understand concept",color=GREEN).scale(1)
        self.play(Write(app))
        self.wait(5)
        self.play(Write(con))
        self.wait(6)

class Jensendef(Scene):
    def construct(self):
        Jensen=Tex("Jensen's Inequality",color=RED).scale(1)
        func=Tex("f(x)",color=GREEN)
        conv=Tex("(Convex)",color=BLUE).shift(RIGHT*2)
        ineq=Tex(r"$f(p_1x_1+p_2x_2+\ldots p_nx_n)\leq p_1f(x_1)+p_2f(x_2)+\ldots p_nf(x_n)$").shift(DOWN*1)
        p=Tex("$p_1+p_2+\ldots p_n=1$").shift(DOWN*2)
        ineq2=Tex("$f(\mathbb{E}(X))\leq \mathbb{E}(f(X))$").shift(DOWN*1)
        self.play(Write(Jensen))
        self.wait(2)
        self.play(Jensen.animate.shift(UP*1))
        self.play(Write(func))
        self.play(Write(conv))
        self.wait(6)
        self.play(Write(ineq))
        self.wait(14)
        self.play(Write(p))
        self.wait(5)
        self.play(Transform(ineq,ineq2),FadeOut(p))
        self.wait(15)

class Convex(Scene):
    def construct(self):
        ax=Axes(x_range=(0,10),y_range=(0,100,10),x_length=5,y_length=5,axis_config={"include_tip": False})
        def func(x):
            return(0.09*(x)**3)
        def func2(x):
            return(100)
        def func3(x):
            return(10*x)
        graph=ax.plot(func,color=GREEN)
        t=ValueTracker(3)
        t2=ValueTracker(9)
        t3=ValueTracker(6)
        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point,color=YELLOW)
        initial_point1 = [ax.coords_to_point(t2.get_value(), func(t2.get_value()))]
        dot2 = Dot(point=initial_point1,color=YELLOW)
        initial_point2 = [ax.coords_to_point(t.get_value(), func3(t.get_value()))]
        dotl = Dot(point=initial_point2)
        initial_point3 = [ax.coords_to_point(t2.get_value(), func3(t2.get_value()))]
        init1 = [ax.coords_to_point(t3.get_value(), func(t3.get_value()))]
        init2 = [ax.coords_to_point(t3.get_value(), func3(t3.get_value()))]
        inity = [ax.coords_to_point(0, func(t.get_value()))]
        inity2 = [ax.coords_to_point(0, func(t2.get_value()))]
        inity3 = [ax.coords_to_point(0, (func(t.get_value())+func(t2.get_value()))/2)]
        inityn = [ax.coords_to_point(0, func3(t.get_value()))]
        inityn2 = [ax.coords_to_point(0, func3(t2.get_value()))]
        initynm1 = [ax.coords_to_point(0, func(t3.get_value()))]
        initynm2 = [ax.coords_to_point(0, func3(t3.get_value()))]
        inityn3 = [ax.coords_to_point(0, (func3(t.get_value())+func3(t2.get_value()))/2)]
        dotm = Dot(point=initial_point3)
        dot3=Dot(point=LEFT)
        i=[ax.coords_to_point(3,0)]
        j=[ax.coords_to_point(9,0)]
        k=[ax.coords_to_point(6,0)]
        pointx=Dot(point= i)
        pointy=Dot(point= j)
        pointm=Dot(point= k)
        dot4=Dot(point=RIGHT*2+UP*2)
        l=ax.plot(func2)
        stline=Line(LEFT,RIGHT*2+UP*2)
        area = ax.get_area(l, [0, 10], bounded_graph=graph,color=BLUE, opacity=0.5)
        li=ax.plot(func3,color=GREEN)
        dote1=Dot(point=init1,color=BLUE)
        dote2=Dot(point=init2,color=BLUE)
        dotyei=Dot(point=initynm1,color=BLUE)
        dotyef=Dot(point=initynm2,color=BLUE)
        doty=Dot(point=inity,color=YELLOW)
        doty2=Dot(point=inity2,color=YELLOW)
        dotym=Dot(point=inity3,color=RED)
        dotyn=Dot(point=inityn,color=YELLOW)
        dotyn2=Dot(point=inityn2,color=YELLOW)
        dotynm=Dot(point=inityn3,color=RED)
        xline_1 = ax.get_vertical_line(ax.i2gp(3, graph), color=YELLOW)
        xline_2 = ax.get_vertical_line(ax.i2gp(6, graph), color=BLUE)
        xline_3 = ax.get_vertical_line(ax.i2gp(9, graph), color=YELLOW)
        yline_1 = ax.get_horizontal_line(ax.i2gp(3, graph), color=YELLOW)
        yline_2 = ax.get_horizontal_line(ax.i2gp(6, graph), color=BLUE)
        yline_3 = ax.get_horizontal_line(ax.i2gp(9, graph), color=YELLOW)
        
        self.play(Write(ax))
        self.play(Write(graph))
        self.wait(5)
        self.play(Write(area))
        self.play(Write(dot3))
        self.play(Write(dot4))
        self.play(Write(stline))
        self.wait(3)
        self.play(FadeOut(stline,dot4,dot3,area))
        self.wait(1)
        self.play(Write(pointx))
        self.play(Write(xline_1),run_time=0.3)
        self.play(Write(dot))
        self.play(Write(pointy))
        self.play(Write(xline_3),run_time=0.3)
        self.play(Write(dot2))
        self.wait(9)
        self.play(Write(pointm))
        self.play(Write(xline_2),run_time=0.3)
        self.play(Write(dote1))
        self.play(Write(yline_1),run_time=0.3)
        self.play(Write(doty))
        self.play(Write(yline_3),run_time=0.3)
        self.play(Write(doty2))
        self.play(Write(yline_2),run_time=0.3)
        self.play(Write(dotyei))
        self.wait()
        self.play(Write(dotym))
        self.play(FadeOut(xline_1,xline_2,xline_3,yline_1,yline_2,yline_3))
        self.wait(5)
        self.play(Transform(graph,li),Transform(dot,dotl),Transform(dot2,dotm),Transform(dote1,dote2),Transform(doty,dotyn),Transform(doty2,dotyn2),Transform(dotym,dotynm),Transform(dotyei,dotyef))
        self.wait(10)
        

class Convex2(Scene):
    def construct(self):
        ax=Axes(x_range=(0,10),y_range=(0,100,10),x_length=5,y_length=5,axis_config={"include_tip": False})
        def func(x):
            return(0.09*(x)**3)
        def func2(x):
            return(100)
        def func3(x):
            return(10*x)
        graph=ax.plot(func,color=GREEN)
        xline_1 = ax.get_vertical_line(ax.i2gp(4, graph), color=YELLOW)
        xline_2 = ax.get_vertical_line(ax.i2gp(5, graph), color=YELLOW)
        xline_3 = ax.get_vertical_line(ax.i2gp(7, graph), color=YELLOW)
        xline_4 = ax.get_vertical_line(ax.i2gp(8, graph), color=YELLOW)
        yline_1 = ax.get_horizontal_line(ax.i2gp(4, graph), color=YELLOW)
        yline_2 = ax.get_horizontal_line(ax.i2gp(5, graph), color=YELLOW)
        yline_3 = ax.get_horizontal_line(ax.i2gp(7, graph), color=YELLOW)
        yline_4 = ax.get_horizontal_line(ax.i2gp(8, graph), color=YELLOW)
        px=(4+5+7+8)/4
        p1=ValueTracker(px)
        py=(func(4)+func(5)+func(7)+func(8))/4
        xline_5 = ax.get_vertical_line(ax.i2gp(p1.get_value(), graph), color=BLUE)
        yline_5 = ax.get_horizontal_line(ax.i2gp(p1.get_value(), graph), color=BLUE)
        ppx=[ax.coords_to_point(0, func(px))]
        ppy=[ax.coords_to_point(0, py)]
        dot1=Dot(point=ppx,color=BLUE)
        dot2=Dot(point=ppy,color=RED)
        ef=Tex("$\mathbb{E}$(f(X))",color=RED).shift(UP*2.5+RIGHT*2)
        fe= Tex("$f(\mathbb{E}(X))$",color=BLUE).shift(UP*2.5+RIGHT*4.2)
        ineq= Tex("$\geq$").shift(UP*2.5+RIGHT*3.1)
        
        self.play(Write(ax))
        self.play(Write(graph))
        self.wait()
        self.play(Write(xline_1),Write(xline_2),Write(xline_3),Write(xline_4),Write(yline_1),Write(yline_2),Write(yline_3),Write(yline_4),run_time=0.3)
        self.wait(5)
        self.play(Write(xline_5))
        self.play(Write(yline_5))
        self.play(Write(dot1))
        self.wait(3)
        self.play(Write(dot2))
        self.wait(6)
        self.play(Transform(dot2,ef))
        self.play(Transform(dot1,fe))
        self.play(Write(ineq))
        self.wait(10)

class Proof(Scene):
    def construct(self):
        proof=Tex("Proof",color=RED)
        base=Tex("$f((1-p)x_1+px_2)\leq(1-p)f(x_1)+pf(x_2)$")
        check=Tex("$\checkmark$",color=GREEN).scale(3)
        ih=Tex("The inequality holds for $n$ inputs",color=GREEN).shift(UP*3)
        p=Tex("$p_1+p_2+\ldots p_n+p_{n+1}=1$").shift(UP*2)
        p2=Tex("$p_1+p_2+\ldots p_n = 1-p_{n+1}$").shift(UP*2)
        sum1=Tex("$f(\sum\limits_{i=1}^{n+1}p_ix_i)$").shift(UP*1+LEFT*4)
        sum1d=Tex("$f(\sum\limits_{i=1}^{n+1}p_ix_i)$").shift(UP*1+LEFT*4)
        sum2=Tex("$=f((1-p_{n+1})(\sum\limits_{i=1}^n\dfrac{p_ix_i}{1-p_{n+1}})+p_{n+1}x_{n+1})$").shift(UP*1+RIGHT*2)
        rect1=Rectangle(width=2.0,height=1.0,color=YELLOW).shift(UP*1+LEFT*0.5)
        rect2=Rectangle(width=1.0,height=1.0,color=YELLOW).shift(UP*1+RIGHT*4.9)
        rect3=Rectangle(width=4.0,height=2.0,color=YELLOW).shift(DOWN*0.3+RIGHT*2)
        sum3=Tex("$\leq (1-p_{n+1})f(\sum\limits_{i=1}^n\dfrac{p_ix_i}{1-p_{n+1}})+p_{n+1}f(x_{n+1})$").shift(DOWN*0.3+RIGHT*2)
        sum4=Tex("$\sum\limits_{i=1}^n\dfrac{p_i}{1-p_{n+1}}=1$",color=GREEN).shift(DOWN*2)
        sum5=Tex("$\leq (1-p_{n+1})\sum\limits_{i=1}^n\dfrac{p_i}{1-p_{n+1}}f(x_i)$").shift(DOWN*2)
        sum6=Tex("$+p_{n+1}f(x_{n+1})$").shift(DOWN*2+RIGHT*5)
        fin=Tex("$\leq\sum\limits_{i=1}^{n+1}p_{i}f(x_i)$").shift(DOWN*2)

        self.play(Write(proof))
        self.wait(2)
        self.play(FadeOut(proof))
        self.wait(5)
        self.play(Write(base))
        self.play(Write(check))
        self.play(FadeOut(base,check))
        self.play(Write(ih))
        self.wait(5)
        self.play(Write(p))
        self.wait(2)
        self.play(Transform(p,p2))
        self.play(Write(sum1),Write(sum1d))
        self.play(Write(sum2))
        self.wait(3)
        self.play(Write(rect1))
        self.play(Write(rect2))
        self.wait(5)
        self.play(FadeOut(rect1,rect2))
        self.play(Write(sum3))
        self.wait(5)
        self.play(Transform(p,sum4))
        self.play(FadeOut(p))
        self.play(Write(rect3))
        self.wait(5)
        self.play(Transform(rect3,sum5))
        self.play(Write(sum6))
        self.wait(2)
        self.play(Transform(rect3,fin),Transform(sum6,fin))
        self.play(sum1.animate.shift(DOWN*3))
        self.wait(10)

class concave(Scene):
    def construct(self):
        jensen=Tex("$f(\mathbb{E}(X))\leq \mathbb{E}(f(X))$")
        jensen2=Tex("$f(\mathbb{E}(X))\geq \mathbb{E}(f(X))$")

        self.play(Write(jensen))
        self.wait(10)
        self.play(Transform(jensen,jensen2))
        self.play(FadeOut(jensen,jensen2))
        self.wait()

class intro(Scene):
    def construct(self):
        intr=Tex("$e^{i\pi}$").scale(2)
        self.play(Write(intr),run_time=5)



