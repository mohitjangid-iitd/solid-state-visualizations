from vpython import *

h1=canvas(background=color.white)
def np(x,y,z):
  n=sphere(pos=vector(x,y,z),radius=0.05,color=color.magenta,canvas=h1)
  return n

def rp(x1,y1,z1,x2,y2,z2):
  m=cylinder(pos=vector(x1,y1,z1),axis=vector(x2,y2,z2),radius=0.01,color=color.blue,canvas=h1)
  return m

s1=np(-1,1,-1)
s2=np(1,1,-1)
s3=np(-1,1,1)
s4=np(1,1,1)
s5=np(-1,-1,1)
s6=np(-1,-1,-1)
s7=np(1,-1,-1)
s8=np(1,-1,1)
s9=np(0,-1,0)
s10=np(-1,0,0)
s11=np(1,0,0)
s12=np(0,0,1)
s13=np(0,0,-1)
s14=np(0,1,0)
s15=np(-1,1,0)
s16=np(1,1,0)
s17=np(0,0,0)
s18=np(-1,-1,0)
s19=np(1,-1,0)
s20=np(0,1,1)
s21=np(-1,0,1)
s22=np(1,0,1)
s23=np(0,-1,1)
s24=np(0,1,-1)
s25=np(-1,0,-1)
s26=np(1,0,-1)
s27=np(0,-1,-1)

b1=rp(0,0,0,0,1,0)
b2=rp(0,0,0,-1,0,0)
b3=rp(0,0,0,1,0,0)
b4=rp(0,0,0,0,-1,0)
b5=rp(0,0,0,0,0,1)
b6=rp(0,0,0,0,0,-1)

m=box(size=vector(1,1,1),color=color.green,opacity=0.5)

h2=canvas(background=color.cyan)
def np(x,y,z):
  n=sphere(pos=vector(x,y,z),radius=0.05,color=color.magenta,canvas=h2)
  return n

def rp(x1,y1,z1,x2,y2,z2):
  m=cylinder(pos=vector(x1,y1,z1),axis=vector(x2,y2,z2),radius=0.01,color=color.blue,canvas=h2)
  return m

p1=np(0,0,0)
p2=np(-1,1,0)
p3=np(1,1,0)
p4=np(-2,0,0)
p5=np(2,0,0)
p6=np(-1,-1,0)
p7=np(1,-1,0)
p8=np(-2,1,-1)
p9=np(0,1,-1)
p10=np(2,1,-1)
p11=np(-1,0,-1)
p12=np(1,0,-1)
p13=np(-2,-1,-1)
p14=np(0,-1,-1)
p15=np(2,-1,-1)
p16=np(-2,1,1)
p17=np(0,1,1)
p18=np(2,1,1)
p19=np(-1,0,1)
p20=np(1,0,1)
p21=np(-2,-1,1)
p22=np(0,-1,1)
p23=np(2,-1,1)

c1=rp(0,0,0,-1,1,0)
c2=rp(0,0,0,1,1,0)
c3=rp(0,0,0,-1,-1,0)
c4=rp(0,0,0,1,-1,0)
c5=rp(0,0,0,0,1,-1)
c6=rp(0,0,0,-1,0,-1)
c7=rp(0,0,0,1,0,-1)
c8=rp(0,0,0,0,-1,-1)
c9=rp(0,0,0,0,1,1)
c10=rp(0,0,0,-1,0,1)
c11=rp(0,0,0,1,0,1)
c12=rp(0,0,0,0,-1,1)

def ap(x,y,z):
  a=pyramid(pos=vector(x,y,z),axis=vector(x,y,z),size=vector(0.5,1,1))
  return a

a1=ap(0.5,0,0)
a2=ap(-0.5,0,0)
a3=ap(0,0.5,0)
a4=ap(0,-0.5,0)
a5=ap(0,0,0.5)
a6=ap(0,0,-0.5)