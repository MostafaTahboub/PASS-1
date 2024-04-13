from INPUT.DEFININGS import *


INPUT = open("INPUT/Source.asm", "r")

# Output file --> intermediate file
OUTPUT = open("Intermediatefile.mdt", "w+")

#Error file --------> store errors 
ERRORS = open("errors_file.txt", "w+")

# define variables 
SYMTAB = {}
LOCCTR = 0
PRGLTH = 0
PRGNAME = ""
ERRCTR = 0
ADDSTA = 0

print("\n**************SIC ASSEMBLER*****************\n")
# Reading from file
# Reading first line
line = INPUT.readline()

if line:
    if line[9:15].strip() == "START":
        PRGNAME = line[0:8].strip()  
        ADDSTA = int(line[16:35].strip(), 16)  
        LOCCTR = ADDSTA
        OUTPUT.write(hex(LOCCTR)[2:] + " " * (10 - len(str(LOCCTR))) + line) 

        
        while True:
            line = INPUT.readline()
            if not line:  
                break
            operation = line[9:15].strip()

            if operation != "END" and ("." not in line):
                if operation == "LTORG":
                    OUTPUT.write(" " * 10 + line)

                else:
                    OUTPUT.write(hex(LOCCTR)[2:] + " " * (10 - len(str(LOCCTR))) + line)  # write line to outputFile

                label = line[0:8].strip()  

                if label != "": 
                    if label in SYMTAB:  
                        ERRORS.write(ERRORLIST[2])
                        print(ERRORLIST[2])
                        ERRCTR += 1

                    else: 
                        SYMTAB[label] = hex(LOCCTR)[2:]

                if operation not in OPTAB:
                    operand = 0

                
                if operation in OPTAB:
                    LOCCTR += 3

                elif operation == "WORD":
                    LOCCTR += 3

                elif operation == "RESB":
                    operand = line[16:35].strip()
                    LOCCTR += int(operand)

                elif operation == "BYTE":
                    operand = line[16:35].strip()

                    if operand[0] == 'X':
                        LOCCTR += int((len(operand) - 3) / 2)

                    elif operand[0] == 'C':
                        LOCCTR += (len(operand) - 3)

                elif operation == "RESW":
                    operand = line[16:35].strip()
                    LOCCTR += 3 * int(operand)

                elif operation == "LTORG":
                    LOCCTR += 0  

                else:
                    ERRORS.write(ERRORLIST[3])
                    print(ERRORLIST[3])
                    ERRCTR += 1

            if operation == "END":
                OUTPUT.write(" " * 10 + line)

    else:
        ERRORS.write(ERRORLIST[1]) 
        print(ERRORLIST[1])

else:
    ERRORS.write(ERRORLIST[0])
    print(ERRORLIST[0])

length = int(LOCCTR) - int(ADDSTA)  # program length ( current location counter - start address)
PRGLTH = hex(int(length))[2:].format(int(length)) 
loc = hex(int(LOCCTR))[2:].format(int(LOCCTR))  


INPUT.close()
OUTPUT.close()
ERRORS.close()

# Print output of pass 1
print("PROGRAM NAME: " + PRGNAME)
print("PROGRAM LENGTH: " + str(PRGLTH).upper())
print("LOCATION COUNTER: " + str(loc).upper())
print("NUMBER OF ERRORS: " + str(ERRCTR) + "\n")

print(" SYMBOL TABLE\n--------------")
for label in SYMTAB:
    print(label + " " * (10 - len(str(label))) + SYMTAB[label].upper())