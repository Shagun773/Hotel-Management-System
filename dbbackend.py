
import sqlite3

# Backend - Create a table for Hotel Management System
def hotelData():
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS hotel (
        id INTEGER PRIMARY KEY,
        RoomNumber text, 
        CustomerName text,
        CheckInDate text,
        CheckOutDate text,
        RoomType text,
        PaymentStatus text
    )
    """)
    con.commit()
    con.close()

# Add new guest (room booking)
def addGuestRec(RoomNumber, CustomerName, CheckInDate, CheckOutDate, RoomType, PaymentStatus):
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("""
    INSERT INTO hotel (RoomNumber, CustomerName, CheckInDate, CheckOutDate, RoomType, PaymentStatus) 
    VALUES (?,?,?,?,?,?) 
    """, (RoomNumber, CustomerName, CheckInDate, CheckOutDate, RoomType, PaymentStatus))
    con.commit()
    con.close()

# View all guest records (rooms)
def viewData():
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM hotel")
    rows = cur.fetchall()
    con.close()
    return rows

# Delete a guest record (room booking)
def deleteRec(id):
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("DELETE FROM hotel WHERE id=?", (id,))
    con.commit()
    con.close()

# Search for guest records based on given criteria
def searchData(RoomNumber="", CustomerName="", CheckInDate="", CheckOutDate="", RoomType="", PaymentStatus=""):
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM hotel 
    WHERE RoomNumber=? OR CustomerName=? OR CheckInDate=? OR CheckOutDate=? OR RoomType=? OR PaymentStatus=?
    """, (RoomNumber, CustomerName, CheckInDate, CheckOutDate, RoomType, PaymentStatus))
    rows = cur.fetchall()
    con.close()
    return rows

# Update guest record
def dataUpdate(id, RoomNumber="", CustomerName="", CheckInDate="", CheckOutDate="", RoomType="", PaymentStatus=""):
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("""
    UPDATE hotel 
    SET RoomNumber=?, CustomerName=?, CheckInDate=?, CheckOutDate=?, RoomType=?, PaymentStatus=? 
    WHERE id=?
    """, (RoomNumber, CustomerName, CheckInDate, CheckOutDate, RoomType, PaymentStatus, id))
    con.commit()
    con.close()

hotelData()
