import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from flex import tokens
from FileHandler import addToFile
from utility import findVar, addVar, convert

def p_class(p):
    '''class : CLASS acs ID '{' '''


def p_function(p):
    '''function : func '(' ')' '{' '}'
                | func '(' ')' '{' stmtlist '}' '''
    addToFile(text="}")

def p_func(p):
    '''func : MAIN'''
    addToFile(text="public static void main(String [] args) {")

def p_fnc_stmt(p):
    '''function : stmtlist'''

def p_stmtlist(p):
    '''stmtlist : stmtlist stmt2 ';'
            | stmt2 ';' '''
    pass

def p_stmt2(p):
    'stmt2 : stmt'
    addToFile(text=p[1] + ";")
    p[0] = p[1]

def p_stmt(p):
    'stmt : expression'
    p[0] = p[1]

def p_declare(p):
    '''stmt : type ID '=' expression
            | type ID '''
    if addVar(p[2]):
        p[0] = ' '.join(str(e) for e in p[1:])
    else:
        raise SyntaxError

def p_type(p):
    '''type : BOOL
            | CHAR
            | BYTE
            | SHORT
            | INT
            | LONG
            | DOUBLE
            | FLOAT '''
    if not type(p[1]):
        raise SyntaxError
    p[0] = convert(p[1])

def p_assign(p):
    '''stmt : ID '=' expression '''
    if findVar(p[1]):
        p[0] = ' '.join(str(e) for e in p[1:])
    else:
        print("'{}' not declared".format(p[1]))
        raise SyntaxError


def p_binary_operators(p):
     '''expression : expression PLUS term
                  | expression MINUS term
       term       : term TIMES factor
                  | term DIVIDE factor'''

     p[0] = ' '.join(str(e) for e in p[1:])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    '''factor : '(' expression ')' '''
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

with open("a.txt", "r") as f:
    data = f.read()

with open("output/test.java", "w+") as f:
    result = parser.parse(data)
    f.write(str(result))
    pass
