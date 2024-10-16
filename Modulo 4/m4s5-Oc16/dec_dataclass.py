from dataclasses import dataclass #pip install dataclasses 
from typing import Any #pip install typing

@dataclass
class Vehiculo:
    color: Any 
    marca: Any 

auto = Vehiculo(2,5)
auto2 = Vehiculo(2,5)
print(auto == auto2)