from PIL import Image 
print("Type L for summing circuit using opamp(linear application)")
print("Type NL for schmitt trigger circuit using opamp(nonlinear application)")
n=input("Type of application :")
if(n=="NL"):
   im = Image.open(r"C:/Users/WINDOWS/OneDrive/Desktop/btech elc/sem3/microeelectronics/seminar assignment/opamp/schmitttrigger.PNG")  
  
   im.show() 

   COMERCIAL_RS = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2,
                6.8, 7.5, 8.2, 9.1,
                10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91,
                100, 110, 120, 130, 140, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470, 510, 560, 620,
                680, 750, 820, 910,
                1000, 1100, 1200, 1300, 1400, 1500, 1600, 1800, 2000, 2200, 2400, 2700, 3000, 3300, 3600, 3900, 4300,
                4700, 5100, 5600, 6200, 6800, 7500, 8200, 9100,
                10000, 11000, 12000, 13000, 14000, 15000, 16000, 18000, 20000, 22000, 24000, 27000, 30000, 33000, 36000,
                39000, 43000, 47000, 51000, 56000, 62000, 68000, 75000, 82000, 91000,
                100000, 110000, 120000, 130000, 140000, 150000, 160000, 180000, 200000, 220000, 240000, 270000, 300000,
                330000, 360000, 390000, 430000, 470000, 510000, 560000, 620000, 680000, 750000, 820000, 910000,
                1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1800000, 2000000, 2200000]


   def calculate_schmitt_trigger_resistors(reference_voltage, output_high_voltage, output_low_voltage, comparison_percentage):

    VREF = reference_voltage
    VOUTP = output_high_voltage
    VOUTN = output_low_voltage
    K = comparison_percentage
    A = K*VREF
    c1 = 0.0
    c2 = 0.0

    for i in range(0, len(COMERCIAL_RS)):
        R1 = COMERCIAL_RS[i]
        for j in range(0, len(COMERCIAL_RS)):
            R2 = COMERCIAL_RS[j]
            for k in range(0, len(COMERCIAL_RS)):
                R3 = COMERCIAL_RS[k]

                if output_low_voltage == 0:
                    c1 = (R3 * (K - 1) / R1) + (K * R3 / R2) + K

                    c2 = (R2*R3)/(R1*R2+R1*R3+R2*R3)

                    c1_max = 1.05 * round(VOUTP/VREF, 3)
                    c1_min = 0.95 * round(VOUTP/VREF, 3)
                    c2_max = 1.05 * round(c2, 3)
                    c2_min = 0.95 * round(c2, 3)
                    if (c1_min <= c1 <= c1_max) and (c2_min <= c2 <= c2_max) and (0.98 <= (K+c2) <= 1):
                        return R1, R2, R3

                elif output_low_voltage < 0:
                    c1 = (R3 * (K - 1) / R1) + (K * R3 / R2) + K

                    c2 = -c1

                    c1_max = 1.05 * round(VOUTP/VREF, 3)
                    c1_min = 0.95 * round(VOUTP/VREF, 3)
                    c2_max = 1.05 * round(VOUTN/VREF, 3)
                    c2_min = 0.95 * round(VOUTN/VREF, 3)
                    if (c1_min <= c1 <= c1_max) and (c2_min >= c2 >= c2_max):
                        return R1, R2, R3

                    continue

    return 0, 0, 0

   def  main():

    VREF = float(input("Enter VREF:"))
    VDDP = float(input("Enter VDDP:"))
    VDDN = float(input("Enter VDDN:"))
    PVREF = float(input("Enter PVREF:"))
    [R1, R2, R3] = calculate_schmitt_trigger_resistors(VREF, VDDP, VDDN, PVREF)

    print("Resistance values: ")
    print("R1: " + str(R1))
    print("R2: " + str(R2))
    print("R3: " + str(R3))

   if __name__ == "__main__":
    main()

if(n=="L"):
     t=int(input("Enter the number of voltages to operate :"))
     if(t==3):
             im = Image.open(r"C:/Users/WINDOWS/OneDrive/Desktop/btech elc/sem3/microeelectronics/seminar assignment/opamp/sumofthree.PNG")  
             im.show()
             v1= float(input("Enter V1:"))
             v2= float(input("Enter V2:"))
             v3= float(input("Enter V3:"))
             c1= float(input("Enter c1:"))
             c2= float(input("Enter c2:"))
             c3= float(input("Enter c3:"))
             rf=float(input("Enter the feedback resistance :"))
             r1=rf/c1
             r2=rf/c2
             r3=rf/c3
             print("R1=",r1)
             print("R2=",r2)
             print("R3=",r3)
             v=((v1*(rf/r1))+(v2*(rf/r2))+(v3*(rf/r3)))
             print("output voltage=",v,"v")
                      
     if(t==4):
             im = Image.open(r"C:/Users/WINDOWS/OneDrive/Desktop/btech elc/sem3/microeelectronics/seminar assignment/opamp/sumoffour.PNG")  
             im.show()
             v1= float(input("Enter V1:"))
             v2= float(input("Enter V2:"))
             v3= float(input("Enter V3:"))
             v4= float(input("Enter V4:"))
             c1= float(input("Enter c1:"))
             c2= float(input("Enter c2:"))
             c3= float(input("Enter c3:"))
             c4= float(input("Enter c4:"))
             rf=float(input("Enter the feedback resistance :"))
             r1=rf/c1
             r2=rf/c2
             r3=rf/c3
             r4=rf/c4
             print("R1=",r1)
             print("R2=",r2)
             print("R3=",r3)
             print("R4=",r4)
             v=((v1*(rf/r1))+(v2*(rf/r2))+(v3*(rf/r3))+(v4*(rf/r4)))
             print("output voltage=",v,"v")     
     if(t==5):
             im = Image.open(r"C:/Users/WINDOWS/OneDrive/Desktop/btech elc/sem3/microeelectronics/seminar assignment/opamp/sumoffive.PNG")  
             im.show()
             v1= float(input("Enter V1:"))
             v2= float(input("Enter V2:"))
             v3= float(input("Enter V3:"))
             v4= float(input("Enter V4:"))
             v5= float(input("Enter V5:"))
             c1= float(input("Enter c1:"))
             c2= float(input("Enter c2:"))
             c3= float(input("Enter c3:"))
             c4= float(input("Enter c4:"))
             c5= float(input("Enter c5:"))
             rf=float(input("Enter the feedback resistance :"))
             r1=rf/c1
             r2=rf/c2
             r3=rf/c3
             r4=rf/c4
             r5=rf/c5
             print("R1=",r1)
             print("R2=",r2)
             print("R3=",r3)
             print("R4=",r4)
             print("R5=",r5)
             v=((v1*(rf/r1))+(v2*(rf/r2))+(v3*(rf/r3))+(v4*(rf/r4))+(v5*(rf/r5)))
             print("output voltage=",v,"v")
     if(t<=2 or t>5):
         print("input out of range")
     
             
        
if(n!="L" and n!="NL"):
    print("invalid")
    

    
   






















