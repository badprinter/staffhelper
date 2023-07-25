import datetime

class Sampler:
   
    def __init__(self) -> None:
        
        self.Open = 0
        self.Close = 0
        self.Low = 0
        self.High = 0
        
        self.Start = datetime.datetime.now()

        self._calculateLengthAttributes()

    def _calculateLengthAttributes(self):

        if self.Close > self.Open or self.Open == self.Close:
            self.IsWhite = True
            self.IsBlack = False

        if self.IsWhite:
            self.ShadowUpLength = self.High - self.Close
            self.ShadowDownLength = self.Open - self.Low
        else: # Черная свеча
            self.ShadowUpLength = self.High - self.Open
            self.ShadowDownLength = self.Close - self.Low
        

            
        


