



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

MessageToEncode= input('Enter any message to be encoded: ')


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

EncodedMessage = EncodeMessage(MessageToEncode)
DecodedMessage = DecodeMessage(EncodedMessage)


print('Encoded Mssg: ', EncodedMessage)
print('Decoded Mssg: ', DecodedMessage)
