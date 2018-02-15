import math

x=868.0
y=0.0
z=416.0
n=-16.0

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
L1=90
z1=35

z3=z
n=(math.pi/180)*n
L3=math.sqrt(x*x+y*y)
beta=math.atan2(y,x)
L2=L3-s3*math.cos(n)
z2=z3-s3*math.sin(n)
dL=L2-L1
dz=z2-z1
F=math.sqrt(dL*dL+dz*dz)
q1=math.atan2(dz,dL)
q2=math.acos((s1*s1+F*F-s2*s2)/(2.0*s1*F))
m=math.acos((s1*s1+s2*s2-F*F)/(2.0*s1*s2))
alpha=math.pi-abs(m)
theta=q1+q2

dr=math.atan(25.0/210)
r=math.pi-dr-theta
dL4=math.sqrt(25*25.0+210.0*210)
d1=math.sqrt(dL4*dL4+s4*s4-2.0*dL4*s4*math.cos(r)) #linear 1 length

dm=math.sqrt(s6*s6+s7*s7-2.0*s6*s7*math.cos(m))
a=math.acos((s6*s6+dm*dm-s7*s7)/(2.0*s6*dm))
b=math.acos((dm*dm+s8*s8-s9*s9)/(2.0*s8*dm))
c=math.pi-a-b
d2=math.sqrt(s5*s5+s8*s8-2.0*s5*s8*math.cos(c)) #linear 2 length


phi=theta-alpha-n
t=math.pi-phi-56/180.0*math.pi
dt=math.sqrt(s11*s11+s14*s14-2.0*s11*s14*math.cos(t))
e=math.acos((dt*dt+s11*s11-s14*s14)/(2.0*dt*s11))
f=math.acos((dt*dt+s12*s12-s13*s13)/(2.0*dt*s12))
g=math.pi-e-f
d3=math.sqrt(s10*s10+s12*s12-2.0*s10*s12*math.cos(g))  #linear 3 length

print("d1=%.2f d2=%.2f d3=%.2f" %(d1,d2,d3))