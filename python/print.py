def code():
    print('print something like this: print greg')
    
    lines = []
    
    while True:
        code = input()
        if code.strip() == 'stop':
           break
        lines.append(code)
        
    full_code = "\n".join(lines)
       
    if full_code.startswith("print"):
        full_code = full_code.replace('print', '').strip()
        print(full_code)
        
code()