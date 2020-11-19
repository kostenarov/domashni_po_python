#1
string = input('Enter a string: ')#usera vuvejda string
vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U']#list susu vsichki glasni
string = list(string)#prevrushtame string v list

for i in vowels:#dva for loopa koito sverqvat glasna ot vowels i simvol ot string
    for j in range(len(string)):
        if i == string[j]:
                string.insert(j, i)

print(string)

#2
string = input("Enter a string: ")# Usera vuvejda string

counter = 0
 #counter variable to count the character in a string
for s in string:#for loop za da prebroim duljinata
      counter = counter+1#counter = counter + 1
print("Length of the input string is:", counter)#printira counter

#3
import math#vuvejdame biblioteka za math operacii

number = int(input('Enter a number: '))
#number kato go pravim v int 
number_copy = number#suzdavame promenliva koqto priema stoinostta na number
counter = 0#suzdavame counter

while number >= 2:#dokato vuvedenoto chislo e >= na dve shte nameri koren kvadraten na number
    number = math.sqrt(number)
    counter += 1#counter = counter +1 

print(number_copy, '-->', counter)#printira finalnata stoinost na counter i nachalnoto chislo

#4
number = int(input("Enter number : "))#vuvejdame number ot tip int
sum = 0; 
#vuvejdame promenliva sum=0
for i in range(0, number + 1):
   if i > 1:#proverqva dali daden element ot number e > 1
       for j in range(2, i):
           if (i % j) == 0:#ako i % j ==0 shte prikluchi cikula
               break
       else: #else sum = sum + 1
           sum += i;

print(sum) #printira sumata