class grandparent():
    def prop(self):
        print('Property : 100000000')
        
class mother():
    def color(self):
        print('Color : White')

class father():
    def height(self):
        print('height : 6 feet')

class son(grandparent,mother,father):
    pass

s=son()
s.color()
s.height()
s.prop()
        
