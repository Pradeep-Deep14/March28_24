class Jacket:
    def getColor(self):
        colors={
            '#ffffff':'white',
            '#00000' :'black'
        }

        return colors[self.__color]
    
    def setColor(self,val):
        self.__color=val


obj=Jacket()
obj.setColor('#ffffff')
print(obj.getColor())