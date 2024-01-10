from shapely.geometry import Point, Polygon

class Zone:

    def __init__(self, geometry, type, lat, lon, brand):
        self.geometry = geometry
        self.type = type
        self.brand = brand
        self.location = self.calc_middle_point()

    
    def __str__(self):
        return f"Zone(type={self.type}, location={self.location}, brand={self.brand})"
    

    def is_inside(self, location):
        return Polygon(self.geometry).contains(Point(location[0], location[1]))
    
    def calc_middle_point(self):
        # Tworzymy obiekt wielokąta z użyciem biblioteki Shapely
        shapely_polygon = Polygon(self.geometry)

        # Pobieramy środek wielokąta
        middle_point = shapely_polygon.centroid

        return (middle_point.x, middle_point.y)