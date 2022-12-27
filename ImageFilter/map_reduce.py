def map_reduce(x: int | float, in_min: int | float, in_max: int | float, out_min: int | float,
               out_max: int | float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
