
from dataclasses import dataclass

@dataclass
class File:
    path_origin:str
    file_name:str = ''
    content:str = ''
