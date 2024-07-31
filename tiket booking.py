from tkinter import *
from tkinter import messagebox
# importing DateEntry from tkcalendar, you need to install tkcalendar-> pip install tkcalendar
from tkcalendar import DateEntry
from datetime import date
import sqlite3
import random
import string

# defining main window, geometry, and title
top = Tk()
top.geometry('550x300')
top.title('Ticket Management: CopyAssignment')

# connecting to database
conn = sqlite3.connect('ticket_booking_database.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ticket (name TEXT, ticket_id TEXT PRIMARY KEY, ticket_date TEXT, ticket_validity TEXT)")

# fetching database
cursor.execute('SELECT * FROM ticket')
tickets = cursor.fetchall()

# getting all tickets id
tickets_id = []
for i in tickets:
  tickets_id.append(i[1]) 

conn.commit() 


Label(top, text='Ticket Management System', font=('Arial', 18)).grid(row=0, column=0, columnspan=2, padx=80, pady=20)

# defining functions
# this function will be used to show messages and errors
def show_message(title, message):
    messagebox.showerror(title, message)
    
# this function will be used to generate random ticket id
def get_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))
  
# this function will be used to book a new ticket  
def Book():
    
    top1 = Tk()
    top1.geometry('350x300')
    top1.title('Book')
    
    name = StringVar(top1)
    ticket_id = StringVar(top1)
    ticket_date = StringVar(top1)
    ticket_date.set(date.today())
    ticket_validity = StringVar(top1)
    
    # this while loop will create a new unique ticket id using get_random_string function
    while True:
        global tickets_id
        t_id = get_random_string()
        if t_id not in tickets_id:
            ticket_id.set(get_random_string())
            break
        continue
    
    def BookNow():
        if len(name.get())<5 or len(ticket_date.get())<7 or len(ticket_validity.get())<7:
            show_message('Error', 'Enter valid details')
            return
        try:
            conn = sqlite3.connect("ticket_booking_database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ticket (name, ticket_id, ticket_date, ticket_validity) VALUES (?, ?, ?, ?)", (str(name.get()), str(ticket_id.get()), str(ticket_date.get()), str(ticket_validity.get())))
            conn.commit()
            show_message('Successful', 'Your booking is successful, your ticket id is {}'.format(ticket_id.get()))
            top1.destroy()
        except sqlite3.Error as e:
            show_message('Error', e)
        finally:
            conn.close()
    
    Label(top1, text='Enter details', font=('Arial', 14)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    
    Label(top1, text='Name', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=name).grid(row=1, column=1)
    
    Label(top1, text='Ticket Id', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Entry(top1, textvariable=ticket_id, state='disabled').grid(row=2, column=1)
    
    Label(top1, text='Booking Date', font=('Arial', 12)).grid(row=3, column=0, padx=10, sticky='w', pady=10)
    DateEntry(top1,selectmode='day', textvariable=ticket_date).grid(row=3, column=1)
    
    Label(top1, text='Validity', font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky='w')
    DateEntry(top1,selectmode='day', year=2023,month=1,day=25, textvariable=ticket_validity).grid(row=4, column=1)
    
    Button(top1, text='Confirm', bg='green', fg='white', font=('Arial', 17), width=9, command=lambda:BookNow()).grid(row=5, column=1, pady=10)

# this function will be used to display all booked tickets 
def ViewHistory():
    
    top2 = Tk()
    top2.geometry('737x300')
    top2.title('View Ticket Booking History')
    
    Label(top2, text='Customer Name', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=0, pady=10)
    Label(top2, text='Ticket ID', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=1, pady=10)
    Label(top2, text='Date of Booking', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=2, pady=10)
    Label(top2, text='Ticket Validity(Date)', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=3, pady=10)
    
    conn = sqlite3.connect('ticket_booking_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ticket')
    tickets = cursor.fetchall()
    for i in range(len(tickets)):
        Label(top2, text=tickets[i][0], borderwidth=1, relief="solid", width=20).grid(row=i+1, column=0)
        Label(top2, text=tickets[i][1], borderwidth=1, relief="solid", width=20).grid(row=i+1, padx=10, column=1)
        Label(top2, text=tickets[i][2], borderwidth=1, relief="solid", width=20).grid(row=i+1, padx=10, column=2)
        Label(top2, text=tickets[i][3], borderwidth=1, relief="solid", width=20).grid(row=i+1, padx=10, column=3)
    top2.mainloop()
    conn.close()

# this function will be used to delete a ticket
def DeleteBooking():
    
    top3 = Tk()
    top3.geometry('785x300')
    top3.title('View Ticket Booking History')
    
    Label(top3, text='Customer Name', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=0, pady=10)
    Label(top3, text='Ticket ID', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=1, pady=10)
    Label(top3, text='Date of Booking', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=2, pady=10)
    Label(top3, text='Ticket Validity(Date)', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=3, pady=10)
    
    def delete_rows(ticket_id):
        try:
            conn = sqlite3.connect("ticket_booking_database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ticket WHERE ticket_id = ?", (ticket_id,))
            conn.commit()
            show_message('Success', 'Ticket deleted')
            conn.close()
        except sqlite3.Error as e:
            show_message('Sqlite error', e)
        finally:
            conn.close()
    conn = sqlite3.connect('ticket_booking_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ticket')
    tickets = cursor.fetchall()
    for i in range(len(tickets)):
        Label(top3, text=tickets[i][0], borderwidth=1, relief="solid", width=20).grid(row=i+1,  column=0)
        Label(top3, text=tickets[i][1], borderwidth=1, relief="solid", width=20).grid(row=i+1,  padx=10, column=1)
        Label(top3, text=tickets[i][2], borderwidth=1, relief="solid", width=20).grid(row=i+1,  padx=10, column=2)
        Label(top3, text=tickets[i][3], borderwidth=1, relief="solid", width=20).grid(row=i+1,  padx=10, column=3)
        Button(top3, text='Delete', command=lambda current_id=tickets[i][1]: delete_rows(current_id)).grid(row=i+1, column=4)
    top3.mainloop()
    

    conn.close()
    
# defining buttons
Button(top, text='Book Ticket', font=('Arial', 14), fg='white', command=lambda:Book(), width=12, height=2, bg='Green').grid(row=1, column=0, padx=80, pady=20)

Button(top, text='View History', font=('Arial', 14), fg='white', command=lambda:ViewHistory(), width=12, height=2, bg='Green').grid(row=1, column=1, pady=20)

Button(top, text='Delete Booking', font=('Arial', 14), fg='white', command=lambda:DeleteBooking(), width=12, height=2, bg='Green').grid(row=2, column=0, pady=30)

Button(top, text='Quit', font=('Arial', 14), fg='white', command=lambda:top.destroy(), width=12, height=2, bg='Green').grid(row=2, column=1, pady=30)

# mainloop
top.mainloop()