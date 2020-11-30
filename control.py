from PIL import Image
print("Enter LM741 for LM741 OpAmp")
print("Enter AD3554SM for AD3554SM OpAmp")
print("Enter AD3280A for AD3280A OpAmp")
print("Enter TL022CD for TL022CD OpAmp")
print("Enter TL031ACP for TL031ACP OpAmp")
print("Enter TLC254CN for TLC254CN OpAmp")
print("Enter OPA111BM for OPA111BM OpAmp")
n=input("Enter the operational amplifier model number : ")
if n=="LM741":
    im = Image.open(r"F:/btech elc/sem3/microeelectronics/seminar assignment/opamp/LM741.PNG")  
    im.show()
    import LM741
if n=="AD3554SM":
    im = Image.open(r"F:/btech elc/sem3/microeelectronics/seminar assignment/opamp/AD3554SM.PNG")  
    im.show()
    import AD3554SM
if n=="AD3280A":
    im = Image.open(r"F:/btech elc/sem3/microeelectronics/seminar assignment/opamp/AD3280.PNG")  
    im.show()
    import AD3280A
if n=="TL022CD":
    im = Image.open(r"F:/btech elc/sem3/microeelectronics/seminar assignment/opamp/TL022CD.PNG")  
    im.show()
    import TL022CD 
if n=="TL031ACP":
    im = Image.open(r"F:/btech elc/sem3/microeelectronics/seminar assignment/opamp/TL031ACP.PNG")  
    im.show() 
    import TL031ACP
if n=="TLC254CN":
    im = Image.open(r"F:/btech elc/sem3/microeelectronics/seminar assignment/opamp/TLC254CN.PNG")  
    im.show()
    import TLC254CN
if n=="OPA111BM":
    im = Image.open(r"F:/btech elc/sem3/microeelectronics/seminar assignment/opamp/OPA111BM.PNG")  
    im.show()
    import OPA111BM

    

