import time

class Leftovers():
    def __init__(self, credits):
        self.credits = credits

    def calculateCredits(self):
        self.userRemain, self.userLimit = self.credits['UserRemaining'], self.credits['UserLimit']
        self.clientRemain, self.clientLimit = self.credits['ClientRemaining'], self.credits['ClientLimit']
        self.timeLeft = self.credits['UserReset']

        return self.printCredits()

    def printCredits(self):
        return str(self.clientRemain) + "/" + str(self.clientLimit) + " credits available and " +\
                      str(self.userRemain) + "/" + str(self.userLimit) + " resets at " +\
                      str(time.strftime('%Y-%m-%d %I:%M:%S %p %Z', time.localtime(self.timeLeft)))