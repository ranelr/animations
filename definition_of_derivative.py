from manim import *
import numpy as np


class Intro(Scene):
    def construct(self):
        definition = Tex(
        '$$\lim_{\Delta x \\to \infty}\\frac{f(x + \Delta x) - f(x)}{\Delta x}$$'
        )

        self.play(Create(definition))
        self.wait()

class Graph(Scene):
    def construct(self):
        
        
        axes = (
            Axes(
                x_range = [0,10,1],
                x_length=9,
                y_range=[0,20,5],
                y_length=6,
                axis_config={'include_numbers':True,'include_tip':False}
            )
            .to_edge(DL)
            .set_color(GREY)
            .shift(DOWN*0.4)
            .scale(0.7)
        )
        axes_labels = axes.get_axis_labels(x_label='x',y_label='y')

        func = axes.plot(lambda x:
            0.2*x**2,
            x_range = [0,10,1],
            color = GREEN
        )

        func_eq = Tex('$$f(x) = 0.2x^2$$',color=RED_D)
        func_eq.shift(UL*3.1)

        definition_index = ValueTracker(0)

        definitions = [
            '$$\lim_{\Delta x \\to 0}\\frac{f(x + \Delta x) - f(x)}{\Delta x}$$',
            '$$\lim_{\Delta x \\to 0}\\frac{0.2 {\Delta x}^2 - 0.2x^2}{\Delta x}$$'
        ]

        def_derv = always_redraw(lambda:
        
            Tex(
            definitions[int(definition_index.get_value())]
            )
            .scale(0.8).shift(UR*3.1)
        )
        x = ValueTracker(7)
        dx = ValueTracker(2)

        secant = always_redraw(
            lambda:axes.get_secant_slope_group(
                x=x.get_value(),
                graph=func,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label='dx',
                dy_label='dy',
                secant_line_color=DARK_BLUE,
                secant_line_length=6
            
            )
        )

        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(x.get_value(),func.underlying_function(x.get_value())))
        )

        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(
                x.get_value()+dx.get_value(),
                func.underlying_function(x.get_value() + dx.get_value()))
            )
        )


        self.play(Create(VGroup(axes,axes_labels,func)),run_time=2)
        self.wait()
        self.play(Create(VGroup(dot1,dot2,secant,func_eq)))
        self.play(Create(def_derv))
        self.play(dx.animate.set_value(1e-3),run_time=6)
        self.wait()
        self.play(definition_index.animate.set_value(1))
        self.wait(2)
        # self.play(x.animate.set_value(1),run_time=5)
        # self.wait()
        # self.play(x.animate.set_value(7),run_time=5)
        # self.wait()
        # self.play(dx.animate.set_value(2),run_time=6)
        # self.wait()



