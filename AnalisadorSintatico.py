from Gramatica import Gramatica
from Reconhecedor import Reconhecedor

class AnalisadorSintatico:
    def __init__ (self):
        self.reconhecedor = Reconhecedor('in.txt')
        self.gramatica = Gramatica()
        self.test = ''
        print('reconhecido: {}'.format(self.run(self.gramatica.gram['X'])))
        print(self.test)
        
    def run(self, rule):
        popped = []
        tokens = self.reconhecedor.tokens
        # if rules == None:
        #     print('Unexpected {} at {}:{}'.format(tokenId, tokenLine, tokenColumn))
        #     return
        print("\nRULE >>> {}".format(rule))
        accepted = True
        for production in rule:
            accepted = True
            print("PRODUCTION >>> {} TOKEN >>> {}".format(production, tokens[0]))
            for symbol in range(len(production)):
                print("[{}] = '{}'".format(symbol, production[symbol]))
                tokenPosition, tokenId = tokens[0]
                tokenLine, tokenColumn = tokenPosition
                tokenName = tokenId[1:-1]
                tokenList = tokenName.split(',')
                token = tokenList[0]

                if self.isTerminal(production[symbol]):
                    if production[symbol] != 'eps' and production[symbol] != token:
                        accepted = False
                        break
                    elif production[symbol] != 'eps':
                        pop = self.reconhecedor.tokens.pop(0)
                        self.test += str(pop)
                        popped.append(pop)
                    
                else: # Não terminal
                    if ['eps'] in self.gramatica.gram[production[symbol]] or self.tokenInFirst(token,production[symbol]):
                        if(not self.run(self.gramatica.gram[production[symbol]])):
                            accepted = False
                            break
                    else:
                        accepted = False
                        break
            
            if accepted:
                break
        
        if not accepted:
            self.reconhecedor.tokens = popped + self.reconhecedor.tokens
        print("out {}".format(rule))
        return accepted
                

    # def findRules(self, token):
    #    if token not in self.gramatica.firsts:
    #         return None
    #     return self.gramatica.firsts[token]

    def isTerminal(self, symbol):
        return symbol not in self.gramatica.gram

    def tokenInFirst(self, token, production):
        return production in self.gramatica.firsts[token]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                