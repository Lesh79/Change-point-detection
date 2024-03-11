from abc import ABC, abstractmethod
from typing import List


class CPD(ABC):
    def __init__(self, graph):
        self.graph = graph

    @abstractmethod
    def calculation_e(self, thao: int) -> float:
        """ "Calculate the mathematical expectation(E) using the formula"""
        pass

    def calculation_var(self, thao: int) -> float:
        """Calculate the variance using the formula"""
        pass

    def calculation_z(self, thao: int) -> float:
        """Calculating statistics"""
        pass

    def find_changepoint(self, border: float, zlist: List[float]) -> List:
        """ "Find change point in data"""
        pass
