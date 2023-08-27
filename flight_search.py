class FlightSearch:
    def __init__(self,city):
        self.city = city

    def getIATA(self):
        self.city['iataCode']="TESTING"
        return self.city