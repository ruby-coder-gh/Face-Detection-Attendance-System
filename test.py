from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")

        # Images for dynamic resizing
        self.img1_path = "/home/ruby/Project/Photos/facial-recognition-system-concept-with-face-recognition-3d-scanning-interface.jpg"
        self.img2_path = "/home/ruby/Project/Photos/images (1).jpeg"
        self.img3_path = "/home/ruby/Project/Photos/face-recognition-attendance-system.jpg"
        self.img4_path = "/home/ruby/Project/Photos/ezgif.com-gif-maker-6 (1).jpeg"
        self.img5_path = "/home/ruby/Project/Photos/—Pngtree—a handsome and young graduate_15457950.png"
        self.img6_path = "Photos/istockphoto-1216528683-612x612.jpg"

        self.initialize_ui()

        # Bind the resize event
        self.root.bind("<Configure>", self.on_resize)

    def initialize_ui(self):
        # Placeholders for dynamic elements
        self.f_lbl1 = Label(self.root)
        self.f_lbl1.place(x=0, y=0, width=500, height=130)

        self.f_lbl2 = Label(self.root)
        self.f_lbl2.place(x=500, y=0, width=500, height=130)

        self.f_lbl3 = Label(self.root)
        self.f_lbl3.place(x=1000, y=0, width=500, height=130)

        self.bgimage = Label(self.root)
        self.bgimage.place(x=0, y=130, width=2000, height=900)

        self.title_lbl = Label(self.bgimage, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                               font=("times new roman", 35, "bold"), bg="white", fg="red")
        self.title_lbl.place(x=0, y=0, width=2000, height=45)

        # Student Details
        self.b1_image = Button(self.bgimage, cursor="hand2")
        self.b1_image.place(x=200, y=100, width=220, height=220)

        self.b1_text = Button(self.bgimage, text="Student Details", cursor="hand2",
                              font=("times new roman", 15, "bold"), bg="RoyalBlue", fg="white")
        self.b1_text.place(x=200, y=300, width=220, height=40)

        # Face Detection
        self.b2_image = Button(self.bgimage, cursor="hand2")
        self.b2_image.place(x=600, y=100, width=220, height=220)

        self.b2_text = Button(self.bgimage, text="Face detection", cursor="hand2",
                              font=("times new roman", 15, "bold"), bg="RoyalBlue", fg="white")
        self.b2_text.place(x=600, y=300, width=220, height=40)

        # Load initial images
        self.update_images()

    def update_images(self):
        # Resize and update images dynamically
        img1 = Image.open(self.img1_path).resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        self.f_lbl1.config(image=self.photoimg1)

        img2 = Image.open(self.img2_path).resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        self.f_lbl2.config(image=self.photoimg2)

        img3 = Image.open(self.img3_path).resize((500, 130))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        self.f_lbl3.config(image=self.photoimg3)

        img4 = Image.open(self.img4_path).resize((self.root.winfo_width(), self.root.winfo_height() - 130))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        self.bgimage.config(image=self.photoimg4)

        img5 = Image.open(self.img5_path).resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        self.b1_image.config(image=self.photoimg5)

        img6 = Image.open(self.img6_path).resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        self.b2_image.config(image=self.photoimg6)

    def on_resize(self, event):
        # Update background and layout on window resize
        self.update_images()
        canvas_width = self.root.winfo_width()
        canvas_height = self.root.winfo_height()

        # Adjust background title width
        self.title_lbl.place(width=canvas_width, height=45)
        self.bgimage.place(width=canvas_width, height=canvas_height - 130)

        # Recalculate button positions if needed
        # Example: Keep buttons proportional to screen size
        self.b1_image.place(x=canvas_width // 10, y=100, width=220, height=220)
        self.b1_text.place(x=canvas_width // 10, y=300, width=220, height=40)

        self.b2_image.place(x=canvas_width // 2, y=100, width=220, height=220)
        self.b2_text.place(x=canvas_width // 2, y=300, width=220, height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
