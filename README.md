# Team Fortress 2 config swapping script

This is a simple script to swap between multiple configs for Team Fortress 2. It's not really intended to be for anyone
but myself, hence why the structure is fairly rigid. It works by literally removing all files of a previous config and
copying the files of a new config in.

## Customize script
Configs need to be in a config folder and separated into their own subfolders (i.e. have a `Configs` directory with
subdirectories for configs like "comp" or "casual"). This folder and the TF2 install's `tf` directory need to be
specified in the `# Settings` section of the script. My own version is included as an example.

## Build .exe for execution in Windows
I'm only specifying this for Windows because that's what I use. I might add instructions for other OS's , but it should
be pretty easy to figure out if you just look up how to create an executable file from a Python script. Provided you
cloned the repo and have Python installed the steps are pretty simple:

1. Install PyInstaller through pip
    ```
    pip install pyinstaller
2. Navigate to the directory of the cloned repo and run (or run in your code editor's terminal):
    ```
    pyinstaller --onefile config_swapper.py
    ```
    An .exe file will then be created in `dist/config_swapper.exe` within the cloned repo.