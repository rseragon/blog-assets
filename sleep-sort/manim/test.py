from manim import *


class PlotPointsAndScale(Scene):
    def construct(self):
        # Define the points to plot
        points = [1, 20, 30, 41, 83, 95, 113, 129]

        # Create axes
        axes = Axes(
            x_range=[-10, 140, 20],
            y_range=[-50, 70, 10],
            axis_config={"color": BLUE, "include_numbers": True},
        )

        # Plot original points
        original_points = []
        for point in points:
            original_points.append(Dot().move_to(axes.c2p(point, 20)))

        # Create animations for plotting original points and line
        self.play(Create(axes, introducer=True))

        # Plot the original line graph
        line = axes.plot_line_graph(
            x_values=points, y_values=[20] * len(points), line_color=BLUE
        )
        self.play(Create(line))

        # Create scaled line graph
        scaled_line = axes.plot_line_graph(
            x_values=[point / 2 for point in points],
            y_values=[10] * len(points),
            line_color=BLUE,
        )

        # Animate scaling of the line graph
        self.play(Transform(line, scaled_line))

        # Create scaled points
        scaled_points = []
        for point in points:
            scaled_point = Dot().move_to(axes.c2p(point / 2, 10))
            scaled_points.append(scaled_point)

        self.wait()
