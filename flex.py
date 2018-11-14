import ply.lex as lex

# List of token names.   This is always required
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'bool': "BOOL",
    'char': "CHAR",
    'byte': "BYTE",
    'short': "SHORT",
    'int': "INT",
    'long': "LONG",
    'double': "DOUBLE",
    'float': "FLOAT",
    'main': "MAIN",
    'class': "CLASS",
    'pub': "PUBLIC",
    'pri': "PRIVATE",
    'pro ': "PROTECTED"
}

# (?i) - case insensitive

tokens = [
             'NUMBER',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'ID',
             'COMMENT',
             'NEWLINE'
         ] + list(reserved.values())

# Regular expression rules for simple tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

literals = [';', '=', '(', ')', '{', '}', ',']


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_COMMENT(t):
    r'\//.*'
    pass


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10
  + -20 *2
  if
  //
'''

# Give the lexer some input
lexer.input(data)

# # Tokenize
# for tok in lexer:
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
