from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from test import path


class Student:
    def __init__(self,root):
         self.root = root
         self.path = "/desired/path/to/file_or_directory"

         self.root.geometry("2530x900+0+0")
         self.root.title("Student Management System")


         # Variables
         self.var_dep = StringVar()
         self.var_course = StringVar()
         self.var_year = StringVar()
         self.var_semester = StringVar()
         self.var_std_id = StringVar()
         self.var_std_name = StringVar()
         self.var_div = StringVar()
         self.var_roll = StringVar()
         self.var_gender = StringVar()
         self.var_dob = StringVar()
         self.var_email = StringVar()
         self.var_phone = StringVar()
         self.var_address = StringVar()
         self.var_teacher = StringVar()
         self.var_search_by = StringVar()
         self.var_search_txt = StringVar()
         self.var_name = StringVar()
         self.var_id = StringVar()
         self.var_roll = StringVar()
         self.var_course = StringVar()
         self.var_dep = StringVar()
         self.var_year = StringVar()
         self.var_semester = StringVar()
         self.var_std_id = StringVar()
         self.var_gen= StringVar()
         
         # 1st image

         img1 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/student1.jpeg")
         img1 = img1.resize((500,130))
         self.photoimg1 = ImageTk.PhotoImage(img1)

         f_lbl = Label(self.root, image=self.photoimg1)
         f_lbl.place(x=0, y=0, width=500, height=130)

        # 2nd image

         img2 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/student2.jpeg")
         img2 = img2.resize((500,130))
         self.photoimg2 = ImageTk.PhotoImage(img2)

         f_lbl = Label(self.root, image=self.photoimg2)
         f_lbl.place(x=500, y=0, width=500, height=130)

         # 3rd image

         img3 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/studnet3.jpg")
         img3 = img3.resize((500,130))
         self.photoimg3 = ImageTk.PhotoImage(img3)

         f_lbl = Label(self.root, image=self.photoimg3)
         f_lbl.place(x=1000, y=0, width=500, height=130)

         # 4th image


         img = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/student4.jpg")
         img = img.resize((500,130))
         self.photoimg = ImageTk.PhotoImage(img)

         f_lbl = Label(self.root, image=self.photoimg)
         f_lbl.place(x=1500, y=0, width=500, height=130)

         # bg Image
         img4 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/ezgif.com-gif-maker-6 (1).jpeg")
         img4 = img4.resize((2000,900))
         self.photoimg4 = ImageTk.PhotoImage(img4)

         bgimage = Label(self.root, image=self.photoimg4)
         bgimage.place(x=0, y=130, width=2000, height=900)

         title_lbl = Label(bgimage,text="STUDENT MANAGMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
         title_lbl.place(x=0, y=0, width=2000, height=45)

         main_frame = Frame(bgimage, bd=2, bg="white")
         main_frame.place(x=10, y=60, width=1900, height=800)

         # Left Label Frame

         left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"), bg="white")
         left_frame.place(x=34, y=10, width=900, height=750)

         img5 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/student5.jpg")
         img5 = img5.resize((890,150))
         self.photoimg5 = ImageTk.PhotoImage(img5)

         f_lbl = Label(left_frame, image=self.photoimg5)
         f_lbl.place(x=4, y=10, width=890, height=150)
   
        # course details
         
         curren_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE, text="Current course information", font=("times new roman", 12, "bold"), bg="white")
         curren_course_frame.place(x=4, y=154, width=890, height=200)

        # Department

         dep_label = Label(curren_course_frame,text="Department", font=("times new roman", 12, "bold"), bg="white")
         dep_label.grid(row=0, column=0, padx=10, sticky=W)

         dep_combo = ttk.Combobox(curren_course_frame,textvariable=self.var_dep,font=("times new roman ",12, "bold"),width=17, state="readonly")
         dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical", "Electrical")
         dep_combo.current(0)
         dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

         # Course

         course_label = Label(curren_course_frame,text="Course", font=("times new roman", 12, "bold"), bg="white")
         course_label.grid(row=0, column=2, padx=10,pady=10,sticky=W)

         course_combo = ttk.Combobox(curren_course_frame,textvariable=self.var_course,font=("times new roman ",12, "bold"),width=17, state="readonly")
         course_combo["values"] = ("Select Course", "BCA", "BBA", "B.Tech", "MBA", "MCA")
         course_combo.current(0)
         course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

         # year

         year_label = Label(curren_course_frame,text="Year", font=("times new roman", 12, "bold"), bg="white")
         year_label.grid(row=1, column=0, padx=10,pady=10,sticky=W)

         year_combo = ttk.Combobox(curren_course_frame,textvariable=self.var_year,font=("times new roman ",12, "bold"),width=17, state="readonly")
         year_combo["values"] = ("Select Year", "1st", "2nd", "3rd", "4th", "5th")
         year_combo.current(0)
         year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
     
         # Semester

         semester_label = Label(curren_course_frame,text="Semester", font=("times new roman", 12, "bold"), bg="white")
         semester_label.grid(row=1, column=2, padx=10,pady=10,sticky=W)

         semester_combo = ttk.Combobox(curren_course_frame,textvariable=self.var_semester,font=("times new roman ",12, "bold"),width=17, state="readonly")
         semester_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th")
         semester_combo.current(0)
         semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
         
         # Class Student Information
         curren_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"), bg="white")
         curren_course_frame.place(x=4, y=354, width=890, height=370)
  
         # Student ID

         Student_id_label = Label(curren_course_frame,text="Student ID", font=("times new roman", 12, "bold"), bg="white")
         Student_id_label.grid(row=0, column=0, padx=10,pady=10,sticky=W)

         Student_id_entry = ttk.Entry(curren_course_frame,textvariable=self.var_std_id,width=20, font=("times new roman ",12, "bold"))
         Student_id_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         # Student Name

         Student_name_label = Label(curren_course_frame,text="Student Name", font=("times new roman", 12, "bold"), bg="white")
         Student_name_label.grid(row=0, column=2, padx=10,pady=10,sticky=W) 
         Student_name_entry = ttk.Entry(curren_course_frame,textvariable=self.var_std_name,width=20, font=("times new roman ",12, "bold"))
         Student_name_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

         # Class Division

         Class_div_label = Label(curren_course_frame,text="Class Division", font=("times new roman", 12, "bold"), bg="white")
         Class_div_label.grid(row=1, column=0, padx=10,pady=10,sticky=W)

         Class_div_entry = ttk.Entry(curren_course_frame,textvariable=self.var_div,width=20, font=("times new roman ",12, "bold"))
         Class_div_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         Class_Div_combo=ttk.Combobox(curren_course_frame,textvariable=self.var_div,font=("times new roman ",12, "bold"),width=19, state="readonly")
         Class_Div_combo["values"]=("Select Division","A","B","C","D")
         Class_Div_combo.current(0)
         Class_Div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
         


         # Roll No

         Roll_no_label = Label(curren_course_frame,text="Roll No", font=("times new roman", 12, "bold"), bg="white")
         Roll_no_label.grid(row=1, column=2, padx=10,pady=10,sticky=W)

         Roll_no_entry = ttk.Entry(curren_course_frame,textvariable=self.var_roll,width=20, font=("times new roman ",12, "bold "))
         Roll_no_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)
         
         # Gender
         
         Gender_label = Label(curren_course_frame,text="Gender", font=("times new roman", 12, "bold"), bg="white")
         Gender_label.grid(row=2, column=0, padx=10,pady=10,sticky=W)

        #  Gender_entry = ttk.Entry(curren_course_frame,textvariable=self.var_gender,width=20, font=("times new roman ",12, "bold"))
        #  Gender_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

         Gender_combo = ttk.Combobox(curren_course_frame,textvariable=self.var_gen,font=("times new roman ",12, "bold",),width=19, state="readonly")
         Gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
         Gender_combo.current(0)
         Gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)


         # DOB

         Dob_label = Label(curren_course_frame,text="DOB", font=("times new roman", 12, "bold"), bg="white")
         Dob_label.grid(row=2, column=2, padx=10,pady=10,sticky=W)

         Dob_entry = ttk.Entry(curren_course_frame,textvariable=self.var_dob,width=20, font=("times new roman ",12, "bold"))
         Dob_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)
            
         # Email  

         email_label=Label(curren_course_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
         email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

         email_entry=ttk.Entry(curren_course_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
         email_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)     

         # Phone No

         phone_label = Label(curren_course_frame,text="Phone No", font=("times new roman", 12, "bold"), bg="white")
         phone_label.grid(row=3, column=2, padx=10,pady=10,sticky=W)

         phone_entry = ttk.Entry(curren_course_frame,textvariable=self.var_phone,width=20, font=("times new roman ",12, "bold"))
         phone_entry.grid(row=3,column=3,padx=2,pady=10,sticky=W)

         # Address

         Adress_label = Label(curren_course_frame,text="Address", font=("times new roman", 12, "bold"), bg="white")
         Adress_label.grid(row=4, column=0, padx=10,pady=10,sticky=W)

         Adress_entry = ttk.Entry(curren_course_frame,textvariable=self.var_address,width=20, font=("times new roman ",12, "bold"))
         Adress_entry.grid(row=4,column=1,padx=2,pady=10,sticky=W)

         # Teacher Name

         Teacher_label = Label(curren_course_frame,text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
         Teacher_label.grid(row=4, column=2, padx=10,pady=10,sticky=W)

         Teacher_entry = ttk.Entry(curren_course_frame,width=20,textvariable=self.var_teacher, font=("times new roman ",12, "bold"))
         Teacher_entry.grid(row=4,column=3,padx=2,pady=10,sticky=W)


         # Radio Buttons

         self.var_radio = StringVar()  

         radio1 = ttk.Radiobutton(curren_course_frame, text="Take Photo Sample", variable=self.var_radio, value="Yes")
         radio1.grid(row=6, column=0)

         radio2 = ttk.Radiobutton(curren_course_frame, text="No Photo Sample", variable=self.var_radio, value="No")
         radio2.grid(row=6, column=1)


         # Button Frame
 
         btn_frame = Frame(curren_course_frame,bd=2,relief=RIDGE, bg="white")
         btn_frame.place(x=3, y=260, width=875, height= 85)

         save_btn = Button(btn_frame, text="Save",command=self.add_data, font=("times new roman", 12, "bold"), bg="blue", fg="white", width=23)
         save_btn.grid(row=0,column=0)

         update_btn = Button(btn_frame, text="Update", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=24)
         update_btn.grid(row=0,column=1)

         reset_btn = Button(btn_frame, text="Reset", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=24)
         reset_btn.grid(row=0,column=2)

         delete_btn = Button(btn_frame, text="Delete", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=24)
         delete_btn.grid(row=0 ,column=3)

         btn_frame1 = Frame(curren_course_frame,bd=2,relief=RIDGE, bg="white")
         btn_frame1.place(x=3, y=298, width=875, height=35)

         take_photo_btn = Button(btn_frame1, text="Take a Photo Sample", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=51)
         take_photo_btn.grid(row=0 ,column=0)

         Update_photo_btn = Button(btn_frame1, text="Update a photo", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=51)
         Update_photo_btn.grid(row=0 ,column=1)
 






         # right Label Frame

         right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"), bg="white")
         right_frame.place(x=960, y=10, width=900, height=750)

         image_right = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/student6.jpg")
         image_right = image_right.resize((890,150))
         self.photoimg_right = ImageTk.PhotoImage(image_right)

         f_label=Label(right_frame,image=self.photoimg_right)
         f_label.place(x=4,y=10,width=890,height=150)


         # Search System

         search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"), bg="white")
         search_frame.place(x=4, y=154, width=890, height=70)

         search_label = Label(search_frame,text="Search By", font=("times new roman", 12, "bold"), bg="white",fg="red")
         search_label.grid(row=0, column=0, padx=15,pady=10,sticky=W)

         search_combo = ttk.Combobox(search_frame,textvariable=self.var_search_by,font=("times new roman ",12, "bold"),width=19, state="readonly")
         search_combo["values"] = ("Select", "Roll No", "Phone No",  "Student ID")
         search_combo.current(0)
         search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         search_entry = ttk.Entry(search_frame,width=24,textvariable=self.var_search_txt,font=("times new roman ",12, "bold"))
         search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W)

         search_btn = Button(search_frame, text="Search", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=20)
         search_btn.grid(row=0,column=3,padx=2)
         
         showall_btn = Button(search_frame, text="Show All", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=20)
         showall_btn.grid(row=0,column=4,padx=2)
         
         # Table Frame

         table_frame = Frame(right_frame,bd=2,relief=RIDGE, bg="white")
         table_frame.place(x=4, y=230, width=890, height=495)
         
         scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y = Scrollbar(table_frame,orient=VERTICAL)
         self.student_table = ttk.Treeview(table_frame,columns=("student_id","dep","course","year","sem","id","name","div","roll","gen","dob","email","phone","add","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set )
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_x.config(command=self.student_table.xview)
         scroll_y.config(command=self.student_table.yview)
         self.student_table.heading("student_id",text="Student ID")
         self.student_table.heading("dep",text="Department")
         self.student_table.heading("course",text="Course")
         self.student_table.heading("year",text="Year")
         self.student_table.heading("sem",text="Semester")
         self.student_table.heading("id",text="Student ID")
         self.student_table.heading("name",text="Student Name")
         self.student_table.heading("div",text="Class Division")
         self.student_table.heading("roll",text="Roll No")
         self.student_table.heading("email",text="Email")
         self.student_table.heading("phone",text="Phone No")
         self.student_table.heading("add",text="Address")
         self.student_table.heading("teacher",text="Teacher")
         self.student_table.heading("photo",text="PhotoSampleStatus")
         self.student_table.heading("gen", text="Gender")  
         self.student_table.heading("dob", text="DOB")

         self.student_table["show"]="headings"

         self.student_table.column("student_id",width=100)
         self.student_table.column("dep",width=100)
         self.student_table.column("course",width=100)
         self.student_table.column("year",width=100)
         self.student_table.column("sem",width=100)
         self.student_table.column("id",width=120)
         self.student_table.column("name",width=120)
         self.student_table.column("div",width=120)
         self.student_table.column("roll",width=100)
         self.student_table.column("gen",width=100)
         self.student_table.column("dob",width=100)
         self.student_table.column("email",width=100)
         self.student_table.column("phone",width=100)
         self.student_table.column("add",width=100)
         self.student_table.column("teacher",width=100)
         self.student_table.column("photo",width=140)
        
         self.student_table.pack(fill=BOTH,expand=1)
         self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

    #function to fetch data from database

   
         self.fetch_data()  # Load initial data when app starts

    def add_data(self):
        if self.var_dep.get() == "" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                conn = sqlite3.connect("student.db")  # Ensure you have a database file named 'student.db'
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO student (dep, course, year, semester, id, name, div, roll, gender, dob, email, phone, address, teacher, photo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio.get(),
                    ),
                )
                conn.commit()
                conn.close()
                self.fetch_data()  # Refresh table
                messagebox.showinfo("Success", "Record has been added successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error while adding record: {e}")

    def fetch_data(self):
        try:
            conn = sqlite3.connect("student.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())  # Clear previous data
                for row in rows:
                    self.student_table.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error while fetching data: {e}")

    def reset(self):
        self.var_dep.set("Select Department")
        self.var_course.set("")
        self.var_year.set("")
        self.var_semester.set("")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio.set("")

    #get cursor

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        row=content["values"]
        self.var_dep.set(row[0])
        self.var_course.set(row[1])
        self.var_year.set(row[2])
        self.var_semester.set(row[3])
        self.var_std_id.set(row[4])
        self.var_std_name.set(row[5])
        self.var_div.set(row[6])
        self.var_roll.set(row[7])
        self.var_gender.set(row[8])
        self.var_dob.set(row[9])
        self.var_email.set(row[10])
        self.var_phone.set(row[11])
        self.var_address.set(row[12])
        self.var_teacher.set(row[13])
        self.var_radio.set(row[14])



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
         