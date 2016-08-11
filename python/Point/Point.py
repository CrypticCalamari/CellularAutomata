from collections import namedtuple

Point2D = namedtuple("Point2D", ["x", "y"])
Point3D = namedtuple("Point3D", ["x", "y", "z"])
Point4D = namedtuple("Point4D", ["x", "y", "z", "t"])
class PointM:
	def __init__(self, *args):
		self.p = tuple(args)







