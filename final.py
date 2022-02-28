from typing import final


class Villager:
    def __init__(self, name, loves, catchphrase):
        self.name = name
        self.loves = loves
        self.catchphrase = catchphrase

    def talk(self):
        name = self.name
        result = name.upper()
        result+= "; "
        result+= self.catchphrase
        print(result)
    
    def loves_item(self, item):
        if item in self.loves:
            return True
        else:
            return False
            
    
    def not_in_common(self, villager):
        result = []
        result1 = []
        for i in villager.loves:
            result.append(i)
        for j in self.loves:
            result1.append(j)
        finalresult = []
        for i in result:
            if i not in result1:
                finalresult.append(i)
        for i in result1:
            if i not in result:
                finalresult.append(i)
        print(finalresult)

    def __str__(self):
        return (self.name)

penny = Villager("Penny", {"sandfish", "tom kha soup"}, "Archaeology is fascinating!")
print(penny)
penny.talk()
print(penny.loves_item("grape"))
print(penny.loves_item("sandfish"))

lenny = Villager("Lenny", {"tom kha soup", "apple fritters"}, "Is it time to milk the cows?")
lenny.talk()
print(lenny.loves_item("cows"))
lenny.not_in_common(penny)