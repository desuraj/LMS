
import getpass
from datetime import date
import pickle
#from adminclass import*
#from testadmin import*


################################ Add_Book ##############################################
def Add_Book(self,bdist):
    print("_"*55)
    tempbname = input("\nEnetr Book Name: ")
    self.bname = tempbname.upper()
    self.bauthor = input("Enter Author of Book: ")
    self.bprice = eval(input("Enter Book Price: "))
    self.isbn = int(input("Enter ISBN Number of Book: "))
    tempsarea = input("Enter Subject Area: ")
    self.sarea=tempsarea.upper()
    self.ncopy = int(input("Enter Total Number of Copies: "))
    tempisbn = repr((self.isbn//3))
    self.bcode = tempisbn
    print(f"______Book Code: {self.bcode}")
    bdist[self.bcode]=[self.ncopy,self.bname,self.sarea]
    
    with open("bdist.pkl","wb") as p:
        pickle.dump(bdist,p)
    print("_"*55)
    
    
    
########################################## display book detail ###################################    
def Display_Book(self):
    print("_"*55)
    print(f"\nBook name: {self.bname}\nAuthor: {self.bauthor}\nPrice: {self.bprice}")
    print(f"ISBN Number: {self.sarea}\nSubject Area: {self.sarea}")
    print(f"Book Code: {self.bcode}")
    print("_"*55)

    
    
################################# student Register ###########################################



def Register_Student(self,sdist,ccode="0187"):
    print("_"*55)
    tempsname = input("\nEnter Student name: ")
    self.sname=tempsname.upper()
    while True:
        op = int(input("Enter Branch:\n1 for Computer Science(CS)\n2 for Mechanical Engineering(ME)\n3 for Civil Engineering(CE)\n4 for Electrical Engineering(EE)\n"))
        if op == 1:
            self.sbranch="CS"
            break
        elif op == 2:
            self.sbranch="ME"
            break
        elif op == 3:
            self.sbranch="CE"
            break
        elif op == 4:
            self.sbranch="EE"
            break
        else:
            print("___________Not valid___________\n")
            
    while True:
        tempsya = int(input("Enter Year of Admission: "))
        if tempsya >= 2015and tempsya <= 2019:
            tempsya1 = tempsya
            self.sya=str(tempsya1)
            break
        else:
            print("__________Not valid____________\n")
    self.sroll =input("Enter Class Roll Number: ")
    self.sid = (ccode+self.sbranch+self.sya[-2::]+self.sroll)
    sdist[self.sid]=[self.sname,0]
    with open("sdist.pkl","wb") as p:
        pickle.dump(sdist,p)
    print(f"Student Library ID is: {self.sid}")
    print("_"*55)

    
    
    ##################################### student Display ######################################



def Display_Student(self):
    print("_"*55)
    print(f"Name Mr.{self.sname}\nLibarary ID: {self.sid}\nBranch: {self.sbranch}")
    print("_"*55)
   
    
    ################################# faculty register #####################################

def Register_Faculty(self,fdist,ccode="0187"):
    print("_"*55)
    tempfname = input("Enter Faculty Name: ")
    self.fname = tempfname.upper()
    while True:
        op = int(input("Enter Depatment:\n1 for Computer Science(CS)\n2 for Mechanical Engineering(ME)\n3 for Civil Engineering(CE)\n4 for Electrical Engineering(EE)\n"))
        if op == 1:
            self.fdept="CS"
            break
        elif op == 2:
            self.fdept="ME"
            break
        elif op == 3:
            self.fdept="CE"
            break
        elif op == 4:
            self.fdept="EE"
            break
        else:
            print("___________Not valid___________\n")
    self.fdeptid = input("Enter 4 last digits of Depatment ID: ")
    self.fid = (ccode+self.fdept+self.fdeptid)
    print(f"Faculty Library ID is: {self.fid}")
    fdist[self.fid]=[self.fname,0]
    with open("fdist.pkl","wb") as p:
        pickle.dump(fdist,p)
        
    print("_"*55)
#     print(f"Pro.{self.fname} Library ID is: {self.fid}")
#     print(fdist)
    
    
  
############################## faculty display ############################################

def Display_Faculty(self):
    print("_"*55)
    print(f"Name Pro.{self.fname}")
    print(f"Library ID: {self.fid}")
    print("_"*55)
#     print(f"Faculty with their ID: {self.fdist} ")
    #\nAddress: {self.faddress}\nDOB: {self.fdob}\nAge: {self.fage}")
    #print(f"Phone: {self.fphone}\nDepatment: {self.fdept}\nCurrent Year: {self.fcyear}")
    #print(f"Date of Joining: {self.fdyear}\nGender: {self.fg}\nEmail: {self.femail}")
    

    ############################# Admin LogIn #################################################
    
def Admin_LogIn(self):
    print("_"*55)
    untemp = input("Enter User Name: ")
    temp = getpass.getpass("Enter password: ")
    if temp=="123" and untemp=="123":
        print("Successfully Login")
        return True
    else:
        print("Invalid  Password or UserId")
        
    print("_"*55)

        
        ############################# Day Calculation #####################################        
def DayFine_cal(self):
    print("_"*55)
    ld1=[eval(_) for _ in input("Enter Deadline Date (yy/mm/dd)").split("/")]
    ld2=[eval(_) for _ in input("Enter Returing date (yy/mm/dd)").split("/")]
    n=int(input("Enter Number of Book: "))
    d0 = date(ld1[0],ld1[1],ld1[2])
    d1 = date(ld2[0],ld2[1],ld2[2])
    totaldate = d1 - d0
    tempfine = (totaldate.days*n*1.5)
    print("_"*55)
    print(f"Fine : {tempfine}")
    print("_"*55)
 
    
    ######################################## Student LogIn ######################################
def Student_LogIn(self):
    print("_"*55)
    count=0
    tempid = input("Enter your Library ID MR.  ")
    lid=tempid.upper()
    with open("sdist.pkl","rb") as p:
        objdist=pickle.load(p)
        for _ in objdist:
            if _ == lid:
                count=1
                print(f"\nWell_Come @SISTec Library________ Mr.{objdist[_][0]} ________")
                print("*"*55)
                while True:
                    n = int(input("Enter Option:\n1 To Search Book\n0 For Exit\n"))
                    if n == 1:
                        Search_Book()
                        break
                    elif n == 0:
                        break
                    else:
                        print("__________Not Valid________________")
            elif count == 0:
                print("\nInvalid ID or You are Not Enroll Mr.")
    print("_"*55)
            
                        
############################### Faculty_LogIn start #########################################

def Faculty_LogIn(self):
    print("_"*55)
    count=0
    tempid = input("Enter your Library ID Pro.  ")
    lid=tempid.upper()
    with open("fdist.pkl","rb") as p:
        objdist=pickle.load(p)
        for _ in objdist:
            if _ == lid:
                count=1
                print(f"\nWell_Come @SISTec Library________ Pro.{objdist[_][0]} ________")
                print("*"*55)
                while True:
                    n = int(input("Enter Option:\n1 To Search Book\n0 For Exit\n"))
                    if n == 1:
                        Search_Book()
                        break
                    elif n == 0:
                        break
                    else:
                        print("__________Not Valid________________")
                
            elif count == 0:
                print("\nInvalid ID or You are Not Enroll Pro.")
                
    print("_"*55)
                
 ############################ faculty login end ##################################
    
 ############################ student Book Issue ##############################
def SBook_Issue(self):
    print("_"*55)
    templid=input("Enter Libarary Id: ")
    lid = templid.upper()
    with open("sdist.pkl","rb") as p:
        objdist = pickle.load(p)
        for _ in objdist:
            if _ == lid:
                n = int(input("Enter number of Book want to Issue: "))
                if n <= 4:
                    for _ in range(n):
                        bcode = input("Enter Book Code: ")
                        with open("bdist.pkl","rb") as bp:
                            bd=pickle.load(bp)
                            for _ in bd:
                                if _ == bcode:
                                    for i in bd[_]:
                                        if type(i)==int and i>0:                        
                                            op = input("Enter 1 continue....: ")
                                            if op == "1":
                                                with open("bdist.pkl","wb") as bpw:
                                                    bd[bcode][0]=i-1
                                                    pickle.dump(bd,bpw)
                                                    for _ in objdist:
                                                        if _ == lid:
                                                            for i in objdist[_]:
                                                                if type(i) == int:
                                                                    i+=n
                                                                    with open("sdist.pkl","wb") as pw:
                                                                        objdist[_][1]=i
                                                                        pickle.dump(objdist,pw)                                                          
                                                                        print("Book successfully Issue")
    print("_"*55)
                                                                
##################################### student book Issue End ##################################

################################### Book Remove ##########################################
def Book_Remove(self):
    print("_"*55)
    bcode = input("Enter Book Code: ")
    with open("bdist.pkl","rb") as bp:
        bd=pickle.load(bp)
        for _ in bd:
            if _ == bcode:
                for i in bd[_]:
                    if type(i)==int and i>=0:                        
                        op = input("Enter 1 continue....: ")
                        if op == "1":
                            with open("bdist.pkl","wb") as bpw:
                                bd[bcode][0]=i-1
                                pickle.dump(bd,bpw)
                                print("Book removed")
    print("_"*55)                   
                                
############################# Book Remove End ###############################################
    
################################# book return Start ####################################
def SBook_Return(self):
    print("_"*55)
    templid=input("Enter Libarary Id: ")
    lid = templid.upper()
    with open("sdist.pkl","rb") as p:
        objdist = pickle.load(p)
        for _ in objdist:
            if _ == lid:
                n = int(input("Enter number of Book to Return: "))
                if n <= 4:
                    for _ in range(n):
                        bcode = input("Enter Book Code: ")
                        with open("bdist.pkl","rb") as bp:
                            bd=pickle.load(bp)
                            for _ in bd:
                                if _ == bcode:
                                    for i in bd[_]:
                                        if type(i)==int and i>0:                        
                                            op = input("Enter 1 continue....: ")
                                            if op == "1":
                                                with open("bdist.pkl","wb") as bpw:
                                                    bd[bcode][0]=i+1
                                                    pickle.dump(bd,bpw)
                                                    for _ in objdist:
                                                        if _ == lid:
                                                            for i in objdist[_]:
                                                                if type(i) == int:
                                                                    i-=n
                                                                    with open("sdist.pkl","wb") as pw:
                                                                        objdist[_][1]=i
                                                                        pickle.dump(objdist,pw)
                                                                        print("Book successfully Return")
      
    print("_"*55)


    ######################### student book return end #####################################################       
                                                                            
def FBook_Issue(self):
    print("_"*55)
    templid=input("Enter Libarary Id: ")
    lid = templid.upper()
    with open("fdist.pkl","rb") as p:
        objdist = pickle.load(p)
        for _ in objdist:
            if _ == lid:
                n = int(input("Enter number of Book want to Issue: "))
                if n <= 4:
                    for _ in range(n):
                        bcode = input("Enter Book Code: ")
                        with open("bdist.pkl","rb") as bp:
                            bd=pickle.load(bp)
                            for _ in bd:
                                if _ == bcode:
                                    for i in bd[_]:
                                        if type(i)==int and i>0:                        
                                            op = input("Enter 1 continue....: ")
                                            if op == "1":
                                                with open("bdist.pkl","wb") as bpw:
                                                    bd[bcode][0]=i-1
                                                    pickle.dump(bd,bpw)
                                                    for _ in objdist:
                                                        if _ == lid:
                                                            for i in objdist[_]:
                                                                if type(i) == int:
                                                                    i+=n
                                                                    with open("fdist.pkl","wb") as pw:
                                                                        objdist[_][1]=i
                                                                        pickle.dump(objdist,pw)                                                          
                                                                        print("Book successfully Issue")
                                                                        
    print("_"*55)
                                                                            
                                                                            
                                                                            
################################# faculty book issue end ###############################

def FBook_Return(self):
    print("_"*55)
    templid=input("Enter Libarary Id: ")
    lid = templid.upper()
    with open("fdist.pkl","rb") as p:
        objdist = pickle.load(p)
        for _ in objdist:
            if _ == lid:
                n = int(input("Enter number of Book to Return: "))
                if n <= 2:
                    for _ in range(n):
                        bcode = input("Enter Book Code: ")
                        with open("bdist.pkl","rb") as bp:
                            bd=pickle.load(bp)
                            for _ in bd:
                                if _ == bcode:
                                    for i in bd[_]:
                                        if type(i)==int and i>0:                        
                                            op = input("Enter 1 continue....: ")
                                            if op == "1":
                                                with open("bdist.pkl","wb") as bpw:
                                                    bd[bcode][0]=i+1
                                                    pickle.dump(bd,bpw)
                                                    for _ in objdist:
                                                        if _ == lid:
                                                            for i in objdist[_]:
                                                                if type(i) == int:
                                                                    i-=n
                                                                    with open("fdist.pkl","wb") as pw:
                                                                        objdist[_][1]=i
                                                                        pickle.dump(objdist,pw)
                                                                        print("Book successfully Return")
                                                                        
    print("_"*55)
    
                                                                            
                                                                            
                                                                            
#################### faculty book return end ########################


################# search for the book ##############################

def Search_Book():
    print("_"*55)
    while True:
        op = int(input("Enetr Option: \n1 for Search By Book name\n2 for Search by Area\n0 for Exit\n"))
        if op == 1:
            sbn()
        elif op == 2:
            sba()
            
        elif op == 0:
            break
        else:
            print("________Not Valid___________")
    print("_"*55)
            
def sbn():
    count=0
    tempbname=input("Enter Book Name: ")
    bname=tempbname.upper()
    with open("bdist.pkl","rb") as bp:
        bd=pickle.load(bp)
        for _ in bd:
            for i in bd[_]:
                if i == bname:
                    count=1
                    print(f"{tempbname}_________is Found")
                    break
        if count==0:
            print(f"{tempbname}_________not Found")
                    
    
def sba():
    count=0
    tempsarea=input("Enter Subject Area: ")
    sarea=tempsarea.upper()
    with open("bdist.pkl","rb") as bp:
        bd=pickle.load(bp)
        for _ in bd:
            for i in bd[_]:
                if i == sarea:
                    count=1
                    print(f"Subject Area_______{tempsarea}_________is Found")
                    break
        if count==0:
            print(f"Subject Area_______________{tempsarea}_________not Found")

                                                                            
                                                                            
############################### Search book end #########################################                                                                            
                                           
                                                                            
                                                                        
                                                            
                                                                
    
    
