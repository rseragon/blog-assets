# Duff copy animation with limit 4

from manim import *

class Duff(Scene):
    def construct(self):
        self.camera.background_color = "#1b1b1e" 

        # Create two grids of size 10x1 and 10x1 and place them next to each other
        grid1 = NumberPlane(x_range=[0, 10, 1], y_range=[0, 1, 1], x_length=10, y_length=1)
        grid2 = NumberPlane(x_range=[0, 10, 1], y_range=[0, 1, 1], x_length=10, y_length=1)
        grid1.shift(UP * 2)
        grid2.shift(DOWN * 2)

        self.play(Create(grid1), Create(grid2))

        # Add src and dest labels
        src = Tex("src")
        dest = Tex("dest")
        # Set src and dest to yellow color
        src.set_color(YELLOW)
        dest.set_color(YELLOW)
        src.next_to(grid1, LEFT)
        dest.next_to(grid2, LEFT)
        self.add(src, dest)

        # Add numbers in the first grid1
        grid1_texts = []
        for i in range(10):
            text = Text(str(i))
            text.move_to(grid1.coords_to_point(i, 0) + UP * 0.5 + RIGHT * 0.5)
            grid1_texts.append(text)
            self.add(text)

        # Add \0 to the second grid
        grid2_texts = []
        for i in range(10):
            text = Text("\\0")
            text.move_to(grid2.coords_to_point(i, 0) + UP * 0.5 + RIGHT * 0.5)
            grid2_texts.append(text)
            self.add(text)

        # Create text in middle of grids
        equation = Tex("n = (len + 3) / 4")
        calculation1 = Tex("n = (10 + 3) / 4")
        calculation2 = Tex("n = 13 / 4")
        calculation3 = Tex("n = 3")
        self.play(Write(equation))
        self.wait(1)
        self.play(ReplacementTransform(equation, calculation1))
        self.wait(1)
        self.play(ReplacementTransform(calculation1, calculation2))
        self.wait(1)
        self.play(ReplacementTransform(calculation2, calculation3))
        self.wait(1)

        case_text_len = Tex("Case: len \% 4").shift(0.75 * DOWN).set_color(BLUE)
        case_text10 = Tex("Case: 10 \% 4").shift(0.75 * DOWN).set_color(BLUE)
        case_text2 = Tex("Case: 2").shift(0.75 * DOWN).set_color(BLUE)

        self.play(Write(case_text_len))
        self.wait(1)
        self.play(ReplacementTransform(case_text_len, case_text10))
        self.wait(1)
        self.play(ReplacementTransform(case_text10, case_text2))
        self.wait(1)


        # Create 4 arrows and move them to the correct positions above the grid 1 and 2
        arrows = []
        for i in range(4):
            arrow = Arrow(start=ORIGIN, end=DOWN)
            arrow.color = BLUE
            arrow.move_to(grid1.coords_to_point(i, 0) + UP * 1.5)
            arrow.shift(RIGHT * 0.5)
            arrows.append(arrow)

        # Create new texts for grid2 containg grid1 texts
        new_grid2_texts = []
        for i in range(10):
            text = Text(str(i))
            text.move_to(grid2.coords_to_point(i, 0) + UP * 0.5 + RIGHT * 0.5)
            new_grid2_texts.append(text)
            
        # First we show 2 texts
        self.play(Create(arrows[0]), Create(arrows[1]))
        for i in range(2):
            # Convert the text in grid2 to grid1 text
            self.play(Uncreate(grid2_texts[i]))
            self.play(TransformFromCopy(grid1_texts[i].copy(), new_grid2_texts[i]))

        # Change the case to 0
        case_text0 = Tex("Case: 0").shift(0.75 * DOWN).set_color(BLUE)
        self.play(ReplacementTransform(case_text2, case_text0))

        # Move the arrows 4 time to the right
        self.add(arrows[2], arrows[3])
        for i in range(2):
            self.play(ApplyMethod(arrows[i].shift, RIGHT * 4))

        for i in range(2, 6):
            self.play(Uncreate(grid2_texts[i]))
            self.play(TransformFromCopy(grid1_texts[i].copy(), new_grid2_texts[i]))

        for i in range(4):
            self.play(ApplyMethod(arrows[i].shift, RIGHT * 4))

        for i in range(6, 10):
            self.play(Uncreate(grid2_texts[i]))
            self.play(TransformFromCopy(grid1_texts[i].copy(), new_grid2_texts[i]))

        self.wait(3)
