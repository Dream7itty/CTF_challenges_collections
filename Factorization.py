from banner import *
banner()

from Factorizations.factordb import *
from Factorizations.fermat import *
from Factorizations.ecm import *
from Factorizations.qs import *

print("""
[1] - Factordb Factorization \033[92m
[2] - Fermat Factorization \033[96m
[3] - ECM Factorization \033[93m
[4] - Quadratic sieve Factorization \033[95m 
[0] - Exit \033[92m
    """)

x = int(input(">>> "))
#Factordb
if x == 1:

    n = int(input("%s\n>>> n = %s"%(B,B)))
    print("\n[+] Please Wait ...\n")
    def factordb(n):
            f =  FactorDB(n)
            f.connect()
            return f.get_factor_list()

    print("%sprimes =%s"%(Y,Y),"%s"%(G),factordb(n))

#Fermet
elif x == 2:
    n = int(input("%s\n>>> n = %s"%(B,B)))
    print("\n[+] Please Wait ...\n")
    fermat(n)

#ECM
elif x == 3:
    n = int(input("%s\n>>> n = %s"%(B,B)))
    print("\n[+] Please Wait ...\n")
    print("%sprimes =%s"%(Y,Y),"%s"%(G),primefactors(n))

elif x == 4:
    N = int(input("%s\n>>> n = %s"%(B,B)))
    if not factorise(N):
        print("Number Must Be Greater Than 0 and Must Be Integer")
    elif factorise(N) == "Long":
        print("N is Too Long ")
    else:
        print("\n[+] Please Wait ...\n")
        print ("%sprimes =%s"%(Y,Y),"%s"%(G),factorise(N))

else:
    exit()
