#! /usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path
import pyinputplus as pyip
from colorama import init, Fore

def main():
    init(autoreset=True)

    if len(sys.argv) > 2:
        print(Fore.RED + "Usage: projectex [project name] - create latex project")
        sys.exit() 
    elif len(sys.argv) < 2:
        prompt = "Enter the name of your latex project: "
        project_name = pyip.inputStr(prompt)
    else:
        project_name = sys.argv[1]
    
    create_project(Path.cwd()/project_name)

def create_project(project_path: str):
    pname, pparent = project_path.name, project_path.parent
    prompt = f"Folder named {pname} in {pparent}. Do you want to delete [y/n]? "
    if not Path.exists(project_path):
        create_directory(project_path)
    elif pyip.inputYesNo(prompt=prompt, yesVal="y", noVal="n") == "y":
        remove_folder(project_path)
        create_directory(project_path)
    else:
        print(Fore.RED + f"Project {pname} not created!")
        
def create_directory(project_path: str):
    Path.mkdir(project_path)   
    pname = project_path.name
    files = [f"{pname}.tex", f"{pname}.sty", f"{pname}.cls", f"{pname}.bib"]
    dirs = ["tex", "img"]
    for f in files: 
        Path.touch(project_path/f)
        print(Fore.GREEN + f"{f} file created.")

    for d in dirs:
        Path.mkdir(project_path/d)
        print(Fore.GREEN + f"{d} directory created.")   

def remove_folder(project_path: str):
    pname = project_path.name
    shutil.rmtree(project_path)
    print(Fore.GREEN + f"{pname} was deleted.")

if "__main__" == __name__:
    main()

    
