import pickle
from function import* 

###############################################################################

###################################################################



class Admin:
    sdist={}
    fdist={}
    bdist={}
#     def Main(self):                 ############## Admin Menu ###################
#         main(self)
    
    
    
    def getbook(self):                 ############ book reg. #################
        Add_Book(self,Admin.bdist)
        
    def showbook(self):               ############### book detail ##########
        Display_Book(self)
        
    
    def getstudent(self):             ############### student reg. ################
        Register_Student(self,Admin.sdist)
        
    def showstudent(self):            ############### student detail #############
        Display_Student(self)
        
       
    def getfaculty(self):             ############## faculty reg. ###############
        Register_Faculty(self,Admin.fdist)
        
        
    def showfaculty(self):            ############# faculty detail ############
        Display_Faculty(self)
    
    def adminlogin(self):          ############## Admin login ##############
        if Admin_LogIn(self):
            main()
        
        
    def sbookissue(self):         ############## Book Issue #################
        SBook_Issue(self)
        
    def bookremove(self):         ################ book remove ##################
        Book_Remove(self)
        
    def sbookreturn(self):         ################# student book return ###############
        SBook_Return(self)
        
    def fbookissue(self):         ##################### faculty book issue ##############
         FBook_Issue(self)
            
    def fbookreturn(self):       ######################## faculty book return ###########
        FBook_Return(self)
    
    def dayfine(self):         #################### fine cal ######################
        DayFine_cal(self)
################################################################################################



#from adminclass import*
#import pickle
# from studentclass import*
# from facultyclass import*
        
########################## BOOK regs. start ##########################################        

def br():
    l=[]
    n=int(input("Enter No of Book to Add: "))
    for _ in range(n):
        print("\n_______________________________________________")
        print(f"Enter Detail for Book: {_+1}")
        l.append(Admin())
        l[_].getbook()
    with open("bookdetail.pkl","wb") as fp:
        for _ in l:
            pickle.dump(_,fp)
    print("\nTHANK YOU_!!!!\nBooks Are Added Successfully")

######################## BOOK regs. End ######################################


########################### Student reg. start ####################################

def sr():
    l=[]
    n = int(input("Enter No of Student To Add: "))
    for _ in range(n):
        print("\n_______________________________________________")
        print(f"Enter Detail for Student: {_+1}\n")
        l.append(Admin())
        l[_].getstudent()
        
    with open("studentdetail.pkl","wb") as fp:
        for _ in l:
            pickle.dump(_,fp)
            print("\nTHANK YOU_!!!!\nStudents Are Added Successfully")
    


########################### student regs. End ####################################

########################## faculti reg. start ##################################

def fr():
    l=[]
    n=int(input("How many Faculty you want to ADD: "))
    for _ in range(n):
        print("\n_______________________________________________")
        print(f"Enter Detail for Faculty: {_+1}\n")
        l.append(Admin())
        l[_].getfaculty()
    with open("facultydetail.pkl","wb") as fp:
        for _ in l:
            pickle.dump(_,fp)
    print("\nTHANK YOU_!!!!\nFaculties Are Added Successfully")
    


######################## faculti register end #############################

################################# show book detail ##############################z

def bs():
    with open("bookdetail.pkl","rb") as fp:
        while True:
            try:
                obj = pickle.load(fp)
                obj.showbook()
            except EOFError:
                print("\n___________________Data Finish")
                break
    print("_"*55)            
    with open("bdist.pkl","rb") as p:
        objdist=pickle.load(p)
        print("Book code with Remaining Copies and Name :")
        print("'{Book code : [no. of Copies , Book Name]}'\n")
        print(objdist)
            
    

############################### show book detail end ###########################


####################### show student detail ##############################
def ss():
    with open("studentdetail.pkl","rb") as fp:
        while True:
            try:
                obj = pickle.load(fp)
               # print(type(obj))
               # print(obj)
                obj.showstudent()
            except EOFError:
                print("\n______________________Data Finish")
                break
                
    print("_"*55)             
    with open("sdist.pkl","rb") as p:
        objdist=pickle.load(p)
        print(objdist)
            
############################ show student detail end #################################

############################ show faculty detail start ##########################

def fs():
    with open("facultydetail.pkl","rb") as fp:
        while True:
            try:
                obj = pickle.load(fp)
                obj.showfaculty()
            except EOFError:
                print("\nData Finish")
                break
    print("_"*55)            
    with open("fdist.pkl","rb") as p:
        objdist=pickle.load(p)
        print(objdist)
            


############################### show faculty detail end ##################################

#################################  Admin LogIn ################################
# def al():
#     a1=Admin()
#     a1.adminlogin()

############################# Admin LogIn End ##################################

############################ Student Log start ##################################
# def sl():
#     s1=Student()
#     s1.studentlogin()
    
############################## student log end ##############################

############################## faculty login start ######################
# def fl():
#     f1=Faculty()
#     f1.facultylogin()
    
    
############################ faculty login End ####################### 
############################ studentbook Issue ###################
def sbi():
    a1=Admin()
    a1.sbookissue()
    
    #################### book remove ###################
def rb():
    a2=Admin()
    a2.bookremove()

def sbr():   ############# student book return #########################
    a3=Admin()
    a3.sbookreturn()

def fbi(): ############### faculty book issue ###################
    a4=Admin()
    a4.fbookissue()
    
def fbr(): ############### faculty book return ###################### 
    a5=Admin()
    a5.fbookreturn()
    
def fc():   #################### fine calculate ###################
    a5=Admin()
    a5.dayfine()
    
def sb():
    Search_Book()


def main():
    
    while True:
        print("\n************************************* Admin Menu ***************************************")
        op = int(input("\nEnter Your Opetion\n1 Book Register\n2 Book Deatil\n3 Student Reg.\n4 Student Detail\n5 Faculty Reg.\n6 Faculty Detail\n7 Student Book Issue \n8 Remove Book \n9 Student Book Return \n10 Faculty Book Issue\n11 Faculty Book Return\n12 To Calculate Fine\n13 for Search Book \n0 for Exit\n"))
        if op == 1:
            br()
        elif op == 2:
            bs()
        elif op == 3:
            sr()
        elif op == 4:
            ss()
        elif op == 5:
            fr()
        elif op == 6:
            fs()
        elif op == 7:
            sbi()
        elif op == 8 :
            rb()
        elif op == 9 :
            sbr()
        elif op == 10:
            fbi()
        elif op == 11:
            fbr()
        elif op == 12:
            fc()
        elif op == 13:
            sb()
        elif op == 0:
            break
