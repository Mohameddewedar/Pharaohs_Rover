import math

theta=0
alpha=0
beta=0
n=0

theta=(math.pi/180)*theta
alpha=(math.pi/180)*alpha
beta=(math.pi/180)*beta
n=(math.pi/180)*n
s1=500
s2=350
s3=330
s4=376
s5=301
s6=61.2
s7=61
s8=89
s9=58
s10=216
s11=71
s12=95
s13=70
s14=77.5
L1=105
z1=35

L3=L1+s1*math.cos(theta)+s2*math.cos(theta-alpha)+s3*math.cos(n)
z=z1+s1*math.sin(theta)+s2*math.sin(theta-alpha)+s3*math.sin(n)
x=L3*math.cos(beta)
y=L3*math.sin(beta)

dr=math.atan2(25,210)
r=math.pi-dr-theta
dL4=math.sqrt(25*25+210*210)
d1=math.sqrt(dL4*dL4+s4*s4-2*dL4*s4*math.cos(r)) #linear 1 length

m=math.pi-alpha
dm=math.sqrt(s6*s6+s7*s7-2*s6*s7*math.cos(m))
a=math.acos((s6*s6+dm*dm-s7*s7)/(2*s6*dm))
b=math.acos((dm*dm+s8*s8-s9*s9)/(2*s8*dm))
c=math.pi-a-b
d2=math.sqrt(s5*s5+s8*s8-2*s5*s8*math.cos(c)) #linear 2 length


phi=theta-alpha-n
t=math.pi-phi-56/180*math.pi
dt=math.sqrt(s11*s11+s14*s14-2*s11*s14*math.cos(t))
e=math.acos((dt*dt+s11*s11-s14*s14)/(2*dt*s11))
f=math.acos((dt*dt+s12*s12-s13*s13)/(2*dt*s12))
g=math.pi-e-f
d3=math.sqrt(s10*s10+s12*s12-2*s10*s12*math.cos(g))  #linear 3 length