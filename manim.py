from manim import *

class Construct45Degree(Scene):
    def construct(self):
        # Step 1: Draw the base line
        base = Line(LEFT * 3, RIGHT * 3)
        self.play(Create(base))

        # Step 2: Draw the first 60-degree arc
        circle1 = Arc(radius=2, angle=PI / 3, arc_center=ORIGIN)
        self.play(Create(circle1))

        # Step 3: Mark the first 60-degree point
        point_60 = Dot(circle1.get_end(), color=BLUE)
        self.play(Create(point_60))

        # Step 4: Use the same radius to mark another 60-degree segment (total 120°)
        circle2 = Arc(radius=2, start_angle=PI / 3, angle=PI / 3, arc_center=point_60.get_center())
        self.play(Create(circle2))

        # Step 5: Mark the second 60-degree point
        point_120 = Dot(circle2.get_end(), color=BLUE)
        self.play(Create(point_120))

        # Step 6: Intersecting arcs to get 45-degree angle
        circle3 = Arc(radius=2.5, arc_center=point_60.get_center(), angle=-PI / 3)
        circle4 = Arc(radius=2.5, arc_center=point_120.get_center(), angle=PI / 3)
        self.play(Create(circle3), Create(circle4))

        # Step 7: Intersection point for 45-degree line
        intersection = Dot(interpolate(circle3.get_end(), circle4.get_end(), 0.5), color=RED)
        self.play(Create(intersection))

        # Step 8: Draw 45-degree angle line
        angle_line = Line(ORIGIN, intersection.get_center(), color=GREEN)
        self.play(Create(angle_line))

        self.wait(2)
