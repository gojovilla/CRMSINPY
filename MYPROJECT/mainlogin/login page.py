from tkinter import*
from tkinter import messagebox
import ast
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from flask import render_template
import tkinter as tk
from tkinter import filedialog
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas


root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

   
  ##  print(r.keys())
   ##  print(r.values())

    if username in r.keys() and password==r[username]:
     class Criminal:
        def __init__(self,root):
          self.root=root
          self.root.geometry('1530x790+0+0')
          self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        
        

# Add a button to generate the report
      #    button = tk.Button(root, text="Generate Report")
       #   button.pack(side="top")

          def Crime_Data():
            
           #messagebox.showinfo('Success','fantastic!!!!')
            db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sonu296702@gmail",
            database="management"
            )

            # Retrieve data from the database
            cursor = db.cursor()
            cursor.execute("SELECT * FROM criminal")
            data = cursor.fetchall()
            
            # Create a tkinter window
            root = tk.Tk()
            root.title("Report")
            
            # Create a table to display the data
            table = ttk.Treeview(root)
            table["columns"] = ["Case_id", "Criminal_no", "Criminal_name","arrest_date","dateOfcrime","age","crimeType"]
            table.heading("Case_id", text="Case_id")
            table.heading("Criminal_no", text="Criminal_no")
            table.heading("Criminal_name", text="Criminal_name")
            table.heading("arrest_date", text="arrest_date")
            table.heading("dateOfcrime", text="dateOfcrime")
            table.heading("age", text="age")
            table.heading("crimeType", text="crimeType")
            table.heading("Criminal_name", text="Criminal_name")
            
            for row in data:
                table.insert("", tk.END, values=row,tags=('centered',))
            
            # Pack the table
            table.pack()
            
            # Create a button to export the data
            def export_data():
                filename = filedialog.asksaveasfilename(defaultextension=".pdf")
                if filename:
                    with open(filename, "w") as f:
                        # Write the column headers
                        f.write("Case_id,Criminal_no, Criminal_name,arrest_date,dateOfcrime,age,crimeType\n",ANCHOR="center")
                        # Write the data rows
                        for row in data:
                            f.write(",".join(str(x) for x in row) + "\n")

            export_button = tk.Button(root, text="Export", command=export_data)
            export_button.pack()
            

          #menu bar
          myMenu=Menu(root)
        
          CrimeMenu=Menu(myMenu,tearoff=0,foreground='blue')

          CrimeMenu.add_command(label='Report',command=Crime_Data)
          myMenu.add_cascade(label='Menu',menu=CrimeMenu)
          root.config(menu=myMenu)

          #variables
          self.var_case_id=StringVar()
          self.var_criminal_no=StringVar()
          self.var_name=StringVar()
          self.var_nickname=StringVar()
          self.var_arrest_date=StringVar()
          self.var_date_of_crime=StringVar()
          self.var_address=StringVar()
          self.var_age=StringVar()
          self.var_occuption=StringVar()
          self.var_birthmark=StringVar()
          self.var_crime_type=StringVar()
          self.var_father_name=StringVar()
          self.var_gender=StringVar()
          self.var_wanted=StringVar()


          
          lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SOFTWARE',font=('times new roman',40,'bold'),bg='black',fg='gold')
          lbl_title.place(x=0,y=0,width=1530,height=70)
  
          img_logo=Image.open('E:\MYPROJECT\images\logo.jpg')
          img_logo=img_logo.resize((60,60),Image.LANCZOS)
          self.photo_logo=ImageTk.PhotoImage(img_logo)
  
          self.logo=Label(self.root,image=self.photo_logo)
          self.logo.place(x=180,y=5,width=60,height=60)
  
  
          # img frame
          img_frame=Frame(self.root, bd=2, relief=RIDGE, bg='white')
          img_frame.place(x=0,y=70,width=1530,height=130)
  
          img1=Image.open('E:\MYPROJECT\images\logo1.jpg')
          img1=img1.resize((540,160), Image.LANCZOS)
          self.photo1=ImageTk.PhotoImage(img1)
  
          self.img_1=Label(img_frame,image=self.photo1)
          self.img_1.place(x=0,y=0,width=540,height=160)
  
           # 2nd image
          img2 = Image.open('images\logo3.jpg')
          img2 = img2.resize((540,160), Image.Resampling.LANCZOS)
          self.photo2 = ImageTk.PhotoImage(img2)
  
          self.img_2 = Label(img_frame, image=self.photo2)
          self.img_2.place(x=540, y=0, width=540, height=160)
  
          # 3rd  image
          img3 = Image.open('images\logo2.jpg')
          img3 = img3.resize((540,160), Image.Resampling.LANCZOS)
          self.photo3 = ImageTk.PhotoImage(img3)
  
          self.img_3 = Label(img_frame, image=self.photo3)
          self.img_3.place(x=1000, y=0, width=540, height=160)
  
           # main frame
          Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
          Main_frame.place(x=10, y=200, width=1500, height=560)
  
          #upper frame
          upper_frame =LabelFrame(Main_frame, bd=2, relief=RIDGE,text='Criminal Information ',font=('times new roman',11,'bold'),fg='red',bg='white')
          upper_frame.place(x=10, y=10, width=1480, height=270)


        
          #Label Entry
          #case id
          caseid=Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),bg='white')
          caseid.grid(row=0,column=0,padx=2,sticky=W)
  
          caseentry=ttk.Entry(upper_frame,width=22,textvariable=self.var_case_id,font=('arial',11,'bold'))
          caseentry.grid(row=0,column=1,padx=2,sticky=W)
  
          #criminal no
          lbl_criminal_no=Label(upper_frame,text='Criminal No:',font=('arial',11,'bold'),bg='white')
          lbl_criminal_no.grid(row=0,column=2,padx=2,sticky=W,pady=7)
  
          txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
          txt_criminal_no.grid(row=0,column=3,padx=2,pady=7)
  
         # Criminal name
          lbl_name=Label(upper_frame,text='Criminal name:',font=('arial',12,'bold'),bg='white')
          lbl_name.grid(row=1,column=0,padx=2,pady=7,sticky=W)
  
          txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
          txt_name.grid(row=1,column=1,sticky=W,padx=2,pady=7)
         
          #nickname
          lbl_nickname=Label(upper_frame,text='nick name:',font=('arial',12,'bold'),bg='white')
          lbl_nickname.grid(row=1,column=2,padx=2,sticky=W,pady=7)
  
          txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
          txt_nickname.grid(row=1,column=3,padx=2,pady=7)
  
          #Arrest date
          lbl_arrestDate=Label(upper_frame,text='Arrest date:',font=('arial',12,'bold'),bg='white')
          lbl_arrestDate.grid(row=2,column=0,padx=2,pady=7,sticky=W)
  
          txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('arial',11,'bold'))
          txt_arrestDate.grid(row=2,column=1,padx=2,pady=7)
  
          #date of crime
          lbl_dateOfCrime=Label(upper_frame,text='Date of crime:',font=('arial',11,'bold'),bg='white')
          lbl_dateOfCrime.grid(row=2,column=2,padx=2,pady=7,sticky=W)
  
          txt_dateOfCrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',11,'bold'))
          txt_dateOfCrime.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #address
          lbl_address=Label(upper_frame,text='address:',font=('arial',12,'bold'),bg='white')
          lbl_address.grid(row=3,column=0,padx=2,pady=7,sticky=W)
  
          txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
          txt_address.grid(row=3,column=1,padx=2,pady=7)
  
          #Age
          lbl_age=Label(upper_frame,text='Age:',font=('arial',12,'bold'),bg='white')
          lbl_age.grid(row=3,column=2,padx=2,pady=7,sticky=W)
  
          txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
          txt_age.grid(row=3,column=3,padx=2,pady=7)
  
          #occuption
          lbl_occupution=Label(upper_frame,text='occuption:',font=('arial',12,'bold'),bg='white')
          lbl_occupution.grid(row=4,column=0,padx=2,pady=7,sticky=W)
  
          txt_occupution=ttk.Entry(upper_frame,textvariable=self.var_occuption,width=22,font=('arial',11,'bold'))
          txt_occupution.grid(row=4,column=1,padx=2,pady=7)
  
          #birthmark
          lbl_birthmark=Label(upper_frame,text='birthmark:',font=('arial',12,'bold'),bg='white')
          lbl_birthmark.grid(row=4,column=2,padx=2,pady=7,sticky=W)
  
          txt_birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthmark,width=22,font=('arial',11,'bold'))
          txt_birthmark.grid(row=4,column=3,padx=2,pady=7,sticky=W)
  
          #Crime type
          lbl_crimeType=Label(upper_frame,text='crime type:',font=('arial',12,'bold'),bg='white')
          lbl_crimeType.grid(row=0,column=4,padx=2,pady=7,sticky=W)

          txt_crimeType=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('arial',11,'bold'))
          txt_crimeType.grid(row=0,column=5,padx=2,pady=7)
  
          #father name
          lbl_fatherName=Label(upper_frame,text='Father name:',font=('arial',12,'bold'),bg='white')
          lbl_fatherName.grid(row=1,column=4,padx=2,pady=7,sticky=W)
  
          txt_fatherName=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('arial',11,'bold'))
          txt_fatherName.grid(row=1,column=5,padx=2,pady=7)
  
          #gender
          lbl_gender=Label(upper_frame,text='Gender:',font=('arial',12,'bold'),bg='white')
          lbl_gender.grid(row=2,column=4,padx=2,pady=7,sticky=W)
  
          #wanted
          lbl_wanted=Label(upper_frame,text='wanted:',font=('arial',11,'bold'),bg='white')
          lbl_wanted.grid(row=3,column=4,padx=2,pady=7,sticky=W)
  
          #radio button gender
          radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
          radio_frame_gender.place(x=680,y=90,width=190,height=30)
  
          male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
          male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
  
          female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
          female.grid(row=0,column=1,pady=2,padx=5,sticky=W)
  
         #radio button wanted
          radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
          radio_frame_wanted.place(x=680,y=130,width=190,height=30)
  
          yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',9,'bold'),bg='white')
          yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
  
          nO=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
          nO.grid(row=0,column=1,pady=2,padx=5,sticky=W)
  
  
          #down frame
          down_frame =LabelFrame(Main_frame, bd=2, relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
          down_frame.place(x=10, y=280, width=1480, height=270)
  
  
             #buttons
          button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
          button_frame.place(x=5,y=200,width=620,height=45)
  
          #add button
          btn_add=Button(button_frame,command=self.add_data,text='Record save',font=("arial",13,"bold",),width=14,bg='blue',fg='white')
          btn_add.grid(row=0,column=0,padx=3,pady=5)
  
           #update button
          btn_update=Button(button_frame,command=self.update_data,text='Update',font=("arial",13,"bold",),width=14,bg='blue',fg='white')
          btn_update.grid(row=0,column=1,padx=3,pady=5)
  
           #delete button
          btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=("arial",13,"bold",),width=14,bg='blue',fg='white')
          btn_delete.grid(row=0,column=2,padx=3,pady=5)
  
          #Clear button
          btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=("arial",13,"bold",),width=14,bg='blue',fg='white')
          btn_clear.grid(row=0,column=3,padx=3,pady=5)

          #background right side image
          img_crime = Image.open('images/criminal2.jpg')
          img_crime = img_crime.resize((470,245), Image.Resampling.LANCZOS)
          self.photocrime = ImageTk.PhotoImage(img_crime)
  
          self.img_crime = Label(upper_frame, image=self.photocrime)
          self.img_crime.place(x=1000, y=0, width=470, height=245)


         #search frame
          search_frame =LabelFrame(down_frame, bd=2, relief=RIDGE,text='search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
          search_frame.place(x=0, y=0, width=1470, height=60)
  
          search_by=Label(search_frame,text='search by:',font=('arial',11,'bold'),bg='red',fg='white')
          search_by.grid(row=0,column=0,padx=5,sticky=W)
  
  
          self.var_com_search=StringVar()
          combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',11,'bold'),width=18,state='readonly')
          combo_search_box['value']=('select option','Case_id','Criminal_no')
          combo_search_box.current(0)
          combo_search_box.grid(row=0,column=1,sticky=W,padx=5)
  
  
          self.var_search=StringVar()
          search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('arial',11,'bold'))
          search_txt.grid(row=0,column=2,sticky=W,padx=5)
  
           #search button
          btn_search=Button(search_frame,command=self.search_data,text='search',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
          btn_search.grid(row=0,column=3,padx=3,pady=5)
  
          #all button
          btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
          btn_all.grid(row=0,column=4,padx=3,pady=5)
  
          crimeagency=Label(search_frame,text='NATIONAL CRIME AGENCY',font=('arial',30,'bold'),bg='white',fg='crimson')
          crimeagency.grid(row=0,column=5,padx=40,sticky=W,pady=0)

          #table frame
          table_frame=Frame(down_frame,bd=2,relief=RIDGE)
          table_frame.place(x=0,y=60,width=1470,height=170)
  
  
          #scroll bar
          scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
          scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
  
          self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
          
          scroll_x.pack(side=BOTTOM,fill=X)
          scroll_y.pack(side=RIGHT,fill=Y)
  
  
          scroll_x.config(command=self.criminal_table.xview)
          scroll_y.config(command=self.criminal_table.yview)

          self.criminal_table.heading('1',text='Case Id')
          self.criminal_table.heading('2',text='Criminal No')
          self.criminal_table.heading('3',text='Criminal Name')
          self.criminal_table.heading('4',text='NickName')
          self.criminal_table.heading('5',text='ArrestDate')
          self.criminal_table.heading('6',text='Date of crime')
          self.criminal_table.heading('7',text='Address')
          self.criminal_table.heading('8',text='Age')
          self.criminal_table.heading('9',text='Occupation')
          self.criminal_table.heading('10',text='Birth Mark')
          self.criminal_table.heading('11',text='crime Type')
          self.criminal_table.heading('12',text='Father Name')
          self.criminal_table.heading('13',text='Gender')
          self.criminal_table.heading('14',text='Wanted')
  
          self.criminal_table['show']='headings'
          self.criminal_table.column('1',width=100)
          self.criminal_table.column('2',width=100)
          self.criminal_table.column('3',width=100)
          self.criminal_table.column('4',width=100)
          self.criminal_table.column('5',width=100)
          self.criminal_table.column('6',width=100)
          self.criminal_table.column('7',width=100)
          self.criminal_table.column('8',width=100)
          self.criminal_table.column('9',width=100)
          self.criminal_table.column('10',width=100)
          self.criminal_table.column('11',width=100)
          self.criminal_table.column('12',width=100)
          self.criminal_table.column('13',width=100)
          self.criminal_table.column('14',width=100)

          self.fetch_data()
  
          self.criminal_table.pack(fill=BOTH,expand=1)
          self.criminal_table.bind("<ButtonRelease>",self.get_curser)


         #Add Function

        def add_data(self):
            if self.var_case_id.get()=="": 
                messagebox.showerror('Error','All Fields as requried')
            else:
                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='sonu296702@gmail',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                              
                                                                                                               self.var_case_id.get(),
                                                                                                               self.var_criminal_no.get(),
                                                                                                               self.var_name.get(),
                                                                                                               self.var_nickname.get(),
                                                                                                               self.var_arrest_date.get(),
                                                                                                               self.var_date_of_crime.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_age.get(),
                                                                                                               self.var_occuption.get(),
                                                                                                               self.var_birthmark.get(),
                                                                                                               self.var_crime_type.get(),
                                                                                                               self.var_father_name.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_wanted.get()
                                                                                                               ))    
    
                    conn.commit()
                    self.fetch_data()
                    self.clear_data()
                    conn.close()
                    messagebox.showinfo('Success','Criminal record has been added')
                except Exception as es:
                    messagebox.showerror('Error',f'Due To{str(es)}')    
       
        #fetch data
        def fetch_data(self):
            conn=mysql.connector.connect(host='localhost',username='root',password='sonu296702@gmail',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute('select * from criminal')
            data=my_cursor.fetchall()
            if len(data)!=0:
                self.criminal_table.delete(*self.criminal_table.get_children())
                for i in data:
                 self.criminal_table.insert("",END,values=i)
                conn.commit()
            conn.close()

         #get curser

        def get_curser(self,event=""):
            cursur_row=self.criminal_table.focus()
            content=self.criminal_table.item(cursur_row)
            data=content['values']
    
            self.var_case_id.set(data[0])
            self.var_criminal_no.set(data[1])
            self.var_name.set(data[2])
            self.var_nickname.set(data[3])
            self.var_arrest_date.set(data[4])
            self.var_date_of_crime.set(data[5])
            self.var_address.set(data[6])
            self.var_age.set(data[7])
            self.var_occuption.set(data[8])
            self.var_birthmark.set(data[9])
            self.var_crime_type.set(data[10])
            self.var_father_name.set(data[11])
            self.var_gender.set(data[12])
            self.var_wanted.set(data[13])

        #update

        def update_data(self):
            if self.var_case_id.get()=="": 
                messagebox.showerror('Error','All Fields as requried')
            else:
                try:
                    update=messagebox.askyesno('update','Are you sure uodate this criminal record')
                    if update>0:
                         conn=mysql.connector.connect(host='localhost',username='root',password='sonu296702@gmail',database='management')
                         my_cursor=conn.cursor()
                         my_cursor.execute('update criminal set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,Age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(
                                                                                                                                                                                                                                self.var_nickname.get(),
                                                                                                                                                                                                                                self.var_criminal_no.get(),
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_arrest_date.get(),
                                                                                                                                                                                                                                self.var_date_of_crime.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_age.get(),
                                                                                                                                                                                                                                self.var_occuption.get(),
                                                                                                                                                                                                                                self.var_birthmark.get(),
                                                                                                                                                                                                                                self.var_crime_type.get(),
                                                                                                                                                                                                                                self.var_father_name.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_wanted.get(),
                                                                                                                                                                                                                                self.var_case_id.get()
                                                                                                                                                                                                                            ))
                    else:
                        if not update:
                            return
                    conn.commit()
                    self.fetch_data()
                    self.clear_data()
                    conn.close()
                    messagebox.showinfo('success','Criminal record successfully updated')
                except Exception as es:
                    messagebox.showerror('Error',f'Due To{str(es)}')     

        #delete

        def delete_data(self):
            if self.var_case_id.get()=="":
               messagebox.showerror('Error','All Fields are require')
            else:
                try:
                   Delete=messagebox.askyesno('Delete','Are you sure Delete this criminal record')
                   if Delete>0:
                        conn=mysql.connector.connect(host='localhost',username='root',password='sonu296702@gmail',database='management')
                        my_cursor=conn.cursor() 
                        sql='delete from criminal where Case_id=%s'
                        value=(self.var_case_id.get(),)
                        my_cursor.execute(sql,value)
                   else:
                        if not Delete:
                            return
                   conn.commit()
                   self.fetch_data()
                   self.clear_data()
                   conn.close()              
                   messagebox.showinfo('success','Criminal record successfully deleted')
                except Exception as es:
                    messagebox.showerror('Error',f'Due To{str(es)}') 
    
         #clear

        def clear_data(self):
            self.var_case_id.set("")
            self.var_criminal_no.set("")
            self.var_name.set("")
            self.var_nickname.set("")
            self.var_arrest_date.set("")
            self.var_date_of_crime.set("")
            self.var_address.set("")
            self.var_age.set("")
            self.var_occuption.set("")
            self.var_birthmark.set("")
            self.var_crime_type.set("")
            self.var_father_name.set("")
            self.var_gender.set("")
            self.var_wanted.set(" ")


        #search
        def search_data(self):
            if self.var_com_search.get()=="":
               messagebox.showerror('Error','All Fields are require')
            else:
                try:
                   conn=mysql.connector.connect(host='localhost',username='root',password='sonu296702@gmail',database='management')
                   my_cursor=conn.cursor() 
                   my_cursor.execute('select * from criminal where  ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'")) 
                   rows=my_cursor.fetchall()
                   if len(rows)!=0:
                       self.criminal_table.delete(*self.criminal_table.get_children())
                       for i in rows:
                          self.criminal_table.insert("",END,values=i)
                   conn.commit()
                   conn.close()  
                except Exception as es:
                    messagebox.showerror('Error',f'Due To{str(es)}') 


     if __name__=="__main__":
           root=Toplevel()
           obj=Criminal(root)
           root.mainloop()  

          
    else: 
        messagebox.showerror('invalid','invalid username and password')
########################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    
def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)


    def signup():
        username=user.get()
        password=code.get()
        conform_password=conform_code.get()

        if password==conform_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('Signup','Sucessfully sign up')
            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid',"Both Password should match")

    def sign():
        window.destroy()


    img=PhotoImage(file='E:\MYPROJECT\mainlogin\signup.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)


    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)


    heading=Label(frame,text='Sign Up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)

###########------------------------------------------------
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'USername')    




    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


############----------------------------------------------------

    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')    




    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


#########################--------------------------------
    def on_enter(e):
        conform_code.delete(0,'end')
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'Conform Password')    




    conform_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0,'Conform Password')
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>",on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)







#######----------------------------------
    Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label.place(x=90,y=340)

    signin=Button(frame,width=6,text='Sign In',border=0,bg='white', cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=340)





    window.mainloop() 
 
    
#########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


img=PhotoImage(file='E:\MYPROJECT\mainlogin\signin.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)


#####################-----------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')    
user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


############-----------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password') 
code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')

code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)



Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)

label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)



root.mainloop()