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

        # Create animations for plotting original points
        self.play(Create(axes, introducer=True))
        for point in original_points:
            self.add(point)

        # Create animations for scaling down points
        scaled_points = []
        for point in points:
            scaled_point = axes.c2p(point / 2, 10)
            scaled_points.append(Dot().move_to(scaled_point))

        line = axes.plot_line_graph(
            x_values=points, y_values=[20] * len(points), line_color=BLUE
        )
        self.play(Create(line))

        for i, point in enumerate(original_points):
            self.play(Transform(point, scaled_points[i]))

        self.wait()
