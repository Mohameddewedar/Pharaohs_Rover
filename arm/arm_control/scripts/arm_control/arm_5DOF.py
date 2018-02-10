#!/usr/bin/env python
import math
import rospy

class arm():
    def __init__(self):
        self.s1 = 500
        self.s2 = 350
        self.s3 = 330
        self.s4 = 376
        self.s5 = 301
        self.s6 = 61.2
        self.s7 = 60.8
        self.s8 = 89
        self.s9 = 58
        self.s10 = 215.6
        self.s11 = 71
        self.s12 = 95
        self.s13 = 70
        self.s14 = 77.4
        self.L1 = 90
        self.z1 = 35
        self.d1 =436
        self.d2 =334
        self.d3 =243
        self.beta=0
        self.x = 532  # Units in Millimeters
        self.y = 0  # Units in Millimeters
        self.z = 482  # Units in Millimeters
        self.n = 0 
        
    def update_inverse(self):
        l = math.pow(self.x,2)+math.pow(self.y,2)
        self.beta = math.atan2(self.y, self.x) #base angles
        l3 = l-self.s3*math.cos(self.n)
        z3 = self.z-self.s3*math.sin(self.n)
        dl = l3-self.L1
        dz = z3-self.z1
        f = math.sqrt(math.pow(dl,2)+math.pow(dz,2))
        q1 = math.atan2(dz,dl)
        q2 = math.acos((math.pow(self.s1,2)+math.pow(f,2)-math.pow(self.s2,2))/(2*self.s1*f))
        theta = 90-q1-q2
        m = math.acos((math.pow(self.s1,2)+math.pow(self.s2,2)-math.pow(f,2))/(2*self.s1*self.s2))
        alpha = 90-m
        dr = math.atan2((60-35),210)
        r = math.pi-theta-dr
        dl4 = math.sqrt(math.pow((60-35),2)+math.pow(210,2))
        self.d1 = math.sqrt(math.pow(dl4,2)+math.pow(self.s4,2)-2*dl4*self.s4*math.cos(r)) #linear_1
        dm = math.sqrt(math.pow(self.s6,2)+math.pow(self.s7,2)-2*self.s6*self.s7*math.cos(m))
        a = math.acos((math.pow(self.s6,2)+math.pow(dm,2)-math.pow(self.s7,2))/(2*self.s6*dm))
        b = math.acos((math.pow(dm,2)+math.pow(self.s8,2)-math.pow(self.s9,2))/(2*dm*self.s8))
        c = math.pi-a-b
        self.d2 = math.sqrt(math.pow(self.s5,2)+math.pow(self.s8,2)-2*self.s5*self.s8*math.cos(c)) #linear_2
        phi = theta-alpha-self.n
        t = math.pi-phi-(56.6*math.pi)/180
        dt = math.sqrt(math.pow(self.s11,2)+math.pow(self.s14,2)-2*self.s11*self.s14*math.cos(t))
        e = math.acos((math.pow(self.s11,2)+math.pow(dt,2)-math.pow(self.s14,2))/(2*self.s11*dt))
        f = math.acos((math.pow(dt,2)+math.pow(self.s12,2)-math.pow(self.s13,2))/(2*dt*self.s12))
        g = math.pi-e-f
        self.d3 = math.sqrt(math.pow(self.s10,2)+math.pow(self.s12,2)-2*self.s10*self.s12*math.cos(g)) #linear_3

    def update_forward(self):
        pass


    def valid_linears(self):
        pass


    def calculate_forward(self):
        dL4=math.sqrt(25*25+210*210)
        dr=math.atan(25/210)
        r=math.acos((dL4*dL4+self.s4*self.s4-self.d1*self.d1)/(2*dL4*self.s4))
        theta=r+dr-math.pi/2
        c=math.acos((self.s5*self.s5+self.s8*self.s8-self.d2*self.d2)/(2*self.s5*self.s8))
        q=math.pi-c
        dq=math.sqrt(self.s8*self.s8+self.s6*self.s6-2*self.s8*self.s6*math.cos(q))
        a=math.acos((dq*dq+self.s8*self.s8-self.s6*self.s6)/(2*dq*self.s8))
        b=math.acos((dq*dq+self.s9*self.s9-self.s7*self.s7)/(2*dq*self.s9))
        dm=math.sqrt(self.s8*self.s8+self.s9*self.s9-2*self.s8*self.s9*math.cos(a+b))
        m=math.acos((self.s6*self.s6+self.s7*self.s7-dm*dm)/(2*self.s6*self.s7))
        alpha=math.pi/2-m
        G=math.acos((self.s10*self.s10+self.s12*self.s12-self.d3*self.d3)/(2*self.s10*self.s12))
        dg=math.pi-G
        dg1=math.sqrt(self.s11*self.s11+self.s12*self.s12-2*self.s11*self.s12*math.cos(dg))
        e=math.acos((self.s11*self.s11+dg1*dg1-self.s12*self.s12)/(2*dg1*self.s14))
        f=math.acos((dg1*dg1+self.s14*self.s14-self.s13*self.s13)/(2*dg1*self.s14))
        t=e+f
        phi=math.pi-56.5/180*math.pi-t
        n=theta+alpha-phi


        L2=self.L1+self.s1*math.sin(theta)
        L3=L2+self.s2*math.sin(theta+alpha+90)
        z2=self.z1+self.s1*math.cos(theta)
        z=z2+self.s2*math.cos(theta+alpha+90)
        x=(L3+self.s3*math.cos(n))*math.cos(self.beta)
        y=(L3+self.s3*math.cos(n))*math.sin(self.beta)

    