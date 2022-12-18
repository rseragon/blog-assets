from manim import *


class WildPtr(Scene):
    def construct(self):
        self.camera.background_color = "#1b1b1e" 
        
        rectangle = Rectangle(width=2.0, height=1.0, color=YELLOW)
        wild_ptr_var = Text("P", color=BLUE).shift(UP)
        wild_ptr_adr = Text("0x000", color="#4c566a").scale(0.6)

        self.play(Create(rectangle), wild_ptr_var.animate(), wild_ptr_adr.animate())
        # self.add(rectangle, wild_ptr_var, wild_ptr_adr, arrow, memory, memory_title)
        self.wait()
