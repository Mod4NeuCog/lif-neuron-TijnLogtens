class Neuron:
    def __init__(self, Vmem = -70, go = False, com = False):
        self.Vmem = Vmem
        self.go = go
        self.Vthr = -55
        self.com = com

    def main(self):
        if (self.com == True) and (self.go == False):
            print('How much potential is added to the membrane?')
            user = int(input())
            self.Vmem += user
            return self.Vmem
        if self.go == False:
            self.Vmem += 20
            print(f"The updated membrane potential is: {self.Vmem}")
        if self.go == True:
            self.Vmem += 20
            return f"The updated membrane potential for our IO neuron is: {self.Vmem}"


    def increasePotential(self, pot):
        self.Vmem += pot

    def checkSpike(self):
        if self.Vmem >= self.Vthr:
            self.Vmem = -70
            return True
        else:
            return False

# Initialise and execute the no IO "neuron"
nQ1 = Neuron()
nQ1.main()

# Initialise and execute the IO "neuron"
nQ2 = Neuron(Vmem = -65, go = True)
print(nQ2.main())

# Initialise and execute the "neuron" that checks for spikes and prints them if a threshold is reached
nQ3 = Neuron(Vmem = -72, go = True)
spike = False
while(spike == False):
    spike = nQ3.checkSpike()
    nQ3.increasePotential(5)
    if spike == True:
        print(f"Spike == {spike}")
    if spike == False:
        print(f"Spike == {spike}")

# Create a "neuron" that allows a user/command line input to add potential to the membrane
nQ4 = Neuron(com=True)
nQ4.main()
print(f"The updated membrane potential is: {nQ4.Vmem}")





