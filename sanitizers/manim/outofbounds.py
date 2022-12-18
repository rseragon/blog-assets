from manim import *

class OutOfBounds(Scene):
    def construct(self):
        self.camera.background_color = "#1b1b1e"

        memory = Rectangle(width=6.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0, color=YELLOW)

        bad_memory = Text("fa", color=RED)
        good_mem   = Text("00", color=GREEN)
        
        bm1 = bad_memory.copy().shift(LEFT * 1.5)
        bm2 = bad_memory.copy().shift(LEFT * 2.5)
        bm3 = bad_memory.copy().shift(RIGHT * 1.5)
        bm4 = bad_memory.copy().shift(RIGHT * 2.5)

        gm1 = good_mem.copy().shift(RIGHT * 0.5)
        gm2 = good_mem.copy().shift(LEFT * 0.5)

        write_arrow = Arrow(start=UP, end=DOWN)
        write_arrow.shift(RIGHT * 1.5).shift(UP)
        
        # Show memory
        self.add(memory, bm1, bm2, bm3, bm4, gm1, gm2)
        self.play(GrowArrow(write_arrow))
        self.wait(1)
    
        # Write failed
        write_arrow.color = RED
        bad_write = Rectangle(width=0.9, height=0.9, color=RED).set_opacity(0.5).shift(RIGHT * 1.5)
        self.play(FadeIn(bad_write), Indicate(write_arrow))

        # Invalid write text
        invalid_write = Text("Error: Write out of bounds", color=RED).shift(DOWN * 2)
        self.play(Write(invalid_write))


        self.wait(2)
