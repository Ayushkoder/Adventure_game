name = input("Type your name")
print("Welcome ",name ,"To this adventure ")

answer=input("You are in the dirt road and there is a choice of moving left or right , then what would you choosee ?").lower()

if  answer == "left" :
    answer = input("You come to river you walk around it or you swim across th river ? type walk to walk or type swim to swim ").lower()
    if answer=="walk":
        print(" You walked aross the river  for 1000 of miles and you lose the game ")
    elif answer=="swim":
     print("You are swimmingnthrough the river ,and the you are eaten by alligator ")
    else :
        print ("Your answer is invalid , you lose") 
elif  answer == "right" :
    answer=input(" You come aross  rthe bridge , decie if you  want go ahead or want toka back ,  type Yes for go ahead and type no for go back ").lower()
    if answer=="yes":
        print(" You have crossed the bridge and  you Win   ")
    elif answer=="no":
     print("You choose to go back , and youu lose ")
    else :
        print ("Your answer is invalid , you lose")
else:
    print (" Not a vaslid option , you lose")

print("  Thankyou for playing the game ")    
                 
    












