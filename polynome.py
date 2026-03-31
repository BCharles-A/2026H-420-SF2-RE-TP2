from expression import Expression
import math

class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    def __init__(self, coefficients: list[float]):
        self.coefficients = coefficients
    def evaluer(self, x: float) -> float:
        print(self.coefficients)
        eval = self.coefficients.copy()
        valeur = 0
        for i in range(0, len(eval)):
            eval[i] = eval[i] * (x**i)
            valeur += eval[i]
        return valeur
    def deriver(self) -> "Expression":
        coefficients_derives = self.coefficients.copy()
        for i in range(0, len(coefficients_derives)):
            coefficients_derives[i] = coefficients_derives[i] * i
        coefficients_derives.pop(0)
        if coefficients_derives == []:
            coefficients_derives = [0]
        return Polynome(coefficients_derives)
    def __str__(self) -> str:
        return str(self.coefficients)
if __name__ == "__main__":
    p = Polynome([1, 2, 5])
    print(p)
    print(p.deriver())