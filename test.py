from pathlib import Path
import os
a=Path(r'C:\ML_project1\src\__init__.py')
print("this is path",os.path.split(a)[1])