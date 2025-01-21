def postfix(s):
    operator = ['+','-','%','*','/']
    st = []
    if s == '':
        return False
    for i in s:
        if i not in operator:
            st.append(i)
        else:
            val1 = st.pop()
            val2 = st.pop()
            
            st.append(str(eval(val1 + i + val2)))
    return st
a='231*+9-'
# a = ''
print(postfix(a)[0])