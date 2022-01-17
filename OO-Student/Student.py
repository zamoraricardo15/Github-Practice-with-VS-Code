
class Student:
    graduationTitle = "Web Developer"
    def __init__( self, fN = "N/A", lN = "N/A", age = -1 ):
        # Attributes
        self.firstName = fN
        self.lastName = lN
        self.age = age

    def printInfo( self ):
        print( f"First name: {self.firstName}\nLast name: {self.lastName}\nAge: {self.age}" )

    def addOneYear( self ):
        self.age += 1
        return self.age    

    def addSomeYears( self, val ):
        self.age += val