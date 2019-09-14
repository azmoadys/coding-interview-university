import sys
try:
    f = open('Learned.txt', 'a')
except:
    f = open('Learned.txt','w')
st = ''
for i in sys.argv[1:]:
    if st == '':
        st+=i
        continue
    st += ' '+i
st += '\n'
f.write(st)
f.close()
