from vpython import *

canvas(background=color.white)

def H2O (x,y,z):
    O=sphere(radius=1.5,color=color.red)
    H1=sphere(radius=.5,color=color.green,pos=vector(0,-2,0))
    H2=sphere(radius=.5,color=color.green,pos=vector(1.7,.5,.95))
    return compound([O,H1,H2],pos=vector(x,y,z))

def tet (x1,y1,z1):
    O1=sphere(radius=1.5,color=color.red)
    H3=sphere(radius=.5,color=color.green,pos=vector(0,2,0))
    H4=sphere(pos=vector(5,-1.5,-2.9)/3,color=color.green,radius=.5)
    WM1=H2O(0,-1.5-.2,5.8)
    WM2=H2O(5,-1.5-.2,-2.9)
    B1=cylinder(axis=vector(0,6,0),radius=.08)
    B2=cylinder(axis=vector(0,-1.5,5.8),radius=.08)
    B3=cylinder(axis=vector(5,-1.5,-2.9),radius=.08)
    B4=cylinder(axis=vector(-5,-1.5,-2.9),radius=.08)
    return compound([O1,WM1,WM2,H3,H4,B1,B2,B3,B4],pos=vector(x1,y1,z1))

i=5
j=7.5
k=5.8

for p1 in range(-4,5,2):
    tet(p1*i,0,0)

for q1 in range(-5,5,2):
    tet(q1*i,0,-1.5*k)

for p2 in range(-5,5,2):
    tet(p2*i,j,k*.5)

for q2 in range(-4,4,2):
    tet(q2*i,j,-k)

for p3 in range(-4,4,2):
    tet(p3*i,-j,k)

for q3 in range(-5,5,2):
    tet(q3*i,-j,-k*.5)