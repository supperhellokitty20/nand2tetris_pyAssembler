#!/usr/bin/python3
#%%
import sys
from typing import Optional
from Parser import Parser 
from Code import Code 

def translateA(cmd:str) -> str : 
    bin = "{0:b}".format(int(cmd)) 
    diff = 13-len(bin) 
    add="000"
    for _ in range(diff) : 
        add+="0"
    return add+bin
def translateC(dest:str , comp:str , jump) ->str : 
    return "111"+Code.dest(dest)+Code.comp(comp)+Code.jump(jump) 

if __name__=="__main__":      
    #Production 
    '''
    if len(sys.argv)<2 or sys.argv[1][-4:]!=".asm": 
        print("You need to input .asm file") 
    else :  
        print("Working ...") 
        f = Parser(sys.argv[1]) 
        f.advance() 
        print(f.current_cmd) 
        print("Loading .asm file to the assembler ...") 

    '''
    #Debug 
    print("Loading .asm file to the assembler ...") 
    parse = Parser("../pong/PongL.asm") 
    f_name = "Pong.hack"
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
    print(out) 
    with open(f_name,"w") as file : 
        file.write(out) 
        file.close() 

# %%
