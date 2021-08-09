#!/usr/bin/python3 
class SymbolTable : 
    def __init__(self) : 
        #On initilize the table already have the predefined symbol 
        self.table = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576,
            'R0':0,'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15
        } 
    def addEntry(self,symbol:str,address:int) -> None :
        self.table[symbol]=address 
        return None 

    def contains(self,symbol:str)->bool : 
        if symbol  in self.table.keys() : return True 
        else : return False  
        
    def getAddress(self,symbol:str)->int: 
        return self.table[symbol] 

#Testing for first pass 
if __name__=="__main__": 
    from Parser import Parser
    table =SymbolTable() 
    cmd_line_number = 0 
    parse = Parser("../max/Max.asm") 
    print(table.contains("R0"))  
    while parse.hasMoreCommands() ==True : 
        parse.advance() 
        if parse.commandTypes()== "L_COMMAND" and table.contains(parse.symbol())==False  :
           table.addEntry(parse.symbol(),cmd_line_number)  
        cmd_line_number+=1
    #Reset 
    print(table.table) 

