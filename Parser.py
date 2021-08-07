from Code import Code 
from typing import NewType 
class Parser : 
    def __init__(self,file_path) : 
        with open(file_path,"r") as file : 
            self.file = file.readlines()   
        self.current_cmd = None 
        self.lin_num =0 
    #Tell if we have reached to the end of the file 
    def hasMoreCommands(self) -> bool:  
        #define if the file is at the end ==> How ? 
        if self.lin_num!=len(self.file) : 
            return True 
        else : 
            return False 

    def _is_trash(self,cmd:str)->bool: 
        if cmd[:3].strip()=="//" or cmd  == "\n" : 
            return True 
        else : return False 

    def advance(self)-> None  :  
        if self.hasMoreCommands() == True: 
            tmp = self.file[self.lin_num]  
            self.lin_num+=1
            while self._is_trash(tmp) : 
                tmp = self.file[self.lin_num]  
                self.lin_num+=1
            self.current_cmd=tmp.strip().strip("\n").split("\\")[0] # this assembler only allow comment after the code for inline comment 
        return None 
    #Ignore breakline line symbol and comment  
    #Return type of command  
    def commandTypes(self)->str :  
        if self.current_cmd[0]=="@":  
            return "A_COMMAND"
        if len(self.current_cmd.strip("=").strip(";"))>2: 
            return "C_COMMAND"
        else : 
            return "L_COMMAND" 
            

    def symbol(self) ->str : 
        #int(cmd.split("@").strip().strip("\n")[1])!=ValueError  
        if self.commandTypes()=="A_COMMAND": 
            result = self.current_cmd.split("@")[1] 
            return result 
        if self.commandTypes()=="L_COMMAND": 
            return self.current_cmd.strip("(").strip(")") 
    def dest(self)->str  :
        if self.commandTypes()=="C_COMMAND": 
          return   self.current_cmd.strip("=").strip(";")[0]

    def comp(self)-> str  : 
        if self.commandTypes()=="C_COMMAND": 
            if "=" in self.current_cmd : 
                return self.current_cmd.split("=")[1].split(";")[0]
            else : 
                return self.current_cmd.split(";")[0]

    def jump(self) -> str : 
        if self.commandTypes()=="C_COMMAND": 
            if ";" in self.current_cmd : 
                return self.current_cmd.split(";")[1]
            else :  
                return None 

if __name__ == "__main__" : 
    parse = Parser("../pong/PongL.asm") 
    while parse.hasMoreCommands() : 
        parse.advance() 
        print("\n") 
        print(parse.current_cmd) 
        print(parse.commandTypes()) 
        print("\n") 
        print("SYM",parse.symbol()) 
        print("DES",parse.dest()) 
        print("COMP",parse.comp()) 
        print("JMP",parse.jump()) 



