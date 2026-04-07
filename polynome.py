from expression import Expression
import math

class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    def __init__(self, coefficients: list[float]):
        self.coefficients = coefficients
    def evaluer(self, x: float) -> float:
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
        format = []
        for i in range(len(self.coefficients)):
            if(self.coefficients[i] != 0):
                if(i == 0):
                    format.append(f"{self.coefficients[i]}")
                elif(i == 1):
                    format.append(f"{self.coefficients[i]}x")
                else:
                    format.append(f"{self.coefficients[i]}x^{i}")
        return f"({'+'.join(format)})"