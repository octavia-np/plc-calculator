from components.LA import MyLexer
from sly import Parser

class CalcParser(Parser):
    debugfile = 'parser.out'
    start = 'E'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    
    @_('T')
    def E(self, p):
        print('E -> T', [p.T])
        return p.T
    
    @_('F')
    def T(self, p):
        print('T -> F', [p.F])
        return p.F

    @_('T "+" F')
    def T(self, p):
        print('T -> T + F', [p.T + p.F])
        return [p.T[0] + p.F[0]]

    @_('E "*" T')
    def E(self, p):
        print('E -> E * T', [p.E + p.T])
        return [p.E[0] * p.T[0]]
    
    @_('N')
    def F(self, p):
        print('F -> N', p.N)
        return [p.N]
    
if __name__ == "__main__":
    lexer = MyLexer()
    parser = CalcParser()
    text = "3 + 5 * 2"
    result = parser.parse(lexer.tokenize(text))
    print("Result:", result)
    
class PrefixParser(Parser):
    debugfile = 'parser.out'
    start = 'E'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    
    @_('T')
    def E(self, p):
        print('E -> T', [p.T])
        return p.T
    
    @_('F')
    def T(self, p):
        print('T -> F', [p.F])
        return p.F

    @_('T "+" F')
    def T(self, p):
        print('T -> T + F', [f'+{p.T[0]}{p.F[0]}'])
        return [ f'+{p.T[0]}{p.F[0]}']

    @_('E "*" T')
    def E(self, p):
        print('E -> E * T', [f'*{p.E[0]}{p.T[0]}'])
        return [f'*{p.E[0]}{p.T[0]}']
    
    @_('N')
    def F(self, p):
        print('F -> N',[p.N])
        return [p.N]
    
if __name__ == "__main__":
    lexer = MyLexer()
    parser = PrefixParser()
    text = "3 + 5 * 2"
    result = parser.parse(lexer.tokenize(text))
    print("Prefix:", result)
    
class PostfixParser(Parser):
    debugfile = 'parser.out'
    start = 'E'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    
    @_('T')
    def E(self, p):
        print('E -> T', [p.T])
        return p.T
    
    @_('F')
    def T(self, p):
        print('T -> F', [p.F])
        return p.F

    @_('T "+" F')
    def T(self, p):
        print('T -> T + F', [ f'{p.T[0]}{p.F[0]}+'])
        return [f'{p.T[0]}{p.F[0]}+']

    @_('E "*" T')
    def E(self, p):
        print('E -> E * T', [f'{p.E[0]}{p.T[0]}*'])
        return [f'{p.E[0]}{p.T[0]}*']
    
    @_('N')
    def F(self, p):
        print('F -> N', [p.N])
        return [p.N]

if __name__ == "__main__":
    lexer = MyLexer()
    parser = PostfixParser()
    text = "3 + 5 * 2"
    result = parser.parse(lexer.tokenize(text))
    print("Postfix:", result)
