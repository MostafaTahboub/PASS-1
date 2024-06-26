# DEFININGs
# OPTAB 
OPTAB = {
    "ADD": "18",
    "AND": "40",
    "COMP": "28",
    "DIV": "24",
    "J": "3C",
    "JEQ": "30",
    "JGT": "34",
    "JLT": "38",
    "JSUB": "48",
    "LDA": "00",
    "LDCH": "50",
    "LDL": "08",
    "LDX": "04",
    "MUL": "20",
    "OR": "44",
    "RD": "D8",
    "RSUB": "4C",
    "STA": "0C",
    "STCH": "54",
    "STL": "14",
    "STSW": "E8",
    "STX": "10",
    "SUB": "1C",
    "TD": "E0",
    "TIX": "2C",
    "WD": "DC"
}
# Directives
DIRECTIVES = [
    "START",
    "END",
    "BYTE",
    "WORD",
    "RESB",
    "RESW",
    "LTORG"
]

#Error List
ERRORLIST = [
    "File is empty\n",
    "Line not in fixed format\n",
    "Duplicated label\n",
    "Invalid operation code\n",
    "Invalid literal\n",
    "Invalid data\n"
]