from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages = ["shutil","os","hashlib","ctypes","subprocess","re","socket","time","multiprocessing"], include = ["Process"])
base = None
 
if sys.platform == "win32":
    base = "WIN32GUI"

setup(
    name= 'rnasomeware',
    version = '0.1',
    author = "IndentErr",
    description = "",
    options = dict(build_exe = buildOptions),
    executables = [Executable("virus.py", base = base)]
)
