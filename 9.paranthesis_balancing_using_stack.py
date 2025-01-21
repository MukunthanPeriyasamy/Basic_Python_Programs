def paranthesis_balancing(s):
    if len(s) %2!=0:
        return False
    if s == "":
        return False
    st = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            st.append(s[i])
        else:
            if st and ((st[-1] == '(' and s[i] == ')') or (st[-1] == '{' and s[i] == '}') or (st[-1] == '[' and s[i] == ']')):
                st.pop()
            else:
                return False
    return  not st

s =  " "
if paranthesis_balancing(s):
    print(True)
else:
    print(False)
    