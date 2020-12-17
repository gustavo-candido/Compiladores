import string

class Gramatica:
    def __init__(self):
        letra = list(string.ascii_letters)
        self.gram = {
            'P': [['programa', 'N', 'B']],
            'B': [['{', 'D', 'E', '}']],
            'E': [["E'",'E'], ['eps']],
            "E'": [['Y'], ['X'], ['I'], ['Q'], ['W']],
            'D': [['T', 'L', 'D'], ['eps']],
            'T': [['int'], ['char'], ['real']],
            'L': [['N', "L'"]],
            "L'": [[',', 'L'], [';']],
            'I': [['se', '(', "I'", ')', 'entao', 'B', "I''"]], 

            "I''": [['senao', 'B'],  ['eps']], 
            "I'": [['K','R','K']],
            'K': [['N'],['F'],['J'], ['C']],
            'R': [['=='],['<>'],['<'],['>'],['<='],['>=']],
            'X': [['H', "X'"]],
            "X'": [['+','H',"X'"], ['-','H', "X'"], ['eps']],
            'H': [['M', "H'"]],
            "H'": [['*','M',"H'"], ['/','M',"H'"], ['eps']],
            'M': [['(','X',')'],['K'], ['-', 'K'], ['+', 'K']], 
            'N': [['id']], 
            'F': [['cntReal']],
            'J': [['cntInt']],
            'C': [['cntChar']],
            'W': [['enquanto', '(', "I'", ')', 'B'] ],
            'Q': [['faca','B','enquanto','(',"I'",')',';']],
            'Y': [["N", ":=","X", ';']]
        }
        


        self.firsts = {
            'programa': ['P'],
            '{': ['B'],
            '(': ['E',"E'", 'X', 'H', 'M'],
            'se': ['E',"E'", 'I'],
            'faca': ['E',"E'", 'Q'],
            'enquanto': ['E',"E'", 'W'],
            'senao': ["I''"],
            '[': [],
            ',': ["L'"],
            ';': ["L'"],
            'int': ['D', 'T'],
            'char': ['D', 'T'],
            'real': ['D', 'T'],

            '<>': ['R'],
            '<': ['R'],
            '>': ['R'],
            '<=': ['R'],
            '>=': ['R'],

            '*': ["H'"],
            '/': ["H'"],
            '+': ["X'", 'M', 'H', 'X', "E'", 'E'],
            '-': ["X'", 'M', 'H', 'X', "E'", 'E'],

            'id': ['E',"E'", 'L', "I'", 'K', 'X', 'H', 'M', 'N', 'Y'],
            'cntReal': ['E',"E'", "I'", 'K', 'X', 'H', 'M', 'F'],
            'cntInt': ['E',"E'", "I'", 'K', 'X', 'H', 'M', 'J'],
            'cntChar': ['E',"E'", "I'", 'K', 'X', 'H', 'M', 'C'],

            'eps' : ['E','D', "X'", "H'", "I''"],

            ':=': [],
            ']': [],
            '.': [],
            ')': [],
            '}': [],

            '': [],
            "'": [],

            "null": [],
            # '\-32768-32767': ['E', "E'", 'X', 'H', 'M', 'K', 'J', "I'"],
            # 'all': ['Z', "Z'", 'S'],
            # 'a-zA-Z': ['E', 'N', "N'", "E'", 'X', 'H', 'M', 'K',  'C', 'L', "I'", 'Y'],
            # '0-9': ['E', "E'", 'X', 'H', 'M', 'K', "N'", "N''", 'F', "F'", "I'"],
        }