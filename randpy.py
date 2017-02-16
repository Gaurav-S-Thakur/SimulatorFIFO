import math

class RandN(object):
    def __init__(self,seed):
        self.dseed = seed
            
    def uniform(self):
        d2p31m = 2147483647
        d2p31  = 2147483711
        self.dseed = 16807*(self.dseed) - math.floor(16807*(self.dseed)/d2p31m) * d2p31m
        return( math.fabs((self.dseed / d2p31)))

    def expon(self, xm):
        return( (-(xm) * math.log(self.uniform())) )