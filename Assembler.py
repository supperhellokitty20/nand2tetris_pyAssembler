#!/usr/bin/python3
import sys
from Parser import Parser 
from Code import Code 
from pathlib import PurePath 
from SymbolTable import SymbolTable
import os 
def translateA(cmd:str) -> str : 
    #Translating label 
    if table.contains(cmd):
        bin = "{0:b}".format(table.getAddress(cmd)) 
        result = "0"+bin 
        while len(result)<16: 
            result = "0"+result
        return result     
    else : 
        bin = "{0:b}".format(int(cmd)) 
        result = "0"+bin 
        while len(result)<16: 
            result = "0"+result
        return result     


def translateC(dest , comp:str , jump) ->str : 
    bin_dest = Code.dest(dest) 
    bin_comp = Code.comp(comp) 
    bin_jump = Code.jump(jump) 
    return "111"+bin_comp+bin_dest+bin_jump
    
def main() : 
    #Keep track of the cmd line without cmt 
    out ="" 
    var_loc = 16
    while parse.hasMoreCommands() : 
        parse.advance() 
        if parse.commandTypes()=="A_COMMAND": 
            sym = parse.symbol() 
            is_var= table.contains(sym) ==False   
            if sym[0].isalpha(): 
                if is_var : 
                    table.addEntry(sym,var_loc) 
                    out+=translateA(sym)+"\n" 
                    var_loc+=1 
                #If it a label comamand 
                else : 
                    out+=translateA(sym)+"\n" 
            #Regular A-command
            else : 
                    out+=translateA(sym)+"\n" 

        if parse.commandTypes()=="C_COMMAND": 
            current_dest = parse.dest()
            current_comp= parse.comp()
            current_jump= parse.jump() 
            out+=translateC(current_dest,current_comp,current_jump)+"\n" 

        if parse.commandTypes()=="L_COMMAND": 
            continue
    return out 
def firstpass() ->None : 
    cmd_line_number = 0
    while parse.hasMoreCommands() : 
        parse.advance() 
        if parse.commandTypes()== "L_COMMAND" and table.contains(parse.symbol())==False  :
           sym = parse.symbol()
           table.addEntry(sym,cmd_line_number)  
        else: 
            cmd_line_number+=1
    #Reset 
    parse.lin_num=0 
    return None 

if __name__=="__main__":      
    print("------------------------------------")
    print("Hack assembly PY") 
    if len(sys.argv)<2 or sys.argv[1][-4:]!=".asm": 
        print("------------------------------------")
        print("You need to input .asm file\n") 
        print("Please provide this script following syntax : python3 ./Assembler.py <file>\n")
        print("The compile code will be output to the OUT directory\n") 
        print("------------------------------------")
    else :  
        file_name =PurePath(sys.argv[1]).name[:-4]+".hack" 
        global parse 
        parse = Parser(sys.argv[1]) 
        global table 
        table = SymbolTable() 
        #Main logic here 
        firstpass()  
        out = main() 

        #Make an output directory 
        if not os.path.isdir("out")  : 
            os.mkdir("out") 
        out_path = "./out/"+file_name 

        with open(out_path,"w") as file : 
            file.write(out) 
            file.close() 
        print("Done translating , please check <out> dir for output\n")
    
    