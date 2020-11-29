import string
import numpy as np

class  AFD:
    def __init__(self):
        letra = list(string.ascii_letters)
        digito = list(string.digits)  
        printable = [x for x in string.printable] + ['']

        self.graph = {
            1 : [
                (2,['p']),
                (11, list(np.setdiff1d(letra,['p', 'i', 'r', 'c', 's', 'f', 'e']))),
                (13,['i']),
                (17,['r']),
                (22,['c']),
                (27,['<']),
                (31,['>']),
                (34,['=']),
                (36,['*']),
                (37,['/']),
                (38,['(']),
                (39,[')']),
                (40,['+']),
                (41,['-']),
                (42,[';']),
                (43,['{']),
                (44,['}']),
                (45,[',']),
                (46,['s']),
                (66,['f']),
                (53,['e']),
                (71,digito),
                (75,["'"]),
                (78,[':']),
                (80,[' ','\t','\n']),  
                (81, [''])         
            ],
            2 : [
                (3,['r']),
                (11,list(np.setdiff1d(letra+digito,['r']))),
                (12, list(np.setdiff1d(printable,letra+digito)))
            ],
            3 : [
                (4,['o']),
                (11,list(np.setdiff1d(letra+digito,['o']))),
            ],
            4 : [
                (5,['g']),
                (11,list(np.setdiff1d(letra+digito,['g']))),
            ],
            5 : [
                (6,['r']),
                (11,list(np.setdiff1d(letra+digito,['r']))),
            ],
            6 : [
                (7,['a']),
                (11,list(np.setdiff1d(letra+digito,['a']))),
            ],
            7 : [
                (8,['m']),
                (11,list(np.setdiff1d(letra+digito,['m']))),
            ],
            8 : [
                (9,['a']),
                (11,list(np.setdiff1d(letra+digito,['a']))),
            ],
            9 : [
                (10,list(np.setdiff1d(printable,letra+digito))),
                (11,letra+digito), 
            ],
            11 : [
                (11,letra+digito),
                (12,list(np.setdiff1d(printable,letra+digito))), 
            ],
            13 : [
                (11,list(np.setdiff1d(letra+digito,['n']))),
                (12, list(np.setdiff1d(printable,letra+digito))),
                (14,['n']),
            ],
            14 : [
                (15,['t']),
                (11,list(np.setdiff1d(letra+digito,['t']))),
            ],
            15 : [
                (16,list(np.setdiff1d(printable,letra+digito))),
                (11,letra+digito),
            ],
            17 : [
                (18,['e']),
                (11,list(np.setdiff1d(letra+digito,['e']))),
                (12,list(np.setdiff1d(printable,letra+digito))),
            ],
            18 : [
                (19,['a']),
                (11,list(np.setdiff1d(letra+digito,['a']))),
            ],
            19 : [
                (20,['l']),
                (11,list(np.setdiff1d(letra+digito,['l']))),
            ],
            20 : [
                (21,list(np.setdiff1d(printable,letra+digito))),
                (11,letra+digito),
            ],
            22 : [
                (23,['h']),
                (11,list(np.setdiff1d(letra+digito,['h']))),
                (12,list(np.setdiff1d(printable,letra+digito))),
            ],
            23 : [
                (24,['a']),
                (11,list(np.setdiff1d(letra+digito,['a']))),
            ],
            24 : [
                (25,['r']),
                (11,list(np.setdiff1d(letra+digito,['r']))),
            ],
            25 : [
                (26,list(np.setdiff1d(printable,letra+digito))),
                (11,letra+digito),
            ],
            27 : [
                (28,list(np.setdiff1d(printable,['>', '=']))),
                (29,['>']),
                (30,['=']),
            ],
            31 : [
                (32,list(np.setdiff1d(printable,['=']))),
                (33,['=']),
            ],
            34 : [
                (35,['=']),
            ],
            46 : [
                (47,['e']),
                (11,list(np.setdiff1d(letra+digito,['e']))),
                (12,list(np.setdiff1d(printable,letra+digito))),
            ],
            47 : [
                (49,['n']),
                (11,list(np.setdiff1d(letra+digito,['n']))),
                (48,list(np.setdiff1d(printable,letra+digito))),
            ],
            49 : [
                (50,['a']),
                (11,list(np.setdiff1d(letra+digito,['a']))),
            ],
            50 : [
                (51,['o']),
                (11,list(np.setdiff1d(letra+digito,['o']))),
            ],
            51 : [
                (52,list(np.setdiff1d(printable,letra+digito))),
                (11,letra+digito),
            ],
            66 : [
                (67,['a']),
                (12,list(np.setdiff1d(printable,letra+digito))),
                (11,list(np.setdiff1d(letra+digito,['a']))),
            ],
            67 : [
                (68,['c']),
                (11,list(np.setdiff1d(letra+digito,['c']))),
            ],
            68 : [
                (69,['a']),
                (11,list(np.setdiff1d(letra+digito,['a']))),
            ],
            69 : [
                (70,list(np.setdiff1d(printable,letra+digito))),
                (11,letra+digito),
            ],
            53 : [
                (54,['n']),
                (12,list(np.setdiff1d(printable,letra+digito))),
                (11,list(np.setdiff1d(letra+digito,['n']))),
            ],
            54 : [
                (55,['t']),
                (59,['q']),
                (11,list(np.setdiff1d(letra+digito,['t','q']))),
            ],
            55 : [
                (56,['a']),
                (11,list(np.setdiff1d(letra+digito,['a']))),
            ],
            56 : [
                (57,['o']),
                (11,list(np.setdiff1d(letra+digito,['o']))),
            ],
            57 : [
                (58,list(np.setdiff1d(printable,letra+digito))),
                (11,letra+digito),
            ],
            59 : [
                (60,['u']),
                (11,list(np.setdiff1d(letra+digito,['u']))),
            ],
            60 : [
                (61,['a']),
                (11,list(np.setdiff1d(letra+digito,['a']))),
            ],
            61 : [
                (62,['n']),
                (11,list(np.setdiff1d(letra+digito,['n']))),
            ],
            62 : [
                (63,['t']),
                (11,list(np.setdiff1d(letra+digito,['t']))),
            ],
            63 : [
                (64,['o']),
                (11,list(np.setdiff1d(letra+digito,['o']))),
            ],
            64 : [
                (65,list(np.setdiff1d(printable,letra+digito))),
                (11,letra+digito),
            ],
            71 : [
                (71,digito),
                (72,['.']),
                (74,list(np.setdiff1d(printable,digito+['.'])))
            ],
            72 : [
                (72,digito),
                (73,list(np.setdiff1d(printable,digito)))
            ],
            75 : [
                (76,list(np.setdiff1d(printable,["'"]))),
            ],
            76 : [
                (77,["'"]),
            ],
            78 : [
                (79,["="]),
            ],
        }
        self.finals = {
            10: 'programa',
            12: 'id,buffer',
            16: 'int',
            21: 'real',
            26: 'char',
            28: 'oprel,lt',
            29: 'oprel,dif',
            30: 'oprel,le',
            32: 'oprel,gt',
            33: 'oprel,ge',            
            35: 'oprel,eq',
            36: 'mul',
            37: 'div',
            38: '(',
            39: ')',
            40: 'add',
            41: 'sub',
            42: ';',
            43: '{',
            44: '}',
            45: ',',
            48: 'se',
            52: 'senao',
            70: 'faca',
            58: 'entao',
            65: 'enquanto',
            73: 'cntReal,buffer',
            74: 'cntInt,buffer',
            77: 'cntChar,buffer',
            79: 'opAtrib',
            80: 'null',
            81: 'eof'        
        }
        self.retreat = [10,12,16,21,26,28,32,48,52,70,58,65,73,74]
