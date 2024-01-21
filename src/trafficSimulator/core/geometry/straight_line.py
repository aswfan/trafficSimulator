from .segment import Segment

PAS = 0.01
CURVE_RESOLUTION = 50

class StraightLine(Segment):
    def __init__(self, id, start, end, **kwargs):
        # Store characteristic points
        self.start = start
        self.end = end

        # Generate path
        path = []
        for i in range(CURVE_RESOLUTION):
            t = i/(CURVE_RESOLUTION-1)
            x = (1 - t) * self.start[0] + t * self.end[0]
            y = (1 - t) * self.start[1] + t * self.end[1]
            path.append((x, y))

        super().__init__(id=id, points=path, **kwargs)

        # Arc-length parametrization
        normalized_path = self.find_normalized_path(CURVE_RESOLUTION)
        super().__init__(id=id, points=normalized_path, **kwargs)

    def compute_x(self, t):
        return (1 - t) * self.start[0] + t * self.end[0]
    def compute_y(self, t):
        return (1 - t) * self.start[1] + t * self.end[1]
    def compute_dx(self, t):
        return self.end[0] - self.start[0]
    def compute_dy(self, t):
        return self.end[1] - self.start[1]