from manim import *
import numpy as np

class TripletPrime(Scene):
    def construct(self):
        
       
        #INTRO
        thm = Tex('Theorem: $\{3, 5, 7\}$ is the Only Prime Triplet')
        
        self.play(Create(thm)), self.wait()

        pn = Tex('Let $p_n \in \N$ be any arbitrary number greater than 5')
