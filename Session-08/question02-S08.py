#question02-S08
logs_text = "C:/Users/Asus/Documents/Programming/Programming/Py Fanavari/Session-08/logs.txt"

with open (logs_text,'r') as logs:
     log = logs.readlines()
     
     
def count_successful_logins():
    successful_login=0

    for line in log:

        name, log_dl, code = line.strip().split(",")
        if log_dl == "LOGIN" and code=="200":
            successful_login+=1

    return successful_login


def count_failed_login():
    failed_login=0

    for line in log:
        name, log_dl, code = line.strip().split(",")
        if log_dl=="LOGIN" and (code=="403"or code=="500"):
            failed_login+=1
            
    return failed_login
    
    
def find_suspicious_users():
    d ={}
    for  i in log:
        i = i.strip()
        name ,log_dl, code = i.split(",")
        
        if code =="403":
            if name in d:
                d[name]+=1
            else:
                d[name]=1
    return d
   
def user_operation():
    op = {}
    for i in log:
        i = i.strip()
        name,log_dl, code = i.split(',')
        if name in op :
            op[name]+=1
        else:
            op[name]=1
    return op           
      

    
def generate_report():
    successful_login = count_successful_logins()
    failed_login = count_failed_login()
    d = find_suspicious_users()
    op = user_operation()
    
    print('Generating report \n---------------------')
    
    print(f'Successful login: {successful_login}')
    print(f'Failed login: {failed_login}')
    print(f'Suspicious User: {d} Unsuccessful login')
    print(f'Number of user operations: {op}')



count_successful_logins()
count_failed_login()
find_suspicious_users()
user_operation()
generate_report()
    
    
    