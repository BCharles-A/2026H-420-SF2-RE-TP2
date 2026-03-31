from expression import Expression
from polynome import Polynome
from operations import Multiplication
import math

class Sin(Expression):
    """Expression representant sin(u)."""
    def __init__(self, u: Expression):
        self.u = u
    def evaluer(self, x: float) -> float:   
        return math.sin(self.u.evaluer(x))
    def deriver(self):
        return Multiplication(Cos(self.u),self.u.deriver())
    def __str__(self):
        return f"sin({self.u})"
        


class Cos(Expression):
    """Expression representant cos(u)."""
    def __init__(self, u: Expression):
        self.u = u
    def evaluer(self, x):
        return math.cos(self.u.evaluer(x))
    def deriver(self):
        return Multiplication(-1, Multiplication(Sin(self.u), self.u.deriver()))
    def __str__(self):
        return f"cos({self.u})"


class Exp(Expression):
    """Expression representant exp(u)."""
    def __init__(self, u: Expression, base: float = math.e):
        self.u = u
        self.base = base
    def evaluer(self, x):
        return math.pow(self.base, self.u.evaluer(x))
    def deriver(self):
        return Multiplication(self.u.deriver(), Multiplication(self.u, Polynome([math.log(self.base)])))
    def __str__(self):
        return f"({self.u})^{self.base}"