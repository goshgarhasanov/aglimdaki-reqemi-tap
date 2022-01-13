from random import randint
import time

class Tapmaca():
    def __init__(self, ad):
        self.ad = ad

    def get_random_number(self,a,b):
        return randint(a,b)

    def play_game(self):
        self.show_welcome_message()

    def show_welcome_message(self):
        print(f"""
               Salam {self.ad}  Oyuna Xosh Gelmisen 
               Baslamazdan Evvel qaydalar ile tanish ol
               Men 0 ile 100 arasinda bir reqem beynimde tutacam
               sende onu 5 addimda tapmaga calisacaqsan
               bu qeder sade ugurlar dostum !
               """)

        while True:
            isPlay = input('Oyuna Baslamaq Ucun 1 duymesini sixin :')
            if (isPlay == '1'):
                self.start_game(5)
            else:
                print("Düzgün seçim etmədiniz!")

    def start_game(self,addim):
        time.sleep(3)
        randomNumber=self.get_random_number(0,100)
        while True:
            try:
                userNumber = int(input('Aglimda Tutdugum Reqemi Texmin Et :'))
                if(addim>0):
                    print(f"{addim}  defe shansiniz qaldi")
                    self.check_number(randomNumber, userNumber)
                    addim -= 1
                else:
                    print(f"Tessuf shansiniz qalmadi siz uduzdunuz aglimda tutdugum reqem {randomNumber}")
                    break
            except ValueError:
                print("Xahish Edirik 0-100 arasinda reqem daxil edesiniz")
    def check_number(self,randomNumber,userNumber):
        if(userNumber>randomNumber):
            print("Asagi En")
        elif(userNumber<randomNumber):
            print("Yuxari Qalx")
        elif(userNumber==randomNumber):
            print("Tebrikler Qazandiniz")
        else:
            print("yalniz 1 ile 100 arasinda reqem Daxil Ede bilersen!")


