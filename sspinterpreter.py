from tkinter import filedialog
from time import sleep

def checksyntax(line, current_line):
    if not ';' in line:
        print(f"\nERROR in line {current_line}: do you need a ';'?")
        sleep(2)
        exit()

def start():
    filepath = filedialog.askopenfilename(initialdir="/", title="Select your SSP file", filetypes=(("ssp files", "*.ssp"), ("any file", "*.*")))
    lines = []
    current_line = 0
    with open(filepath) as f:
        for line in f.readlines(): lines.append(line)
    for line in lines:
        current_line += 1
        if line[0] == "-" and line[1] == "-": pass
        elif "outcs" in line:
            checksyntax(line, current_line)
            print(line[7:-3])
        elif "getcs" in line:
            checksyntax(line, current_line)
            exec(line.replace("getcs>","input(").replace(";",")"))
        elif "outf" in line:
            checksyntax(line, current_line)
            with open(line[8:-4],"r") as a:
                for line in a.readlines(): print(line)
        elif "wrtf" in line:
            checksyntax(line, current_line)
            file = line.replace("wrtf[l,\"", "").split("\"")
            with open(file[0],"w") as b: b.write(file[2])

if __name__ == "__main__": start()