from expression import Expression
from polynome import Polynome
from operations import Multiplication
import math

class Sin(Expression):
    """Expression representant sin(u)."""
    def __init__(self, u: Expression):
        self.u = u
        self.coefficients = []
    def evaluer(self, x: float) -> float:   
        return math.sin(self.u.evaluer(x))
    def deriver(self):
        return Multiplication(Cos(self.u),self.u.deriver())
    def __str__(self):
        format = []
        for i in range(len(self.u.coefficients)):
            if(self.u.coefficients[i] != 0):
                format.append(f"{self.u.coefficients[i]}x^{i}")
        return f"sin({'+'.join(format)})"


class Cos(Expression):
    """Expression representant cos(u)."""
    def __init__(self, u: Expression):
        self.u = u
        self.coefficients = []
    def evaluer(self, x):
        return math.cos(self.u.evaluer(x))
    def deriver(self):
        return Multiplication(Polynome([-1]), Multiplication(Sin(self.u), self.u.deriver()))
    def __str__(self):
        format = []
        for i in range(len(self.u.coefficients)):
            if(self.u.coefficients[i] != 0):
                format.append(f"{self.u.coefficients[i]}x^{i}")
        return f"cos({'+'.join(format)})"

class Exp(Expression):
    """Expression representant exp(u)."""
    def __init__(self, u: Expression, base: float = math.e):
        self.u = u
        self.base = base
        self.coefficients = []
    def evaluer(self, x):
        return self.base ** self.u.evaluer(x)
    def deriver(self):
        return Multiplication(self.u.deriver(), Multiplication(Exp(self.u, self.base), Polynome([math.log(self.base)])))
    def __str__(self):
        format = []
        for i in range(len(self.u.coefficients)):
            format.append(f"{self.u.coefficients[i]}x^{i}")
        return f"({self.base})^{'+'.join(format)}"