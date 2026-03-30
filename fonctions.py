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
        return
        


class Cos(Expression):
    """Expression representant cos(u)."""
    def __init__(self, u: Expression):
        self.u = u
    def evaluer(self, x):
        return math.cos(self.u.evaluer(x))
    def deriver(self):
        return Multiplication(Sin(self.u), self.u.deriver())
            


class Exp(Expression):
    """Expression representant exp(u)."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    pass
