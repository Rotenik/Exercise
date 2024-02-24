import dataclasses

@dataclasses.dataclass
class DasAuto():
    name: str
    mileage: int
    color: str
    price: int

    def __str__(self):
        return f'{self.name}\nMileage: {self.mileage}\nColor: {self.color}\nPrice: {self.price}zł'

car = DasAuto('Opel Vectra', 72034, 'Blue', 12000)
print(car)