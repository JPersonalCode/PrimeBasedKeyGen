import random
Salt = random.getrandbits(256)
def isprime (n):
    if str(n)[len(str(n))-1] in ("0","2","4","6","8") and n>=10 :return False
    if n == 2 or n == 3 : return True
    if n%2 == 0 or n < 2 : return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True
def genprime ():
    x = 6
    while isprime(x) == False : 
            x = random.randint(1000000000000000,10000000000000000)
    return x     
PrimeList = []
i = 2
while i!=   0 :
     PrimeList.append(genprime())
     i = i - 1
Key = int(PrimeList[0]) * int(PrimeList[1]) +  Salt
print("Public Key: "+hex(Key))
print ('Salt: ',hex(Salt))
print ('Primes: ',PrimeList)
