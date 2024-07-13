Encoder = {
    'a':'h','b':'i','c':'j',
    'd':'k','e':'l','f':'m',
    'g':'n','h':'o','i':'p',
    'j':'q','k':'r','l':'s','m':'t',
    'n':'u','o':'v','p':'w','q':'x'
    ,'r':'y','s':'z','t':'a','u':'b','v':'c'
    ,'w':'d','x':'e','y':'f','z':'g'
}

UpperEncoder = {k.upper(): v.upper() for k, v in Encoder.items()}


Decoder = {v:k for k,v in Encoder.items()}
UpperDecoder = {v.upper():k.upper() for k,v in Encoder.items()}


def EncodeMessage(Message):
    EncodedMssg = []

    for x in Message:

        if x.isupper():
            EncodedMssg.append(UpperEncoder.get(x))
        elif x.islower():
            EncodedMssg.append(Encoder.get(x))
        else:
            EncodedMssg.append(x)
    return "".join(EncodedMssg)

def DecodeMessage(EncodedMssg):
    DecodedMessage = []

    for x in EncodedMssg:
        if x.isupper():
            DecodedMessage.append(UpperDecoder.get(x))
        elif x.islower():
            DecodedMessage.append(Decoder.get(x))
        else:
            DecodedMessage.append(x)

    return "".join(DecodedMessage)


choice = int(input("Enter choice 0-Exit 1-Encode 2-Decode: "))

while True:
 if choice == 1:
    try:
       name = input("Enter File Name: ")
       file = open(name + ".txt")
       MessageToEncode = "".join([line.strip() for line in file.readlines() if line.strip()])
       
       EncodedMessage = EncodeMessage(MessageToEncode)

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

      DecodedMessage = DecodeMessage(MessageToDecode)
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
     
     



    

