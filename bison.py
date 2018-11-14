import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from flex import tokens
from FileHandler import addToFile
from utility import findVar, addVar, convert, isType, addclass


def p_class(p):
    '''class : CLASS acs classname '{' fnclist '}' '''




def p_classname(p):
    ''' classname : ID '''
    addclass(p[3])


def p_acs(p):
    ''' acs : PRIVATE
            | PUBLIC
            | PROTECTED '''
    addToFile(text=convert(p[1]) + " ")


def p_funclst(p):
    '''fnclist : fnclist function
                | function '''


def p_stmtlist(p):
    '''stmtlist : stmtlist stmt ';'
            | stmt ';'
            | '''


def p_stmt(p):
    '''stmt : ifstmt
            | loopstnt
            | switchstmt
            | assignstmt'''
    p[0] = p[1]


def p_function(p):
    '''function : func '(' arglist ')' '{' stmtlist '}' '''
    addToFile(text="}")


def p_arglist(p):
    '''arglist : args
                | '''


def p_args(p):
    '''args : args ',' type ID
            | type ID'''


def p_main(p):
    '''func : MAIN
            | acs static rettype ID '''
    if p[1] == 'main':
        addToFile(text="public static void main(String [] args) {")
    else:
        addToFile(text="public static void main(String [] args) {")


def p_rettype(p):
    '''rettype : type '''


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
            | FLOAT
            | ID '''
    if not isType(p[1]):
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
