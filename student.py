from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self,root):
         self.root = root
         self.root.geometry("2530x900+0+0")
         self.root.title("Student Management System")
         
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

         dep_combo = ttk.Combobox(curren_course_frame,font=("times new roman ",12, "bold"),width=17, state="readonly")
         dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical", "Electrical")
         dep_combo.current(0)
         dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

         # Course

         course_label = Label(curren_course_frame,text="Course", font=("times new roman", 12, "bold"), bg="white")
         course_label.grid(row=0, column=2, padx=10,pady=10,sticky=W)

         course_combo = ttk.Combobox(curren_course_frame,font=("times new roman ",12, "bold"),width=17, state="readonly")
         course_combo["values"] = ("Select Course", "BCA", "BBA", "B.Tech", "MBA", "MCA")
         course_combo.current(0)
         course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

         # year

         year_label = Label(curren_course_frame,text="Year", font=("times new roman", 12, "bold"), bg="white")
         year_label.grid(row=1, column=0, padx=10,pady=10,sticky=W)

         year_combo = ttk.Combobox(curren_course_frame,font=("times new roman ",12, "bold"),width=17, state="readonly")
         year_combo["values"] = ("Select Year", "1st", "2nd", "3rd", "4th", "5th")
         year_combo.current(0)
         year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
     
         # Semester

         semester_label = Label(curren_course_frame,text="Semester", font=("times new roman", 12, "bold"), bg="white")
         semester_label.grid(row=1, column=2, padx=10,pady=10,sticky=W)

         semester_combo = ttk.Combobox(curren_course_frame,font=("times new roman ",12, "bold"),width=17, state="readonly")
         semester_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th")
         semester_combo.current(0)
         semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
         
         # Class Student Information
         curren_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"), bg="white")
         curren_course_frame.place(x=4, y=354, width=890, height=370)
  
         # Student ID

         Student_id_label = Label(curren_course_frame,text="Student ID", font=("times new roman", 12, "bold"), bg="white")
         Student_id_label.grid(row=0, column=0, padx=10,pady=10,sticky=W)

         Student_id_entry = ttk.Entry(curren_course_frame,width=20, font=("times new roman ",12, "bold"))
         Student_id_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         # Student Name

         Student_name_label = Label(curren_course_frame,text="Student Name", font=("times new roman", 12, "bold"), bg="white")
         Student_name_label.grid(row=0, column=2, padx=10,pady=10,sticky=W) 
         Student_name_entry = ttk.Entry(curren_course_frame,width=20, font=("times new roman ",12, "bold"))
         Student_name_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

         # Class Division

         Class_div_label = Label(curren_course_frame,text="Class Division", font=("times new roman", 12, "bold"), bg="white")
         Class_div_label.grid(row=1, column=0, padx=10,pady=10,sticky=W)

         Class_div_entry = ttk.Entry(curren_course_frame,width=20, font=("times new roman ",12, "bold"))
         Class_div_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)


         # Roll No

         Roll_no_label = Label(curren_course_frame,text="Roll No", font=("times new roman", 12, "bold"), bg="white")
         Roll_no_label.grid(row=1, column=2, padx=10,pady=10,sticky=W)

         Roll_no_entry = ttk.Entry(curren_course_frame,width=20, font=("times new roman ",12, "bold "))
         Roll_no_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)
         
         # Gender
         
         Gender_label = Label(curren_course_frame,text="Gender", font=("times new roman", 12, "bold"), bg="white")
         Gender_label.grid(row=2, column=0, padx=10,pady=10,sticky=W)

         Gender_entry = ttk.Entry(curren_course_frame,width=20, font=("times new roman ",12, "bold"))
         Gender_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

         # DOB

         Dob_label = Label(curren_course_frame,text="DOB", font=("times new roman", 12, "bold"), bg="white")
         Dob_label.grid(row=2, column=2, padx=10,pady=10,sticky=W)

         Dob_entry = ttk.Entry(curren_course_frame,width=20, font=("times new roman ",12, "bold"))
         Dob_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)
            
         # Email  

         email_label=Label(curren_course_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
         email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

         email_entry=ttk.Entry(curren_course_frame,width=20,font=("times new roman",12,"bold"))
         email_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)     

         # Phone No

         phone_label = Label(curren_course_frame,text="Phone No", font=("times new roman", 12, "bold"), bg="white")
         phone_label.grid(row=3, column=2, padx=10,pady=10,sticky=W)

         phone_entry = ttk.Entry(curren_course_frame,width=20, font=("times new roman ",12, "bold"))
         phone_entry.grid(row=3,column=3,padx=2,pady=10,sticky=W)

         # Address

         Adress_label = Label(curren_course_frame,text="Address", font=("times new roman", 12, "bold"), bg="white")
         Adress_label.grid(row=4, column=0, padx=10,pady=10,sticky=W)

         Adress_entry = ttk.Entry(curren_course_frame,width=20, font=("times new roman ",12, "bold"))
         Adress_entry.grid(row=4,column=1,padx=2,pady=10,sticky=W)

         # Teacher Name

         Teacher_label = Label(curren_course_frame,text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
         Teacher_label.grid(row=4, column=2, padx=10,pady=10,sticky=W)

         Teacher_entry = ttk.Entry(curren_course_frame,width=20, font=("times new roman ",12, "bold"))
         Teacher_entry.grid(row=4,column=3,padx=2,pady=10,sticky=W)


         # Radio Buttons

         self.var_radio1 = StringVar()
         radio1 = ttk.Radiobutton(curren_course_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
         radio1.grid(row=6,column=0)

         radio2 = ttk.Radiobutton(curren_course_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
         radio2.grid(row=6,column=1)

         # Button Frame
 
         btn_frame = Frame(curren_course_frame,bd=2,relief=RIDGE, bg="white")
         btn_frame.place(x=3, y=260, width=875, height=85)

         save_btn = Button(btn_frame, text="Save", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=23)
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

         

           
         


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
         