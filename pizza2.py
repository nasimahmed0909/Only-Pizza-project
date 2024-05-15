

from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from tkinter import ttk, messagebox, scrolledtext
from tkinter import Button,Toplevel
import tkinter.simpledialog as simpledialog
import sqlite3

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Only pizza Management System')
        
# Set the width of the second column to 100 pixels
        # root.columnconfigure(1, minsize=100)
        

        # Variable:
        self.pizza_id = StringVar()
        self.pizza_name = StringVar()
        self.pizza_category = StringVar()
        self.pizza_ingredients = StringVar()
        self.pizza_id_for_delete = StringVar()
        self.pizza_id_for_update = StringVar()
        self.search_id = StringVar()

        self.pizza_info_id = StringVar()
        self.pizza_info_type_id= StringVar()
        self.pizza_size = StringVar()
        self.pizza_price = StringVar()
        self.pizza_id_info_for_delete = StringVar()
        self.pizza_id_info_for_update = StringVar()
        self.search_info_id = StringVar()

        self.limit = StringVar()
        self.limit2 = StringVar()
        self.order_id_entry= StringVar()
        self.more_limit = StringVar()
        self.less_limit = StringVar()
        self.num_of_order = StringVar()
        self.based_on_revenue = StringVar()
        self.cum_revenue  = StringVar()
        



        

        lbl_title = Label(self.root, text='ONLY PIZZA', font=('times new roman', 37, 'bold'), fg='red3')
        lbl_title.place(x=0, y=0, width=1530, height=50)

        img_logo = Image.open('photo/logo.png')
        img_logo = img_logo.resize((100, 90))
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=550, y=0, width=60, height=60)

        # Image frame;
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='White')
        img_frame.place(x=0, y=50, width=1530, height=160)

        # Images
        img1 = Image.open('photo/image_1.jpg')
        img1 = img1.resize((540, 160))
        self.photo1 = ImageTk.PhotoImage(img1)
        self.img1 = Label(img_frame, image=self.photo1)
        self.img1.place(x=0, y=0, width=540, height=160)

        img2 = Image.open('photo/image_2.jpg')
        img2 = img2.resize((540, 160))
        self.photo2 = ImageTk.PhotoImage(img2)
        self.img2 = Label(img_frame, image=self.photo2)
        self.img2.place(x=540, y=0, width=540, height=160)

        img3 = Image.open('photo/image_3.jpg')
        img3 = img3.resize((540, 160))
        self.photo3 = ImageTk.PhotoImage(img3)
        self.img3 = Label(img_frame, image=self.photo3)
        self.img3.place(x=1000, y=0, width=540, height=160)

        # Main frame:
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='White')
        main_frame.place(x=5, y=220, width=1520, height=566)

        # Upper frame:
        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='White', text='Pizza details', font=('times new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=8, y=5, width=1505, height=450)

        # # lower frame
        # down_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,bg='White',text='Employee Information Table',font= ('times new roman',11,'bold'), fg = 'red')
        # down_frame.place(x=10,y=280,width=1480,height = 270)

        lower_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='#000000', font=('times new roman', 11, 'bold'), fg='red1')
        lower_frame.place(x=8, y=452, width=1505, height=110)

        # Labels and Entry for Pizza details
        lbl_pizza_id = Label(upper_frame, text='Pizza ID:', font=('arial', 8, 'bold'), bg='white')
        lbl_pizza_id.grid(row=0, column=2, padx=2, pady=7, sticky=W)
        txt_pizza_id = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_id)
        txt_pizza_id.grid(row=0, column=3, sticky=W, padx=2, pady=7)

        lbl_pizza_category = Label(upper_frame, text='Category:', font=('arial', 8, 'bold'), bg='white')
        lbl_pizza_category.grid(row=0, column=4, padx=2, pady=7, sticky=W)
        txt_pizza_category = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_category)
        txt_pizza_category.grid(row=0, column=5, sticky=W, padx=2, pady=7)

        lbl_pizza_ingredients = Label(upper_frame, text='Ingredients:', font=('arial', 8, 'bold'), bg='white')
        lbl_pizza_ingredients.grid(row=0, column=6, padx=2, pady=7, sticky=W)
        txt_pizza_ingredients = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_ingredients)
        txt_pizza_ingredients.grid(row=0, column=7, sticky=W, padx=2, pady=7)

        lbl_name = Label(upper_frame, text='Name:', font=('arial', 8, 'bold'), bg='white')
        lbl_name.grid(row=0, column=8, padx=2, pady=7, sticky=W)
        txt_name = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_name)
        txt_name.grid(row=0, column=9, sticky=W, padx=2, pady=7)

        btn_add = Button(upper_frame, text='ADD PIZZA', font=('Lato', 8, 'bold'), width=12, bg='red', fg='white', command=self.add_data)
        btn_add.grid(row=0, column=10, padx=10, pady=5)

        lbl_delete_pizza = Label(upper_frame, text='Enter Pizza ID to Delete:', font=('arial', 8, 'bold'), bg='white')
        lbl_delete_pizza.grid(row=1, column=2, padx=2, pady=7, sticky=W)
        txt_delete_pizza = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_id_for_delete)
        txt_delete_pizza.grid(row=1, column=3, sticky=W, padx=2, pady=7)

        btn_delete = Button(upper_frame, text='DELETE PIZZA', font=('Lato', 8, 'bold'), width=12, bg='red', fg='white', command=self.delete_data)
        btn_delete.grid(row=1, column=4, padx=10, pady=5)

        # New: Update Label and Entry
        lbl_update_pizza = Label(upper_frame, text='Enter Pizza ID to Update:', font=('arial', 8, 'bold'), bg='white')
        lbl_update_pizza.grid(row=1, column=5, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_id_for_update)
        txt_update_pizza.grid(row=1, column=6, sticky=W, padx=2, pady=7)
        btn_update = Button(upper_frame, text='UPDATE PIZZA', font=('Lato', 8, 'bold'), width=12, bg='red', fg='white', command=self.update_data)
        btn_update.grid(row=1, column=7, padx=10, pady=5)
       

        # New: Search Label and Entry
        lbl_search_pizza = Label(upper_frame, text='Enter Pizza ID to Search:', font=('arial', 8, 'bold'), bg='white')
        lbl_search_pizza.grid(row=1, column=8, padx=2, pady=7, sticky=W)
        txt_search_pizza = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.search_id)
        txt_search_pizza.grid(row=1, column=9, sticky=W, padx=2, pady=7)

        btn_search = Button(upper_frame, text='SEARCH PIZZA', font=('Lato', 8, 'bold'), width=15, bg='red', fg='white', command=self.search_data)
        btn_search.grid(row=1, column=10, padx=10, pady=5)

        #show whole table:
        lbl_show_all = Label(upper_frame, text='Click show all button for see all data :', font=('arial', 8, 'bold'), bg='white')
        lbl_show_all.grid(row=2, column=2, padx=2, pady=7, sticky=W)
        btn_show_all = Button(upper_frame, text='SHOW ALL PIZZAS', font=('Lato', 8, 'bold'), width=15, bg='red', fg='white', command=self.show_all_pizzas)
        btn_show_all.grid(row=2, column=3, padx=10, pady=5)
        #clear button:
        lbl_clear_all = Label(upper_frame, text='Click clear button for clear all data :', font=('arial', 8, 'bold'), bg='white')
        lbl_clear_all.grid(row=2, column=4, padx=2, pady=7, sticky=W)
        btn_clear_all = Button(upper_frame, text='CLEAR', font=('Lato', 8, 'bold'), width=15, bg='red', fg='white', command=self.clear_data)
        btn_clear_all.grid(row=2, column=5, padx=10, pady=5)

        #pizzas table:
        lbl_show_all = Label(upper_frame, text='Pizzas table information :', font=('Courier', 9, 'bold',), bg='khaki2',fg='red4')
        lbl_show_all.grid(row=3, column=5, padx=2, pady=7, sticky=W)

        lbl_pizza_id = Label(upper_frame, text='Pizza ID:', font=('arial', 8, 'bold'), bg='white')
        lbl_pizza_id.grid(row=4, column=2, padx=2, pady=7, sticky=W)
        txt_pizza_id = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_info_id)
        txt_pizza_id.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        lbl_pizza_type_id = Label(upper_frame, text='Pizza type ID:', font=('arial', 8, 'bold'), bg='white')
        lbl_pizza_type_id.grid(row=4, column=4, padx=2, pady=7, sticky=W)
        txt_pizza_type_id = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_info_type_id)
        txt_pizza_type_id.grid(row=4, column=5, sticky=W, padx=2, pady=7)

        lbl_pizza_size = Label(upper_frame, text='Size:', font=('arial', 8, 'bold'), bg='white')
        lbl_pizza_size.grid(row=4, column=6, padx=2, pady=7, sticky=W)
        txt_pizza_size = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_size)
        txt_pizza_size.grid(row=4, column=7, sticky=W, padx=2, pady=7)

        lbl_price = Label(upper_frame, text='Price:', font=('arial', 8, 'bold'), bg='white')
        lbl_price.grid(row=4, column=8, padx=2, pady=7, sticky=W)
        txt_price = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_price)
        txt_price.grid(row=4, column=9, sticky=W, padx=2, pady=7)

        btn_set = Button(upper_frame, text='ADD INFO', font=('Lato', 8, 'bold'), width=12, bg='red', fg='white', command=self.set_data)
        btn_set.grid(row=4, column=10, padx=10, pady=5)
        # delete
        lbl_delete_pizza = Label(upper_frame, text='Enter Pizza ID to Delete pizza INFO:', font=('arial', 8, 'bold'), bg='white')
        lbl_delete_pizza.grid(row=5, column=2, padx=2, pady=7, sticky=W)
        txt_delete_pizza = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_id_info_for_delete)
        txt_delete_pizza.grid(row=5, column=3, sticky=W, padx=2, pady=7)

        btn_delete = Button(upper_frame, text='DELETE INFO', font=('Lato', 8, 'bold'), width=12, bg='red', fg='white', command=self.delete_pizza_INFO)
        btn_delete.grid(row=5, column=4, padx=10, pady=5)


        # New: Update Label and Entry
        lbl_update_pizza = Label(upper_frame, text='Enter Pizza ID to Update INFO', font=('arial', 8, 'bold'), bg='white')
        lbl_update_pizza.grid(row=5, column=5, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.pizza_id_info_for_update)
        txt_update_pizza.grid(row=5, column=6, sticky=W, padx=2, pady=7)

        btn_update = Button(upper_frame, text='UPDATE INFO', font=('Lato', 8, 'bold'), width=12, bg='red', fg='white', command=self.update_pizza_data)
        btn_update.grid(row=5, column=7, padx=10, pady=5)
        
        # New: Search Label and Entry
        lbl_search_pizza = Label(upper_frame, text='Enter PizzaID to Search INFO:', font=('arial', 8, 'bold'), bg='white')
        lbl_search_pizza.grid(row=5, column=8, padx=2, pady=7, sticky=W)
        txt_search_pizza = ttk.Entry(upper_frame, width=20, font=('arial', 8, 'bold'), textvariable=self.search_info_id)
        txt_search_pizza.grid(row=5, column=9, sticky=W, padx=2, pady=7)

        btn_search = Button(upper_frame, text='SEARCH INFO', font=('Lato', 8, 'bold'), width=15, bg='red', fg='white', command=self.search_data_INFO)
        btn_search.grid(row=5, column=10, padx=10, pady=5)

        #show whole table:
        lbl_show_all = Label(upper_frame, text='Click show all button for see all data :', font=('arial', 8, 'bold'), bg='white')
        lbl_show_all.grid(row=6, column=2, padx=2, pady=7, sticky=W)
        btn_show_all = Button(upper_frame, text='SHOW ALL INFO', font=('Lato', 8, 'bold'), width=15, bg='red', fg='white', command=self.show_all_pizzas_info)
        btn_show_all.grid(row=6, column=3, padx=10, pady=5)
        #clear button:
        lbl_clear_all = Label(upper_frame, text='Click reset button for clear all data :', font=('arial', 8, 'bold'), bg='white')
        lbl_clear_all.grid(row=6, column=4, padx=2, pady=7, sticky=W)
        btn_clear_all = Button(upper_frame, text='RESET', font=('Lato', 8, 'bold'), width=15, bg='red', fg='white', command=self.reset_data)
        btn_clear_all.grid(row=6, column=5, padx=10, pady=5)

        # special Query:
        lbl_show_all = Label(upper_frame, text='Perfrom some special Ouery :', font=('Courier', 9, 'bold',), bg='khaki2',fg='red4')
        lbl_show_all.grid(row=7, column=5, padx=2, pady=7, sticky=W)

        lbl_show_all = Label(upper_frame, text='Click to see TOTAL revenue:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=9, column=2, padx=2, pady=7, sticky=W)
        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.calculate_total_revenue)
        btn_total.grid(row=9, column=3, pady=7)

        lbl_show_all = Label(upper_frame, text='Click to \n see Highest-price pizza:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=9, column=4, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=5, font=('arial', 8, 'bold'), textvariable=self.limit)
        txt_update_pizza.grid(row=9, column=5, sticky=W, padx=2, pady=2)

        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.execute_sql_query)
        btn_total.grid(row=9, column=5, pady=7)

        lbl_show_all = Label(upper_frame, text='Top ordered pizza\nbased their quatity:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=9, column=6, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=5, font=('arial', 8, 'bold'), textvariable=self.limit2)
        txt_update_pizza.grid(row=9, column=7, sticky=W, padx=7, pady=2)

        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.top_ordered)
        btn_total.grid(row=9, column=7, padx=5,pady=7,sticky=E)

        lbl_show_all = Label(upper_frame, text='Top ordered pizza based on\n their revenue:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=9, column=8, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=6, font=('arial', 8, 'bold'), textvariable=self.based_on_revenue)
        txt_update_pizza.grid(row=9, column=9,sticky=W)
        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.Top_revenue)
        btn_total.grid(row=9, column=9, padx=5,pady=7,sticky=E)

        lbl_show_all = Label(upper_frame, text='Find all pizzas that \ncost more than', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=10, column=2, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=6, font=('arial', 8, 'bold'), textvariable=self.more_limit)
        txt_update_pizza.grid(row=10, column=2,sticky=E)
        lbl_show_all = Label(upper_frame, text='less then:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=10, column=3, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=6, font=('arial', 8, 'bold'), textvariable=self.less_limit)
        txt_update_pizza.grid(row=10, column=3,sticky=E)
        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.find_and_show_pizzas)
        btn_total.grid(row=10, column=4, padx=5,pady=7,sticky=W)


        lbl_show_all = Label(upper_frame, text='Number of pizzas ordered per\nday:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=10, column=5, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=6, font=('arial', 8, 'bold'), textvariable=self.num_of_order)
        txt_update_pizza.grid(row=10, column=6,sticky=W)
        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.number_of_order)
        btn_total.grid(row=10, column=6, padx=5,pady=7,sticky=E)



        lbl_show_all = Label(upper_frame, text='See Order details\nalong their Order_ID:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=10, column=8, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=6, font=('arial', 8, 'bold'), textvariable=self.order_id_entry)
        txt_update_pizza.grid(row=10, column=9, sticky=W, padx=7, pady=2)
        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.details_order)
        btn_total.grid(row=10, column=9, padx=5,pady=7,sticky=E)

        lbl_show_all = Label(upper_frame, text='Orders by hour of the day:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=11, column=2, padx=2, pady=7, sticky=W)
        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.show_order_per_hour)
        btn_total.grid(row=11, column=3, padx=5,pady=7,sticky=W)

        lbl_show_all = Label(upper_frame, text='Contribute each pizza type\n total revenue:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=11, column=4, padx=2, pady=7, sticky=W)
        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.show_revenue_percentage)
        btn_total.grid(row=11, column=5, padx=5,pady=7,sticky=W)


        lbl_show_all = Label(upper_frame, text='Calculate cumulative\n revenue over time:', font=('Courier', 8,), bg='seagreen1',fg='black')

        lbl_show_all.grid(row=11, column=6, padx=2, pady=7, sticky=W)
        txt_update_pizza = ttk.Entry(upper_frame, width=6, font=('arial', 8, 'bold'), textvariable=self.cum_revenue)
        txt_update_pizza.grid(row=11, column=7, sticky=W, padx=7, pady=2)
        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.show_cumulative_revenue)
        btn_total.grid(row=11, column=7, padx=5,pady=7,sticky=E)

        lbl_show_all = Label(upper_frame, text='Total ordered pizza based\n on thier quantity:', font=('Courier', 8,), bg='seagreen1',fg='black')
        lbl_show_all.grid(row=11, column=8, padx=2, pady=7, sticky=W)
        btn_total = Button(upper_frame, text='CLICK', font=('Lato', 8, 'bold'), width=8, bg='black', fg='white', command=self.show_pizza_quantity_by_size)
        btn_total.grid(row=11, column=9, padx=5,pady=7,sticky=E)





        #footer:
        lbl_show_all = Label(lower_frame, text='Join our Pizza Family:', font=('Courier', 16,'bold'),fg= 'white',bg='#000000')

        lbl_show_all.grid(row=2, column=5, padx=2, pady=2, sticky=W)
        lbl_show_all = Label(lower_frame, text='Enter your email:', font=('Courier', 10,'bold'),fg='White',bg='#000000')
        lbl_show_all.grid(row=3, column=5, padx=2, pady=2, sticky=W)
        txt_update_pizza = ttk.Entry(lower_frame, width=25, font=('Courier', 10), textvariable=self.cum_revenue)
        txt_update_pizza.grid(row=4, column=5, sticky=W, padx=5, pady=2)
        btn_total = Button(lower_frame, text='Enter', font=('Courier', 8, 'bold'), width=8, bg='white', fg='black')
        btn_total.grid(row=4, column=5, padx=0,pady=0,sticky=E)

        img_footer = Image.open('photo/footer.jpeg')
        img_footer = img_footer.resize((320, 110))
        self.photo_footer = ImageTk.PhotoImage(img_footer)
        self.img_footer= Label(lower_frame, image=self.photo_footer)
        self.img_footer.place(x=570, y=0, width=320, height=110)

     




        












    def add_data(self):
        if self.pizza_id.get() == "" or self.pizza_category.get() == "":
            messagebox.showerror('Error', 'All fields are required!')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO pizza_types VALUES(%s, %s, %s, %s)', (
                    self.pizza_id.get(),
                    self.pizza_name.get(),
                    self.pizza_category.get(),
                    self.pizza_ingredients.get(),
                ))
                conn.commit()
                conn.close()

                # Success message with pizza details
                success_message = f"Pizza has been added!\n\n" \
                                f"ID: {self.pizza_id.get()}\n" \
                                f"Name: {self.pizza_name.get()}\n" \
                                f"Category: {self.pizza_category.get()}\n" \
                                f"Ingredients: {self.pizza_ingredients.get()}"
                messagebox.showinfo('Success', success_message, parent=self.root)

            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)





    def delete_data(self):
        if self.pizza_id_for_delete.get() == "":
            messagebox.showerror('Error', 'Pizza ID is required for deletion!')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
                my_cursor = conn.cursor()

                # Fetch pizza details before deletion
                my_cursor.execute('SELECT * FROM pizza_types WHERE pizza_type_id = %s', (self.pizza_id_for_delete.get(),))
                pizza = my_cursor.fetchone()

                if pizza:
                    # Prepare the message to show the details of the pizza being deleted
                    pizza_details = f"Deleting Pizza:\n\nID: {pizza[0]}\nName: {pizza[1]}\nCategory: {pizza[2]}\nIngredients: {pizza[3]}"
                    # Proceed to delete
                    my_cursor.execute('DELETE FROM pizza_types WHERE pizza_type_id = %s', (self.pizza_id_for_delete.get(),))
                    conn.commit()
                    messagebox.showinfo('Deleted', pizza_details, parent=self.root)  # Show deletion info
                else:
                    messagebox.showinfo('Not Found', 'No pizza found with the given ID.', parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)





    def update_data(self):
        pizza_id = self.pizza_id_for_update.get()

        if not pizza_id:
            messagebox.showerror("Input Error", "Please enter a Pizza ID.")
            return

        # Prompt for new values using message boxes
        new_category = simpledialog.askstring("Input", "Enter new Category:")
        if not new_category:
            messagebox.showerror("Input Error", "Please enter a Category.")
            return

        new_name = simpledialog.askstring("Input", "Enter new Name:")
        if not new_name:
            messagebox.showerror("Input Error", "Please enter a Name.")
            return

        new_ingredients = simpledialog.askstring("Input", "Enter new Ingredients:")
        if not new_ingredients:
            messagebox.showerror("Input Error", "Please enter Ingredients.")
            return

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='nas@123',  
                database='pizzahut'
            )
            cursor = conn.cursor()

            # Construct and execute the update query
            query = """
            UPDATE pizza_types
            SET name = %s, category = %s, ingredients = %s
            WHERE pizza_type_id = %s
            """
            cursor.execute(query, (new_name, new_category, new_ingredients, pizza_id))
            conn.commit()

            # if cursor.rowcount > 0:
            #     messagebox.showinfo("Success", "Pizza type updated successfully!")
            # else:
            #     messagebox.showwarning("No Match", "No matching record found to update.")
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Pizza type updated successfully!\n\n"
                                           f"Name: {new_name}\n"
                                           f"Category: {new_category}\n"
                                           f"Ingredients: {new_ingredients}")
            else:
                messagebox.showwarning("No Match", "No matching record found to update.")
            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")



    def search_data(self):
        if self.search_id.get() == "":
            messagebox.showerror('Error', 'Pizza ID is required for search!')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
                my_cursor = conn.cursor()

                # Fetch pizza details for the given ID
                my_cursor.execute('SELECT * FROM pizza_types WHERE pizza_type_id = %s', (self.search_id.get(),))
                pizza = my_cursor.fetchone()

                if pizza:
                    # Prepare the message to display pizza details
                    pizza_details = f"Search Result:\n\nID: {pizza[0]}\nName: {pizza[1]}\nCategory: {pizza[2]}\nIngredients: {pizza[3]}"
                    messagebox.showinfo('Search Result', pizza_details, parent=self.root)
                    

                else:
                    messagebox.showinfo('Not Found', 'No pizza found with the given ID.', parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)


    def show_all_pizzas(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
            my_cursor = conn.cursor()

            # Fetch all data from the pizza_types table
            my_cursor.execute('SELECT * FROM pizza_types')
            pizzas = my_cursor.fetchall()

            if pizzas:
                # Create a Tkinter window for the scrolling message box
                scroll_window = Toplevel(self.root)
                scroll_window.title("All Pizzas")
                scroll_window.configure(bg="lightgrey")  # Set background color

                # Create a scrolledtext widget for displaying pizza details
                scroll_box = scrolledtext.ScrolledText(scroll_window, width=100, height=40, wrap=WORD)
                scroll_box.pack(expand=True, fill="both")

                # Prepare the message to display all pizza details
                all_pizza_details = "All Pizzas:\n\n"
                for pizza in pizzas:
                    all_pizza_details += f"ID: {pizza[0]}\nName: {pizza[1]}\nCategory: {pizza[2]}\nIngredients: {pizza[3]}\n\n"

                # Insert the message into the scrolling message box
                scroll_box.insert(END, all_pizza_details)
                scroll_box.configure(state='disabled', bg="green", fg="white")  # Customize text colors

                # Create a cancel button
                cancel_button = Button(scroll_window, text="Cancel", command=scroll_window.destroy, bg="red", fg="white")
                cancel_button.pack(pady=10)

            else:
                messagebox.showinfo('Empty', 'No pizzas found in the database.', parent=self.root)

            conn.close()
        except Exception as es:
            messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)

    def clear_data(self):
        self.pizza_id.set('')
        self.pizza_category.set('')
        self.pizza_id_for_delete.set('')
        self.pizza_id_for_update.set('')
        self.pizza_ingredients.set('')
        self.pizza_name.set('')


    def set_data(self):
        if self.pizza_info_id.get() == "" or self.pizza_info_type_id.get() == "":
            messagebox.showerror('Error', 'All fields are required!')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO pizzas VALUES(%s, %s, %s, %s)', (
                    self.pizza_info_id.get(),
                    self.pizza_info_type_id.get(),
                    self.pizza_size.get(),
                    self.pizza_price.get(),
                ))
                conn.commit()
                conn.close()

                # Success message with pizza details
                success_message = f"Pizza INFO has been added!\n\n" \
                                f"ID: {self.pizza_info_id.get()}\n" \
                                f"Name: {self.pizza_info_type_id.get()}\n" \
                                f"Category: {self.pizza_size.get()}\n" \
                                f"Ingredients: {self.pizza_price.get()}"
                messagebox.showinfo('Success', success_message, parent=self.root)

            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)



    def show_all_pizzas_info(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
            my_cursor = conn.cursor()

            # Fetch all data from the pizza_types table
            my_cursor.execute('SELECT * FROM pizzas')
            pizzas = my_cursor.fetchall()

            if pizzas:
                # Create a Tkinter window for the scrolling message box
                scroll_window = Toplevel(self.root)
                scroll_window.title("All Pizzas INFO")
                scroll_window.configure(bg="lightgray")  # Set background color

                # Create a scrolledtext widget for displaying pizza details
                scroll_box = scrolledtext.ScrolledText(scroll_window, width=100, height=35, wrap=WORD)
                scroll_box.pack(expand=True, fill="both")

                # Prepare the message to display all pizza details
                all_pizza_details = "All Pizzas:\n\n"
                for pizza in pizzas:
                    all_pizza_details += f"Pizza_ID: {pizza[0]}\Pizza_type_ID: {pizza[1]}\Size: {pizza[2]}\nPrice: {pizza[3]}\n\n"

                # Insert the message into the scrolling message box
                scroll_box.insert(END, all_pizza_details)
                scroll_box.configure(state='disabled', bg="red3", fg="white", font=('Courier', 10, 'bold'))  # Customize text colors

                # Create a cancel button
                cancel_button = Button(scroll_window, text="EXIT", command=scroll_window.destroy, bg="darkgreen", fg="white")
                cancel_button.pack(pady=10)

            else:
                messagebox.showinfo('Empty', 'No pizzas found in the database.', parent=self.root)

            conn.close()
        except Exception as es:
            messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)


    def delete_pizza_INFO(self):
        if self.pizza_id_info_for_delete.get() == "":
            messagebox.showerror('Error', 'Pizza ID is required for deletion!')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
                my_cursor = conn.cursor()

                # Fetch pizza details before deletion
                my_cursor.execute('SELECT * FROM pizzas WHERE pizza_id = %s', (self.pizza_id_info_for_delete.get(),))
                pizza = my_cursor.fetchone()

                if pizza:
                    # Prepare the message to show the details of the pizza being deleted
                    pizza_details = f"Deleting Pizza:\n\nID: {pizza[0]}\nPizza_type_ID: {pizza[1]}\nPizza_size: {pizza[2]}\nPizza_price: {pizza[3]}"
                    # Proceed to delete
                    my_cursor.execute('DELETE FROM pizzas WHERE pizza_id = %s', (self.pizza_id_info_for_delete.get(),))
                    conn.commit()
                    messagebox.showinfo('Deleted', pizza_details, parent=self.root)  # Show deletion info
                else:
                    messagebox.showinfo('Not Found', 'No pizza found with the given ID.', parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)


    def update_pizza_data(self):
        pizza_id = self.pizza_id_info_for_update.get()

        if not pizza_id:
            messagebox.showerror("Input Error", "Please enter a Pizza ID.")
            return

        # Prompt for new values using message boxes
        new_pizza_type_id = simpledialog.askstring("Input", "Enter new Pizza Type ID:")
        if not new_pizza_type_id:
            messagebox.showerror("Input Error", "Please enter a Pizza Type ID.")
            return

        new_size = simpledialog.askstring("Input", "Enter new Size:")
        if not new_size:
            messagebox.showerror("Input Error", "Please enter a Size.")
            return

        new_price = simpledialog.askstring("Input", "Enter new Price:")
        if not new_price:
            messagebox.showerror("Input Error", "Please enter a Price.")
            return

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='nas@123',  
                database='pizzahut'
            )
            cursor = conn.cursor()

            # Construct and execute the update query
            query = """
            UPDATE pizzas
            SET pizza_type_id = %s, size = %s, price = %s
            WHERE pizza_id = %s
            """
            cursor.execute(query, (new_pizza_type_id, new_size, new_price, pizza_id))
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Pizza updated successfully!\n\n"
                                           f"Name: {new_pizza_type_id}\n"
                                           f"Category: {new_size}\n"
                                           f"Ingredients: {new_price}")
            else:
                messagebox.showwarning("No Match", "No matching record found to update.")

            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        

    def search_data_INFO(self):
        if self.search_info_id.get() == "":
            messagebox.showerror('Error', 'Pizza ID is required for search!')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
                my_cursor = conn.cursor()

                # Fetch pizza details for the given ID
                my_cursor.execute('SELECT * FROM pizzas WHERE pizza_id = %s', (self.search_info_id.get(),))
                pizza = my_cursor.fetchone()

                if pizza:
                    # Prepare the message to display pizza details
                    pizza_details = f"Search Result:\n\npizza_ID: {pizza[0]}\nPizza_type_ID: {pizza[1]}\nSize: {pizza[2]}\nPrice: {pizza[3]}"
                    messagebox.showinfo('Search Result', pizza_details, parent=self.root)
                    

                else:
                    messagebox.showinfo('Not Found', 'No pizza found with the given ID.', parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)



    def reset_data(self):
        self.pizza_info_id.set('')
        self.pizza_info_type_id.set('')
        self.pizza_size.set('')
        self.pizza_price.set('')
        self.pizza_id_info_for_delete.set('')
        self.pizza_id_info_for_update.set('')



    def calculate_total_revenue(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
            my_cursor = conn.cursor()
            my_cursor.execute('SELECT SUM(orders_details.quantity * pizzas.price) AS total_revenue FROM orders_details JOIN pizzas ON pizzas.pizza_id = orders_details.pizza_id')

            total_revenue = my_cursor.fetchone()[0]
            messagebox.showinfo('Total Revenue', f'Total Revenue: ${total_revenue}')
            # self.custom_message_box('Total Revenue', f'Total Revenue: ${total_revenue}')
            conn.close()
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {str(e)}')


    
    def execute_sql_query(self):
    # Connect to the SQLite database
        conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
        cursor = conn.cursor()
        query = f"""
        SELECT pizza_types.name, pizzas.price
        FROM pizza_types
        JOIN pizzas ON pizza_types.pizza_type_id = pizzas.pizza_type_id
        ORDER BY pizzas.price DESC
        LIMIT {self.limit.get()};
    """
        cursor.execute(query)
    
        # Fetch all the results
        results = cursor.fetchall()
    
        if results:
            # Prepare the message to display
            message = f"Top {self.limit.get()} Pizzas:\n\n"
            for result in results:
                message += f"{result[0]} - Price: ${result[1]}\n"
        # Display the message box with the results
            messagebox.showinfo(f"Top {self.limit.get()} Pizzas", message)
        else:
            messagebox.showinfo(f"Top {self.limit.get()} Pizzas", "No pizzas found.")
    
        # Close the database connection
        conn.close()


    def top_ordered(self):
    # Connect to the SQLite database
        conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
        cursor = conn.cursor()
        query = f"""
        SELECT pizza_types.name, SUM(orders_details.quantity) as quantity
        FROM pizza_types
        JOIN pizzas ON pizza_types.pizza_type_id = pizzas.pizza_type_id
        JOIN orders_details ON orders_details.pizza_id = pizzas.pizza_id
        GROUP BY pizza_types.name
        ORDER BY quantity DESC
        LIMIT {self.limit2.get()};
        """
        cursor.execute(query)
    
        # Fetch all the results
        results = cursor.fetchall()
    
        if results:
            # Prepare the message to display
            message = f"Top {self.limit2.get()} Pizza Types by Quantity Ordered:\n\n"
            for result in results:
                message += f"{result[0]} -> Quantity: {result[1]}\n"
            # Display the message box with the results
            messagebox.showinfo(f"Top {self.limit2.get()} Pizza Types", message)
        else:
            messagebox.showinfo(f"Top {self.limit2.get()} Pizza Types", "No pizza types found.")
    
        # Close the database connection
        conn.close()
    

    def details_order(self):
        order_id = self.order_id_entry.get()
        if order_id.isdigit():
            conn =  mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    pt.name AS PizzaName,
                    od.quantity AS Quantity,
                    p.price AS PricePerPizza,
                    o.order_date AS OrderDate,
                    o.order_time AS OrderTime
                FROM 
                    orders o
                JOIN 
                    orders_details od ON o.order_id = od.order_id
                JOIN 
                    pizzas p ON od.pizza_id = p.pizza_id
                JOIN 
                    pizza_types pt ON p.pizza_type_id = pt.pizza_type_id
                WHERE 
                    o.order_id = %s;
            """, (order_id,))
            result = cursor.fetchall()
            conn.close()
            if result:
                message = "\n".join([f"Pizza: {r[0]}\n, Quantity: {r[1]}\n, Price: ${r[2]}\n, Date: {r[3]}\n, Time: {r[4]}\n" for r in result])
                messagebox.showinfo("Order Details", message)
            else:
                messagebox.showinfo("Order Details", "No details found for this order ID.")
        else:
            messagebox.showerror("Input Error", "Please enter a valid numeric Order ID.")


    def find_and_show_pizzas(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='nas@123', database='pizzahut')
        cursor = conn.cursor()
        query = "SELECT * FROM pizzas WHERE price > %s AND price < %s"
        cursor.execute(query, (self.more_limit.get(), self.less_limit.get()))

        results = cursor.fetchall()
    
        if results:
            message = "\n".join([f"ID: {pizza[0]}, Name: {pizza[1]}, Type ID: {pizza[2]}, Price: ${pizza[3]:.2f}" for pizza in results])
        else:
            message = "No pizzas found in the specified price range."

        messagebox.showinfo("Pizzas", message)
        conn.close()


        

    def number_of_order(self):
        try:
            limit = int(self.num_of_order.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer value for the limit.")
            return

        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(host='localhost', user='root', password='nas@123', database='pizzahut')
            cursor = conn.cursor()

            # Construct and execute the query with the dynamic limit
            query = """
            SELECT orders.order_date as dd, SUM(orders_details.quantity)
            FROM orders 
            JOIN orders_details ON orders.order_id = orders_details.order_id
            GROUP BY orders.order_date 
            ORDER BY dd DESC 
            LIMIT %s
            """
            cursor.execute(query, (limit,))
            results = cursor.fetchall()

            conn.close()

            # Prepare and show the message
            if results:
                message = "\n".join([f"Date: {row[0]}, Total Quantity: {row[1]}" for row in results])
            else:
                message = "No orders found for the specified limit."
            messagebox.showinfo("Orders", message)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

   
    

    def Top_revenue(self):
        try:
            limit = int(self.based_on_revenue.get())  # Convert entry to an integer
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer value for the limit.")
            return

        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(host='localhost', user='root', password='nas@123', database='pizzahut')
            cursor = conn.cursor()

            # Construct and execute the query with the dynamic limit
            query = """
            SELECT pizza_types.name, SUM(orders_details.quantity * pizzas.price) AS revenue
            FROM pizza_types
            JOIN pizzas ON pizzas.pizza_type_id = pizza_types.pizza_type_id
            JOIN orders_details ON orders_details.pizza_id = pizzas.pizza_id
            GROUP BY pizza_types.name 
            ORDER BY revenue DESC 
            LIMIT %s
            """
            cursor.execute(query, (limit,))
            results = cursor.fetchall()

            conn.close()

            # Prepare and show the message
            if results:
                message = "\n".join([f"Pizza Type: {row[0]}, Total Revenue: ${row[1]:,.2f}\n" for row in results])
            else:
                message = "No data available for the specified limit."
            messagebox.showinfo("Revenue Report", message)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            



    def show_order_per_hour(self):
        try:
            
            conn = mysql.connector.connect(host='localhost', user='root', password='nas@123', database='pizzahut')
            cursor = conn.cursor()

            query = """
            SELECT HOUR(order_time) as hour, COUNT(order_id) as order_count
            FROM orders
            GROUP BY HOUR(order_time)
            """
            cursor.execute(query)
            results = cursor.fetchall()

            conn.close()

            if results:
                message = "\n".join([f"Hour: {row[0]}, Order Count: {row[1]}" for row in results])
            else:
                message = "No data available."
            messagebox.showinfo("Order Counts by Hour", message)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")



    def show_revenue_percentage(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='nas@123',  
                database='pizzahut'
            )
            cursor = conn.cursor()

            query = """
            SELECT pizza_types.category,
                   ROUND(SUM(orders_details.quantity * pizzas.price) / 
                         (SELECT ROUND(SUM(orders_details.quantity * pizzas.price), 2) 
                          FROM orders_details 
                          JOIN pizzas ON pizzas.pizza_id = orders_details.pizza_id) * 100, 2) AS revenue
            FROM pizza_types 
            JOIN pizzas ON pizza_types.pizza_type_id = pizzas.pizza_type_id
            JOIN orders_details ON orders_details.pizza_id = pizzas.pizza_id
            GROUP BY pizza_types.category 
            ORDER BY revenue DESC;
            """
            cursor.execute(query)
            results = cursor.fetchall()

            conn.close()

            if results:
                message = "\n".join([f"Category: {row[0]}, Revenue Percentage: {row[1]}%" for row in results])
            else:
                message = "No data available."
            messagebox.showinfo("Revenue Percentage by Category", message)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")




    def show_cumulative_revenue(self):
        try:
            limit = int(self.cum_revenue.get())  
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer value for the limit.")
            return

        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='nas@123',  
                database='pizzahut'
            )
            cursor = conn.cursor()
            query = """
            SELECT order_date,
                   SUM(revenue) OVER (ORDER BY order_date) AS cum_revenue
            FROM (
                SELECT orders.order_date,
                       SUM(orders_details.quantity * pizzas.price) AS revenue
                FROM orders_details
                JOIN pizzas ON orders_details.pizza_id = pizzas.pizza_id
                JOIN orders ON orders.order_id = orders_details.order_id
                GROUP BY orders.order_date
            ) AS sales
            ORDER BY cum_revenue
            LIMIT %s
            """
            cursor.execute(query, (limit,))
            results = cursor.fetchall()

            conn.close()

            # Prepare and show the message
            if results:
                message = "\n".join([f"Date: {row[0]}, Cumulative Revenue: ${row[1]:,.2f}" for row in results])
            else:
                message = "No data available for the specified limit."
            messagebox.showinfo("Cumulative Revenue by Date", message)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")



    def show_pizza_quantity_by_size(self):
        try:
           
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='nas@123', 
                database='pizzahut'
            )
            cursor = conn.cursor()

            query = """
            SELECT pizzas.size AS Size, COUNT(orders_details.order_details_id) AS Quantity
            FROM pizzas 
            JOIN orders_details ON pizzas.pizza_id = orders_details.pizza_id
            GROUP BY pizzas.size
            """
            cursor.execute(query)
            results = cursor.fetchall()

            conn.close()

            # Prepare and show the message
            if results:
                message = "\n".join([f"Size: {row[0]}, Quantity: {row[1]}" for row in results])
            else:
                message = "No data available."
            messagebox.showinfo("Pizza Quantity by Size", message)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")



if __name__ == '__main__':
    root = Tk()
    obj = Employee(root)
    root.mainloop()
    
