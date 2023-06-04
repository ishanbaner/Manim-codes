from manim import *
import numpy as np 
from scipy.integrate import odeint 
class figures(Scene):
    def construct(self):
        text=Tex("Lotka Voletrra Model")
        self.play(Write(text))
        self.wait(5)
        self.play(FadeOut(text))
        self.wait()
        face=VGroup()
        f1=Arc(angle=PI/2,color=ORANGE).shift(RIGHT*0.5)
        f2=Arc(angle=PI/2,color=ORANGE).rotate(angle=PI/2).shift(LEFT*0.5)
        nose=VGroup()
        s11=Line(start=LEFT*0.5,end=DOWN*1+RIGHT*0.5,color=ORANGE)
        s21=Line(start=RIGHT*1.5,end=DOWN*1+RIGHT*0.5,color=ORANGE)
        nose.add(s11,s21)
        e1=VGroup()
        s21=Line(start=LEFT*0.5,end=DOWN*1.5+RIGHT*0.5,color=ORANGE)
        s22=Line(start=RIGHT*1.5,end=DOWN*1.5+RIGHT*0.5,color=ORANGE)
        e1.add(s21,s22)
        e2=VGroup()
        s31=Line(start=LEFT*0.5,end=DOWN*1.5+RIGHT*0.5,color=ORANGE)
        s32=Line(start=RIGHT*1.5,end=DOWN*1.5+RIGHT*0.5,color=ORANGE)
        e2.add(s31,s32)
        e1.rotate(angle=-3*PI/4-0.1).scale(0.5).shift(UP*1.8+LEFT*0.95)
        e2.rotate(angle=3*PI/4+0.1).scale(0.5).shift(UP*1.8+RIGHT*0.95)
        eye1=Dot().shift(LEFT*0.3).shift(RIGHT*0.5)
        eye2=Dot().shift(RIGHT*0.3).shift(RIGHT*0.5)
        face.add(nose,f1,f2,e1,e2,eye1,eye2)
        #-----------------------------------------------------------------------------
        face1=VGroup()
        f1=Circle(color=WHITE)
        e11=VGroup()
        arc2=ArcBetweenPoints(start=DOWN*3+LEFT*0.5,end=DOWN*3+RIGHT*1.5)
        s211=Line(start=LEFT*0.5,end=DOWN*3+LEFT*0.5)
        s221=Line(start=RIGHT*1.5,end=DOWN*3+RIGHT*1.5)
        e11.add(s211,s221,arc2)
        e21=VGroup()
        s311=Line(start=LEFT*0.5,end=DOWN*3)
        s321=Line(start=RIGHT*1.5,end=DOWN*3+RIGHT*2)
        arc1=ArcBetweenPoints(start=DOWN*3,end=DOWN*3+RIGHT*2)
        e21.add(s311,s321,arc1)
        e11.rotate(angle=-3*PI/4-0.1).scale(0.5).shift(UP*3+LEFT*1.6)
        e21.rotate(angle=3*PI/4).scale(0.5).shift(UP*3+RIGHT*0.43)
        eye11=Dot().shift(LEFT*0.3)
        eye21=Dot().shift(RIGHT*0.3)
        nose=Dot(color=RED).shift(DOWN*0.3)
        face1.add(f1,e11,e21,eye11,eye21,nose)
        #--------------------------------------------------------------------------------------------------
        axe=Axes(x_range=[0,5,1],y_range=[0,5,1])
        funct=FunctionGraph(lambda x:2**x,x_range=[0,5,1],color=YELLOW).shift(DOWN*4+LEFT*5)
        graph1=VGroup(axe,funct)
        graph1.shift(DOWN*0.5)
        #--------------------------------------------------------------------------------------------------
        eq1=Tex(r"$\frac{dr}{dt}=\alpha r$")
        eq2=Tex(r"$\frac{df}{dt}=\gamma rf$",color=ORANGE)
        mr=Tex(r"$-\beta rf$").shift(RIGHT*1.5)
        mf=Tex(r"$-\delta f$",color=ORANGE).shift(RIGHT*1.5)
        self.play(FadeIn(face.scale(0.5).shift(LEFT*1),face1.scale(0.3).shift(RIGHT*1+DOWN*0.5)))
        self.wait(7)
        self.play(FadeOut(face),face1.animate.shift(LEFT*1))
        self.wait()
        self.play(Transform(face1,eq1))
        self.wait(4)
        self.play(Write(graph1))
        self.wait()
        self.play(FadeOut(graph1))
        self.wait(20)
        self.play(Write(mr))
        self.wait(2)
        self.play(FadeOut(face1,mr))
        self.wait()
        self.play(FadeIn(face.shift(RIGHT*1)))
        self.wait()
        self.play(Transform(face,eq2))
        self.wait(19)
        self.play(Write(mf))
        self.wait()
        self.play(FadeIn(eq1.shift(UP*0.5),mr.shift(UP*0.5)),face.animate.shift(DOWN*0.5),mf.animate.shift(DOWN*0.5))
        self.wait(15)

class phaseplot1(Scene):
    def dix(x,y):
        dx=2*x-1.1*x*y-0.1*x**2
        return(dx)
    def diy(x,y):
        dy=0.9*x*y-y-0.1*y**2
        return(dy)
    def dix1(x,y):
        dx=2*x-1.1*x*y
        return(dx)
    def diy1(x,y):
        dy=0.9*x*y-y
        return(dy)
    def pop(s,t):
        a=2
        b=1.1
        g=1
        d=0.9
        x=s[0]
        y=s[1]
        dxdt=a*x-b*x*y-0.1*x**2
        dydt=d*x*y-y*g-0.1*y**2
        return([dxdt,dydt])
    def pop2(s,t):
        a=2
        b=1.1
        g=1
        d=0.9
        x=s[0]
        y=s[1]
        dxdt=a*x-b*x*y
        dydt=d*x*y-y*g
        return([dxdt,dydt])
    def construct(self):
        ax = Axes(x_length = 25, y_length = 25,).add_coordinates()
        plane = NumberPlane(x_range=(0,20,1),y_range=(0,20,1), axis_config={"include_numbers": False},)
        
        popy=Tex("Foxes",color=RED).shift(LEFT*4+DOWN*0.5)
        popx=Tex("Rabbits").shift(DOWN*3.5)
        
#--------------------------------------------------------------------------------------------------------------------------------------------------
        d1=VGroup()
        for i1 in range(-10,10):
            for j1 in range(-10,10):
                d111=phaseplot1.dix1(i1,j1)
                d211=phaseplot1.diy1(i1,j1)
                if d111!=0 or d211!=0:
                    d11=phaseplot1.dix1(i1,j1)*(1/(d111**2+d211**2)**0.5)
                    d21=phaseplot1.diy1(i1,j1)*(1/(d111**2+d211**2)**0.5)
                else:
                    d11=phaseplot1.dix1(i1,j1)
                    d21=phaseplot1.diy1(i1,j1)
                ar1=Arrow(start=RIGHT*i1+UP*j1, end=RIGHT*(i1+d11)+UP*(j1+d21),color=rgb_to_color([0.5,i1**2/100.1,j1**2/100.1]))
                d1.add(ar1)
        d1.shift(DOWN*3+LEFT*3)
        for y21 in range(1,10):
            t1=np.linspace(0,11,100)
            y01=[10,y21]
            s1=odeint(phaseplot1.pop2,y01,t1)
        axes1=Axes().add_coordinates()
        dots_axes1=[None]*(len(s1[:,0]))
        lines1=VGroup()
        lines11=VGroup()
        for m1 in range(len(s1[:,0])):
            dots_axes1[m1]=Dot(axes1.coords_to_point(s1[:,0][m1],s1[:,1][m1])).shift(DOWN*3+LEFT*3)
        for t2 in range(len(s1[:,0])-1):
            li1=Line(start=dots_axes1[t2].get_center(),end=dots_axes1[t2+1].get_center(),color=GREEN) 
            li11=Line(start=dots_axes1[t2].get_center(),end=dots_axes1[t2+1].get_center(),color=GREEN)  
            lines1.add(li1)
            lines11.add(li11)
        ax1=VGroup()
        ax1.add(Line(start=[-3,-10,0],end=[-3,10,0]))
        ax1.add(Line(start=[-10,-3,0],end=[10,-3,0]))
        self.play(Write(plane.shift(DOWN*3+LEFT*3)),Write(ax1),Write(popx),Write(popy))
        self.wait(4)
        self.play(FadeIn(lines1.scale(0.5).shift(DOWN*2.7+LEFT*3.2)))
        self.wait()
        self.play(Write(d1))
        self.wait(40)
        self.play(FadeOut(lines1,d1,plane,ax1,popx,popy))
        self.wait()
        self.wait()
        self.wait()
        

class periodicplot(Scene):
    def construct(self):
        d1=VGroup()
        for i1 in range(-10,10):
            for j1 in range(-10,10):
                d111=phaseplot1.dix1(i1,j1)
                d211=phaseplot1.diy1(i1,j1)
                if d111!=0 or d211!=0:
                    d11=phaseplot1.dix1(i1,j1)*(1/(d111**2+d211**2)**0.5)
                    d21=phaseplot1.diy1(i1,j1)*(1/(d111**2+d211**2)**0.5)
                else:
                    d11=phaseplot1.dix1(i1,j1)
                    d21=phaseplot1.diy1(i1,j1)
                ar1=Arrow(start=RIGHT*i1+UP*j1, end=RIGHT*(i1+d11)+UP*(j1+d21),color=rgb_to_color([0.5,i1**2/100.1,j1**2/100.1]))
                d1.add(ar1)
        d1.shift(DOWN*3+LEFT*3)
        for y21 in range(1,10):
            t1=np.linspace(0,11,100)
            y01=[10,y21]
            s1=odeint(phaseplot1.pop2,y01,t1)
        axes1=Axes().add_coordinates()
        dots_axes1=[None]*(len(s1[:,0]))
        lines1=VGroup()
        lines11=VGroup()
        for m1 in range(len(s1[:,0])):
            dots_axes1[m1]=Dot(axes1.coords_to_point(s1[:,0][m1],s1[:,1][m1])).shift(DOWN*3+LEFT*3)
        for t2 in range(len(s1[:,0])-1):
            li1=Line(start=dots_axes1[t2].get_center(),end=dots_axes1[t2+1].get_center(),color=GREEN) 
            li11=Line(start=dots_axes1[t2].get_center(),end=dots_axes1[t2+1].get_center(),color=GREEN)  
            lines1.add(li1)
            lines11.add(li11)
        foxface=Tex("Foxes",color=RED).shift(UP*3+LEFT*4.7)
        pos1x=foxface.get_x()
        pos1y=foxface.get_y()
        rabbitface=Tex("Rabbits",color=WHITE).shift(LEFT*4.7+DOWN*3)
        pos2x=rabbitface.get_x()
        pos2y=rabbitface.get_y()
        poptext=Tex("Population").shift(UP*3+RIGHT*3)
        timetext=Tex("Time").shift(DOWN*3+RIGHT*3.7)
        lines11.scale(0.25).shift(DOWN*2.7+LEFT*4.8)
        self.wait()
        line1=Line(start=[0,1.2,0],end=[0,-3.9,0],color=GREEN,stroke_width=0.1).shift(LEFT*2.8+UP*1.2).scale(0.5)
        line2=Line(start=[0,-3.9,0],end=[2.7,-3.9,0],color=GREEN,stroke_width=0.1).shift(UP*2.45+LEFT*3.5).scale(0.5)
        group=VGroup()
        group.add(lines11,line1,line2)
        group.shift(LEFT*2)
        self.play(FadeIn(lines11))
        dd=Dot()
        dd1=Dot()         
        dd1=Dot().move_to([1,dd.get_y(),0])
        dd2=Dot().move_to([1,dd.get_y(),0])
        dd3=Dot().move_to([1,dd.get_y(),0])
        self.add(TracedPath(dd1.get_center, stroke_color=RED))
        dd1.add_updater(lambda m: m.shift(UP*(dd.get_y()-dd1.get_y())))
        joinline1=DashedLine(start=dd.get_center(),end=dd1.get_center(),dashed_ratio=0.5)
        joinline1.add_updater(lambda m: m.become(DashedLine(start=dd.get_center(),end=dd1.get_center(),dashed_ratio=0.5)))
        
        fox=DoubleArrow(start=[-6,-3,0],end=[-6,3,0])
        rabbits=DoubleArrow(start=[-7,-2,0],end=[-0,-2,0])
        popu=DoubleArrow(start=[-6,-3,0],end=[-6,3,0])
        tim=DoubleArrow(start=[-7,-2,0],end=[-0,-2,0])
        fox1=DoubleArrow(start=[-6,-3,0],end=[-6,4,0])
        rabbits1=DoubleArrow(start=[-7,-2,0],end=[-0,-2,0])
        popu1=DoubleArrow(start=[-6,-3,0],end=[-6,4,0])
        tim1=DoubleArrow(start=[-7,-2,0],end=[-0,-2,0])
        group11=VGroup()
        group11.add(popu,tim)
        group11.shift(RIGHT*7)
        self.play(Write(fox),Write(rabbits),Write(group11),FadeIn(foxface,rabbitface,poptext,timetext))
        #self.play(FadeIn(dd,dd1,joinline1))
        self.wait()
        for tt in range(2):
            for k1 in range(3):
                
                if k1==1 or k1==2:
                    self.play(MoveAlongPath(dd,lines11[k1]),dd1.animate.shift(RIGHT*0.25),rate_func=linear,run_time=0.2)
                    self.add(joinline1)
                else:
                    self.play(MoveAlongPath(dd,lines11[k1]),dd1.animate.shift(RIGHT*0.25),rate_func=linear)
                    self.add(joinline1)
            self.play(MoveAlongPath(dd,line1),dd1.animate.shift(RIGHT*0.25),rate_func=linear)
            self.play(MoveAlongPath(dd,line2),dd1.animate.shift(RIGHT*0.25),rate_func=linear)
            for k1 in range(90,96):
                if k1==90 or k1==91:
                    self.play(MoveAlongPath(dd,lines11[k1]),dd1.animate.shift(RIGHT*0.25),rate_func=linear,run_time=0.4)
                else:
                    self.play(MoveAlongPath(dd,lines11[k1]),dd1.animate.shift(RIGHT*0.25),rate_func=linear,run_time=0.5)
        
        self.wait()
        self.play(group.animate.rotate(angle=PI/2),FadeOut(dd1,dd),rabbitface.animate.move_to([pos1x,pos1y,0]),foxface.animate.move_to([pos2x,pos2y,0]),FadeOut(joinline1))
        self.play(group.animate.flip())

        self.add(TracedPath(dd2.get_center, stroke_color=WHITE))
        dd2.add_updater(lambda m: m.shift(UP*(dd.get_y()-dd2.get_y())))
        joinline2=DashedLine(start=dd.get_center(),end=dd2.get_center(),dashed_ratio=0.5)
        joinline2.add_updater(lambda m: m.become(DashedLine(start=dd.get_center(),end=dd2.get_center(),dashed_ratio=0.5)))
        self.play(FadeIn(dd2))
        for tt in range(2):
            for k1 in range(3):
                if k1==1 or k1==2:
                    self.play(MoveAlongPath(dd,lines11[k1]),dd2.animate.shift(RIGHT*0.25),rate_func=linear,run_time=0.2)
                    self.add(joinline2)
                else:
                    self.play(FadeOut(joinline2),MoveAlongPath(dd,lines11[k1]),dd2.animate.shift(RIGHT*0.25),rate_func=linear)
                    self.add(joinline2)
            self.play(MoveAlongPath(dd,line1),dd2.animate.shift(RIGHT*0.25),rate_func=linear)
            self.play(MoveAlongPath(dd,line2),dd2.animate.shift(RIGHT*0.25),rate_func=linear)
            for k1 in range(90,96):
                if k1==90 or k1==91:
                    self.play(MoveAlongPath(dd,lines11[k1]),dd2.animate.shift(RIGHT*0.25),rate_func=linear,run_time=0.4)
                else:
                    self.play(MoveAlongPath(dd,lines11[k1]),dd2.animate.shift(RIGHT*0.25),rate_func=linear,run_time=0.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class figures1h(Scene):
    def construct(self):
        eq1=Tex(r"$\frac{dr}{dt}=\alpha r - \beta rf$")
        l1=Tex("$-\lambda r^2$").shift(RIGHT*2.3)
        equ2=Tex(r"$\frac{df}{dt}=-\gamma f - \kappa f^2 +\delta rf$",color=ORANGE)
        equ1=VGroup(eq1,l1).shift(LEFT*0.8)
        self.play(Write(eq1))
        self.wait(3)
        self.play(Write(l1))
        self.wait(10)
        self.play(equ1.animate.shift(UP*0.5),FadeIn(equ2.shift(DOWN*0.5)))
        self.wait(10)

class phaseplot2(Scene):
    def construct(self):
        ax1=VGroup()
        ax1.add(Line(start=[-3,-10,0],end=[-3,10,0]))
        ax1.add(Line(start=[-10,-3,0],end=[10,-3,0]))
        plane = NumberPlane(x_range=(0,20,1),y_range=(0,20,1), axis_config={"include_numbers": False},)
        d=VGroup()
        for i in range(-10,10):
            for j in range(-10,10):
                d11=phaseplot1.dix(i,j)
                d21=phaseplot1.diy(i,j)
                if d11!=0 or d21!=0:
                    d1=phaseplot1.dix(i,j)*(1/(d11**2+d21**2)**0.5)
                    d2=phaseplot1.diy(i,j)*(1/(d11**2+d21**2)**0.5)
                else:
                    d1=phaseplot1.dix(i,j)
                    d2=phaseplot1.diy(i,j)
                ar=Arrow(start=RIGHT*i+UP*j, end=RIGHT*(i+d1)+UP*(j+d2),color=rgb_to_color([0.5,i**2/100.1,j**2/100.1]))
                d.add(ar)
        d.shift(DOWN*3+LEFT*3)
        popy=Tex("Foxes",color=RED).shift(LEFT*4+DOWN*0.5)
        popx=Tex("Rabbits").shift(DOWN*3.5)
        for y20 in range(1,10):
            t=np.linspace(0,11,100)
            y0=[10,y20]
            s=odeint(phaseplot1.pop,y0,t)
        axes=Axes().add_coordinates()
        dots_axes=[None]*(len(s[:,0]))
        lines=VGroup()
        for m in range(len(s[:,0])):
            dots_axes[m]=Dot(axes.coords_to_point(s[:,0][m],s[:,1][m])).shift(DOWN*3+LEFT*3)
        for t in range(len(s[:,0])-1):
            li=Line(start=dots_axes[t].get_center(),end=dots_axes[t+1].get_center(),color=GREEN)   
            lines.add(li)
        self.play(Write(plane))
        self.play(Write(ax1),Write(popx),Write(popy))
        self.play(FadeIn(lines))
        self.play(Write(d))
        self.wait(13)
        self.play(FadeOut(lines,d,ax1,popx,popy,plane))
        self.wait()

class dampedplot(Scene):
    def construct(self):
        for y21 in range(1,10):
            t1=np.linspace(0,11,100)
            y01=[10,y21]
            s1=odeint(phaseplot1.pop2,y01,t1)
        axes1=Axes().add_coordinates()
        dots_axes1=[None]*(len(s1[:,0]))
        lines11=VGroup()
        for m1 in range(len(s1[:,0])):
            dots_axes1[m1]=Dot(axes1.coords_to_point(s1[:,0][m1],s1[:,1][m1])).shift(DOWN*3+LEFT*3)
        for t2 in range(len(s1[:,0])-1):
            li1=Line(start=dots_axes1[t2].get_center(),end=dots_axes1[t2+1].get_center(),color=GREEN) 
            li11=Line(start=dots_axes1[t2].get_center(),end=dots_axes1[t2+1].get_center(),color=GREEN)  
            lines11.add(li11)
        for y20 in range(1,10):
            t=np.linspace(0,11,100)
            y0=[10,y20]
            s=odeint(phaseplot1.pop,y0,t)
        axes=Axes().add_coordinates()
        dots_axes=[None]*(len(s[:,0]))
        lines=VGroup()
        for m in range(len(s[:,0])):
            dots_axes[m]=Dot(axes.coords_to_point(s[:,0][m],s[:,1][m])).shift(DOWN*3+LEFT*3)
        for t in range(len(s[:,0])-1):
            li=Line(start=dots_axes[t].get_center(),end=dots_axes[t+1].get_center(),color=GREEN)   
            lines.add(li)
        foxface=Tex("Foxes",color=RED).shift(UP*3+LEFT*4.7)
        pos1x=foxface.get_x()
        pos1y=foxface.get_y()
        rabbitface=Tex("Rabbits",color=WHITE).shift(LEFT*4.7+DOWN*3)
        pos2x=rabbitface.get_x()
        pos2y=rabbitface.get_y()
        poptext=Tex("Population").shift(UP*3+RIGHT*3)
        timetext=Tex("Time").shift(DOWN*3+RIGHT*3.7)
        lines11.scale(0.25).shift(DOWN*2.7+LEFT*4.8)
        line1=Line(start=[0,1.2,0],end=[0,-3.9,0],color=GREEN,stroke_width=0.1).shift(LEFT*2.8+UP*1.2).scale(0.5)
        line2=Line(start=[0,-3.9,0],end=[2.7,-3.9,0],color=GREEN,stroke_width=0.1).shift(UP*2.45+LEFT*3.5).scale(0.5)
        group=VGroup()
        group.add(lines11,line1,line2)
        group.shift(LEFT*2)
        #self.play(FadeIn(lines11))
        dd=Dot()
        dd1=Dot()         
        dd1=Dot().move_to([1,dd.get_y(),0])
        dd2=Dot().move_to([1,dd.get_y(),0])
        dd3=Dot().move_to([1,dd.get_y(),0])
        self.add(TracedPath(dd1.get_center, stroke_color=RED))
        dd1.add_updater(lambda m: m.shift(UP*(dd.get_y()-dd1.get_y())))
        joinline1=DashedLine(start=dd.get_center(),end=dd1.get_center(),dashed_ratio=0.5)
        joinline1.add_updater(lambda m: m.become(DashedLine(start=dd.get_center(),end=dd1.get_center(),dashed_ratio=0.5)))
        
        fox=DoubleArrow(start=[-6,-3,0],end=[-6,3,0])
        rabbits=DoubleArrow(start=[-7,-2,0],end=[-0,-2,0])
        popu=DoubleArrow(start=[-6,-3,0],end=[-6,3,0])
        tim=DoubleArrow(start=[-7,-2,0],end=[-0,-2,0])
        fox1=DoubleArrow(start=[-6,-3,0],end=[-6,4,0])
        rabbits1=DoubleArrow(start=[-7,-2,0],end=[0,-2,0])
        popu1=DoubleArrow(start=[-6,-3,0],end=[-6,4,0])
        tim1=DoubleArrow(start=[-7,-2,0],end=[0,-2,0])
        group11=VGroup()
        group11.add(popu,tim)
        group11.shift(RIGHT*7)
        
        dd3.add_updater(lambda m: m.shift(UP*(dd.get_y()-dd3.get_y())))
        joinline3=DashedLine(start=dd.get_center(),end=dd3.get_center(),dashed_ratio=0.5)
        joinline3.add_updater(lambda m: m.become(DashedLine(start=dd.get_center(),end=dd3.get_center(),dashed_ratio=0.5)))
        self.add(TracedPath(dd3.get_center, stroke_color=RED))
        rabbitface.move_to([pos1x,pos1y,0])
        spiral=lines.scale(0.5).shift(LEFT*5+DOWN*1.5)
        self.play(Write(spiral))
        foxface.move_to([pos2x,pos2y,0])
        self.play(Write(fox1.shift(DOWN*0.5)),Write(rabbits1.shift(DOWN*0.5)),Write(foxface),Write(rabbitface),Write(popu1.shift(RIGHT*7+DOWN*0.5)),Write(tim1.shift(RIGHT*7+DOWN*0.5)),Write(poptext),Write(timetext))
        for k2 in range(0,len(lines)-1):
            if k2==0:
                self.add(joinline3)
            self.play(MoveAlongPath(dd,lines[k2]),dd3.animate.shift(RIGHT*0.05),rate_func=linear,run_time=0.1)
        self.wait(10)

class threeplot(Scene):
    def pop3(s,t):
        x=s[0]
        y=s[1]
        z=s[2]
        a1=5
        b1=3
        a2=0.1
        b2=2
        d1=0.4
        d2=0.01
        f1x=a1*x/(1+b1*x)
        f2y=a2*y/(1+b2*y)
        dxdt=x*(1-x)-f1x*y
        dydt=f1x*y-f2y*z-d1*y
        dzdt=f2y*z-d2*z
        return([dxdt,dydt,dzdt])
    def construct(self):
        s0=[0.8,0.8,9]
        t=np.linspace(5000,6500)
        s1=odeint(threeplot.pop3,s0,t)
        axes1=Axes(x_range=[5000,6500,100],y_range=[0,1,0.1]).scale(0.25).shift(UP*2)
        axes2=Axes(x_range=[5000,6500,100],y_range=[0,1,0.1]).scale(0.25)
        axes3=Axes(x_range=[5000,6500,100],y_range=[5,10,1]).scale(0.25).shift(DOWN*2)
        dots_axes1=[None]*(len(s1[:,0]))
        lines1=VGroup()
        for m1 in range(len(s1[:,0])):
            dots_axes1[m1]=Dot(axes1.coords_to_point(t[m1],s1[:,0][m1]))
        for t2 in range(len(s1[:,0])-1):
            li1=Line(start=dots_axes1[t2].get_center(),end=dots_axes1[t2+1].get_center(),color=GREEN) 
            lines1.add(li1)
        dots_axes2=[None]*(len(s1[:,1]))
        lines2=VGroup()
        for m2 in range(len(s1[:,1])):
            dots_axes2[m2]=Dot(axes2.coords_to_point(t[m2],s1[:,1][m2]))
        for t2 in range(len(s1[:,1])-1):
            li2=Line(start=dots_axes2[t2].get_center(),end=dots_axes2[t2+1].get_center(),color=BLUE) 
            lines2.add(li2)
        dots_axes3=[None]*(len(s1[:,2]))
        lines3=VGroup()
        for m3 in range(len(s1[:,0])):
            dots_axes3[m3]=Dot(axes3.coords_to_point(t[m3],s1[:,2][m3]))
        for t2 in range(len(s1[:,2])-1):
            li3=Line(start=dots_axes3[t2].get_center(),end=dots_axes3[t2+1].get_center(),color=RED) 
            lines3.add(li3)
        ax3=VGroup()
        ax3.add(Line(start=[-3,-10,0],end=[-3,10,0]))
        ax3.add(Line(start=[-10,-3,0],end=[10,-3,0]))
        self.play(Write(axes1),Write(lines1),Write(axes2),Write(lines2),Write(axes3),Write(lines3))
        self.wait(5)

class threedphaseplot(ThreeDScene):
    def pop4(s,t):
        x=s[0]
        y=s[1]
        z=s[2]
        a1=5
        b1=3
        a2=0.1
        b2=2
        d1=0.4
        d2=0.01
        f1x=a1*x/(1+b1*x)
        f2y=a2*y/(1+b2*y)
        dxdt=x*(1-x)-f1x*y
        dydt=f1x*y-f2y*z-d1*y
        dzdt=f2y*z-d2*z
        return([dxdt,dydt,dzdt])
    def construct(self):
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        for y20 in np.arange(7.5,10,0.05):
            t=np.linspace(1,700)
            y0=[0.8,0.2,y20]
            s=odeint(threedphaseplot.pop4,y0,t)
        axes4=ThreeDAxes(x_range=[0,1,0.05],y_range=[0,0.5,0.05],z_range=[7.5,10.5,0.05])
        labels=axes4.get_axis_labels(Tex("X"), Tex("Y"))
        dots_axes=[None]*(len(s[:,0]))
        lines=VGroup()
        for m in range(len(s[:,0])):
            dots_axes[m]=Dot(axes4.coords_to_point(s[:,0][m],s[:,1][m],s[:,2][m]))
        for t in range(len(s[:,0])-1):
            li=Line(start=dots_axes[t].get_center(),end=dots_axes[t+1].get_center(),color=GREEN)   
            lines.add(li)
        self.play(Write(axes4.scale(0.5).move_to([0,0,0])),Write(labels))
        self.play(FadeIn(lines.scale(0.5).move_to([0,0,0])))
        self.begin_ambient_camera_rotation(rate=PI/10, about="theta")
        self.wait(2)
        self.stop_ambient_camera_rotation()
        self.wait()
        self.begin_ambient_camera_rotation(rate=PI/10, about="phi")
        self.wait(2)
        self.stop_ambient_camera_rotation()
        self.wait(2)

class bifurcation(Scene):
    def pop5(s,t,b1):
        x=s[0]
        y=s[1]
        z=s[2]
        a1=5
        a2=0.1
        b2=2
        d1=0.4
        d2=0.01
        f1x=a1*x/(1+b1*x)
        f2y=a2*y/(1+b2*y)
        dxdt=x*(1-x)-f1x*y
        dydt=f1x*y-f2y*z-d1*y
        dzdt=f2y*z-d2*z
        return([dxdt,dydt,dzdt])
    def construct(self):
        s0=[0.8,0.8,9]
        t=np.linspace(5000,5700)
        Y=[]
        Y1=[]
        X1=[]
        c=0
        buff=[]
        count=[]
        for i in np.arange(2,3,0.01):
            s=odeint(bifurcation.pop5,s0,t,args=(i,))
            for k in range(24,48):
                if (s[:,2][k-1]-s[:,2][k])*(s[:,2][k]-s[:,2][k+1])>0 and (s[:,2][k-1]-s[:,2][k])<0 :
                    buff.append(s[:,2][k])
            count.append(len(buff))
            Y.append(buff)
            buff=[]
        for j in Y:
            for j1 in j:
                Y1.append(j1)
        for j2 in np.arange(2,2.5,0.01):
            for j3 in range(count[c]):
                X1.append(j2)
        rect=Rectangle(width=5,height=2,color=BLACK).scale(2.5).shift(RIGHT*0.5)
        rect.set_fill(BLACK, opacity=1)
        self.add(rect)
        axes2=Axes(x_range=[2,2.5,0.01],y_range=[10,14,0.1],axis_config={"numbers_to_include":np.arange(2,2.5,0.1),"font_size":10}).add_coordinates()
        labels=axes2.get_axis_labels(Tex("$b_1$"),Tex(r"$f_{max}$"))
        self.play(Write(axes2),Write(labels))
        gr=VGroup()
        dots_axes2=[None]*(len(X1))
        for m2 in range(len(X1)):
            dots_axes2[m2]=Dot(axes2.coords_to_point(X1[m2],Y1[m2])).scale(0.5)
            gr.add(dots_axes2[m2])
        gr.set_z_index(rect.z_index-1)
        self.wait(5)
        self.play(FadeIn(gr),rect.animate.shift(RIGHT*12),rate_func=linear,run_time=5)
        self.wait(10)

class figures2(Scene):
    def construct(self):
        face=VGroup()
        f1=Arc(angle=PI/2,color=ORANGE).shift(RIGHT*0.5)
        f2=Arc(angle=PI/2,color=ORANGE).rotate(angle=PI/2).shift(LEFT*0.5)
        nose=VGroup()
        s11=Line(start=LEFT*0.5,end=DOWN*1+RIGHT*0.5,color=ORANGE)
        s21=Line(start=RIGHT*1.5,end=DOWN*1+RIGHT*0.5,color=ORANGE)
        nose.add(s11,s21)
        e1=VGroup()
        s21=Line(start=LEFT*0.5,end=DOWN*1.5+RIGHT*0.5,color=ORANGE)
        s22=Line(start=RIGHT*1.5,end=DOWN*1.5+RIGHT*0.5,color=ORANGE)
        e1.add(s21,s22)
        e2=VGroup()
        s31=Line(start=LEFT*0.5,end=DOWN*1.5+RIGHT*0.5,color=ORANGE)
        s32=Line(start=RIGHT*1.5,end=DOWN*1.5+RIGHT*0.5,color=ORANGE)
        e2.add(s31,s32)
        e1.rotate(angle=-3*PI/4-0.1).scale(0.5).shift(UP*1.8+LEFT*0.95)
        e2.rotate(angle=3*PI/4+0.1).scale(0.5).shift(UP*1.8+RIGHT*0.95)
        eye1=Dot().shift(LEFT*0.3).shift(RIGHT*0.5)
        eye2=Dot().shift(RIGHT*0.3).shift(RIGHT*0.5)
        face.add(nose,f1,f2,e1,e2,eye1,eye2)
        #-----------------------------------------------------------------------------
        face1=VGroup()
        f1=Circle(color=WHITE)
        e11=VGroup()
        arc2=ArcBetweenPoints(start=DOWN*3+LEFT*0.5,end=DOWN*3+RIGHT*1.5)
        s211=Line(start=LEFT*0.5,end=DOWN*3+LEFT*0.5)
        s221=Line(start=RIGHT*1.5,end=DOWN*3+RIGHT*1.5)
        e11.add(s211,s221,arc2)
        e21=VGroup()
        s311=Line(start=LEFT*0.5,end=DOWN*3)
        s321=Line(start=RIGHT*1.5,end=DOWN*3+RIGHT*2)
        arc1=ArcBetweenPoints(start=DOWN*3,end=DOWN*3+RIGHT*2)
        e21.add(s311,s321,arc1)
        e11.rotate(angle=-3*PI/4-0.1).scale(0.5).shift(UP*3+LEFT*1.6)
        e21.rotate(angle=3*PI/4).scale(0.5).shift(UP*3+RIGHT*0.43)
        eye11=Dot().shift(LEFT*0.3)
        eye21=Dot().shift(RIGHT*0.3)
        nose=Dot(color=RED).shift(DOWN*0.3)
        face1.add(f1,e11,e21,eye11,eye21,nose)
        #--------------------------------------------------------------------------------------------------
        carrot=VGroup()
        shape=Polygon([2,1,0],[3,1,0],[2.5,-2,0],color=ORANGE)
        leaf=Polygon([2.125,1,0],[2.25,1.4,0],[2.375,1.2,0],[2.5,1.4,0],[2.625,1.2,0],[2.75,1.4,0],[2.875,1,0],color=GREEN)
        carrot.add(shape)
        carrot.add(leaf)
        carrot.scale(0.5)
        #--------------------------------------------------------------------------------------------------
        ax2=Axes(x_range=[0,10,1],y_range=[0,5,1])
        func=FunctionGraph(lambda m:3*m/(1+m),x_range=[0,10,1]).shift(DOWN*3+LEFT*6)
        gra=VGroup(ax2,func)
        gra.scale(0.5).shift(DOWN*2)
        labels=ax2.get_axis_labels(Text("Prey population density").scale(0.3),Text("Prey consumed").scale(0.3))
        fi1=Tex(r"$f_1(u)=\frac{a_1}{1+b_1u}$",color=BLUE)
        fi2=Tex(r"$f_2(u)=\frac{a_2}{1+b_2u}$",color=BLUE)
        #--------------------------------------------------------------------------------------------------
        eq1=Tex(r"$\frac{dp}{dt}=p(1-p)$",color=GREEN).shift(LEFT*1)
        f1=Tex("$-f_1(p)r$",color=GREEN).shift(RIGHT*2.5).shift(LEFT*1)
        eq2=Tex(r"$\frac{dr}{dt}=f_1(p)r$").shift(LEFT*1)
        f2=Tex("$-f_2(r)f$").shift(RIGHT*2.3).shift(LEFT*1)
        d1=Tex("$-d_1r$").shift(RIGHT*3.8).shift(LEFT*1)
        eq3=Tex(r"$\frac{df}{dt}=f_2(r)f$",color=ORANGE).shift(LEFT*0.5)
        d2=Tex("$-d_2f$",color=ORANGE).shift(RIGHT*2.5).shift(LEFT*1)
        equ1=VGroup(eq1,f1)
        equ2=VGroup(eq2,f2,d1)
        equ3=VGroup(eq3,d2)
        box=Rectangle(width=1,height=1,color=YELLOW).shift(DOWN*1.1+RIGHT*1).scale(0.5)
        #--------------------------------------------------------------------------------------------------
        self.play(FadeIn(face.scale(0.5).shift(LEFT*2+UP*0.2),face1.scale(0.3).shift(DOWN*0.5+UP*0.2)))
        self.wait(10)
        self.play(FadeIn(carrot.shift(LEFT*1+UP*0.2)))
        self.wait(8)
        self.play(Write(ax2),Write(labels))
        self.play(Write(func))
        self.wait(8)
        self.play(FadeOut(ax2,func,labels))
        self.play(FadeOut(carrot,face,face1))
        self.wait()
        self.play(Write(eq1))
        self.wait(15)
        self.play(Write(f1))
        self.wait(8)
        self.play(FadeOut(eq1,f1))
        self.wait()
        self.play(Write(eq2))
        self.wait(14)
        self.play(Write(f2))
        self.wait(5)
        self.play(Write(d1))
        self.wait()
        self.play(FadeOut(eq2,f2,d1))
        self.wait()
        self.play(Write(eq3))
        self.wait(10)
        self.play(Write(d2))
        self.wait()
        self.play(equ3.animate.shift(DOWN*1))
        self.play(FadeIn(equ1.shift(UP*1),equ2))
        self.wait(8)
        equs=VGroup(equ1,equ2,equ3)
        self.play(equs.animate.shift(UP*1))
        self.play(Write(fi1.shift(DOWN*1)),Write(fi2.shift(DOWN*2)))
        self.wait(10)
        self.play(Write(box))
        self.wait()
        self.play(FadeOut(box))
        self.wait(10)
    
class response(Scene):
    def construct(self):
        b=Tex("What is up with this $b_1$?").shift(UP*0.5)
        t2=Tex("Type 2 functional response",color=GREEN).shift(DOWN*0.5)
        box1=Rectangle(width=0.3,height=0.3,color=YELLOW).shift(UP*0.25+RIGHT*0.7)
        box2=Rectangle(width=0.25,height=0.5,color=YELLOW).shift(DOWN*0.25+RIGHT*1.1)    
        att=Tex("Attack rate",color=YELLOW).shift(UP*1)
        time=Tex("Handling time",color=YELLOW).shift(DOWN*1) 
        fi1=Tex(r"$f(u)=\frac{au}{1+ahu}$")
        f11=Tex(r"$f_1(u)=\frac{a_1u}{1+b_1u}$",color=BLUE).shift(DOWN*0.5)
        b1=Tex("$b_1=ah$")
        self.play(Write(b))
        self.wait(7)
        self.play(Write(t2))
        self.wait(3)
        self.play(FadeOut(b,t2))
        self.play(Write(fi1))
        self.wait()
        self.play(Write(box1))
        self.wait()
        self.play(Transform(box1,att))
        self.wait()
        self.play(Transform(box1,box2))
        self.wait(5)
        self.play(Transform(box1,time))
        self.wait()
        self.play(FadeOut(box1))
        self.wait(4)
        self.play(fi1.animate.shift(UP*0.5),FadeIn(f11))
        self.wait()
        self.play(Transform(fi1,b1),Transform(f11,b1))
        self.wait(15)

class microbe(Scene):
    def construct(self):
        m1=Dot(color=BLUE).shift(DOWN*1+LEFT*0.25)
        m2=Dot(color=GREEN).shift(DOWN*1+RIGHT*0.25)
        m3=Dot(color=RED).shift(DOWN*0.5)        
        a1=Arrow(start=[0,3,0], end=[0,0,0],color=BLUE)
        a2=Arrow(start=[1.1,0.1,0], end=[2,0.1,0],color=BLUE)
        l1=Line(start=[-3,-3,0],end=[-3,3,0])
        l2=Line(start=[-3,-3,0],end=[3,-3,0])
        l3=Line(start=[3,-3,0],end=[3,0,0])
        l4=Line(start=[3,0.2,0],end=[3,3,0])
        beaker=VGroup(l1,l2,l3,l4)
        medium=Line(start=[-3,0,0],end=[3,0,0],color=BLUE)
        beaker.add(medium)
        self.play(FadeIn(beaker.scale(0.5)))
        self.wait(3)
        self.play(FadeIn(m1,m2,m3))
        self.wait(10)
        self.play(Write(a1))
        self.wait(2)
        self.play(Write(a2))
        self.wait(14)

class diff(Scene):
    def construct(self):
        box=Rectangle(width=2.5,height=1,color=YELLOW).shift(LEFT*2.3+UP*1)
        box2=Rectangle(width=6,height=1,color=YELLOW).shift(DOWN*1)
        box3=Rectangle(width=1,height=1,color=YELLOW).shift(DOWN*1+RIGHT*3.6)
        dcdt=Tex(r"$\frac{dC}{dt}=(C_0-C)D-\epsilon_1N_1\mu_1(C)-\epsilon_2N_2\mu_2(C)$").shift(UP*1)
        dndt=Tex(r"$\frac{dN_i}{dt}=N_i\mu_i(C)-P\phi_i(N_i)-DN_i$",color=rgb_to_color([0,1,1]))
        dpdt=Tex(r"$\frac{dP}{dt}=\beta_1 P \phi_1(N_1)+\beta_2 P\phi_2(N_2)-DP$",color=RED).shift(DOWN*1)
        phi=Tex(r"$\phi_i=\frac{\hat{\phi}N_i}{K_{N_i}+N_i}$",color=BLUE).shift(DOWN*1)
        mu=Tex(r"$\mu_i=\frac{\hat{\mu_i}C}{K_{si}+C}$",color=BLUE).shift(DOWN*2)
        eqs=VGroup(dcdt,dndt,dpdt)
        self.play(Write(dcdt),Write(dndt),Write(dpdt))
        self.wait()
        self.play(Write(box))
        self.wait(5)
        self.play(box.animate.shift(RIGHT*3))
        self.play(box.animate.shift(RIGHT*3))
        self.wait(2)
        self.play(box.animate.shift(LEFT*5+DOWN*1))
        self.wait(5)
        self.play(box.animate.shift(RIGHT*2.5))
        self.wait(7)        
        self.play(box.animate.shift(RIGHT*2.5))
        self.wait(7)        
        self.play(Transform(box,box2))
        self.wait(5)
        self.play(Transform(box,box3))
        self.wait()
        self.play(FadeOut(box))
        self.wait()
        self.play(eqs.animate.shift(UP*1))
        self.play(Write(phi),Write(mu))
        self.wait(40)

class lifesp(Scene):
    def construct(self):
        eq=Tex("1/Life span $\propto$ Chaos")
        self.play(Write(eq))
        self.wait(10)
