# mantendo estados dentro da classe

class Cam:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording


    def record(self):
        if self.recording:
            print(f'{self.name} is already filming..')
            return
        
        print(f'{self.name} is filming..')
        self.recording = True 

    def record_stop(self):
        if self.recording is False:
            print(f"{self.name} it's already stopped..")
            return
        
        self.recording = False
        print(f'{self.name} stopped recording..') 
    

    def photograph(self):
        if self.recording:
            print(f"{self.name} can't take a picture while recording")
            return
            
        print(f"{self.name} take a picture")


c1 = Cam('Canon')
c2 = Cam('Sony')


print(c1.name)
c1.record() #mandei ela filmar
print(c1.recording) #estado que ela tá -> filmando (True) ou não (False)
print()


print(c2.name)
print(c2.recording) #como não mandei ela filmar -> c2.record -> vai retornar false
print()


c1.record()
c1.record_stop()
c1.photograph()