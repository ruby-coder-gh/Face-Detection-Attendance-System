from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self,root):
         self.root = root
         self.root.geometry("2530x900+0+0")
         self.root.title("Face Recognition System")
         
         # 1st image

         img1 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/facial-recognition-system-concept-with-face-recognition-3d-scanning-interface.jpg")
         img1 = img1.resize((500,130))
         self.photoimg1 = ImageTk.PhotoImage(img1)

         f_lbl = Label(self.root, image=self.photoimg1)
         f_lbl.place(x=0, y=0, width=500, height=130)

        # 2nd image

         img2 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/images (1).jpeg")
         img2 = img2.resize((500,130))
         self.photoimg2 = ImageTk.PhotoImage(img2)

         f_lbl = Label(self.root, image=self.photoimg2)
         f_lbl.place(x=500, y=0, width=500, height=130)

         # 3rd image

         img3 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/face-recognition-attendance-system.jpg")
         img3 = img3.resize((500,130))
         self.photoimg3 = ImageTk.PhotoImage(img3)

         f_lbl = Label(self.root, image=self.photoimg3)
         f_lbl.place(x=1000, y=0, width=500, height=130)

         # 4th image


         img = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/1_E5rexDhotCqksxqT4LKwyQ.jpg")
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

         title_lbl = Label(bgimage,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
         title_lbl.place(x=0, y=0, width=2000, height=45)


        # Student Details
         img5 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/—Pngtree—a handsome and young graduate_15457950.png")
         img5 = img5.resize((220,220))
         self.photoimg5 = ImageTk.PhotoImage(img5)

         b1 = Button(bgimage, image=self.photoimg5,command=self.Student_details, cursor="hand2")
         b1.place(x=200, y=100, width=220, height=220)

         b1 = Button(bgimage,text="Student Details", cursor="hand2",command=self.Student_details, font=("times new roman", 15, "bold"), bg="RoyalBlue", fg="white")
         b1.place(x=200, y=300, width=220, height=40)

        # Face detection
         img6 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/facial-recognition-system-concept-with-face-recognition-3d-scanning-interface.jpg")
         img6 = img6.resize((220,220))
         self.photoimg6 = ImageTk.PhotoImage(img6)

         b1 = Button(bgimage, image=self.photoimg6, cursor="hand2")
         b1.place(x=600, y=100, width=220, height=220)

         b1 = Button(bgimage,text="Face detection", cursor="hand2", font=("times new roman", 15, "bold"), bg="RoyalBlue", fg="white")
         b1.place(x=600, y=300, width=220, height=40)

        # Attendance
         img7 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/attendance.jpg")
         img7 = img7.resize((220,220))
         self.photoimg7 = ImageTk.PhotoImage(img7)
    
         b1 = Button(bgimage, image=self.photoimg7, cursor="hand2")
         b1.place(x=1000, y=100, width=220, height=220)
    
         b1 = Button(bgimage,text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="RoyalBlue", fg="white")
         b1.place(x=1000, y=300, width=220, height=40)

        # Help Desk
         img8 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/help.jpg")
         img8 = img8.resize((220,220))
         self.photoimg8 = ImageTk.PhotoImage(img8)
        
         b1 = Button(bgimage, image=self.photoimg8, cursor="hand2")
         b1.place(x=1400, y=100, width=220, height=220)
        
         b1 = Button(bgimage,text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="RoyalBlue", fg="white")
         b1.place(x=1400, y=300, width=220, height=40)

        # Train Data
         img9 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/train.jpg")
         img9 = img9.resize((220,220))
         self.photoimg9 = ImageTk.PhotoImage(img9)
            
         b1 = Button(bgimage, image=self.photoimg9, cursor="hand2")
         b1.place(x=200, y=480, width=220, height=220)
            
         b1 = Button(bgimage,text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="RoyalBlue", fg="white")
         b1.place(x=200, y=680, width=220, height=40)

        # Photos
         img10 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/photos.jpg")
         img10 = img10.resize((220,220))
         self.photoimg10 = ImageTk.PhotoImage(img10)
                    
         b1 = Button(bgimage, image=self.photoimg10, cursor="hand2")
         b1.place(x=600, y=480, width=220, height=220)
                    
         b1 = Button(bgimage,text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="RoyalBlue", fg="white")
         b1.place(x=600, y=680, width=220, height=40)

        # Developer
         img11 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/developer.jpeg")
         img11 = img11.resize((220,220))
         self.photoimg11 = ImageTk.PhotoImage(img11)
                            
         b1 = Button(bgimage, image=self.photoimg11, cursor="hand2")
         b1.place(x=1000, y=480, width=220, height=220)
                            
         b1 = Button(bgimage,text="Developer", cursor="hand2", font=("times new roman", 15, "bold "), bg="RoyalBlue", fg="white")
         b1.place(x=1000, y=680, width=220, height=40)
         
        # Exit
         img12 = Image.open("/home/ruby/Project/Face-Detection-Attendance-System/Photos/exit.jpg")
         img12 = img12.resize((220,220))
         self.photoimg12 = ImageTk.PhotoImage(img12)
                                    
         b1 = Button(bgimage, image=self.photoimg12, cursor="hand2")
         b1.place(x=1400, y=480, width=220, height=220)
                                    
         b1 = Button(bgimage,text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="RoyalBlue", fg="white")
         b1.place(x=1400, y=680, width=220, height=40)

    def Student_details(self):
             self.new_window = Toplevel(self.root)
             self.app = Student(self.new_window)

     

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
         