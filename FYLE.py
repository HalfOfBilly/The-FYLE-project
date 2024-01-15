import glob, sys, threading, pathlib, tkinter, os, subprocess
from tkinter import *
from tkinter.filedialog import *
from pathlib import *
from time import sleep

debugmode = False

invalid = ["", "/"] # Invalid file selections

def I(): # Import function
    global importfolder, discardfolder, importloc, batchfolder
    if process_type == "B": # Batch mode
        importloc = len(command)
        batchfolder = F()
        return batchfolder
    else:
        if process_type == "C": # Woodchipper mode
            importfolder = F()
            print("Select folder to move files after conversion")
            discardfolder = F()
            importloc = len(command)
            return importfolder
        else: # Single file mode
            window = Tk() 
            window.update()
            window.iconify()
            file = ""
            while file in invalid:
                try:
                    file = str(PureWindowsPath((tkinter.filedialog.askopenfile()).name))
                except:
                    continue
            window.destroy()
            return file

def F(): # Folder function
    window = Tk()
    window.update()
    window.iconify()
    folder = ""
    while folder in invalid:
        folder = tkinter.filedialog.askdirectory()
    window.destroy()
    return folder

def S(): # String function
    string = ""
    while string == "":
        string = input(">> ")
    return string
        
def N(): # Integer function
    num = ""
    while num == "":
        try:
            num = int(input(f"Enter number between {argument1} and {argument2} >> "))
            if not (num >= int(argument1) and num <= int(argument2)):
                print(f"Invalid input- number must be between {argument1} and {argument2}")
                num = ""
        except:
            print("Invalid input- must be a whole number")
            num = ""
    return str(num)

def D(): # Dropdown function
    selection = ""
    while selection == "":
        if "y" in argument1:
            print(f"Reccomended options: {options}")
        else:
            print(f"Options: {options}")
        selection = input(">> ")
        if (selection in options or argument1 == 'y'):
            return selection
        else:
            print("Invalid option")
            selection = ""

def C(): # Checkbox function
    selection = ""
    while selection == "":
        yesvalid = ["y", "Y"]
        novalid = ["n", "N"]
        selection = input("y/n >> ")
        if selection in yesvalid:
            return "1"
        else:
            if selection in novalid:
                return "0"
            else:
                print("Invalid option")
                selection = ""

def CHIPPER(): # Woodchipper manager (function to terminate the process)
    global runthread
    input("Press enter to stop woodchipper...")
    runthread = False

def QUIT():
    sys.exit()
           
subpro = {'I':I, 'F':F, 'S':S, 'N':N, 'D':D, 'C':C}
morecommands = {'Quit':QUIT}

Programs = glob.glob(f"Programs//*.FYLE") # Finds and analyses programs based on their .FYLE configuration
Prog_data = list() 
for i in range(len(Programs)):
    with open(Programs[i]) as P:
        P = P.read().splitlines() 
        Prog_data.append(P)

print("""The FYLE Project
The virtually nothing version.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

while(True):
    print("CHOOSE PROCESS:")

    Program_no = ""
    while Program_no == "": # Selects the program, and ensures input is a valid number
        for i in range(len(Prog_data)):
            print(f"{i} : {Prog_data[i][0]}")
        Program_no = input(">> ")
        if Program_no.isdigit():
            try:
                Process= Prog_data[int(Program_no)]
            except:
                print("Invalid input: invalid number")
                Program_no = ""
        else:
            if Program_no in morecommands:
                morecommands[Program_no]()
            else:
                print("Invalid input: make sure you only enter valid numbers or commands")
                Program_no = ""
    
    print(Process[0])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("CHOOSE PROCESS TYPE (S: single | B: batch | C: chipper):")
    process_type = input(">> ")
    
    command = [f"{os.path.dirname(os.path.realpath(__file__))}\\Programs\\{Process[1]}"]

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(len(Process)-3):
        CurrentLine = Process[i+3]
        argument1, argument2, dialogue, options = " ", " ", "", []
        function = CurrentLine[0]
        if CurrentLine[2] != '<': # Checks for additional arguments in character 3
            for a in range(len(CurrentLine)-2):
                if CurrentLine[a+2] == " ":
                    argument1 = CurrentLine[2:a+2]
                    break
            if CurrentLine[len(argument1)+2] != '<':  # Checks for additional arguments in character 5
                for a in range(len(CurrentLine)-4):
                    if CurrentLine[a+4] == " ":
                        argument2 = CurrentLine[4:a+4]
                        break
        for o in range(len(CurrentLine)):
            if Process[i+3][o] == '<': # Checks for dialogue markers
                for u in range(len(CurrentLine)):
                    if CurrentLine[u] == '>': # Finds closing for dialogue markers
                        dialogue = CurrentLine[o+1:u]
                        break
                if dialogue == "": # Failsafe is dialogue marker has not been closed
                    print(f"ERROR: {P[int(Program_no)]} at line {i+3}: <dialogue indicator> has not been closed.")
                    print("This error is not fatal")
                    dialogue = CurrentLine[o+1:len(CurrentLine)]
        if function == "D": # Only dropdown currently uses option markers
            for o in range(len(CurrentLine)):
                if CurrentLine[o] == '{': # Checks for option markers
                    u = o
                    while CurrentLine[u] != '}' and CurrentLine[u+1] != '{':
                        u += 1
                        if u > len(CurrentLine): # Failsafe is option marker has not been closed
                            print(f"ERROR: {P[int(Program_no)]} at line {i+3}: option indicator has not been closed.")
                            print("This error is not fatal")
                            break
                    try:
                        options.append(CurrentLine[o+1:u])
                    except:
                        continue
        print(dialogue)

        value = subpro[function]()
        command.append(value)
        if debugmode:
            print(f"Argument: {value}")
    if debugmode:
        print(f"Complete command: {command}")
    print("Running process...")
    if process_type == "B": # Batch mode
        files_in = glob.glob(f"{batchfolder}//*")
        for i in range(len(files_in)):
            command[importloc] = files_in[i]
            subprocess.call(command, shell=True)
    else:
        if process_type == "C": # Woodchipper mode
            runthread = True
            WoodChipper = threading.Thread(target=CHIPPER)
            WoodChipper.start()
            while(runthread): # Main woodchipper loop
                sleep(0.2) # Prevents loop running too fast and using up absurd amount of resources
                files_in = glob.glob(f"{importfolder}//*")
                if len(files_in) > 0:
                    for i in range(len(files_in)):
                        command[importloc] = files_in[i]
                        subprocess.call(command, shell=True) # Converts file
                        os.replace(files_in[i], f"{discardfolder}//{os.path.basename(files_in[i])}") # Moves files to discard folder
        else: # Single file mode
            subprocess.call(command, shell=True)
    print("Process complete!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
