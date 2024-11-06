from tkinter import *
import tkinter.messagebox
import dbbackend

class Hotel:

    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")  # Set the window size for the application
        self.root.config(bg="#f4f4f4")

        # Define StringVar() variables for the fields
        RoomNumber = StringVar()
        CustomerName = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        RoomType = StringVar()
        PaymentStatus = StringVar()

        # -------------------FUNCTIONS-----------------------------------

        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Management System", "Do you want to exit?")
            if iExit > 0:
                root.destroy()

        def clearData():
            self.txtRoomNumber.delete(0, END)
            self.txtCustomerName.delete(0, END)
            self.txtCheckIn.delete(0, END)
            self.txtCheckOut.delete(0, END)
            self.txtRoomType.delete(0, END)
            self.txtPaymentStatus.delete(0, END)

        def addData():
            if len(RoomNumber.get()) != 0:
                dbbackend.addGuestRec(RoomNumber.get(), CustomerName.get(), CheckInDate.get(), CheckOutDate.get(), RoomType.get(), PaymentStatus.get())
                guestList.delete(0, END)
                guestList.insert(END, self.formatRecord(RoomNumber.get(), CustomerName.get(), CheckInDate.get(), CheckOutDate.get(), RoomType.get(), PaymentStatus.get()))

        def displayData():
            guestList.delete(0, END)
            for row in dbbackend.viewData():
                guestList.insert(END, self.formatRecord(row[1], row[2], row[3], row[4], row[5], row[6]))

        def guestRec(event):
            global sd
            searchGuest = guestList.curselection()[0]
            sd = guestList.get(searchGuest)

            self.txtRoomNumber.delete(0, END)
            self.txtRoomNumber.insert(END, sd[1])
            self.txtCustomerName.delete(0, END)
            self.txtCustomerName.insert(END, sd[2])
            self.txtCheckIn.delete(0, END)
            self.txtCheckIn.insert(END, sd[3])
            self.txtCheckOut.delete(0, END)
            self.txtCheckOut.insert(END, sd[4])
            self.txtRoomType.delete(0, END)
            self.txtRoomType.insert(END, sd[5])
            self.txtPaymentStatus.delete(0, END)
            self.txtPaymentStatus.insert(END, sd[6])

        def deleteData():
            if len(RoomNumber.get()) != 0:
                dbbackend.deleteRec(sd[0])
                clearData()
                displayData()

        def searchDatabase():
            guestList.delete(0, END)
            for row in dbbackend.searchData(RoomNumber.get(), CustomerName.get(), CheckInDate.get(), CheckOutDate.get(), RoomType.get(), PaymentStatus.get()):
                guestList.insert(END, self.formatRecord(row[1], row[2], row[3], row[4], row[5], row[6]))

        def update():
            if len(RoomNumber.get()) != 0:
                dbbackend.dataUpdate(sd[0], RoomNumber.get(), CustomerName.get(), CheckInDate.get(), CheckOutDate.get(), RoomType.get(), PaymentStatus.get())
                guestList.delete(0, END)
                guestList.insert(END, self.formatRecord(RoomNumber.get(), CustomerName.get(), CheckInDate.get(), CheckOutDate.get(), RoomType.get(), PaymentStatus.get()))

        # Format record for Listbox display
        def formatRecord(room, customer, checkin, checkout, roomtype, payment):
            return f"Room: {room} | Customer: {customer} | Check-In: {checkin} | Check-Out: {checkout} | Type: {roomtype} | Status: {payment}"

        # -------------------UI Elements-----------------------------------

        MainFrame = Frame(self.root, bg="#f4f4f4")
        MainFrame.grid(row=0, column=0, sticky="nsew")  # Ensure it fills the available space

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="#003366", relief=RIDGE)
        TitFrame.grid(row=0, column=0, sticky="ew")  # Ensures the title frame expands horizontally

        self.lblTit = Label(TitFrame, font=('Arial', 40, 'bold'), text="Hotel Management System", bg="#003366", fg="white")
        self.lblTit.grid(row=0, column=0)

        ButtonFrame = Frame(MainFrame, bd=2, width=1500, height=70, padx=19, pady=10, bg="#003366", relief=RIDGE)
        ButtonFrame.grid(row=1, column=0, sticky="ew")  # Ensures the button frame expands horizontally

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="#e3e3e3")
        DataFrame.grid(row=2, column=0, sticky="nsew")  # Make sure this frame expands as well

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="white", font=('times new roman', 26, 'bold'), text="Guest Info\n")
        DataFrameLEFT.grid(row=0, column=0, sticky="nsew")  # Left part of the data frame

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="white", font=('times new roman', 20, 'bold'), text="Guest Details\n")
        DataFrameRIGHT.grid(row=0, column=1, sticky="nsew")  # Right part of the data frame

        # -------------------Entries------------------------------------

        self.lblRoomNumber = Label(DataFrameLEFT, font=('Arial', 18, 'bold'), text="Room Number:", padx=2, pady=2, bg="white")
        self.lblRoomNumber.grid(row=0, column=0, sticky=W)
        self.txtRoomNumber = Entry(DataFrameLEFT, font=('Arial', 18), textvariable=RoomNumber, width=39, bd=2)
        self.txtRoomNumber.grid(row=0, column=1)

        self.lblCustomerName = Label(DataFrameLEFT, font=('Arial', 18, 'bold'), text="Customer Name:", padx=2, pady=2, bg="white")
        self.lblCustomerName.grid(row=1, column=0, sticky=W)
        self.txtCustomerName = Entry(DataFrameLEFT, font=('Arial', 18), textvariable=CustomerName, width=39, bd=2)
        self.txtCustomerName.grid(row=1, column=1)

        self.lblCheckIn = Label(DataFrameLEFT, font=('Arial', 18, 'bold'), text="Check-In Date:", padx=2, pady=2, bg="white")
        self.lblCheckIn.grid(row=2, column=0, sticky=W)
        self.txtCheckIn = Entry(DataFrameLEFT, font=('Arial', 18), textvariable=CheckInDate, width=39, bd=2)
        self.txtCheckIn.grid(row=2, column=1)

        self.lblCheckOut = Label(DataFrameLEFT, font=('Arial', 18, 'bold'), text="Check-Out Date:", padx=2, pady=2, bg="white")
        self.lblCheckOut.grid(row=3, column=0, sticky=W)
        self.txtCheckOut = Entry(DataFrameLEFT, font=('Arial', 18), textvariable=CheckOutDate, width=39, bd=2)
        self.txtCheckOut.grid(row=3, column=1)

        self.lblRoomType = Label(DataFrameLEFT, font=('Arial', 18, 'bold'), text="Room Type:", padx=2, pady=2, bg="white")
        self.lblRoomType.grid(row=4, column=0, sticky=W)
        self.txtRoomType = Entry(DataFrameLEFT, font=('Arial', 18), textvariable=RoomType, width=39, bd=2)
        self.txtRoomType.grid(row=4, column=1)

        self.lblPaymentStatus = Label(DataFrameLEFT, font=('Arial', 18, 'bold'), text="Payment Status:", padx=2, pady=2, bg="white")
        self.lblPaymentStatus.grid(row=5, column=0, sticky=W)
        self.txtPaymentStatus = Entry(DataFrameLEFT, font=('Arial', 18), textvariable=PaymentStatus, width=39, bd=2)
        self.txtPaymentStatus.grid(row=5, column=1)

        # -------------------Listbox and Scrollbar----------------------

        scroll = Scrollbar(DataFrameRIGHT)
        guestList = Listbox(DataFrameRIGHT, width=50, height=16, font=('Arial', 14), bd=2)
        scroll.pack(side=RIGHT, fill=Y)
        guestList.pack(side=LEFT, fill=BOTH, expand=True)
        scroll.config(command=guestList.yview)
        guestList.bind("<ButtonRelease-1>", guestRec)

        # -------------------Buttons------------------------------------

        self.btnAddNew = Button(ButtonFrame, text="Add New", font=('Arial', 18, 'bold'), width=15, bg="#4CAF50", fg="white", command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=10)

        self.btnDisplay = Button(ButtonFrame, text="Display", font=('Arial', 18, 'bold'), width=15, bg="#2196F3", fg="white", command=displayData)
        self.btnDisplay.grid(row=0, column=1, padx=10)

        self.btnClear = Button(ButtonFrame, text="Clear", font=('Arial', 18, 'bold'), width=15, bg="#FF9800", fg="white", command=clearData)
        self.btnClear.grid(row=0, column=2, padx=10)

        self.btnDelete = Button(ButtonFrame, text="Delete", font=('Arial', 18, 'bold'), width=15, bg="#f44336", fg="white", command=deleteData)
        self.btnDelete.grid(row=0, column=3, padx=10)

        self.btnSearch = Button(ButtonFrame, text="Search", font=('Arial', 18, 'bold'), width=15, bg="#9C27B0", fg="white", command=searchDatabase)
        self.btnSearch.grid(row=0, column=4, padx=10)

        self.btnUpdate = Button(ButtonFrame, text="Update", font=('Arial', 18, 'bold'), width=15, bg="#3F51B5", fg="white", command=update)
        self.btnUpdate.grid(row=0, column=5, padx=10)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('Arial', 18, 'bold'), width=15, bg="#607D8B", fg="white", command=iExit)
        self.btnExit.grid(row=0, column=6, padx=10)

if __name__ == '__main__':
    root = Tk()
    hotel = Hotel(root)
    root.mainloop()
