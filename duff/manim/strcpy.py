from manim import *

class Strcpy(Scene):
    def construct(self):
        # Create 2 grids of size 5 x 1 and 5 x 1
        grid1 = NumberPlane(x_range=[0, 5, 1], y_range=[0, 1, 1])
        grid2 = NumberPlane(x_range=[0, 5, 1], y_range=[0, 1, 1])

        # Display the grids side by side with space between them
        grid1.shift(LEFT * 3)
        grid2.shift(RIGHT * 3)

        # Initialize the grids with the labels src and dest
        src = Tex("src")
        dest = Tex("dest")
        src.next_to(grid1, UP)
        dest.next_to(grid2, UP)

        # Create the labels for the characters
        src_char_h = Tex("H")
        dest_char_h = Tex("\\textbackslash 0")
        src_char_h.shift(LEFT * 5)
        dest_char_h.shift(RIGHT * 1)

        src_char_o = Tex("O")
        dest_char_o = Tex("\\textbackslash 0")
        src_char_o.shift(LEFT * 4)
        dest_char_o.shift(RIGHT * 2)

        src_char_l = Tex("L")
        dest_char_l = Tex("\\textbackslash 0")
        src_char_l.shift(LEFT * 3)
        dest_char_l.shift(RIGHT * 3)

        src_char_a = Tex("A")
        dest_char_a = Tex("\\textbackslash 0")
        src_char_a.shift(LEFT * 2)
        dest_char_a.shift(RIGHT * 4)

        src_char_0 = Tex("\\textbackslash 0")
        dest_char_0 = Tex("\\textbackslash 0")
        src_char_0.shift(LEFT * 1)
        dest_char_0.shift(RIGHT * 5)

        # Create the labels for the arrows
        src_arrow = Arrow(start=ORIGIN, end=UP)
        dest_arrow = Arrow(start=ORIGIN, end=UP)
        src_arrow.color = YELLOW
        dest_arrow.color = GREEN
        src_arrow.next_to(grid1, DOWN)
        dest_arrow.next_to(grid2, DOWN)
        src_arrow.shift(LEFT * 2)
        dest_arrow.shift(LEFT * 2)

        # Show the grids
        self.play(Create(grid1), Create(grid2))
        self.add(src, dest)

        self.add(src_char_h, dest_char_h)
        self.add(src_char_o, dest_char_o)
        self.add(src_char_l, dest_char_l)
        self.add(src_char_a, dest_char_a)
        self.add(src_char_0, dest_char_0)

        self.play(Create(src_arrow), Create(dest_arrow))
        self.wait(0.5)

        # Move the first char from src to dest and blink the arrow and move them
        self.play(Indicate(src_char_h), Indicate(dest_char_h), Indicate(src_arrow), Indicate(dest_arrow))
        src_char_h_copy = src_char_h.copy()
        self.play(src_char_h_copy.animate.shift(RIGHT * 6))
        self.remove(dest_char_h)
        self.wait(0.5)
        
        # Move the arrows by 1
        self.play(src_arrow.animate.shift(RIGHT * 1), dest_arrow.animate.shift(RIGHT * 1))

        # Move the second char from src to dest and blink the arrow and move them
        self.play(Indicate(src_char_o), Indicate(dest_char_o), Indicate(src_arrow), Indicate(dest_arrow))
        src_char_o_copy = src_char_o.copy()
        self.play(src_char_o_copy.animate.shift(RIGHT * 6))
        self.remove(dest_char_o)
        self.wait(0.5)
        
        # Move the arrows by 1
        self.play(src_arrow.animate.shift(RIGHT * 1), dest_arrow.animate.shift(RIGHT * 1))

        # Move the thrid char from src to dest and blink the arrow and move them
        self.play(Indicate(src_char_l), Indicate(dest_char_l), Indicate(src_arrow), Indicate(dest_arrow))
        src_char_l_copy = src_char_l.copy()
        self.play(src_char_l_copy.animate.shift(RIGHT * 6))
        self.remove(dest_char_l)
        self.wait(0.5)
        
        # Move the arrows by 1
        self.play(src_arrow.animate.shift(RIGHT * 1), dest_arrow.animate.shift(RIGHT * 1))

        # Move the thrid char from src to dest and blink the arrow and move them
        self.play(Indicate(src_char_a), Indicate(dest_char_a), Indicate(src_arrow), Indicate(dest_arrow))
        src_char_a_copy = src_char_a.copy()
        self.play(src_char_a_copy.animate.shift(RIGHT * 6))
        self.remove(dest_char_a)
        self.wait(0.5)
        
        # Move the arrows by 1
        self.play(src_arrow.animate.shift(RIGHT * 1), dest_arrow.animate.shift(RIGHT * 1))

        # Move the thrid char from src to dest and blink the arrow and move them
        self.play(Indicate(src_char_0), Indicate(dest_char_0), Indicate(src_arrow), Indicate(dest_arrow))
        src_char_0_copy = src_char_0.copy()
        self.play(src_char_0_copy.animate.shift(RIGHT * 6))
        self.remove(dest_char_0)
        self.wait(0.5)
        
        self.play(Indicate(dest_char_0, color=RED), Indicate(src_char_0, color=RED))
