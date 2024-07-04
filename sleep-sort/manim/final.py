from manim import *
from math import sqrt


def point_scaler(points):
    m = max(points)
    return [4000 * sqrt(p) / m for p in points]


class PlotPointsAndScale(Scene):
    def construct(self):
        # Define the points to plot
        points = [1, 100, 231, 444, 555, 766]

        # Create axes
        axes = Axes(
            x_range=[-10, 800, 100],
            y_range=[-10, 70, 10],
            axis_config={"color": BLUE},
        )

        # Plot original points
        original_points = []
        for point in points:
            original_points.append(Dot().move_to(axes.c2p(point, 20)))

        # Create axes and plot them
        self.add(axes)

        # Plot the original line graph
        line = axes.plot_line_graph(
            x_values=points, y_values=[20] * len(points), line_color=BLUE
        )
        self.add(line)

        # Create scaled line graph
        scaled_line = axes.plot_line_graph(
            x_values=point_scaler(points),
            y_values=[10] * len(points),
            line_color=BLUE,
        )

        # Animate scaling of the line graph
        self.play(Transform(line, scaled_line))

        # Animate scaling back to the original line graph
        self.play(
            Transform(
                line,
                axes.plot_line_graph(
                    x_values=points, y_values=[20] * len(points), line_color=BLUE
                ),
            )
        )

        self.wait()
