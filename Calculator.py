def main():
    a=float(input("num"))
    b=float(input("num"))
    op=input('operator(+,-,*,/):')
    if op=='+':
        res=a+b
    elif op=='-':
        res=a-b
    elif op=='*':
        res=a*b
    elif op=='a/b':
        res=a/b
    else:
        print("invalid operator".format(op))
        return
    print(res)
    return
main()