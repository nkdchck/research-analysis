from pathlib import Path
from typing import List



def all_files_in_directory(directory_path: str, extensions_to_avoid: List[str] = [], extensions_to_include: List[str] = []) -> List[str]:
    """
    Extracts all files in a directory, including subdirectories, and returns a list of files with their absolute paths.

    Args:
        directory_path (str): The path to the directory to scan.
        extensions_to_avoid (List[str]): File extensions to exclude from the results.
        extensions_to_include (List[str]): File extensions to include in the results. If empty, all extensions are included.

    Returns:
        List[str]: A list of file paths with their absolute paths.
    """
    assert isinstance(directory_path, str), f'directory_path must be a string, but got {type(directory_path)}'
    assert Path(directory_path).exists(), f'directory_path does not exist: {directory_path}'

    base_path = Path(directory_path)
    if extensions_to_avoid and extensions_to_include:
        files = [
            str(path.resolve())
            for path in base_path.rglob('*')
            if path.is_file() and path.suffix not in extensions_to_avoid and path.suffix in extensions_to_include
        ]
    elif extensions_to_avoid:
        files = [
            str(path.resolve())
            for path in base_path.rglob('*')
            if path.is_file() and path.suffix not in extensions_to_avoid
        ]
    elif extensions_to_include:
        files = [
            str(path.resolve())
            for path in base_path.rglob('*')
            if path.is_file() and path.suffix in extensions_to_include
        ]
    else:
        files = [str(path.resolve()) for path in base_path.rglob('*') if path.is_file()]

    files.sort()
    return files
