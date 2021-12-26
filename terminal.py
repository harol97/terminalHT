from os import getcwd, chdir, listdir, pipe, system
from subprocess import PIPE, Popen
from colorama import init, Fore
from colorama.ansi import Style

class Terminal:
    

    __SPECIAL_COMMANDS = ["touch", "ls"]

    def __init__(self) -> None:
        self.__path = getcwd()
        self.__executing = True
        system("title Terminal HT")
        init()

    def __touch(self, command:str):
        files = [i.strip() for i in command.split(" ") if i.strip()]
        for i in files:
            with open(i, "w") as _:
                pass

    def __ls(self, directory):
        directory = directory.strip()
        if not directory:
            directory = "."
        for i in listdir(directory):
            print(i, end=" ")
        print()

    def run(self):
        while self.__executing:
            print(Fore.GREEN+self.__path + " >> ", end="")
            print(Style.RESET_ALL,end="", sep="")
            command = input().strip()
            if command == "exit":
                exit(1)
            elif command.startswith("touch"):
                self.__touch(command[5:])

            elif command.startswith("ls"):
                self.__ls(command[2:])

            else:
                if command.startswith("cd"):
                    chdir(command[3:].strip())
                    self.__path = getcwd()
                else:
                    process = Popen(command, shell=True,stdout=PIPE, stdin=PIPE, stderr=PIPE)  # aqui
                    out, err = process.communicate()
                    result = out + err
                    if len(result)>0:
                        try:
                            print(result.decode(), end="")
                        except:
                            print(result.decode('windows-1252'))
                        