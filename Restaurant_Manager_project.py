import mysql.connector
from tkinter import *

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Ashwin@319",database="school")
#change the passwd and database name etc according to the computer.
mycur=mydb.cursor()

# Define SQL statements for table creation
create_reservation_list_table = """
CREATE TABLE IF NOT EXISTS reservation_list (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    name VARCHAR(255),
    guests INT,
    reservation_time TIME
)
"""

create_customer_order_table = """
CREATE TABLE IF NOT EXISTS customer_order (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    c_order VARCHAR(255)
)
"""

# Execute table creation SQL statements
mycur.execute(create_reservation_list_table)
mycur.execute(create_customer_order_table)

window1=Tk()
window1.title("Welcome")
window1.geometry("350x250")
welcome=Label(window1,text="Welcome to Customer Manager")
welcome.grid(column=1,row=1)

def log():
    window1.destroy()
    	
    def log2():
        windowlog=Tk()
        windowlog.geometry("350x250")
        windowlog.title("Login")
        entrylab=Label(windowlog,text="Enter the admin password:-")
        entrylab.grid(column=1,row=1)
        passentry=Entry(windowlog,width=10,show="*")
        passentry.grid(column=1,row=2)
        
        def login():
            if passentry.get()=="admin1234":
                windowlog.destroy()
                
                def homepage(): 
                    window=Tk()
                    window.geometry('350x250')
                    window.title("Reservation Database")
                    
                    id=Label(window,text="Enter the Customer Id")
                    id.grid(column=0,row=0)
                    data_id=Entry(window,width=10)
                    data_id.grid(column=1,row=0)   
                    
                    name=Label(window,text="Enter the name")
                    name.grid(column=0,row=1)
                    data_name=Entry(window,width=10)
                    data_name.grid(column=1,row=1)
                    
                    guest=Label(window,text="No.of guests")
                    guest.grid(column=0,row=2)
                    data_guest=Entry(window,width=10)
                    data_guest.grid(column=1,row=2)
                    
                    res_time=Label(window,text="Entry Time")
                    res_time.grid(column=0,row=3)
                    time=Entry(window,width=10)
                    time.grid(column=1,row=3)
                    
                    order=Label(window,text="order")
                    order.grid(column=0,row=4)
                    order_e=Entry(window,width=10)
                    order_e.grid(column=1,row=4)
                    
                    def click():
                        st="insert into reservation_list(customer_id,name,guests,reservation_time)values(%s,%s,%s,%s)"
                        value=(data_id.get(),data_name.get(),data_guest.get(),time.get())
                        mycur.execute(st,value)
                        mydb.commit()
                        
                        st2="insert into customer_order(customer_id,c_order)values(%s,%s)"
                        value2=(data_id.get(),order_e.get())
                        mycur.execute(st2,value2)
                        mydb.commit() 
                        
                        window.destroy()
                         
                        success=Tk()
                        success.title("Entry Succesful")
                        success.geometry('350x250')
                        succ=Label(success,text="Entry has been recorded into the database")
                        succ.grid(column=0,row=0)
                        def homesucc():
                            success.destroy()
                            homepage()
                        homebutton=Button(success,text="Return to Homepage",command=homesucc)
                        homebutton.grid(column=0,row=1)
                    bt=Button(window,text="Enter",command=click)
                    bt.grid(column=1,row=5)
                    
                    def clicked():
                        window.destroy()
                        window2=Tk()
                        window2.geometry('350x250') 
                        window2.title("View Records")
                        
                        def clickorder():
                            window2.destroy()
                            windoworder=Tk()
                            windoworder.geometry('350x250')
                            windoworder.title("view order")
                            id=Label(windoworder,text="Enter the Customer Id")
                            id.grid(column=0,row=0)
                            data_id=Entry(windoworder,width=10)
                            data_id.grid(column=1,row=0) 
                            
                            def homeorder():
                                windoworder.destroy()
                                homepage()
                            choice=Button(windoworder,text="Return to Homepage",command=homeorder)
                            choice.grid(column=1,row=4)
                            
                            def clickorderview():
                                idd=str(data_id.get())
                                st="select c_order from customer_order where customer_id="
                                str2=st+'"'+idd+'"'
                                mycur.execute(str2)
                                for x in mycur: 
                                    label2=Label(windoworder,text=x)
                                    label2.grid(column=1,row=3)
                                    
                            bt4=Button(windoworder,text="Enter",command=clickorderview)
                            bt4.grid(column=1,row=2)
                        
                        def clickdata():
                            window2.destroy()
                            windowdata=Tk()
                            windowdata.geometry('350x250')
                            windowdata.title("view customer details")
                            id=Label(windowdata,text="Enter the Customer Id")
                            id.grid(column=0,row=0)
                            data_id=Entry(windowdata,width=10)
                            data_id.grid(column=1,row=0) 
                            def homedata():
                                windowdata.destroy()
                                homepage()
                            choice1=Button(windowdata,text="Return to Homepage",command=homedata)
                            choice1.grid(column=1,row=4)
                            
                            def clickdataview():
                                idd=str(data_id.get())
                                st="select * from reservation_list where customer_id="
                                str2=st+'"'+idd+'"'
                                mycur.execute(str2)
                                for x in mycur: 
                                    label2=Label(windowdata,text=x)
                                    label2.grid(column=1,row=3)
                                    
                            bt4=Button(windowdata,text="Enter",command=clickdataview)
                            bt4.grid(column=1,row=2)
                            
                        label=Label(window2,text="View:-")
                        label.grid(column=0,row=0)
                        btorder=Button(window2,text="View customer order",bg="yellow",fg="red",command=clickorder)
                        btorder.grid(column=0,row=1)
                        
                        
                        btdata=Button(window2,text="View customer details",bg="yellow",fg="red",command=clickdata)
                        btdata.grid(column=1,row=1)
                    
                    bt2=Button(window,text="View entry",command=clicked)
                    bt2.grid(column=1,row=6)
                    window.mainloop()
                
                homepage()
                
            else:
                windowlog.destroy()
                fail=Tk()
                fail.geometry("350x250")
                fail.title("Error")
                flabel=Label(fail,text="Failed to Login")
                flabel.grid(column=1,row=1)
                
                def retry():
                    fail.destroy()
                    log2()
                    
                retrybt=Button(fail,text="Retry",command=retry)
                retrybt.grid(column=1,row=2)
            
                
        passbt=Button(windowlog,text="Enter",command=login)
        passbt.grid(column=1,row=3)
        windowlog.mainloop()
        
    log2()
    
entrybt=Button(window1,text="login",command=log)
entrybt.grid(column=1,row=2)
window1.mainloop()
