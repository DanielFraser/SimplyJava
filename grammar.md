# Grammar

Starting Symbol: mainclass


mainclass : classlist


classlist : classlist class
          | class
       
          
class : classacs CLASS classname '{' classstmtlist '}'


classacs : PUBLIC
        | empty
   
        
classname : ID


classstmtlist : classstmtlist classstmt
                | classstmt
    
                
classstmt : function 
        | declarestmt


function : acs static funcname '(' args ')' '{' stmtlist '}'


static : STATIC | empty


funcname : ID


stmtlist : stmtlist stmt ';'
        | stmt ';'


stmt : ifstmt
        | loopstmt
        | switchstmt
        | assignstmt
        | declarestmt