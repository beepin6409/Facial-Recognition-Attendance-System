from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #(1530 is width , 790 is height, +0 +0 is x axis and yaxis starting from top left corner )
        root.configure(bg='#B0E0E6')
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text='Face Recognition',font=('times new roman',35,'bold'),fg='green')
        title_lbl.place(x=0,y=0,width=1530, height= 45)

        b1 = Button(self.root,command=self.face_recog, text="Face Recognition", cursor="hand2",font=('times new roman',20,'bold'),fg='white',bg='lightgreen')
        b1.place(x=600,y=385,width=300,height=50)

    def mark_attendance(self,roll,name,department):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])

            if((roll not in name_list)) and (name not in name_list) and (department not in name_list):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{roll},{name},{department},{dtString},{d1},Present")






    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf):
            # Ensure the image is not empty
            if img is None or img.size == 0:
                print("Empty frame captured")
                return []

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host='localhost', 
                    user="root", 
                    password='R00tpp123..Abc', 
                    database='face_recognition', 
                    auth_plugin='mysql_native_password'
                )
                my_cursor = conn.cursor()

                # Safeguard database queries
                my_cursor.execute("SELECT Name, Department, RollNo FROM student WHERE RollNo = %s", (str(id),))
                result = my_cursor.fetchone()
                
                if result is not None:
                    name, department, rollno = result
                else:
                    name, department, rollno = "Unknown", "Unknown", "Unknown"
                
                my_cursor.execute("SELECT RollNo FROM student WHERE RollNo = %s", (str(id),))
                i = my_cursor.fetchone()
                i="+".join(i)



                if confidence > 77:
                    cv2.putText(img, f"Roll : {rollno}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name : {name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department : {department}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(rollno,name,department)

                else:
                    # Corrected the rectangle drawing and text for unknown face
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()

            if not ret:
                print("Failed to capture video.")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to break
                break

        # Release resources after the loop ends
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()