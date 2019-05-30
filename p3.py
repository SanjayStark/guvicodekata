c=input()
vow=['a','e','i','o','u']
cons=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
if c in vow:
    print("Vowel")
elif c in cons:
    print("Consonant")
else:
    print("invalid")
