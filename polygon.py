import math

class Polygon:
    """
    Implementation of Polygon class
    I/P: n_edges, circumradius
    Output can be interior_angle, edge_length, apothem, area, perimeter, __repr__, __eq__, __gt__
    """
    def __init__(self, n_edges: int, circumradius: float) -> None:
        self.n_edges = n_edges
        self.circumradius = circumradius

    def __repr__(self) -> str:
        """
        This function displays output of the class object.
        """
        return f"Polygon with {self.n_edges} sides and {self.circumradius} circumradius"

    @property
    def interior_angle(self) -> float:
        """
        Calculates the interior angle
        """
        return (self.n_edges-2)*(180/self.n_edges)

    @property
    def edge_length(self) -> float:
        """
        Calculates edge length
        """
        return (2*self.circumradius*math.sin(math.pi/self.n_edges))

    @property
    def apothem(self) -> float:
        """
        Calculates apothem
        """
        return (self.circumradius*math.cos(math.pi/self.n_edges))

    @property
    def area(self) -> float:
        """
        Calulates area
        """
        return ((1/2)*self.n_edges*self.edge_length*self.apothem)

    @property
    def perimeter(self) -> float:
        """
        Calculates perimeter
        """
        return (self.n_edges*self.edge_length)

    def __eq__(self, other) -> bool:
        """
        Equality check between polygon classes
        """
        if not isinstance(other, Polygon):
            raise ValueError("Polygons must be compared with polygons")

        return ((self.n_edges == other.n_edges) and (self.circumradius == other.circumradius))

    def __gt__(self, other) -> bool:
        """
        Check if n_edges is greater between classes
        """
        if not isinstance(other, Polygon):
            raise ValueError("Polygons must be compared with polygons")

        return (self.n_edges > other.n_edges)
