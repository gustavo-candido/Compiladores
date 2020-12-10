import string

class Gramatica:
    def isNumber(self,x):
        if not x.isnumeric():
            return False
        x1 = int(x)
        return -32767 <= x1 and 32767 >= x1
            
    def isLetter(self, x):
        return x.isalpha()

    def AllExceptComment(self, x, y = None):
        if not y:
            return True

        if x == '*' and y and y == ']':
            return False

        return True

    def __init__(self):
        letra = list(string.ascii_letters)
        self.gram = {
            'P': [['programa', 'N', 'B']],
            'B': [['{', 'D', 'E', '}']],
            'E': [["E'",'E'], 'eps'],
            "E'": [['X'], ['I'], ['Y'], ['Q'], ['W'], ['G']],
            'D': [['T', 'L', 'D'], ['eps']],
            'T': [['int'], ['char'], ['real']],
            'L': [['N', "L'"]],
            "L'": [[',', 'L'], [';']],
            'I': [['se', '(', "I'", ')', 'entao', 'B', "I''"]], 
            "I''": [['senao', 'B'], ['se', '(', "I'", ')', 'entao', 'B'],  ['eps']], 
            "I'": [['K','R','K']],
            'K': [['N'],['F'],['J']],
            'R': [['=='],['<>'],['<'],['>'],['<='],['>=']],
            'N': [['C', "N'"] ], 
            "N'": [["N''","N'"],['C',"N'"],['eps'] ],
            "N''": [ ['0'],['1'],['2'],['3'],['4'],['5'],['6'],['7'], ['8'], ['9'] ],
            'F': [['-',"F'"],['+',"F'"],["F'"]],
            "F'": [["N''", '.', "N''"] ],
            'J': self.isNumber,
            'C': self.isLetter,
            "S": self.AllExceptComment,
            'G': [['[','*','Z','*'']']],
            'Z': [["Z'"],['eps']],
            "Z'": [["S","Z'"]],
            'W': [['enquanto', '(', "I'", ')', 'B'] ],
            'Q': [['faca','B','enquanto','(',"I'",')',';']],
            'Y': [["N", ":=","X"]]
        }
        
        self.needEval = ['P', 'B', 'E', "E'", 'D', 'L', "L'", 'I', "I''", "I'", 'K', 'N', "N'", 'F', "F'", 'G', 'Z', "Z'", 'W', 'Q', 'Y']


        self.firsts = {
            'programa': ['P'],
            '{': ['B'],
            'a-zA-Z': ['E', 'N', "N'", "E'", 'X', 'H', 'M', 'K',  'C', 'L', "I'", 'Y'],
            '0-9': ['E', "E'", 'X', 'H', 'M', 'K', "N'", "N''", 'F', "F'", "I'"],
            '\-32768-32767': ['E', "E'", 'X', 'H', 'M', 'K', 'J', "I'"],
            '(': ['E', "E'", 'X', 'H', 'M'],
            'se': ['E', "E'", 'I', "I''"],
            'faca': ['E', "E'", 'Q'],
            'enquanto': ['E', "E'", 'W'],
            'senao': ["I''"],
            '[': ['E', "E'", 'G'],
            '+': ['E', "E'", 'X', "X'", 'H', 'M', 'K', 'F', "I'"],
            '-': ['E', "E'", 'X', "X'", 'H', 'M', 'K', 'F', "I'"],
            'eps' : ['E', "X'", "H'", "N'", "I''", 'D'],
            '*': ["H'"],
            '/': ["H'"],
            ',': ["L'"],
            ';': ["L'"],
            'int': ['D', 'T'],
            'char': ['D', 'T'],
            'real': ['D', 'T'],
            '==': ['R'],
            '<>': ['R'],
            '<': ['R'],
            '>': ['R'],
            '<=': ['R'],
            '>=': ['R'],
            'all': ['Z', "Z'", 'S'],
        }