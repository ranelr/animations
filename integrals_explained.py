from manim import *
import numpy as np




class IntegralVid(Scene):
    def construct(self):
        
        config.frame_height = 9
        config.frame_width = 16

        #INTRO
        opening_text = Tex('Integrals Explained in 51 seconds')

        fx = MathTex('f(x) = 2x')

        self.play(Create(opening_text))
        self.wait()
        self.play(FadeOut(opening_text))
        self.wait()
        self.play(Create(fx))
        self.wait()

        #CREATE GRAPH
        axes = Axes(
            x_range=[0,10,1], x_length=10,
            y_range=[0,20,2], y_length = 10,
            axis_config={'include_numbers':True,'include_tip':False}
        ).scale(0.6).to_edge(DL,buff=1)

        self.play(Create(axes),fx.animate.to_edge(UR,buff=1.5))
        self.wait()

        #CREATE FUNCTION
        func_eq = axes.plot(
            lambda x: 2*x,
            x_range = [0,10,1],
            color = GREEN
        )

        self.play(Create(func_eq))
        self.wait()

        
        #DRAW RECTANGLES
        dx_list = [2,1,0.5, 0.3, 0.1, 0.05, 0.025, 0.01]
        
        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=func_eq,
                    x_range=[0,5],
                    stroke_width=0.1,
                    stroke_color=WHITE,
                    dx=dx
                )
                for dx in dx_list
            ]
        )
        
        
        
        new_area = rectangles[1]
        
        self.play(Create(new_area),FadeOut(fx),
                    run_time=0.5)
        self.wait ()

        #FUNCTION VALUES
        f4 = MathTex('f(4) = 8',color=RED).to_edge(RIGHT,buff=8).shift(DOWN)
        f3 = MathTex('f(3) = 6',color=RED).to_edge(RIGHT,buff=8).shift(DOWN*1.5)
        f2 = MathTex('f(2) = 4',color=RED).to_edge(RIGHT,buff=8).shift(DOWN*2)
        f1 = MathTex('f(1) = 2',color=RED).to_edge(RIGHT,buff=8).shift(DOWN*2.5)

        funcs = VGroup(f1,f2,f3,f4)
        

        #CREATE DOTS ON CORNERS
        for i in range(1,len(new_area)):
            dot = Dot().move_to(new_area[i].get_corner(UL)).scale(1e-3)
            self.play(Create(SurroundingRectangle(dot,color=RED)),Create(funcs[i-1]))
            self.wait()
        

        #INTEGRAL - SUM FORM
        integral = MathTex('\lim_{n \\to 4}','\sum_{i=1}^{n}','\Delta x','\cdot','f(x_i)',
                           color=BLUE)
        

        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in funcs],
                  funcs.animate.move_to([0,-2,0]).scale(0.7),
                Create(integral)
                  )
        self.wait()

        expanded_sum = MathTex('= \Delta x \cdot ','f(1)','+',
                               '\Delta x \cdot ','f(2)','+',
                               '\Delta x \cdot ','f(3)','+',
                               '\Delta x \cdot ','f(4)',
                               color=BLUE
                               ).set_color_by_tex_to_color_map({'f(1)':RED,'f(2)':RED,'f(3)':RED,'f(4)':RED})
        
        self.play(FadeOut(funcs),Create(expanded_sum), integral.animate.shift(UP*2))
        self.wait(2)
        ans = MathTex('= 20', color=BLUE)
        self.play(ReplacementTransform(expanded_sum,ans))
        self.wait()


        #BRING BACK GRAPH W/ DELTA X AND AREA
        deltax = MathTex('\Delta x = ',str(dx_list[1]),color=BLUE).to_edge(DR,buff=2).shift(UP*2)
        approx_vals = [20,20,22.7,23.6,24.5,24.7,24.9,25]
        first_area_val = MathTex('Area \\approx ',approx_vals[1],color=BLUE).to_edge(DR,buff=2).shift(UP*3)

        self.play(FadeOut(ans),FadeIn(VGroup(axes,func_eq,new_area,first_area_val)),integral.animate.to_edge(RIGHT,buff=1),Create(deltax))
        self.wait()
        

        #INFINITE RECTANGLE ANIMATION
        first_area = rectangles[1]
        
        for k in range(2, len(dx_list)):
            new_area = rectangles[k]
            new_deltax = MathTex('\Delta x = ',str(dx_list[k]),color=BLUE).to_edge(DR,buff=2).shift(UP*2)
            new_integral = MathTex('\lim_{n \\to ',str(len(new_area)),'}','\sum_{i=1}^{n}','\Delta x','\cdot','f(x_i)',
                           color=BLUE).shift(UP*2).to_edge(RIGHT,buff=1)
            area_val = MathTex('Area \\approx ',approx_vals[k],color=BLUE).to_edge(DR,buff=2).shift(UP*3)


            self.play(Transform(first_area, new_area), Transform(deltax,new_deltax), 
                      Transform(integral,new_integral), Transform(first_area_val,area_val),
                       run_time=0.5)
            self.wait ()

            
        #SUM NOTATION TO INTEGRAL SYMBOL
        self.play(FadeOut(VGroup(axes, func_eq,first_area,deltax)),
                  integral.animate.move_to([-2,-1,0]).scale(1.5),first_area_val.animate.move_to([-2,-2,0]))
        self.wait()
        new_integral = MathTex('\lim_{n \\to \infty}','\sum_{i=1}^{n}','\Delta x','\cdot','f(x_i)',
                           color=BLUE).move_to([0,0,0]).scale(1.5)
        new_area_val = MathTex('Area = 25',color=BLUE).move_to([-2,-2,0])
        self.play(Transform(integral,new_integral),Transform(first_area_val,new_area_val))
        self.wait(2)

        integral2 = MathTex('\int_{0}^{5}2xdx = 25')

        self.play(ReplacementTransform(VGroup(integral,first_area_val),integral2))
        self.wait()
        self.play(Create(SurroundingRectangle(integral2,color=WHITE)))
        self.wait()


        
        