originalTxt = "ORIGIN 1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed 61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"
reword = "ORIGIN"

def remove(input_string, x,n):
    input_string=input_string.replace(x,'',n)
    return input_string

modifytxt=remove(originalTxt,reword,1)
print(modifytxt)

reword = "1"
modifytxt=remove(modifytxt,reword,1)
print(modifytxt)

reword = "61"
modifytxt=remove(modifytxt,reword,1)
print(modifytxt)

reword = " "
modifytxt=remove(modifytxt,reword,len(modifytxt))

print("Text its clean aoutomaticlly")
print("-----------------------------------------------------------------")
print(modifytxt)
print(len(modifytxt))
print("Text its clean manually")
print("-----------------------------------------------------------------")
txt ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
print(txt)
print(len(txt))

print (txt[0:24])
print (txt[25:54])
print (txt[55:89])
print (txt[90:110])