# Lab 10
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
print(modifytxt)
print(len(modifytxt))
txt ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
print(txt)
print(len(txt))

print (txt[0:24])
print (txt[25:54])
print (txt[55:89])
print (txt[90:110])

## Result
As it appears

## reasons
- Automated processes are quicker and more efficient
- Ensures all steps are followed according to the system
- Tracking shows exactly where the request is at any stage.

Higher operational efficiency,Reduced time,Reduces the likelihood of error,Better collaborative working 

- Manual processes take longer to complete
- Tracking requests in manual processes is either impossible or requires additional things
- Manual Process may cause errors because depends on each person's ability.

Time-consuming,Inaccurate data