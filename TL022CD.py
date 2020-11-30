import math
from PIL import Image 
print("TL022CD Operational Amplifier")
print("Function : Dual Low-Power General-Purpose Operational Amplifier")
print("Type I for Inverting configuration")
print("type NI for non Inverting configuration")
n=input("Enter the configuration of OPAMP :")
if n=="I": 
    im = Image.open(r"C:/Users/WINDOWS/OneDrive/Desktop/btech elc/sem3/microeelectronics/seminar assignment/opamp/invertingopamp.png")  
    im.show()
    p1=float(input("Enter the power supply voltage 1 in volt :"))
    p2=float(input("Enter the power supply voltage 2 in volt :"))
    rf=float(input("Enter the feedback resistance in ohms :"))
    rin=float(input("Enter the input resistance in ohms :"))
    vin=float(input("Enter the input voltage in volt:"))
    Ib1=float(input("Enter the input biasing current 1 in ampere :"))
    Ib2=float(input("Enter the input biasing current 2 in ampere :"))
    bandwidth = 0.5*pow(10,6)
    gain = -(rf/rin)
    vout=gain * vin
    decibelgain = math.log(abs(gain),10)
    bandwidthproduct=abs(gain) * bandwidth
    slewrate=0.5
    offsetvoltage=0.005
    power=(vout-vin)*rin
    CMRR=(vin/vout)*(rin/(rin+rf))
    offsetcurrent=abs(Ib2 - Ib1)
if n=="NI":
    im = Image.open(r"C:/Users/WINDOWS/OneDrive/Desktop/btech elc/sem3/microeelectronics/seminar assignment/opamp/noninvertopamp.png")  
    im.show()
    p1=float(input("Enter the power supply voltage 1 in volt :"))
    p2=float(input("Enter the power supply voltage 2 in volt :"))
    rf=float(input("Enter the feedback resistance in ohms :"))
    rin=float(input("Enter the input resistance in ohms :"))
    vin=float(input("Enter the input voltage in volt:"))
    Ib1=float(input("Enter the input biasing current 1 in ampere :"))
    Ib2=float(input("Enter the input biasing current 2 in ampere :"))
    bandwidth = 0.5*pow(10,6)
    gain = 1 + (rf/rin)
    vout=gain * vin
    decibelgain = math.log(abs(gain),10)
    bandwidthproduct=abs(gain) * bandwidth
    slewrate=0.5
    offsetvoltage=0.005
    power=(vout-vin)*rin
    CMRR=(vin/vout)*(rin/(rin+rf))
    offsetcurrent=abs(Ib2 - Ib1)
print("Bandwidth of the operational amplifier :",bandwidth,"hertz")
print("Gain of the operational amplifier :",gain)
print("output voltage  of the operational amplifier :",vout,"volt")
print("Decibel gain of the operational amplifier :",decibelgain,"db")
print("Bandwidth product of the operational amplifier :",bandwidthproduct)
print("Slew Rate of the operational amplifier :",slewrate,"v/microsec")
print("Input Offset Voltage of the operational amplifier :",offsetvoltage)
print("power consumed :",power,"watts")
print("Common mode rejection ratio of the operational amplifier :",CMRR)
print("offset current :",offsetcurrent,"Ampere")
