from cx_Freeze import setup, Executable
base = None
executables = [Executable("main.py", base=base)]
packages = ["idna", "pygame"]
options = {
    'build_exe': {
        'packages': packages,
    },
}
setup(
    name="shooter",
    options=options,
    version="1.0",
    description='mon premier jeu shooter',
    executables=executables
)