from manim import *
from math import sqrt


def point_scaler(points, with_k=True):
    m = max(points)
    K = 4000  # A constant so that it looks good while drawing
    if with_k:
        return [K * sqrt(p) / m for p in points]
    else:
        return [sqrt(p) / m for p in points]


class PlotPointsAndScale(Scene):
    def construct(self):
        self.camera.background_color = "#1b1b1e"

        # Define the points to plot
        points = [1, 100, 231, 444, 555, 766]

        # Create axes
        axes = Axes(
            x_range=[-10, 800, 100],
            y_range=[-10, 70, 10],
            axis_config={"color": BLUE},
        )

        # Plot original points with labels
        original_points = []
        labels_original = []  # To store labels for original points
        for point in points:
            dot = Dot().move_to(axes.c2p(point, 20))
            original_points.append(dot)
            label = MathTex(f"{point}").next_to(dot, UP)
            labels_original.append(label)
            self.add(dot, label)

        # Create axes and plot them
        self.add(axes)

        # Plot the original line graph
        line = axes.plot_line_graph(
            x_values=points, y_values=[20] * len(points), line_color=BLUE
        )
        self.add(line)

        # Create scaled line graph
        scaled_points = point_scaler(points)
        scaled_points_show = point_scaler(points, False)
        scaled_line = axes.plot_line_graph(
            x_values=scaled_points,
            y_values=[10] * len(points),
            line_color=BLUE,
        )

        # Animate scaling of the line graph and labels
        animations = []
        for i in range(len(points)):
            animations.append(
                Transform(
                    original_points[i], Dot().move_to(axes.c2p(scaled_points[i], 10))
                )
            )
            animations.append(
                Transform(
                    labels_original[i],
                    MathTex(f"{scaled_points_show[i] * 100:.01f}").next_to(
                        axes.c2p(scaled_points[i], 10), UP if i % 2 else DOWN
                    ),
                )
            )
            animations.append(Transform(line, scaled_line))

        self.play(*animations)

        # Animate scaling back to the original line graph and labels
        animations = []
        for i in range(len(points)):
            animations.append(
                Transform(original_points[i], Dot().move_to(axes.c2p(points[i], 20)))
            )
            animations.append(
                Transform(
                    labels_original[i],
                    MathTex(f"{points[i]}").next_to(axes.c2p(points[i], 20), UP),
                )
            )
            animations.append(
                Transform(
                    line,
                    axes.plot_line_graph(
                        x_values=points, y_values=[20] * len(points), line_color=BLUE
                    ),
                )
            )

        self.play(*animations)

        self.wait()
