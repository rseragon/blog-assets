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
        case_text = Text("Case: 4")
        self.play(Write(case_text))

        # Create 4 arrows and move them to the correct positions above the grid 1 and 2
        arrows = []
        for i in range(4):
            arrow = Arrow(start=ORIGIN, end=DOWN)
            arrow.color = BLUE
            arrow.move_to(grid1.coords_to_point(i, 0) + UP * 1.5)
            arrow.shift(RIGHT * 0.5)
            arrows.append(arrow)
            self.add(arrow)
            #self.play(Create(arrow))

        # Create new texts for grid2 containg grid1 texts
        new_grid2_texts = []
        for i in range(10):
            text = Text(str(i))
            text.move_to(grid2.coords_to_point(i, 0) + UP * 0.5 + RIGHT * 0.5)
            new_grid2_texts.append(text)
            
        for i in range(4):
            # Convert the text in grid2 to grid1 text
            self.play(Uncreate(grid2_texts[i]))
            self.play(TransformFromCopy(grid1_texts[i].copy(), new_grid2_texts[i]))

        ## Part 2

        # Move the arrows 4 time to the right
        for i in range(4):
            self.play(ApplyMethod(arrows[i].shift, RIGHT * 4))

        for i in range(4, 8):
            self.play(Uncreate(grid2_texts[i]))
            self.play(TransformFromCopy(grid1_texts[i].copy(), new_grid2_texts[i]))

        # Move the arrows 4 time to the right
        # Remove the last 2 arrows
        for i in range(2):
            self.play(ApplyMethod(arrows[i].shift, RIGHT * 4))
        self.remove(arrows[3], arrows[2])

        # Set the middle text to case 2
        new_case_text = Text("Case: 2")
        self.play(Transform(case_text, new_case_text))

        for i in range(8, 10):
            self.play(Uncreate(grid2_texts[i]))
            self.play(TransformFromCopy(grid1_texts[i].copy(), new_grid2_texts[i]))

        self.wait(3)
