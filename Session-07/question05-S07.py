#question05-S07
def operation_analysis():
    logs = [("Ali", "LOGIN", 200),("Ali", "DOWNLOAD", 200),\
            ("Sara", "LOGIN", 403),("Reza", "LOGIN", 200),\
                ("Sara", "LOGIN", 403),("Sara", "LOGIN", 403)]
        
                
    names = set([i[0] for i in logs])
    result={}
    

    for name in names:
        log=0
        log1=0
        for i in logs:
            if i[0]==name and i[1]=="LOGIN" and i[2]==200:
                log+=1
            if i[0]==name and i[1]=="LOGIN" and i[2]==403:
                log1+=1

        result[name]=(log,log1)
    return logs,names,result 
   
    
def final_report():
    logs, names, result = operation_analysis()
    print("___________final report_______________")

    print(f'Successful login: {[(name,value[0]) for name,value in result.items() if value[0]>0]}')
    print(f'UnSuccessful login: {[(name,value[1]) for name,value in result.items() if value[1]>0]}')
    
    for name, value in result.items():
        if value[1]>=3:
         print(f'Suspicious login: {name}')
    
    for name in names:
        op=0
        for i in logs:
           if i[0]== name:
               op+=1
        print(f"# of operations: {name, op}")

        

        
operation_analysis()        
final_report()         
                            

                    
                