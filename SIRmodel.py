from manim import *
import math

class Example12(Scene):
    def construct(self):
        ax = Axes(x_range=(0,10),y_range=(0,10),x_length = 14, y_length = 7, axis_config={"include_numbers":False},)

        plane = NumberPlane(x_range=(0,10),y_range=(0,10),x_length = 14 , y_length = 7 , axis_config={"include_numbers": False},)
        arrow1 = Arrow(start=DOWN,end=UP*2.4+RIGHT*2.3,color=GOLD).shift(UP*0.8+LEFT*0.2)

        def Sus(b,g):
            s=10
            inf=1
            r=0
            sus = []
            for i in range(1,20):
                ds = -1*b*inf*s
                di = b*inf*s-g*inf
                dr = g*inf
                s=s+ds
                inf = inf+di
                r = r+dr
                sus = sus+[s]
            return(sus)
        def Rec(b,g):
            s=10
            inf=1
            r=0
            rec = []
            for i in range(1,20):
                ds = -1*b*inf*s
                di = b*inf*s-g*inf
                dr = g*inf
                s=s+ds
                inf = inf+di
                r = r+dr
                rec = rec+[r]
            return(rec)
        def Inf(b,g):
            s=10
            inf=1
            r=0
            infc = []
            for i in range(1,20):
                ds = -1*b*inf*s
                di = b*inf*s-g*inf
                dr = g*inf
                s=s+ds
                inf = inf+di
                r = r+dr
                infc = infc+[inf]
            return(infc)
            
                
        self.play(Write(ax))
        
        for i in range(1,20):
            dot1=Dot(point=(0.5*i,0.5*Sus(0.1,0.1)[i-1],0),color=BLUE).shift(LEFT*6+DOWN*3)
            dot2=Dot(point=(0.5*i,0.5*Inf(0.1,0.1)[i-1],0),color=RED).shift(LEFT*6+DOWN*3)
            dot3=Dot(point=(0.5*i,0.5*Rec(0.1,0.1)[i-1],0),color=GREEN).shift(LEFT*6+DOWN*3)

            self.play(Write(dot1))
            self.play(Write(dot2))
            self.play(Write(dot3))
            
    
        self.wait(5)
