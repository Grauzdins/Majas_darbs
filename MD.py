fails = input("fails: ")
vards=input("meklejamais vards:")
a = 0
 
with open(fails, 'r') as f:
    for line in f:
        vardi = line.split()
        for i in vardi:
            if(i==vards):
                a=a+1
print("skaits:")
print(a)