#question01-S10.py
import json
import os

class Ticket:
    
    tasks = {101: {"id": 101,"title": "Fix login bug","assignee": "Ali","priority": "HIGH", "status": "OPEN"},102: {"id": 102,"title": "Update API","assignee": "Sara",
                                           "priority": "MEDIUM","status": "IN_PROGRESS"},
                                           103: {"id": 103,"title": "Write tests","assignee": "Ali",
                                                 "priority": "LOW","status": "DONE"}} 
    tickets={}
    priorities = ["high", "medium", "low"]
    status = ["open","in_progress","done"]
 
    def __init__(self):

      if os.path.exists("ticket.json"):
          with open("ticket.json", "r") as file:
              try:
                  Ticket.tickets=json.load(file)
                  Ticket.tickets={int(key):value for key,value in Ticket.tickets.items()}
              except json.JSONDecodeError:
                    Ticket.tickets = {key: value.copy()for key, value in Ticket.tasks.items()}
                    self.save()
      else:
           Ticket.tickets={key:value.copy() for key,value in Ticket.tasks.items()}
           self.save()
           
    def save(self):
       with open ("ticket.json","w") as file:
           json.dump(Ticket.tickets, file, indent=4)
    
    
    def create(self):
       
       self.id = max(Ticket.tickets.keys(),default=100)+1
       self.title =input('enter your title:')
       
       self.issue=input("Issue type: software,hardware ? :").strip().lower()
       
       if self.issue == "software":
           self.assignee = "Ali"
       elif self.issue == "hardware":
               self.assignee= "Sara"
       else:
            print('invalid issue type!')
            return
        
       self.priority=input('priority: High/Medium/Low:  ').strip().lower()
       if self.priority not in Ticket.priorities:
           print('Invalid Priority')
           return
        
       self.status=input('status: ').strip().lower()
       if self.status not in Ticket.status:
           print('invalid status')
           return
 
       self.info = {"id":self.id,"title": self.title,"issue": self.issue,"assignee": self.assignee,"priority": self.priority,"status": self.status}
       Ticket.tickets[self.id] = self.info
       self.save()
       
       print('Ticket created successfully')
 

    def read(self):
        r = input('Read one ID or all?  ')
        if r == "one id":
           ID = int(input('Enter ID: '))
           if ID in Ticket.tickets:
               print(Ticket.tickets[ID])
           else:
               print('ID not found')

        elif r == "all":
            with open("ticket.json", "r") as file:
                f = json.load(file)
                print(f)

        else:
            print('Invalid choice')
            
    def edit(self):
        try:
            ID = int(input('enter your ID: '))
        except ValueError:
           print('ID must be a number')
           return

        if ID not in Ticket.tickets:
            print('ID not found')
            return

        print(Ticket.tickets[ID])
        
        while True:
            edit=input('what to change? title/issue/priority: ').strip().lower()
            
            if edit == "":
                print("input can not be empty!")
                continue
            if edit not in ["title", "issue", "priority", "status"]:
                print('invalid request')
                continue
            break
                            
         
        if edit == "title":
            new_title = input('enetr new title : ').strip().lower()
            Ticket.tickets[ID]["title"]=new_title
            self.save()
            print('title changed')
        elif edit == "issue":
            new_issue = input('enetr new issue : ').strip().lower()
            Ticket.tickets[ID]["issue"]=new_issue
            self.save()
            print('new-issue changed')
        elif edit == "priority":
            new_priority = input('enetr new priority : ').strip().lower()
            Ticket.tickets[ID]["priority"]=new_priority
            self.save()
            print('priority changed')
      
        else:
            print('invalid request')
            return
    def change_status(self):
        try:
           ID = int(input('enetr ID : '))
        except ValueError:
            print('ID must be a number')
            return
        if ID not in Ticket.tickets:
            print('ID not found')
            return
        old_status = Ticket.tickets[ID]["status"].lower()
        new_status = input('enetr new status: ') 
        if new_status not in Ticket.status:
            print('Invalid status')
            return
        if old_status == "open" and new_status == "in_progress":
            Ticket.tickets[ID]["status"]=new_status

        elif old_status == "in_progress" and new_status == "done":
            Ticket.tickets[ID]["status"]=new_status

        else:
            print('not allowed')
            return
        self.save()
        print("Status changed successfully")


    def delet(self):
        
     try:
         ID = int(input('enter your ID: '))
     except ValueError:
         print('ID must be number')
         return
     
     
     if ID in Ticket.tickets:
         print(Ticket.tickets[ID])
     
         if Ticket.tickets[ID]["status"] in ["open","in_progress"]:
             confirm=input('This ticket is in progress or open, delet? yes|no ').strip().lower()
             
             if confirm =="yes":
                 del Ticket.tickets[ID]
                 self.save()
                 print('Deleted')
             else:
              
              print("deletion canceled")
              return
          
         elif Ticket.tickets[ID]["status"] == "done":
              
              print('Not allowed')
              return
         else:
              print('ID not found')
              return
          
    def search(self):
        filt = input('Search by assignee,priority, status')
        
        if filt in ["assignee","priority", "status"]:
            
         value = input(f'Enter {filt}: ').strip().lower()

        for ticket in Ticket.tickets.values():
            if ticket.get(filt, '').lower() == value:
                print(ticket)

        
            elif filt not in ["assignee","priority", "status"]:
                print( 'filter not found')
                return
            
    def report(self):
         print("Final Report: \n---------------------")
         total_tickets = len(Ticket.tickets)
         print(f'Total tickets: {total_tickets}')
         open_tickets = 0
         closed_tickets=0
         for ticket in Ticket.tickets.values():
             if ticket["status"].lower() == "open":
                 open_tickets+=1 
             elif ticket["status"].lower() == "done":
                 closed_tickets+=1
         print(f'Open tickets: {open_tickets}')
         print(f'Closed tickets : {closed_tickets}')
         self.save()
             
    def assignee(self):
        sara=0
        ali=0
        
        for i in Ticket.tickets.values():
            
            if i["assignee"].lower()=="sara":
                sara+=1
            elif i["assignee"].lower()=="ali":
                ali+=1    
        print(f'assignee tickets : Sara --> {sara},\n Ali --> {ali}')
        self.save()

             
while True :
   question = input('create / read / edit / change_status / delet / search /report/  assignee /exit : ')        
   if question == "exit":
       break
   
   elif question =="create":
        ticket1 =Ticket()
        ticket1.create()
    
   elif question == "read":
        ticket2=Ticket()
        ticket2.read()
    
   elif question == "edit":
        ticket3=Ticket()
        ticket3.edit()
        
   elif question == "change_status":
       ticket4 = Ticket()
       ticket4.change_status()
        
   elif question == "delet":
        ticket5=Ticket()
        ticket5.delet()
        
   elif question == "search":
       ticket6=Ticket()
       ticket6.search() 
       
   elif question == "report":
       ticket7=Ticket()
       ticket7.report()
       
   elif question == "assignee":
       ticket8=Ticket()
       ticket8.assignee()
      
   else:
       print("Invalid input")