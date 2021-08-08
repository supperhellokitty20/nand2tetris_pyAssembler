

class Code : 
    def dest(field:str) :  
        dest = {
        "null": "000",
        "M": "001",
        "D": "010",
        "A": "100",
        "MD": "011",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
        }
        for key in dest.keys() :  
            if field == key : return dest[key] 


    def comp(field:str) : 
        comp = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101"
        }
        for key in comp.keys() :  
            if field == key : return comp[key] 

    def jump(field:str)->str : 

        jump = {
            "null": "000",
            "jgt": "001",
            "jeq": "010",
            "jge": "011",
            "jlt": "100",
            "jne": "101",
            "jle": "110",
            "jmp": "111"
        }
        for key in jump.keys() :  
            if field.lower() == key : return jump[key] 

#Testings 
if __name__=="__main__": 
    print("" + x for x in str(Code.dest("MD"))  ) 


