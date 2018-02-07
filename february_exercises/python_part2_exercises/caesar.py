encr_mess = "lbh zhfg hayrnea jung lbh unir yrnearq"
encr_mess_xspace = encr_mess.replace(" ", "")
###convert message to a list of characters
encr_list = []
for i in range(0, len(encr_mess_xspace)):
  encr_list.append(encr_mess_xspace[i])
#convert each text item in list to AD=SCII code
asc_conv = []
for j in range(0, len(encr_list)):
    asc_conv.append(ord(encr_list[j]))
print(asc_conv)
#subtract 13 from each ascii letter to get deciphered ascii of text
deci_asc = []
for k in range(0, len(asc_conv)):
  deci_asc.append(asc_conv[k] - 13)
    
print(deci_asc)

#now convert it back to characters 
deciph = []
for l in range(0, len(deci_asc)):
  deciph.append(chr(deci_asc[l]))
print(deciph)