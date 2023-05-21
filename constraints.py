class BinaryExpression:
    pass

class Variable:

    def __init__(self, value = None):
        self.value = value

    def assign(self, value):
        self.value = value

    def evaluate(self):
        return self.value
    
    def assigned(self):
        return self.value == None
    
    def unassign(self):
        self.value = None
    
    def __eq__(self, other) -> BinaryExpression:
        return EqExpression(self, other)
    
    def __add__(self, other) -> BinaryExpression:
        return AddExpression(self, other)
    
    def __lt__(self, other) -> BinaryExpression:
        return LtExpression(self, other)
    
    def __le__(self, other) -> BinaryExpression:
        return LeExpression(self, other)
    
    def __ge__(self, other) -> BinaryExpression: 
        return GeExpression(self, other)
    
    def __gt__(self, other) -> BinaryExpression:
        return GtExpression(self, other)
    
    def __mul__(self, other) -> BinaryExpression:
        return MultExpression(self, other)
    
    def __rmul__(self, other) -> BinaryExpression:
        return self * other
    
    def __sub__(self, other) -> BinaryExpression:
        return SubExpression(self, other)
    
    def __truediv__(self, other) -> BinaryExpression:
        return DivExpression(self, other)

    def __ne__(self, other) -> BinaryExpression:
        return NeqExpression(self, other)
    
class Expression:
    def evaluate():
        pass

    def __eq__(self, other) -> BinaryExpression:
        return EqExpression(self, other)
    
    def __add__(self, other) -> BinaryExpression:
        return AddExpression(self, other)
    
    def __lt__(self, other) -> BinaryExpression:
        return LtExpression(self, other)
     
    def __le__(self, other) -> BinaryExpression:
        return LeExpression(self, other)
    
    def __ge__(self, other) -> BinaryExpression:
        return GeExpression(self, other)
    
    def __gt__(self, other) -> BinaryExpression:
        return GtExpression(self, other)
    
    def __mul__(self, other) -> BinaryExpression:
        return MultExpression(self, other)
    
    def __sub__(self, other) -> BinaryExpression:
        return SubExpression(self, other)
    
    def __truediv__(self, other) -> BinaryExpression:
        return DivExpression(self, other)
    
    def __ne__(self, other) -> BinaryExpression:
        return NeqExpression(self, other)
    
class BinaryExpression(Expression):

    def __init__(self, x, y):
        if type(x) != Variable and not issubclass(type(x), Expression):
            x = Variable(x)
        self.x = x
        if type(y) != Variable and not issubclass(type(y), Expression):
            y = Variable(y)
        self.y = y
    
class EqExpression(BinaryExpression):

    def evaluate(self):
        return self.x.evaluate() == self.y.evaluate()
    

class AddExpression(BinaryExpression):
    
    def evaluate(self):
        return self.x.evaluate() + self.y.evaluate()
    
class SubExpression(BinaryExpression):
    
    def evaluate(self):
        return self.x.evaluate() - self.y.evaluate()
    

class MultExpression(BinaryExpression):

    def evaluate(self):
        return self.x.evaluate() * self.y.evaluate()

class DivExpression(BinaryExpression):

    def evaluate(self):
        return self.x.evaluate() / self.y.evaluate()
    
class LtExpression(BinaryExpression):

    def evaluate(self):
        return self.x.evaluate() < self.y.evaluate()
    
class LeExpression(BinaryExpression):

    def evaluate(self):
        return self.x.evaluate() <= self.y.evaluate()
    
class GtExpression(BinaryExpression):

    def evaluate(self):
        return self.x.evaluate() > self.y.evaluate()
    
class GeExpression(BinaryExpression):

    def evaluate(self):
        return self.x.evaluate() >= self.y.evaluate()
    
class NeqExpression(BinaryExpression):

    def evaluate(self):
        return self.x.evaluate() != self.y.evaluate()

