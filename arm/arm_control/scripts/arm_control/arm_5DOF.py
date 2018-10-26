#!/usr/bin/env python
import math
import rospy

class arm():
    def __init__(self):
        self.s1 = 500.0
        self.s2 = 350.0
        self.s3 = 330.0
        self.s4 = 376.0
        self.s5 = 301.0
        self.s6 = 61.2
        self.s7 = 61.0
        self.s8 = 89.0
        self.s9 = 58.0
        self.s10 = 216.0
        self.s11 = 71.0
        self.s12 = 95.0
        self.s13 = 70.0
        self.s14 = 77.5
        self.L1 = 90.0
        self.z1 = 35.0
        self.d1 =436.0
        self.d2 =334.0
        self.d3 =243.0
        self.beta=0.0
        self.x = 868.53  # Units in Millimeters
        self.y = 0.0# Units in Millimeters
        self.z = 416.59  # Units in Millimeters
        self.n = -16.8 #Units in Degrees
        self.gripper=0
        self.twist=0
        self.new_link=90
        
    def update_inverse(self):   
        z3=self.z
        n=math.radians(self.n)
        L3=math.sqrt(self.x*self.x+self.y*self.y)
        self.beta=math.atan2(self.y,self.x)
        L2=L3-self.s3*math.cos(n)
        z2=z3-self.s3*math.sin(n)
        dL=L2-self.L1
        dz=z2-self.z1
        F=math.sqrt(dL*dL+dz*dz)
        q1=math.atan2(dz,dL)
        if F >=780:
            theta=q1
            alpha=0
            m=math.pi
        else:
            q2=math.acos((self.s1*self.s1+F*F-self.s2*self.s2)/(2.0*self.s1*F))
            m=math.acos((self.s1*self.s1+self.s2*self.s2-F*F)/(2.0*self.s1*self.s2))
            alpha=math.pi-abs(m)
            theta=q1+q2
        dr=math.atan(25.0/210.0)
        r=math.pi-dr-theta
        dL4=math.sqrt(25*25.0+210.0*210)

        # if(self.d1 >= 420 and self.d1 <= 580):
        self.d1=math.sqrt(dL4*dL4+self.s4*self.s4-2.0*dL4*self.s4*math.cos(r)) #linear 1 length

        dm=math.sqrt(self.s6*self.s6+self.s7*self.s7-2.0*self.s6*self.s7*math.cos(m))
        a=math.acos((self.s6*self.s6+dm*dm-self.s7*self.s7)/(2.0*self.s6*dm))
        b=math.acos((dm*dm+self.s8*self.s8-self.s9*self.s9)/(2.0*self.s8*dm))
        c=math.pi-a-b

        # if self.d2 > 330 and self.d2 < 400:
        self.d2=math.sqrt(self.s5*self.s5+self.s8*self.s8-2.0*self.s5*self.s8*math.cos(c)) #linear 2 length

        phi=theta-alpha-n
        t=math.pi-phi-56.0/180.0*math.pi
        dt=math.sqrt(self.s11*self.s11+self.s14*self.s14-2.0*self.s11*self.s14*math.cos(t))
        e=math.acos((dt*dt+self.s11*self.s11-self.s14*self.s14)/(2.0*dt*self.s11))
        f=math.acos((dt*dt+self.s12*self.s12-self.s13*self.s13)/(2.0*dt*self.s12))
        g=math.pi-e-f
        # if(self.d3 > 260 and self.d3 < 300):
        self.d3=math.sqrt(self.s10*self.s10+self.s12*self.s12-2.0*self.s10*self.s12*math.cos(g))  #linear 3 length
 
    def valid_linears(self):
        pass

    def initialize(self):
        self.d1 = 451
        self.d2 = 334
        self.d3 = 270
        self.beta = 0
        self.new_link = 90

    def calculate_forward(self):
        dL4=math.sqrt(25*25.0+210.0*210)
        dr=math.atan2(25.0,210.0)
        r=math.acos((dL4*dL4+self.s4*self.s4-self.d1*self.d1)/(2.0*dL4*self.s4))
        theta=r+dr-math.pi/2
        c=math.acos((self.s5*self.s5+self.s8*self.s8-self.d2*self.d2)/(2.0*self.s5*self.s8))
        q=math.pi-c
        dq=math.sqrt(self.s8*self.s8+self.s6*self.s6-2.0*self.s8*self.s6*math.cos(q))
        a=math.acos((dq*dq+self.s8*self.s8-self.s6*self.s6)/(2.0*dq*self.s8))
        b=math.acos((dq*dq+self.s9*self.s9-self.s7*self.s7)/(2.0*dq*self.s9))
        dm=math.sqrt(self.s8*self.s8+self.s9*self.s9-2*self.s8*self.s9*math.cos(a+b))
        m=math.acos((self.s6*self.s6+self.s7*self.s7-dm*dm)/(2.0*self.s6*self.s7))
        alpha=math.pi/2.0-m
        G=math.acos((self.s10*self.s10+self.s12*self.s12-self.d3*self.d3)/(2.0*self.s10*self.s12))
        dg=math.pi-G
        dg1=math.sqrt(self.s11*self.s11+self.s12*self.s12-2.0*self.s11*self.s12*math.cos(dg))
        e=math.acos((self.s11*self.s11+dg1*dg1-self.s12*self.s12)/(2.0*dg1*self.s14))
        f=math.acos((dg1*dg1+self.s14*self.s14-self.s13*self.s13)/(2.0*dg1*self.s14))
        t=e+f
        phi=math.pi-56.5/180*math.pi-t
        n=theta+alpha-phi

        L2=self.L1+self.s1*math.sin(theta)
        L3=L2+self.s2*math.sin(theta+alpha+90)
        z2=self.z1+self.s1*math.cos(theta)
        self.x=(L3+self.s3*math.cos(n))*math.cos(self.beta)
        self.y=(L3+self.s3*math.cos(n))*math.sin(self.beta)
        self.z=z2+self.s2*math.cos(theta+alpha+90)

    