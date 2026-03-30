from expression import Expression
from polynome import Polynome

class Addition(Expression):
    """Expression representant u + v."""
    def __init__(self, u: Expression, v: Expression):
        self.u = u
        self.v = v
    def evaluer(self, x: float) -> float:
        return self.u.evaluer(x) + self.v.evaluer(x)
    def deriver(self) -> "Expression":
        return Addition(self.u.deriver(), self.v.deriver())
    def __str__(self) -> str:
        return f"({self.u} + {self.v})"
    
print(Addition(Polynome([1, 2]), Polynome([3, 4])).deriver())

class Multiplication(Expression):
    """Expression representant u * v."""
    def __init__(self, u: Expression, v: Expression):
        self.u = u
        self.v = v
    def evaluer(self, x: float) -> float:
        return self.u.evaluer(x) * self.v.evaluer(x)
    def deriver(self) -> "Expression":
        return Addition(Multiplication(self.u.deriver(), self.v),Multiplication(self.u, self.v.deriver()))
    def __str__(self) -> str:
            return f"({self.u} * {self.v})"
    
print(Multiplication(Polynome([1, 2]), Polynome([3, 4])).deriver())