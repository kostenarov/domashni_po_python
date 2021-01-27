import math #importvame math
def shlong(sentence): #funkciq za nai dulga duma
    long_word = max(sentence.split(), key=len) #namirame q 
    return long_word #vrushatme nai dulgata duma

def gcd(list): #funkciq za delitel
    a = math.gcd(*list) #izpozvame funkciqta za delitel vgradena v python i davame stoinostta  na math.gcd(*list) na a
    return a #vrushtame a

sentence = input("vkarai izrechenie: ") #vuvejdame izrechenie
longer_word = shlong(sentence) #promenliva koito priema stoinostta na shlong
print("nai-dulgata duma e :" + longer_word) #prinitrame nai-dulgata funkciq
list = [3, 6, 9, 12, 15, 18] #list za chisla
if len(list) < 5: #proverqva dali lista e po-golqm ot 5
    print("kus e")  #prinitra che e kus
else:
    print(gcd(list)) #ako ne e izpulneno printira delitelq i duljinata
print(len(list))