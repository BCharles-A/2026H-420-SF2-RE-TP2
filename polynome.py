from expression import Expression


class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    def __init__(self, coefficients: list[float]):
        self.coefficients = coefficients
    def evaluer(self, x: float) -> float:
        valeur = 0
        for i in range(0, len(self.coefficients)):
            self.coefficients[i] = self.coefficients[i] * (x**i)
            valeur += self.coefficients[i]
        return valeur
    def deriver(self) -> "Expression":
        coefficients_derives = self.coefficients.copy()
        coefficients_derives.pop(0)     
        for i in range(0, len(self.coefficients)-1):
            coefficients_derives[i] = self.coefficients[i] * (i+2)
        return coefficients_derives
    def __str__(self) -> str:
        return str(self.coefficients)

x = Polynome([1, 2, 3])
derivee = x.evaluer(2)
print(derivee)