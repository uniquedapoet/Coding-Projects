from typing import Tuple 
import numpy as np

# Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # Unicode codepoint  
        ("fg", "3B"), # 3 unsigned bytes for RGB colors 
        ("bg", "3B"), 
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool), # True or False
        ("transparent", np.bool), 
        ("dark", graphic_dt), # The dtype from above
    ]
)

def new_tile(
        *, # Enforce the use of keywords, so that parameter order doesn't matter
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]
) -> np.ndarray:
    """Helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)))

wall = new_tile(walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)))