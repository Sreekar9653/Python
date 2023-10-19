# Program to show first two and last two letters in a word
# Return the same character if the length of string is less than 2

a = input("Enter word, enter stop if done")

while(a!="stop"):
    print(a if(len(a)<2) else a[:2]+a[-2:])		# python -> py+on -> pyon
    a=input("Enter word, enter stop if done")
          
