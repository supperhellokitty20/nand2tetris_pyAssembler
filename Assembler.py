#!/usr/bin/python3
import sys
from Parser import Parser 
from Code import Code 
from pathlib import PurePath 
import os 
def translateA(cmd:str) -> str : 
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

def main(path:str) : 
    parse = Parser(path) 
    out ="" 
    while parse.hasMoreCommands() : 
        parse.advance() 
        if parse.commandTypes() =="A_COMMAND": 
            out+= translateA(parse.symbol())+"\n" 
        if parse.commandTypes()=="C_COMMAND": 
            current_dest = parse.dest()
            current_comp= parse.comp()
            current_jump= parse.jump() 
            out+=translateC(current_dest,current_comp,current_jump)+"\n" 
    return out 
if __name__=="__main__":      
    #Production 
    print("Cant handle symbol") 
    file_name =PurePath(sys.argv[1]).name[:-4]+".hack" 

    print("out putting to file" ,file_name) 
    if len(sys.argv)<2 or sys.argv[1][-4:]!=".asm": 
        print("You need to input .asm file") 
    else :  
       out=  main(sys.argv[1]) 
       print(out) 

    #Make an output directory 
    if not os.path.isdir("out")  : 
        os.mkdir("out") 
    out_path = "./out/"+file_name 

    with open(out_path,"w") as file : 
        file.write(out) 
        file.close() 
    #Debug 
