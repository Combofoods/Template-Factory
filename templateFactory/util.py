#TODO.: 
#   - Read a file ...       /user/doc/content_input.txt
#   - Read all files from a folder ... /user/doc/
#   - Read all files from a folder by a pattern ... /user/doc/*.txt
#   - Write a file ... /user/doc/content_output.txt
#   - Write all files in a target directory with the same input name ...
#   - convert 'str' ( YAML ) -> dict
#   - convert 'str' ( JSON ) -> dict
#   - convert 'str' ( XML  ) -> dict


from templateFactory.models    import File
from templateFactory.messages  import Error
from typing                    import List
import os


def is_a_directory(path:str) -> bool:
    pass


def get_filename(path:str) -> str:
    return os.path.basename(path)


def read_file(path:str) -> str:
    content = None
    with open(path, 'r', encoding='utf-8') as data:
        content = data.read()
    
    if content is None:
        raise Exception(Error.WRONG_NULL)
    
    return content


def Factory_File(path:str) -> File:
    return File( path_origin=path, file_name=get_filename(path), content=read_file(path) )


def read_directory(path:str) -> List[File]:
    pass


def read(path:str) -> List[File]: ...



### DEBUG .:
if __name__ == "__main__":
    print(read_file(__file__))
