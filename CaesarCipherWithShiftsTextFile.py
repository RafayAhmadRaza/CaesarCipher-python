Alphabet = "abcdefghijklmnopqrstuvwxyz"
UpperAlphabet = Alphabet.upper()


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
   



choice = int(input("Enter choice 0-Exit 1-Encode 2-Decode: "))
Shift = int(input("Enter the number of shifts: "))

while True:
 if choice == 1:
    try:
       name = input("Enter File Name: ")
       file = open(name + ".txt")
       MessageToEncode = "".join([line.strip() for line in file.readlines() if line.strip()])
       
       EncodedMessage = EncodeMessage(MessageToEncode,Shift)

       Name = file.name



       f  = open(Name[:-4] +'EncodedMessage.txt','w')
       f.write(EncodedMessage)
       f.close()
       break
    except:
       print('File could not be opened')
       break
 elif choice == 2:
     try:
      name = input("Enter File Name: ")
      file = open(name + "EncodedMessage.txt")
      MessageToDecode = "".join([line.strip() for line in file.readlines() if line.strip()])

      DecodedMessage = DecodeMessage(MessageToDecode,Shift)
      Name = file.name
      Name = "".join(Name.split("EncodedMessage.txt"))
      print(Name)

      f  = open(Name + 'DecodedMessage.txt','w')
      f.write(DecodedMessage)
      f.close()
      break
     except:
        print('File could not be opened')
        MessageToDecode=""
        break
 elif choice == 0:
    break
 else:
    choice = int(input("Invalid Choice re enter:"))