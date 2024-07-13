

def EncodeMessage(Mssg,Shift):
    EncodedMssg = []
 
    for x in Mssg:
     if x in Alphabet:
         Number = Alphabet.find(x)
         shiftedX = Number + Shift
         if shiftedX > 25:
            shiftedX = shiftedX-25
         EncodedMssg.append(Alphabet[shiftedX])
     elif x in UpperAlphabet:
         Number = UpperAlphabet.find(x)
         shiftedX = Number + Shift
         if shiftedX > 25:
            shiftedX = shiftedX-25
         EncodedMssg.append(UpperAlphabet[shiftedX])
     else:
         EncodedMssg.append(x)
    
    
    return "".join(EncodedMssg)

def DecodeMessage(Mssg,Shift):
    DecodedMssg = []
 
    for x in Mssg:
     if x in Alphabet:
         Number = Alphabet.find(x)
         shiftedX = Number - Shift
         if shiftedX < 0:
            shiftedX=shiftedX+25
         DecodedMssg.append(Alphabet[shiftedX])
     elif x in UpperAlphabet:
         Number = UpperAlphabet.find(x)
         shiftedX = Number - Shift
         if shiftedX<0:
            shiftedX= shiftedX+25
         DecodedMssg.append(UpperAlphabet[shiftedX])
     else:
         DecodedMssg.append(x)
    return "".join(DecodedMssg)
   


Alphabet = "abcdefghijklmnopqrstuvwxyz"
UpperAlphabet = Alphabet.upper()

Shift = int(input("Enter the number of shifts: "))



Mssg = input('Enter any message to be encoded: ')


EncodedMessage = EncodeMessage(Mssg,Shift)

print(f"Encoded Message with {Shift} Shift/s is: {EncodedMessage}")

DecodedMessage = DecodeMessage(EncodedMessage,Shift)
print(f"Decoded Message with {Shift} Shift/s is: {DecodedMessage}")
