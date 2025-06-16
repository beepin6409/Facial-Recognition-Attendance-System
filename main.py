#tkinter is a python library that can be used to construct basic GUI applications.
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
import os

class Face_recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #(1530 is width , 790 is height, +0 +0 is x axis and yaxis starting from top left corner )
        root.configure(bg='#B0E0E6')
        self.root.title("Face Recognition System")


        #first image
        img = Image.open(r"C:\Users\KIIT01\Downloads\Face recognition\Image 1.png")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img=img.resize((490,300),Image.ANTIALIAS)  # ANTIALIAS converts high level image into low levels
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=10,y=0,width=490,height=300)

        #second image
        img1 = Image.open(r"C:\Users\KIIT01\Downloads\Face recognition\Image 2.jpg")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img1=img1.resize((490,300),Image.ANTIALIAS)  # ANTIALIAS converts high level image into low levels
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=520,y=0,width=490,height=300)

        #third image
        img2 = Image.open(r"C:\Users\KIIT01\Downloads\Face recognition\image_3.png")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img2=img2.resize((500,300),Image.ANTIALIAS)  # ANTIALIAS converts high level image into low levels
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=1030,y=0,width=490,height=300)

        #title name
        title_lbl = Label(self.root, text='Face Recognition Attendance System',font=('times new roman',35,'bold'),fg='green')
        title_lbl.place(x=10,y=310,width=1530, height= 55)

        #student button
        img4 = Image.open(r"C:\Users\KIIT01\Downloads\Face recognition\add_student.png")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img4=img4.resize((350,100),Image.ANTIALIAS)  # ANTIALIAS converts high level image into low levels
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Label(self.root, image = self.photoimg4)
        b1.place(x=100,y=380,width=350,height=100)

        b1_1 = Button(self.root, text="Add Student Details", command=self.student_details,cursor="hand2",font=('times new roman',15,'bold'),fg='white',bg='lightgreen')
        b1_1.place(x=100,y=480,width=350,height=50)

        #Add New face button
        img5 = Image.open(r"C:\Users\KIIT01\Downloads\Face recognition\face detection.webp")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img5=img5.resize((350,100),Image.ANTIALIAS)  # ANTIALIAS converts high level image into low levels
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Label(self.root, image = self.photoimg5)
        b2.place(x=600,y=380,width=350,height=100)

        b2_1 = Button(self.root,command=self.face_recognize, text="Recognize Face", cursor="hand2",font=('times new roman',15,'bold'),fg='white',bg='lightgreen')
        b2_1.place(x=600,y=480,width=350,height=50)

        #Mark Attendance button
        img6 = Image.open(r"C:\Users\KIIT01\Downloads\Face recognition\Attendance_2 (1).jpg")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img6=img6.resize((350,100),Image.ANTIALIAS)  # ANTIALIAS converts high level image into low levels
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Label(self.root, image = self.photoimg6)
        b2.place(x=1100,y=380,width=350,height=100)

        b2_1 = Button(self.root,command=self.attendance_list, text="Attendance List", cursor="hand2",font=('times new roman',15,'bold'),fg='white',bg='lightgreen')
        b2_1.place(x=1100,y=480,width=350,height=50)

        #Train Data
        img7 = Image.open(r"C:\Users\KIIT01\Downloads\Face recognition\images.jpg")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img7=img7.resize((350,100),Image.ANTIALIAS)  # ANTIALIAS converts high level image into low levels
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b2 = Label(self.root, image = self.photoimg7)
        b2.place(x=100,y=580,width=350,height=100)

        b2_1 = Button(self.root, command=self.train_photos,text="Train Data", cursor="hand2",font=('times new roman',15,'bold'),fg='white',bg='lightgreen')
        b2_1.place(x=100,y=680,width=350,height=50)

        #Photos Database
        img8 = Image.open(r"C:\Users\KIIT01\Downloads\Face recognition\images (1).jpg")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img8=img8.resize((350,100),Image.ANTIALIAS)  # ANTIALIAS converts high level image into low levels
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2 = Label(self.root, image = self.photoimg8)
        b2.place(x=600,y=580,width=350,height=100)

        b2_1 = Button(self.root,command=self.open_img, text="Photos Database", cursor="hand2",font=('times new roman',15,'bold'),fg='white',bg='lightgreen')
        b2_1.place(x=600,y=680,width=350,height=50)

        #Developers Details
        img9 = Image.open(r"C:\Users\KIIT01\Downloads\Face recognition\developer.jpg")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img9=img9.resize((350,100),Image.ANTIALIAS)  # ANTIALIAS converts high level image into low levels
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2 = Label(self.root, image = self.photoimg9)
        b2.place(x=1100,y=580,width=350,height=100)

        b2_1 = Button(self.root, text="Developer Details", cursor="hand2",font=('times new roman',15,'bold'),fg='white',bg='lightgreen')
        b2_1.place(x=1100,y=680,width=350,height=50)


    def open_img(self):
        os.startfile("data")

    # Function Buttons

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    def train_photos(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    def face_recognize(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)
    def attendance_list(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)







if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_System(root)
    root.mainloop()




