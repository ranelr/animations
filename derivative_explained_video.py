from manim import *
import numpy as np


class Video(Scene):
    def construct(self):

        #INTRO
        opening_text = Tex('Definition of a Derivative in 58 seconds')

        definition_eq = (
            MathTex('\lim_{\Delta x \\to 0}','\\frac{f(x + \Delta x)-f(x)}{\Delta x}') 
        )


        #BRING IN GRAPH
        axes = (
            Axes(
                x_range=[0,8,1], x_length = 10, y_range = [0,64,4], y_length = 8,
                axis_config={'include_tip':False,'include_numbers':True}
            )
            .scale(0.7)
            .to_edge(DL)
            
        )
        
        func_eq = axes.plot(
            lambda x: x**2, x_range=[0,8,0.5], color=GREEN
        )

        func_text = MathTex('f(x) = x^2',color = GREEN).move_to(axes,UP)
        
        #CHANGE DEF DERV EQUATION TO FIT X^2

        framebox1 = SurroundingRectangle(definition_eq[1][:12], buff = .1)

        text1 = MathTex('(x + \Delta x)^2 - x^2',color = GREEN).move_to([1,1,0])
        text2 = MathTex('(x^2 + 2x \Delta x + \Delta x^2) - ','x^2',color=GREEN).move_to([1,1,0])
        text3 = MathTex('2x \Delta x + ','\Delta x^2',color=GREEN).move_to([1,1,0])
        
        definition_eq2 = MathTex('\lim_{\Delta x \\to 0}','{2x + ','\Delta x}',color = WHITE)


        #DRAW TANGENT LINE AND VISUALIZE DERIVATIVE

        x = ValueTracker(3)
        dx = ValueTracker(2)
        
        secant_line = always_redraw(lambda:
            axes.get_secant_slope_group(
                x=x.get_value(),
                graph=func_eq,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label=MathTex('\Delta x'),
                dy_label=MathTex('f(x + \Delta x) - f(x)'),
                secant_line_color=DARK_BLUE,
                secant_line_length=6
            )
        )

        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(x.get_value(),func_eq.underlying_function(x.get_value())))
        )

        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(
                x.get_value()+dx.get_value(),
                func_eq.underlying_function(x.get_value() + dx.get_value()))
            )
        )


        deltax = always_redraw(lambda:
            MathTex('\Delta x = ',str(round(dx.get_value(),3))).to_edge(RIGHT,buff=2)
        )

        deltax2 = MathTex('\Delta x \\approx 0').to_edge(RIGHT,buff=2)


        #ENDING
        definition_eq3 = MathTex('2x').to_edge(UR,buff=2)
        final_eq = MathTex('\\frac{d}{dx}x^2 = 2x',color=WHITE)

        #PLAY ANIMATION
        self.play(Create(opening_text))
        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.play(Create(definition_eq))
        self.wait()
        self.play(definition_eq.animate.to_edge(UR,buff=0.5).scale(0.7),run_time=2)
        self.play(Create(axes))
        self.wait()
        self.play(Create(func_eq))
        self.wait()
        self.play(Create(func_text))
        self.wait()
        self.play(VGroup(axes,func_eq,func_text).animate.scale(0.3).to_edge(DL),definition_eq.animate.move_to([0,0,0]).scale(0.7**-1),
                  run_time=2)
        self.wait()
        self.play(Create(framebox1))
        self.wait()
        self.play(Create(text1))
        self.wait()
        self.play(ReplacementTransform(text1,target_mobject=text2))
        self.wait()
        self.play(Circumscribe(text2[0][:3],time_width=0.7),Circumscribe(text2[1][:2],time_width=0.7))
        self.wait()
        self.play(ReplacementTransform(text2,target_mobject=text3))
        self.wait()
        self.play(Circumscribe(text3[0][2:4],time_width=1),Circumscribe(text3[1],time_width=1),
                  Circumscribe(definition_eq[1][13:],time_width=1))
        self.wait()
        self.play(FadeOut(framebox1),ReplacementTransform(VGroup(definition_eq,text3),target_mobject=definition_eq2))
        self.wait()
        self.play(definition_eq2.animate.to_edge(UR,buff=2),VGroup(axes,func_eq,func_text).animate.scale(0.3**-1).to_edge(DL))
        self.wait()
        self.play(Create(VGroup(secant_line,dot1,dot2)),run_time=2)
        self.wait()
        self.play(Create(deltax))
        self.wait()
        self.play(Circumscribe(definition_eq2[0],time_width=3))
        self.wait()
        self.play(dx.animate.set_value(1e-3),run_time=6)
        self.wait()
        self.play(ReplacementTransform(deltax,target_mobject=deltax2))
        self.wait()
        self.play(Circumscribe(deltax2,time_width=1),Circumscribe(definition_eq2[2],time_width=1))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob is not definition_eq2],definition_eq2.animate.move_to(ORIGIN).scale(1.5))
        self.wait()
        self.play(FadeOut(definition_eq2[0]),FadeOut(definition_eq2[2]),FadeOut(definition_eq2[1][2:]))
        self.wait()
        self.play(ReplacementTransform(definition_eq2[1][:2],target_mobject=final_eq))
        self.wait()
        self.play(Create(SurroundingRectangle(final_eq,color=WHITE)))
        self.wait()

        

        

