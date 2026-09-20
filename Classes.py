from datetime import datetime

class XAUUSD:
    def __init__(self, Influence, Price, Direction):
        self.Influence = Influence
        self.Price = Price 
        self.Direction = Direction
        self.Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S" )
        
    def Influence(self):
        if self.Influence != "Geopolitics, Oilprice, Dollar, FedRates":
            return("False..")
        else:
            return {"Direction": self.Direction, "Price": self.Price}
    def to_dict(self):
        return {
            "Influence": self.Influence,
            "Price": self.Price,
            "Direction": self.Direction,
            "Date": self.Date
        }   
            