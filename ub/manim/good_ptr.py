from manim import *


class WildPtr(Scene):
    def construct(self):
        self.camera.background_color = "#1b1b1e" 
        
        rectangle = Rectangle(width=2.0, height=1.0, color=YELLOW).shift(4 * LEFT)
        wild_ptr_var = Text("P", color=BLUE).shift(4 * LEFT).shift(UP)
        wild_ptr_adr = Text("0xb0f..", color=GREEN).shift(4 * LEFT).scale(0.6)
        arrow = Arrow(start=LEFT, end=RIGHT, color=GREEN).next_to(rectangle)

        memory = Rectangle(width=4.0, height = 7.0, grid_xstep=1.0, grid_ystep=1.0, color=YELLOW).shift(RIGHT).shift(DOWN)
        memory_title = Text("Memory").scale(0.8).shift(RIGHT).shift(3 * UP)

        good_memory = Rectangle(width=4.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0, color=GREEN).shift(RIGHT)
        good_memory.set_fill(GREEN)
        good_memory.set_opacity(0.5)


        self.play(Create(rectangle), wild_ptr_var.animate(), wild_ptr_adr.animate(), Create(arrow), Create(memory), memory_title.animate(), good_memory.animate())
        # self.add(rectangle, wild_ptr_var, wild_ptr_adr, arrow, memory, memory_title)
        self.wait()
