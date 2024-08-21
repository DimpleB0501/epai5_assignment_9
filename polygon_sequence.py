from polygon import Polygon
from functools import lru_cache

class PolygonSequence:
    """
    Custom polygon sequence
    """
    def __init__(self, n_edges: int, circumradius: float) -> None:
        self.largest_num_edges = n_edges
        self.circumradius = circumradius
        self.ratios = dict()

    def __repr__(self) -> str:
        """
        This function displays output of the class object.
        """
        if bool(self.ratios):
            data = [f"{key}:{value}\n" for key, value in self.ratios.items()]
            dict_info = "".join(data)
        else:
            dict_info = "Empty Dictionary"
        return f"Polygon starting from {3} to {self.largest_num_edges} sides and {self.circumradius} circumradius \n {dict_info}"

    def __len__(self) -> int:
        """
        This function returns the length (vertices/ edges)
        """
        return self.n_edges

    @staticmethod
    @lru_cache(512)
    def ratio(n_edges:int, circumradius:int) -> float:
        """
        This function calculates ratio(area:perimeter)
        """
        if n_edges < 2:
            return 1
        else:
            obj = Polygon(n_edges, circumradius)
            return obj.area/obj.perimeter

    def __getitem__(self, edge: int) -> float:
        """
        This function takes edges and returns a sequence containing ratio(area: perimeter )
        """
        if isinstance(edge, int):
            if edge < 0:
                edge = edge + self.largest_num_edges
            if edge <0 or edge >= self.largest_num_edges:
                raise IndexError
            else:
                if edge > 1:
                    return PolygonSequence.ratio(edge, self.circumradius)
        else:
            raise IndexError

    @property
    def max_efficiency_polygon(self) -> str:
        """
        Returns the Polygon with the highest area: perimeter ratio
        """
        for r in range(self.largest_num_edges):
            if r > 1:
                self.ratios[r+1] = self.__getitem__(r)
        key = max(self.ratios, key = self.ratios.get)
        return f"Max ratio is {self.ratios[key]} at edge{key}"
