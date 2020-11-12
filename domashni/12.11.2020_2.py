#1
number = input ("vuvedi num : ") #vuvejdame number i count
count = input("vuevidu count : ")

for x in range(1, int(count) + 1, 1): #zapochvaiki ot edno do count + 1 i vseki put dobavq 1 dokato ne stigne do count + 1
print(int(number) * x) #printirame number*1 dokato e izpulnen for loopa
#2
string=input("Enter string:")#vuvejdame string ot user
glasni=0#promenliva glasni = 0
for i in string: #za element i ot string
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'): #proverqvame dali e glasna
            glasni=glasni+1 #ako e taka glasni priema stoinostta na glasni+1
print("Number of vowels are:") 
print(glasni) #printira finalnata stoinost na glasni
#3
items = ["my", "1", "turtle", "explain", "3"]

new_items = [item for item in items if not item.isdigit()] #za item susdavame for loop koito proverqva dali daden item e cifra i ako ne e go zapisva v new_items

print(new_items)

#4
num=int(input("Enter a number:"))
temp=num #suzdavame si promenliva za da proverim po-kusno dali e ogledalno
rev=0 #promenliva rev=0
while(num>0): #shte go izpulqva samo za polojitelni
    dig = num % 10 #dig shte e ravno na dig/10
    rev = rev*10 + dig #rev=rev*10+dig/10
    num = num // 10
if(temp == rev): #proverqva dali temp = rev
    print("The number is palindrome!")
else:
    print("Not a palindrome!")