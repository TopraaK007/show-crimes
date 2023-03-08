# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import  requests
from collections import Counter
class Crime_type():
    def __init__(self,crime="all-crime"):
        self.crime=crime
        self.status=True

    def run(self):
        self.menu()
        choice=self.choice()
        if choice==1:
            self.show_cities()
            while True:
                try:
                    choice=int(input("Şehir seçiniz:"))
                    if choice<1 or choice>5:
                        print("(1-5)arasında değer giriniz!")
                        continue
                    break
                except ValueError:
                    print("Lütfen rakam seçiniz!!!")
            self.city_crime(choice)
        if choice==2:
            self.exit()
    def menu(self):
        print("""
        ***HOŞGELDİNİZ***
        
        1)Şehirlere göre işlenilen suçlar
        2)Çıkış""")
    def choice(self):
        while True:
            try:
                choice=int(input("Yapmak istediğiniz işlemi seçiniz:"))
                if choice>=1 and choice<=2:
                    return choice
                else:
                    print("(1-2) arasında seçim yapınız!!!")
            except ValueError:
                print("Lütfen (1-2) arasında seçim yapınız!!!")

    def city_crime(self,choice):
        if choice==1:
            crimes_url = "https://data.police.uk/api/crimes-no-location"
            payload={
                "category":"all-crime",
                "force"   :"city-of-london",
                }
            response=requests.get(crimes_url,params=payload)
            if response.status_code==200:
                crime_list=[]
                value=response.json()
                for crime in value:
                    crime_list.append(crime["category"])
                show=Counter(crime_list)
                for x,y in show.items():
                    print("--> {}={}".format(x,y))
            else:
                print("Hata")
        if choice==2:
            crimes_url = "https://data.police.uk/api/crimes-no-location"
            payload={
                "category":"all-crime",
                "force"   :"cambridgeshire",
                }
            response=requests.get(crimes_url,params=payload)
            if response.status_code==200:
                crime_list=[]
                value=response.json()
                for crime in value:
                    crime_list.append(crime["category"])
                show = Counter(crime_list)
                for x, y in show.items():
                    print("--> {}={}".format(x, y))
            else:
                print("Hata")
        if choice==3:
            crimes_url = "https://data.police.uk/api/crimes-no-location"
            payload={
                "category":"all-crime",
                "force"   :"leicestershire",
                }
            response=requests.get(crimes_url,params=payload)
            if response.status_code==200:
                crime_list=[]
                value=response.json()
                for crime in value:
                    crime_list.append(crime["category"])
                show = Counter(crime_list)
                for x, y in show.items():
                    print("--> {}={}".format(x, y))
            else:
                print("Hata")

        if choice==4:
            crimes_url = "https://data.police.uk/api/crimes-no-location"
            payload={
                "category":"all-crime",
                "force"   :"nottinghamshire",
                }
            response=requests.get(crimes_url,params=payload)
            if response.status_code==200:
                crime_list=[]
                value=response.json()
                for crime in value:
                    crime_list.append(crime["category"])
                show = Counter(crime_list)
                for x, y in show.items():
                    print("--> {}={}".format(x, y))
            else:
                print("Hata")

        if choice==5:
            crimes_url = "https://data.police.uk/api/crimes-no-location"
            payload={
                "category":"all-crime",
                "force"   :"metropolitan",
                }
            response=requests.get(crimes_url,params=payload)
            if response.status_code==200:
                crime_list=[]
                value=response.json()
                for crime in value:
                    crime_list.append(crime["category"])
                show = Counter(crime_list)
                for x, y in show.items():
                    print("--> {}={}".format(x, y))
            else:
                print("Hata")



    def show_cities(self):
        print("1)City of London\n2)Cambridgeshire\n3)Leicestershire\n4)Nottinghamshire\n5)Metropolitan")
    def exit(self):
        self.status=False

crime=Crime_type()
while crime.status:
    crime.run()