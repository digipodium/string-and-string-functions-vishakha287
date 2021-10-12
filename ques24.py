text='%p34@y!*-*!t68h#&on404'
x=['%','@','!','*','#','-','&','1','2','3','4','5','6','7','8','9','0']
l=len(text)
new=''
for i in range(l):
    if text[i] not in x :
        new=new+text[i]
print(new)