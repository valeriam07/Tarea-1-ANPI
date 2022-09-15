from mimetypes import common_types
import tkinter as tk
from tkinter import ttk as tkk
from tkinter.font import BOLD, Font

import funtras as mn

# Class that creates all the interface stuff and contains
#functions to run the gui program correctly
class App(tk.Tk):
    # ----- Class Variables-----
    
    textX=""
    textY=""
    result=""
    
    # Initialize the GUI with principle values and call the functions to setup the interface
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Calculator')
        self.geometry('420x520')
        self.load_designs()
        self.load_Canvas()
        self.load_elements_Canva1()
        self.load_elements_Canva2()
        self.load_elements_Canva3()

    # Sets the styles to be used by the components 
    def load_designs(self):
        # button style
        style = tkk.Style()
 
        style.configure('TButton', font =
                    ('calibri', 13, 'bold'),
                            borderwidth = '3')
        self.bold25 = Font(self.master, size=23, weight="normal",family="Helvetica")
        self.bold26 = Font(self.master, size=11, weight="normal",family="Helvetica")
        
        # Changes will be reflected
        # by the movement of mouse.
        style.map('TButton', foreground = [('active', '!disabled', 'green')],
                            background = [('active', 'black')])

    # Creates all canvas of the interface where the elements are placed
    def load_Canvas(self):
        #---------------------------------- Canvas in Main Window -------------------------------------
        self.canva1 = tk.Canvas(self, height=190, width=650)
        self.canva1.pack()
        self.canva2 = tk.Canvas(self, bg="#BABABA", height=250, width=420)
        self.canva2.pack()
        self.canva4 = tk.Canvas(self, height=10, width=420)
        self.canva4.pack()
        self.canva3 = tk.Canvas(self, bg="#999999", height=250, width=420)
        self.canva3.pack()

        self.checkbox1_value = tk.BooleanVar(self.canva1)
        self.checkbox1_value.set(False)

        self.checkbox2_value = tk.BooleanVar(self.canva1)
        self.checkbox2_value.set(False)

    # Sets all elements in the first Canva created
    # Contains labels and checkbox where the user can see the numbers to be calculated
    def load_elements_Canva1(self):
        #------------------------ Elements First Canva ---------------------------------
        self.label2 = tkk.Label(self.canva1,text="Basic Calculator",font=self.bold25, foreground='#476063')
        self.label2.place(x=100, y=10)
        self.buttonHelp= tk.Button(self.canva1, text="Help", width=20,command=self.openNewWindow, bg='#476063',fg='white')
        self.buttonHelp.place(x=15, y=10, width=50, height=30)
        self.buttonClear= tk.Button(self.canva1, text="Clear", command=self.clearText, bg='#736B68',fg='white')
        self.buttonClear.place(x=100, y=150, width=220, height=23)

        #-------------------------- Input label and entry's ----------------------------
        self.labelX=tkk.Label(self.canva1, text="X =",font=self.bold26)
        self.labelX.place(x=100,y=60)
        self.labelY=tkk.Label(self.canva1, text="Y =",font=self.bold26)
        self.labelY.place(x=100,y=90)
        self.labelResult= tkk.Label(self.canva1, text="Answer =",font=self.bold26)
        self.labelResult.place(x=100,y=120)

        self.InputX = tk.Label(self.canva1,borderwidth=2, relief="groove",width=15)
        self.InputX.place(x=170,y=60)
        self.InputY = tk.Label(self.canva1,borderwidth=2, relief="groove",width=15)
        self.InputY.place(x=170,y=90)
        self.InputResult=tk.Label(self.canva1,borderwidth=2, relief="groove",width=15)
        self.InputResult.place(x=170,y=120)

        self.checkbox1 = tkk.Checkbutton(self, text="",variable=self.checkbox1_value, command=lambda: self.check(1))
        self.checkbox1.place(x=290, y=60)
        self.checkbox2 = tkk.Checkbutton(self, text="",variable=self.checkbox2_value, command=lambda: self.check(2))
        self.checkbox2.place(x=290, y=90)

    
    #Set all elements in the second canva created
    #Contains the buttons related to the functions implemented
    def load_elements_Canva2(self):
        #------------------------ Elements Second Canva ---------------------------------
        self.button1= tk.Button(self.canva2, text="senh(x)",width=15,command=lambda:self.function(1))
        self.button1.grid(row=0, column=0,padx=1, pady=1)
        self.button2= tk.Button(self.canva2, text="cosh(x)",width=15,command=lambda:self.function(2))
        self.button2.grid(row=0, column=1,padx=1, pady=1)
        self.button3= tk.Button(self.canva2, text="tanh(x)",width=15,command=lambda:self.function(3))
        self.button3.grid(row=0, column=2,padx=1, pady=1)
        self.button4= tk.Button(self.canva2, text="asen(x)",width=15,command=lambda:self.function(4))
        self.button4.grid(row=1, column=0,padx=1, pady=1)
        self.button5= tk.Button(self.canva2, text="acos(x)",width=15,command=lambda:self.function(5))
        self.button5.grid(row=1, column=1,padx=1, pady=1)
        self.button6= tk.Button(self.canva2, text="atan(x)",width=15,command=lambda:self.function(6))
        self.button6.grid(row=1, column=2,padx=1, pady=1)
        self.button7= tk.Button(self.canva2, text="sec(x)",width=15,command=lambda:self.function(7))
        self.button7.grid(row=2, column=0,padx=1, pady=1)
        self.button8= tk.Button(self.canva2, text="csc(x)",width=15,command=lambda:self.function(8))
        self.button8.grid(row=2, column=1,padx=1, pady=1)
        self.button9= tk.Button(self.canva2, text="cot(x)",width=15,command=lambda:self.function(9))
        self.button9.grid(row=2, column=2,padx=1, pady=1)
        self.button10= tk.Button(self.canva2, text="sen(x)",width=15,command=lambda:self.function(10))
        self.button10.grid(row=3, column=0,padx=1, pady=1)
        self.button11= tk.Button(self.canva2, text="cos(x)",width=15,command=lambda:self.function(11))
        self.button11.grid(row=3, column=1,padx=1, pady=1)
        self.button12= tk.Button(self.canva2, text="tan(x)",width=15,command=lambda:self.function(12))
        self.button12.grid(row=3, column=2,padx=1, pady=1)
        self.button13= tk.Button(self.canva2, text="ln(x)",width=15,command=lambda:self.function(13))
        self.button13.grid(row=4, column=0,padx=1, pady=1)
        self.button14= tk.Button(self.canva2, text="log_10(x)",width=15,command=lambda:self.function(14))
        self.button14.grid(row=4, column=1,padx=1, pady=1)
        self.button15= tk.Button(self.canva2, text="log_y(x)",width=15,command=lambda:self.function(15))
        self.button15.grid(row=4, column=2,padx=1, pady=1)
        self.button16= tk.Button(self.canva2, text="1/x",width=15,command=lambda:self.function(16))
        self.button16.grid(row=5, column=0,padx=1, pady=1)
        self.button17= tk.Button(self.canva2, text="√x",width=15,command=lambda:self.function(17))
        self.button17.grid(row=5, column=1,padx=1, pady=1)
        self.button18= tk.Button(self.canva2, text="y√x",width=15,command=lambda:self.function(18))
        self.button18.grid(row=5, column=2,padx=1, pady=1)
        self.button19= tk.Button(self.canva2, text="exp(x)",width=15,command=lambda:self.function(19))
        self.button19.grid(row=6, column=0,padx=1, pady=1)
        self.button20= tk.Button(self.canva2, text="x^y",width=15,command=lambda:self.function(20))
        self.button20.grid(row=6, column=1,padx=1, pady=1)
        self.button21= tk.Button(self.canva2, text="x!",width=15,command=lambda:self.function(21))
        self.button21.grid(row=6, column=2,padx=1, pady=1)
    
    #Set all elements in the third canva created
    #Contains the buttons related to the numbers and values that can be used by the user
    def load_elements_Canva3(self):
        #------------------------ Elements Second Canva ---------------------------------
        self.btn1= tk.Button(self.canva3, text="1",width=15,command=lambda: self.addNum("1"))
        self.btn1.grid(row=0, column=0,padx=1, pady=1)
        self.btn2= tk.Button(self.canva3, text="2",width=15,command=lambda: self.addNum("2"))
        self.btn2.grid(row=0, column=1,padx=1, pady=1)
        self.btn3= tk.Button(self.canva3, text="3",width=15,command=lambda: self.addNum("3"))
        self.btn3.grid(row=0, column=2,padx=1, pady=1)
        self.btn4= tk.Button(self.canva3, text="4",width=15,command=lambda: self.addNum("4"))
        self.btn4.grid(row=1, column=0,padx=1, pady=1)
        self.btn5= tk.Button(self.canva3, text="5",width=15,command=lambda: self.addNum("5"))
        self.btn5.grid(row=1, column=1,padx=1, pady=1)
        self.btn6= tk.Button(self.canva3, text="6",width=15,command=lambda: self.addNum("6"))
        self.btn6.grid(row=1, column=2,padx=1, pady=1)
        self.btn7= tk.Button(self.canva3, text="7",width=15,command=lambda: self.addNum("7"))
        self.btn7.grid(row=2, column=0,padx=1, pady=1)
        self.btn8= tk.Button(self.canva3, text="8",width=15,command=lambda: self.addNum("8"))
        self.btn8.grid(row=2, column=1,padx=1, pady=1)
        self.btn9= tk.Button(self.canva3, text="9",width=15,command=lambda: self.addNum("9"))
        self.btn9.grid(row=2, column=2,padx=1, pady=1)
        self.btnpi= tk.Button(self.canva3, text="π",width=15,command=lambda: self.addNum("π"))
        self.btnpi.grid(row=3, column=0,padx=1, pady=1)
        self.btn0= tk.Button(self.canva3, text="0",width=15,command=lambda: self.addNum("0"))
        self.btn0.grid(row=3, column=1,padx=1, pady=1)
        self.btndot= tk.Button(self.canva3, text=".",width=15,command=lambda: self.addNum("."))
        self.btndot.grid(row=3, column=2,padx=1, pady=1)

    # Open a new window that is activated with the button Help
    # Contains instructions for use
    def openNewWindow(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("Help")
        newWindow.geometry("450x300")
    
        # ------------ Elements of the window ----------------
        label1= tk.Label(newWindow,text ="Estudiantes: ",font='Helvetica 12 bold')
        label1.place(x=10,y=5)
        text="Fátima Leiva Chinchilla 2019153089\nArmando Fallas Garro 2019226675\nValeria Morales Alvarado 2019052012"
        label2= tk.Label(newWindow,text =text,font='Helvetica 9 bold')
        label2.place(x=105,y=30)

        label3= tk.Label(newWindow,text ="Instrucciones: ",font='Helvetica 12 bold')
        label3.place(x=10,y=90)

        text2="Para poder ingresar los números de X y Y debe marcar los ckeckbox que están \nal lado de cada input, y mediante las teclas de número que\ncontiene la calculadora, le va a permitir ingresar los números"
        text3="\nPara poder llevar a cabo una función específica solo basta con presionar la tecla \nque representa la función e inmediatamente se desplegará\nel resultado."
        text4="\nUna vez haya llevado a cabo una operación, debe presionar el botón Clear\n y volver a ingresar nuevamente el número para realizar la siguiente\noperación que desee realizar."
        text2+=text3+text4
        label2= tk.Label(newWindow,text =text2)
        label2.place(x=17,y=120)

        exitBtn= tk.Button(newWindow,text="close",command=newWindow.destroy,bg='#476063',fg='white')
        exitBtn.place(x=170,y=265,width=100)

        
    # Calls the functions related to the Funtras algorithms to be implemented
    # and saves the result in the result variable of the class
    def function(self,num):
        tempNumX= self.getNum(self.textX)
        tempNumY=self.getNum(self.textY)

        if(num==1):
            self.result=mn.sinh_t(tempNumX)
        elif(num==2):
            self.result=mn.cosh_t(tempNumX)
        elif(num==3):
            self.result=mn.tanh_t(tempNumX)
        elif(num==4):
            self.result=mn.asint_t(tempNumX)
        elif(num==5):
            self.result=mn.acos_t(tempNumX)
        elif(num==6):
            self.result=mn.atan_t(tempNumX)
        elif(num==7):
            self.result=mn.sec_t(tempNumX)
        elif(num==8):
            self.result=mn.csc_t(tempNumX)
        elif(num==9):
            self.result=mn.cot_t(tempNumX)
        elif(num==10):
            self.result=mn.sin_t(tempNumX)
        elif(num==11):
            self.result=mn.cos_t(tempNumX)
        elif(num==12):
            self.result=mn.tan_t(tempNumX)
        elif(num==13):
            self.result=mn.ln_t(tempNumX)
        elif(num==14):
            self.result=mn.log_t(tempNumX,10)
        elif(num==15):
            self.result=mn.log_t(tempNumX,tempNumY)
        elif(num==16):
            self.result=mn.div_t(tempNumX)
        elif(num==17):
            self.result=mn.sqrt_t(tempNumX)
        elif(num==18):
            self.result=mn.root_t(tempNumX,tempNumY)
        elif(num==19):
            self.result=mn.exp_t(tempNumX)
        elif(num==20):
            self.result=mn.power_t(tempNumX,tempNumY)
        elif(num==21):
            self.result=mn.factorial(tempNumX)
        print("result: ",self.result)
        self.InputResult.config(text = self.result)
        
            
    # Receive a number in string and convert it to float
    # If the number has pi it's converted too to a float number
    def getNum(self,text):
        if(text.find('π')!=-1):
            print("sffer")
            print(text)
            pi = 3.1415926
            s1 = text.translate({ord('π'): None})
            if(s1==''):
                return pi
            else:
                s1_num=float(s1)
                res=s1_num*pi
                return res          
        else:            
            if(text==''):
                return 0
            else:
                s1_num=float(text)
            return s1_num 
         
    # This functions is activated when the Clear button is pressed
    # Clears the values of X, Y and result numbers so the user can enter new ones     
    def clearText(self):
        self.textX=""
        self.textY=""
        self.result=""
        self.InputX.config(text = self.textX)
        self.InputY.config(text = self.textY)
        self.checkbox1_value.set(False)
        self.checkbox2_value.set(False)
        self.InputResult.config(text=self.result)

    # Add values to X or Y number depending on checkbox and the button pressed by the user
    def addNum(self,num):
        if(self.checkbox1_value.get()==True):
            self.textX+=num
            self.InputX.config(text = self.textX)
        elif(self.checkbox2_value.get()==True):
            self.textY+=num
            self.InputY.config(text = self.textY)

    # If some checkbox is in True state and another is pressed, sets the first one
    # in false and the new one in True
    def check(self,num):
        if(num==1):
            self.checkbox2_value.set(False)
        else:
            self.checkbox1_value.set(False)
    
    

#----- Call function ----
if __name__ == "__main__":
  app = App()
  app.mainloop()