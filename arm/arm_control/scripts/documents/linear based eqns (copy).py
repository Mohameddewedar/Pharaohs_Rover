import math


d1=436
d2=334
d3=243
beta=0

beta=math.radians(beta)

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


dL4=math.sqrt(25*25+210*210)
dr=math.atan2(25.0,210.0)
r=math.acos((dL4*dL4+s4*s4-d1*d1)/(2*dL4*s4))
theta=math.pi-dr-r

c=math.acos((s5*s5+s8*s8-d2*d2)/(2.0*s5*s8))
q=math.pi-c
dq=math.sqrt(s8*s8+s6*s6-2*s8*s6*math.cos(q))
a=math.acos((dq*dq+s8*s8-s6*s6)/(2.0*dq*s8))
b=math.acos((dq*dq+s9*s9-s7*s7)/(2.0*dq*s9))
dm=math.sqrt(s8*s8+s9*s9-2.0*s8*s9*math.cos(a+b))
m=math.acos((s6*s6+s7*s7-dm*dm)/(2.0*s6*s7))
alpha=math.pi-m

G=math.acos((s10*s10+s12*s12-d3*d3)/(2.0*s10*s12))
dg=math.pi-G
dg1=math.sqrt(s11*s11+s12*s12-2.0*s11*s12*math.cos(dg))
e=math.acos((s11*s11+dg1*dg1-s12*s12)/(2.0*dg1*s11))
f=math.acos((dg1*dg1+s14*s14-s13*s13)/(2.0*dg1*s14))
t=e+f
phi=math.pi-56.5/180*math.pi-t
n=theta-alpha-phi


L3=L1+s1*math.cos(theta)+s2*math.cos(theta-alpha)+s3*math.cos(n)
z=z1+s1*math.sin(theta)+s2*math.sin(theta-alpha)+s3*math.sin(n)
x=L3*math.cos(beta)
y=L3*math.sin(beta)
n=math.degrees(n)

print("x=%.2f  y=%.2f  z=%.2f  n=%.2f" %(x,y,z,n))