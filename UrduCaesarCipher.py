

def EncodeMessage(Mssg,Shift):
    EncodedMssg = []
 
    for x in Mssg:
     if x in urdu_characters_string:
         Number = urdu_characters_string.find(x)
         shiftedX = Number + Shift
         if shiftedX > 42:
            shiftedX = shiftedX-42
         EncodedMssg.append(urdu_characters_string[shiftedX])
     else:
         EncodedMssg.append(x)
    
    
    return "".join(EncodedMssg)

def DecodeMessage(Mssg,Shift):
    DecodedMssg = []
 
    for x in Mssg:
     if x in urdu_characters_string:
         Number = urdu_characters_string.find(x)
         shiftedX = Number - Shift
         if shiftedX < 0:
            shiftedX=shiftedX+42
         DecodedMssg.append(urdu_characters_string[shiftedX])
   
     else:
         DecodedMssg.append(x)
    return "".join(DecodedMssg)
   

urdu_characters = [
    'آ', 'ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ڈ', 'ذ', 'ر', 'ڑ',
    'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م',
    'ن', 'ں', 'و', 'ؤ', 'ہ', 'ہ', 'ہ', 'ہ', 'ء', 'ی', 'ے',
]

urdu_characters_string = ''.join(urdu_characters)

Shift = int(input("Enter the number of shifts: "))



Mssg = input('Enter any message to be encoded: ')


EncodedMessage = EncodeMessage(Mssg,Shift)

print(f"Encoded Message with {Shift} Shift/s is: {EncodedMessage}")

DecodedMessage = DecodeMessage(EncodedMessage,Shift)
print(f"Decoded Message with {Shift} Shift/s is: {DecodedMessage}")


