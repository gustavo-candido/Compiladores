from Gramatica import Gramatica
from Reconhecedor import Reconhecedor
class AnalisadorSintatico:
    def __init__ (self):
        self.reconhecedor = Reconhecedor('in.txt')
        self.gramatica = Gramatica()
        self.run(self.gramatica.gram['P'], False)

    def run(self, rules, finish):
        if finish:
            return

        tokenPosition, tokenId = self.reconhecedor.tokens.pop(0)
        tokenLine, tokenColumn = tokenPosition

        rule = choosedRule(rules, tokenId)
        
        if rule == None:
            print('Unexpected {} at {}:{}'.format(tokenId, tokenLine, tokenColumn))
        
    def matchRuleWithToken(rules, token):
        return None
