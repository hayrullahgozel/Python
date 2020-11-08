class cember :

    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    def çevre(self):
        return self.pi * self.yaricap * self.yaricap

    def alan(self):
        return 2*self.pi * self.yaricap * self.yaricap    


p1=cember(8)
print(f"alan = {p1.alan()}")
print(f"çevre = {p1.çevre()}")