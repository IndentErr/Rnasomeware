from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages = ["shutil","os","hashlib","ctypes","subprocess","re","socket","time"])

exe = [Executable("virus.py")]

setup(
    name= 'rnasomeware',
    version = '0.1',
    author = "IndentErr",
    description = "",
    options = dict(build_exe = buildOptions),
    executables = exe
)

