# Author KR

"""
Stützstellen: x0,...,xn (müssen alle unterschiedlich sein)
Stützwerte: y0,...yn

Newton'sches Interpolationsverfahren
p(x)=a0+a1(x−x0)+a2(x−x0)(x−x1)+...+an(x−x0)(x−x1)(x−x2)⋅...⋅(x−xn−1)

y0=a0
y1=a0+a1(x1−x0)
y2=a0+a1(x2−x0)+a2(x2−x0)(x2−x1)
...
yn=a0+a1(xn−x0)+a2(xn−x0)(xn−x1)+ ... +an(xn−x0)(xn−x1)(xn−x2)⋅ ... ⋅(xn−xn−1)

Beispiel:
P0(1;2), P1(2;3), P2(3;1), P3(4;3)
p(x)=a0+a1(x−1)+a2(x−1)(x−2)     +a3(x−1)(x−2)(x−3)
->
2=a0⇒a0=2
3=2+a1(2−1)⇒a1=1
1=2+1(3−1)+a2(3−1)(3−2)⇒a2=−3/2=−1,5
3=2+1(4−1)−1,5(4−1)(4−2)+a3(4−1)(4−2)(4−3)⇒a3=7/6
"""

# Setup der Variablen
x = [1, 2, 3, 4]
y = [2, 3, 1, 3]
P = []
a = []

for i in x:
    P.append((x[i-1], y[i-1]))

# Berechnen der a-Werte


def main():
    print(P)


main()
exit()
