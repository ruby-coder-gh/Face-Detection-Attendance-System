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
         dep_combo.grid(row=0,column=1)


         # right Label Frame

         right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"), bg="white")
         right_frame.place(x=960, y=10, width=900, height=750)

         

           
         


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
         