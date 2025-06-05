# module city
from dataclasses import dataclass, field

# NB: dataclass since python 3.6
# or pydantic (used by fastapi): + constraints + serialization JSON

@dataclass
class City:
    """class representing a french city with its name, zipcode, population
    """

    name: str
    population: int | None = field(default=None, repr=False)
    zipcode: str | None = None

    # implements builtin function str
    def __str__(self) -> str:
        return f"{self.name} ({self.zipcode})"
    
    def department(self) -> str | None:
        # return self.zipcode[:2] if self.zipcode is not None else None
        if self.zipcode is None:
            return None
        # Tutorial Pattern Matching: https://peps.python.org/pep-0636/ 
        match self.zipcode[:2]:
            case "20" if self.zipcode < "20200":
                # Corse du Sud
                return "2A"
            case "20":
                " Haute Corse"
                return "2B"
            case "97":
                # DROM
                return self.zipcode[:3]
            case _ as code2:
                return code2
