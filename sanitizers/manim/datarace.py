from manim import *

class DataRace(Scene):
    def construct(self):
        self.camera.background_color = "#252525"
        # GLOBAL VARIABLE
        global_text = Text("GLOBAL", color=GREY).shift(UP)
        global_count = Text("0")
        global_box = Rectangle(width= 3, height= 1.0, color=YELLOW)

        global_group = VGroup()
        global_group.add(global_box, global_text, global_count)

        self.add(global_group)

        # Threads
        t1_text = Text("Thread 1", color=GREEN_A).shift(3 * DOWN).shift(2.2 * LEFT)
        t1_box  = Rectangle(width=4.0, height=1.0, color=WHITE).shift(3 * DOWN).shift(2.2 * LEFT)
        thread1 = VGroup().add(t1_box, t1_text)

        t2_text = Text("Thread 2", color=GREEN_A).shift(3 * DOWN).shift(2.2 * RIGHT)
        t2_box  = Rectangle(width=4.0, height=1.0, color=WHITE).shift(3 * DOWN).shift(2.2 * RIGHT)
        thread2 = VGroup().add(t2_box, t2_text)

        self.add(thread1, thread2)

        
        # Write try
        t1_write = Arrow(start=(DOWN * 3) + (LEFT * 2), end=DOWN * 0.1 ) 
        t2_write = Arrow(start=(DOWN * 3) + (RIGHT * 2), end=DOWN * 0.1 ) 

        self.play(GrowArrow(t1_write), GrowArrow(t2_write))

        # T2 fails
        t1_count = Text("1")
        t1_succ = Text("T1: Success\nT2: Failed", color=BLUE, t2c={"Success": GREEN, "Failed": RED})
        t1_succ.shift(UP * 2.5).shift(LEFT * 3).scale(0.5)

        self.remove(global_count)
        self.add(t1_count)
        t1_write.set_color(GREEN)
        t2_write.set_color(RED)
        self.play(Indicate(t1_write), Indicate(t1_count), Write(t1_succ))

        # Reset
        t1_write.set_color(WHITE)
        t2_write.set_color(WHITE)
        self.remove(t1_succ)


        # T1 fails
        t2_count = Text("2")
        t2_succ = Text("T1: Failed\nT2: Success", color=BLUE, t2c={"Success": GREEN, "Failed": RED})
        t2_succ.shift(UP * 2.5).shift(LEFT * 3).scale(0.5)

        self.remove(t1_count)
        self.add(t2_count)
        t1_write.set_color(RED)
        t2_write.set_color(GREEN)
        self.play(Indicate(t2_write), Indicate(t2_count), Write(t2_succ))


        self.wait(3)
