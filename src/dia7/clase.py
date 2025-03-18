class Pajaro:
    def __init__(self, color: str, especie: str):
        self.color = color
        self.especie = especie
    def __repr__(self):
        return f"Pajaro(color='{self.color}', especie='{self.especie}')"

mi_pajaro = Pajaro('rojo','cardenal')
print(mi_pajaro.__repr__())  # Pajaro(color='rojo', especie='cardenal')


