from manim import *


class WildPtr(Scene):
    def construct(self):
        self.camera.background_color = "#1b1b1e" 
        
        memory = Rectangle(width=12.0, height = 7.0, grid_xstep=3.0, grid_ystep=1.0).shift(DOWN)
        memory_title = Text("Memory").scale(0.8).shift(3 * UP)

        wild_ptr_var = Text("P").shift(4 * LEFT).shift(UP)
        wild_ptr_adr = Text("0x0ef..").shift(4 * LEFT).scale(0.6)


        arrow = Arrow(start=LEFT, end=RIGHT).next_to(wild_ptr_adr)

        # self.play(Create(rectangle), wild_ptr_var.animate(), wild_ptr_adr.animate(), Create(arrow), memory.animate())
        self.add(wild_ptr_var, wild_ptr_adr, arrow, memory, memory_title)
