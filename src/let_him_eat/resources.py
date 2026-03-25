# File Funzioni - è il file dove si prendono le musiche.

# In questo file ci sono le funzioni che prendono la musica e le immagini

# License: See LICENSE file in the project root for details.

# Authors: 
# Paolo Vannucci <email: paolo.vannucci2009@gmail.com>
# Andrea Cittadini <email: Andreacittadini7@gamil.com>
# Dmytro Ihnatiuk <email: >

# =========================================================================================================================================ì

# Moduli Standard
from importlib.resources import files
from pathlib import Path

# eventualmente aggiungere tutte le funzioni relative alle cartelle che avete creato in src.
def get_sound(filename: str) -> Path:
    return files(__package__) / "sounds" / filename

def get_image(filename: str) -> Path:
    return files(__package__) / "images" / filename