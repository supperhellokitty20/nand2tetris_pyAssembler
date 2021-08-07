#!/usr/bin/python3 
class SymbolTable : 
    def __init__(self) : 
        table = {} 
    def addEntry(self,symbol:str,address:int)  :
        return table[symbol]=address 
    def getAdress(self,symbol:str) : 
        return table[symbol] 




