from manim import *
import numpy as np

class DerivativeGeometry(Scene):
    def construct(self):
        #INTRO
        opening_text = Tex('A Geometric Representation for the Derivative of $x^2$')

        self.play(Create(opening_text))
        self.wait(2)

        fx = MathTex('y = Area = x^2')

        self.remove(opening_text)
        self.play(Create(fx))
        self.wait(1.5)
        self.play(fx.animate.to_edge(UL,buff=1).scale(0.7))
        self.wait()
        
        #DRAW SQUARE 
        square = Square(4).shift(DOWN)
        x = MathTex('x').move_to(square.get_right()).shift(RIGHT*0.5).scale(1.5)
        x2 = x.copy().move_to(square.get_bottom()).shift(DOWN*0.5)

        self.play(Create(square))
        self.wait()
        self.play(Create(x),Create(x2))
        self.wait()

        #AREA ANIMATION
        area = MathTex('Area = x \cdot x').to_edge(LEFT,buff=1)
        a2 = MathTex('x^2').move_to(square.get_center()).scale(1.5)
    
        self.play(Create(area))
        self.wait()
        self.play(Transform(area,a2))
        self.wait()

        #AREA FUNCTION
        def animate_area_eq(eq, rect,area_val):
            self.play(Create(eq))
            self.wait()
            self.play(Transform(eq,area_val))
            self.wait()
        
        #INCREASE LENGTH 1
        dx = ValueTracker(1)

        def rct_update(x):
            x.set_height(dx.get_value())
            x.set_width(dx.get_value())

        def sqr_update(x):
            x.set_side_length(dx.get_value)

        rect1 = Rectangle(height=4, width = dx.get_value()).align_to(square,LEFT).shift(DL)
        deltax1 = MathTex('\Delta x').move_to(rect1.get_bottom()).shift(DOWN*0.5)
        added1 = MathTex('+ x\Delta x').move_to(fx.get_right()).shift(RIGHT*0.5).scale(0.7)

        area1 = MathTex('Area = x \cdot \Delta x').to_edge(LEFT,buff=0.5).shift(DOWN*0.5)
        val1 = MathTex('x \Delta x').rotate(PI / 2).move_to(rect1.get_center())

        self.play(Create(rect1),Create(deltax1))
        self.wait()
        animate_area_eq(area1,rect1,val1)
        self.play(Create(added1))
        self.wait()

        #INCREASE LENGTH 2
        rect2 = Rectangle(height=dx.get_value(), width=4).move_to(square.get_top()).shift(UP*0.5)
        deltax2 = deltax1.copy().move_to(rect2.get_right()).shift(RIGHT*0.5)
        added2 = MathTex('+ x\Delta x').move_to(added1.get_right()).shift(RIGHT*0.5).scale(0.7)

        area2 = MathTex('Area = x \cdot \Delta x').to_edge(LEFT,buff=0.5).shift(DOWN*0.5)
        val2 = MathTex('x \Delta x').move_to(rect2.get_center())

        self.play(Create(rect2),Create(deltax2))
        self.wait()
        animate_area_eq(area2,rect2,val2)
        self.play(Create(added2))
        self.wait()

        #INCREASE LENGTH 3
        mini_square = Square(dx.get_value()).move_to(square.get_corner(UL)).shift(UL*0.5)
        added3 = MathTex('+ \Delta x^2').move_to(added2.get_right()).shift(RIGHT*0.5).scale(0.7)

        area3 = MathTex('Area = \Delta x \cdot \Delta x').to_edge(LEFT,buff=0.5).shift(DOWN*0.5)
        val3 = MathTex('\Delta x^2').move_to(mini_square.get_center())

        self.play(Create(mini_square))
        self.wait()
        animate_area_eq(area3,mini_square,val3)
        self.play(Create(added3))
        self.wait()

        #CHANGE IN AREA
        fx_eq = VGroup(fx,added1,added2,added3)

        added4 = MathTex('\lim_{\Delta x \\to 0}').move_to(fx_eq.get_left()).shift(LEFT*0.5).scale(0.7) 

        fx_eq = VGroup(
            fx,added1,added2,added3,added4
        )

        square_shi = VGroup(square,rect1,rect2,mini_square,area,area1,area2,area3,x,x2,deltax1,deltax2)

        self.play(square_shi.animate.scale(0.4).to_edge(DR),
                  fx_eq.animate.move_to(ORIGIN).scale(1.3)
                  )
        self.wait()

        self.play(Circumscribe(fx_eq[4],time_width=0.5))
        self.wait()

        new_fx = MathTex('Area = ','x^2','+','2xdx').move_to(fx_eq)

        self.play(ReplacementTransform(fx_eq,new_fx))
        self.wait()

        self.play(
            new_fx.animate.to_edge(UL,buff=1),
            square_shi.animate.scale(0.4**-1).move_to([0,-1,0])
        )

        rect_color = WHITE

        new_rect1 = always_redraw(lambda: Rectangle(height=4, width = dx.get_value(),color=rect_color).move_to(rect1))
        new_rect2 = always_redraw(lambda: Rectangle(height=dx.get_value(), width = 4,color=rect_color).move_to(rect2))
        new_square = always_redraw(lambda: Square(dx.get_value()).move_to(mini_square))

        self.play(ReplacementTransform(rect1,new_rect1),ReplacementTransform(rect2,new_rect2),ReplacementTransform(mini_square,new_square))
        self.wait()
        self.play(FadeOut(
            VGroup(deltax1,deltax2,area1,area2,area3)
        ))
        self.play(dx.animate.set_value(1e-2))
        self.play(FadeOut(new_square))
        self.play(*[Circumscribe(mob,color=BLUE,run_time=2) for mob in [new_fx[3],new_rect1,new_rect2]])
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob is not new_fx],new_fx.animate.scale(1.5).move_to(ORIGIN))
        self.wait()

        #FINAL ALGEBRA
        box1 = SurroundingRectangle(new_fx[1],color=RED)
        box2 = SurroundingRectangle(new_fx[3],color=BLUE)

        text1 = Tex('Original Area',color=RED).move_to(box1.get_top()).shift(UP*0.5).scale(0.7)
        text2 = Tex('Change in Area',color=BLUE).move_to(box2.get_bottom()).shift(DOWN*0.5).scale(0.7)

        eq1 = Tex('Change in Area $= 2xdx$')

        self.play(Create(box1),Create(text1))
        self.wait()
        self.play(Create(box2),Create(text2))
        self.wait(1.5)
        self.play(ReplacementTransform(VGroup(new_fx,box1,box2,text1,text2),eq1))
        self.wait()

        eq2 = MathTex('da = 2xdx')
        eq3 = MathTex('dy = 2xdx')
        eq4 = MathTex('\\frac{dy}{dx} = 2x')

        eqs = [eq1,eq2,eq3,eq4]

        for i in range(len(eqs[:-1])):
            self.play(ReplacementTransform(eqs[i],eqs[i+1]))
            self.wait()

        self.play(Create(SurroundingRectangle(eq4,color=WHITE,buff=1)))
        self.wait()





        
        
