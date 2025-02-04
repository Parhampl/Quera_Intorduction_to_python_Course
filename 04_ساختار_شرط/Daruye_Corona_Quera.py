'''
 Shekarestan
 2 vurudi aval be tartib tedad mobtalayan va tedad foti hast.
 
 namakestan
  2 vurudi dovom be tartib tedad mobtalayan va tedad foti hast.

 har keshvari ke tedad darmani haye bishtari dashte bashe daruye behtari dare.
 
 '''
# Shekarestan
Sh_Infected = int(input())
Sh_Dead = int(input())

# Namakestan
Na_Infected = int(input())
Na_Dead = int(input())

if (Sh_Infected - Sh_Dead) > (Na_Infected - Na_Dead):
    print("Shekarestan")
elif (Sh_Infected - Sh_Dead) < (Na_Infected - Na_Dead):
    print("Namakestan")
else:
    print("Equal")
