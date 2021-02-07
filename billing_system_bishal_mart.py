from tkinter import*
from tkinter import Tk
import math,random
from tkinter import messagebox
import os

class billings:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x470+0+0")
        self.root.title("BISHAL_MART_BILLING_SYSTEM")
        bg_color="#074463"
        #--------title frame------
        def title_frame():
            title=Label(self.root,text="BISHAL_MART",bd=10,relief="groove",bg=bg_color,fg="white",font=("times new roman",14,"bold"),pady=2)
            title.pack(side=TOP,fill=X)
        title_frame()

        #===========variables declarations===========
        def variables():
            #=====foods=====
            def foodings():
                self.momo=IntVar()
                self.chowmein=IntVar()
                self.burger=IntVar()
                self.pizza=IntVar()
                self.potato=IntVar()
            foodings()

            #========beverages===========
            def beveragees():
                self.coke=IntVar()
                self.fanta=IntVar()
                self.dew=IntVar()
                self.khukuri_rum=IntVar()
                self.gold_lebel=IntVar()
            beveragees()

            #========pastry======
            def pastries():
                self.black_forest=IntVar()
                self.hot_choclate=IntVar()
                self.jerry=IntVar()
                self.kitkat=IntVar()
                self.choco_pie=IntVar()
            pastries()

            #=========bills and taxes=========
            def billings():
                self.foods_total=StringVar()
                self.beverages_total=StringVar()
                self.pastry_total=StringVar()
                self.foods_tax=StringVar()
                self.beverages_tax=StringVar()
                self.pastry_tax=StringVar()
            billings()

            def bill_final():
                self.total_bill_amount=StringVar()
                self.total_discount=StringVar()
                self.grand_total=StringVar()

            bill_final()


            #==========customer=========
            def customers():
                self.c_name=StringVar()
                self.p_number=StringVar()
                self.bill_number=StringVar()
                x=random.randint(500,1000)
                self.bill_number.set(str(x))
                self.search_bill=StringVar()
            customers()
        variables()

        #-----customer details frame-----
        #bd=10,relief="groove"
        def customer_details_frame():
            frame1=Label(self.root,bd=8.,relief=GROOVE,text="CUSTOMER_DETAILS",font=("times new roman",8,"bold"),fg="gold",bg=bg_color)
            frame1.place(x=0,y=80,relwidth=1)

            c_name_lbl=Label(frame1,text="Customer name",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=5)
            c_name_txt=Entry(frame1,textvariable=self.c_name,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

            c_phone_lbl=Label(frame1,text="Phone number",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=5)
            c_phone_txt=Entry(frame1,textvariable=self.p_number,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

            bill_lbl=Label(frame1,text="Bill number",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=4,padx=20,pady=5)
            bill_txt=Entry(frame1,textvariable=self.bill_number,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)
        
            search_btn=Button(frame1,text="Search",command=self.search_records,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        customer_details_frame()

        def foods():
            frame2=Label(self.root,bd=10,relief=GROOVE,text="FOODS",font=("times new roman",8,"bold"),fg="gold",bg=bg_color)
            frame2.place(x=5,y=159,width=325,height=380)

            food_lbl=Label(frame2,text="mo:mo:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=5,sticky="w")
            food_txt=Entry(frame2,textvariable=self.momo,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            food_lbl=Label(frame2,text="chowmein:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=5,sticky="w")
            food_txt=Entry(frame2,textvariable=self.chowmein,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
  
            food_lbl=Label(frame2,text="burger:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=5,sticky="w")
            food_txt=Entry(frame2,textvariable=self.burger,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
  
            food_lbl=Label(frame2,text="pizza:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=3,column=0,padx=20,pady=5,sticky="w")
            food_txt=Entry(frame2,textvariable=self.pizza,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
  
            food_lbl=Label(frame2,text="potato fry:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=4,column=0,padx=20,pady=5,sticky="w")
            food_txt=Entry(frame2,textvariable=self.potato,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        foods()

        def beherages():
            frame3=Label(self.root,bd=10,relief=GROOVE,text="beverages",font=("times new roman",8,"bold"),fg="gold",bg=bg_color)
            frame3.place(x=330,y=159,width=325,height=380)

            bvg_lbl=Label(frame3,text="coke:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=5,sticky="w")
            bvg_txt=Entry(frame3,textvariable=self.coke,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            bvg_lbl=Label(frame3,text="fanta:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=5,sticky="w")
            bvg_txt=Entry(frame3,textvariable=self.fanta,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
  
            bvg_lbl=Label(frame3,text="dew:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=5,sticky="w")
            bvg_txt=Entry(frame3,textvariable=self.dew,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
  
            bvglbl=Label(frame3,text="khukuri rum:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=3,column=0,padx=20,pady=5,sticky="w")
            bvg_txt=Entry(frame3,textvariable=self.khukuri_rum,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
  
            bvg_lbl=Label(frame3,text="gold level:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=4,column=0,padx=20,pady=5,sticky="w")
            bvg_txt=Entry(frame3,textvariable=self.gold_lebel,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        beherages()

        def pastry():
            frame4=Label(self.root,bd=10,relief=GROOVE,text="pastry",font=("times new roman",8,"bold"),fg="gold",bg=bg_color)
            frame4.place(x=655,y=159,width=325,height=380)

            pastry_lbl=Label(frame4,text="black forest:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=5,sticky="w")
            pastry_txt=Entry(frame4,textvariable=self.black_forest,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            pastry_lbl=Label(frame4,text="hot choclate:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=5,sticky="w")
            pastry_txt=Entry(frame4,textvariable=self.hot_choclate,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
  
            pastry_lbl=Label(frame4,text="jerry:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=5,sticky="w")
            pastry_txt=Entry(frame4,textvariable=self.jerry,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
  
            pastry_lbl=Label(frame4,text="kit kat:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=3,column=0,padx=20,pady=5,sticky="w")
            pastry_txt=Entry(frame4,textvariable=self.kitkat,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
  
            pastry_lbl=Label(frame4,text="choco-pie:",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=4,column=0,padx=20,pady=5,sticky="w")
            pastry_txt=Entry(frame4,textvariable=self.choco_pie,width=10,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        pastry()

        #------------bill frame-----------------------
        def bill_area():
            frame5=Label(self.root,bd=10,relief=GROOVE)
            frame5.place(x=1000,y=159,width=350,height=380)

            bill_title=Label(frame5,bd=7,relief=GROOVE,text="Bill Area",font="arial 14 bold",fg="black",bg=bg_color)
            bill_title.pack(fill=X)

            def scrolls():
                y_scroll=Scrollbar(frame5,orient=VERTICAL)
                self.textarea=Text(frame5,yscrollcommand=y_scroll.set)
                y_scroll.pack(side=RIGHT,fill=Y)
                y_scroll.config(command=self.textarea.yview)
                self.textarea.pack(fill=BOTH,expand=1)
            scrolls()
        bill_area()

        #-----------buttons frame--------------
        def button_frame():
            #---frame-----
            frame6=Label(self.root,bd=10,relief=GROOVE,text="billings",font=("times new roman",14,"bold"),fg="gold",bg=bg_color)
            frame6.place(x=0,y=539,relwidth=1,height=160)
            #------variables----
            def bills():
                food_bill_lbl=Label(frame6,text="Total foods bill:",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=5,sticky="w")
                food_bill_txt=Entry(frame6,textvariable=self.foods_total,width=20,font="arial 10  bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

                bvg_bill_lbl=Label(frame6,text="Total beverages bill:",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=5,sticky="w")
                bvg_bill_txt=Entry(frame6,textvariable=self.beverages_total,width=20,font="arial 10  bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
                                
                pastry_bill_lbl=Label(frame6,text="Total pastry bill:",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=5,sticky="w")
                pastry_bill_txt=Entry(frame6,textvariable=self.pastry_total,width=20,font="arial 10  bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

                food_bill__tax_lbl=Label(frame6,text="Total foods tax:",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=5,sticky="w")
                food_bill_tax_txt=Entry(frame6,textvariable=self.foods_tax,width=20,font="arial 10  bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

                bvg_bill_txt_lbl=Label(frame6,text="Total beverages tax:",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=5,sticky="w")
                bvg_bill_txt=Entry(frame6,textvariable=self.beverages_tax,width=20,font="arial 10  bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
                                
                pastry_tax_bill_lbl=Label(frame6,text="Total pastry tax:",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=5,sticky="w")
                pastry_tax_bill_txt=Entry(frame6,textvariable=self.pastry_tax,width=20,font="arial 10  bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

            bills()

        
            def menus():
                menu_frame=Label(frame6,bd=8,relief=GROOVE)
                menu_frame.place(x=770,y=2,width=578,height=108)

                total_btn=Button(menu_frame,command=self.total,bd=2,text="Total",bg="cadetblue",fg="black",font=("times new roman",14,"bold"),pady=15,width=10).grid(row=0,column=0,padx=6,pady=6)
                generate_bill_btn=Button(menu_frame,command=self.bill_area,bd=2,text="Generate bill",bg="cadetblue",fg="black",font=("times new roman",14,"bold"),pady=15,width=12).grid(row=0,column=1,padx=6,pady=6)
                clear_btn=Button(menu_frame,bd=2,text="Clear",command=self.clear_data,bg="cadetblue",fg="black",font=("times new roman",14,"bold"),pady=15,width=10).grid(row=0,column=2,padx=6,pady=6)
                exit_btn=Button(menu_frame,bd=2,text="Exit",command=self.exit_system,bg="cadetblue",fg="black",font=("times new roman",14,"bold"),pady=15,width=10).grid(row=0,column=3,padx=6,pady=6)

            menus()
        button_frame()
        self.bill_welcomes()


    #==============billings and taxations:==========
    def total(self):
        self.momos=(self.momo.get()*120)
        self.chowmeins=(self.chowmein.get()*160)
        self.burgers=(self.burger.get()*250)
        self.pizzas=(self.pizza.get()*350)
        self.potatoes=(self.potato.get()*80)

        self.foods_total_price=float(self.momos+self.chowmeins+self.burgers+self.pizzas+self.potatoes )
        
        self.foods_total.set("Rs."+str(self.foods_total_price))
        self.food_tax=round((self.foods_total_price*0.05),2)
        self.foods_tax.set("Rs."+str(self.food_tax))

        self.cokes=(self.coke.get()*50)
        self.fantas=(self.fanta.get()*50)
        self.dews=(self.dew.get()*60)
        self.khukuri_rums=(self.khukuri_rum.get()*200)
        self.gold_lebels=(self.gold_lebel.get()*8000)

        self.beverages_total_price=float(self.cokes+self.fantas+self.dews+self.khukuri_rums+self.gold_lebels)
        
        self.beverages_total.set("Rs."+str(self.beverages_total_price))
        self.beverage_tax=round((self.beverages_total_price*0.05),2)
        self.beverages_tax.set("Rs."+str(self.beverage_tax))

        self.black_forests=(self.black_forest.get()*150)
        self.hot_choclates=(self.hot_choclate.get()*250)
        self.jerrys=(self.jerry.get()*25)
        self.kitkats=(self.kitkat.get()*250)
        self.choco_pies=(self.choco_pie.get()*30)

        self.pastry_total_price=float(self.black_forests+self.hot_choclates+self.jerrys+self.kitkats+self.choco_pies)
        
        self.pastry_total.set("Rs."+str(self.pastry_total_price))
        self.pastryy_tax=round((self.pastry_total_price*0.05),2)
        self.pastry_tax.set("Rs."+str(self.pastryy_tax))

        self.total_bill_amount=( self.foods_total_price+self.beverages_total_price+self.pastry_total_price+
                                  self.food_tax+self.beverage_tax+self.pastryy_tax
                                )

        #self.total_discount=(self.total_bill_amount*2/100)
        
        def customer_grading(bill):
            if bill>=0 and self.bill<= 15000:
                category=='normal_customer'
                discount=2/100
            elif bill<=30000:
                category=='bronze_customer'
                discount=15/100
            elif bill<=50000:
                category=='silver_customer'
                discount=25/100
            elif bill>50000:
                category=='gold_customer'
                discount=40/100

            else:
                breakpoint()

            return category,discount

        self.c_category,self.total_discount=customer_grading(self.total_bill_amount)
        self.grand_total=(self.total_bill_amount-self.total_discount)



    #total(self)

    #============welcome nav to bill=======
    def bill_welcomes(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome to BISHAL_MART\n")
        self.textarea.insert(END,f"\nBill Number: {self.bill_number.get()}")
        self.textarea.insert(END,f"\nCustomer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\nPhone Number: {self.p_number.get()}")
        self.textarea.insert(END,f"\n\n======================================")
        self.textarea.insert(END,f"\nProduct name\t\tQuantity\t\tAmount")
        self.textarea.insert(END,f"\n======================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.p_number.get()=="":
            messagebox.showerror("Error on data","Error! Customer details can't be empty")

        elif self.foods_total.get()=="Rs.0.0" and self.beverages_total.get()=="Rs.0.0" and self.pastry_total.get()=="Rs.0.0":
            messagebox.showerror("Error on items","No items purchased//ordered")
        else:
            self.bill_welcomes()
            #========methods for the bill areas to get the products quantity and amounts and display it at bill area======
            def foods_billings():
                if self.momo.get()!=0:
                    self.textarea.insert(END,f"\nmo:mo\t\t{self.momo.get()}\t\t{self.momos}")
                if self.chowmein.get()!=0:
                    self.textarea.insert(END,f"\nChowmein\t\t{self.chowmein.get()}\t\t{self.chowmeins}")
                if self.burger.get()!=0:
                    self.textarea.insert(END,f"\nBurger\t\t{self.burger.get()}\t\t{self.burgers}")
                if self.pizza.get()!=0:
                    self.textarea.insert(END,f"\nPizza\t\t{self.pizza.get()}\t\t{self.pizzas}")
                if self.potato.get()!=0:
                    self.textarea.insert(END,f"\nPotatoes\t\t{self.potato.get()}\t\t{self.potatoes}")
            foods_billings()
            def beverages_billings():
                if self.coke.get()!=0:
                    self.textarea.insert(END,f"\nCoke\t\t{self.coke.get()}\t\t{self.cokes}")
                if self.fanta.get()!=0:
                    self.textarea.insert(END,f"\nFanta\t\t{self.fanta.get()}\t\t{self.fantas}")
                if self.dew.get()!=0:
                    self.textarea.insert(END,f"\nDew\t\t{self.dew.get()}\t\t{self.dew}")
                if self.khukuri_rum.get()!=0:
                    self.textarea.insert(END,f"\nKhukuri Rum\t\t{self.khukuri_rum.get()}\t\t{self.khukuri_rums}")
                if self.gold_lebel.get()!=0:
                    self.textarea.insert(END,f"\nGold Label\t\t{self.gold_lebel.get()}\t\t{self.gold_lebels}")
            beverages_billings()

            def pastry_billings():
                if self.black_forest.get()!=0:
                    self.textarea.insert(END,f"\nBlack forest\t\t{self.black_forest.get()}\t\t{self.black_forests}")
                if self.hot_choclate.get()!=0:
                    self.textarea.insert(END,f"\nHot choclate\t\t{self.hot_choclate.get()}\t\t{self.hot_choclates}")
                if self.jerry.get()!=0:
                    self.textarea.insert(END,f"\Jerry\t\t{self.jerry.get()}\t\t{self.jerry}")
                if self.kitkat.get()!=0:
                    self.textarea.insert(END,f"\nKit Kat\t\t{self.kitkat.get()}\t\t{self.kitkats}")
                if self.choco_pie.get()!=0:
                    self.textarea.insert(END,f"\nChoco pie\t\t{self.choco_pie.get()}\t\t{self.choco_pies}")
            pastry_billings()
            #=====gettings and displaying tax amounts at bill===========
            def taxations():
                self.textarea.insert(END,f"\n\n--------------------------------------\n")
                if self.foods_tax.get()!="Rs.0.0":
                    self.textarea.insert(END,f"Foods Tax\t\t{self.foods_tax.get()}")
                if self.beverages_tax.get()!="Rs.0.0":
                    self.textarea.insert(END,f"\nBeverages Tax\t\t{self.beverages_tax.get()}")
                if self.pastry_tax.get()!="Rs.0.0":
                    self.textarea.insert(END,f"\nPastry Tax\t\t{self.pastry_tax.get()}")
                self.textarea.insert(END,f"\n--------------------------------------\n")
            taxations()

            def final_bills():
                self.textarea.insert(END,f"\n--------------------------------------")
                self.textarea.insert(END,f"\nTotal Amount:\t\tRs. {self.total_bill_amount}")
                self.textarea.insert(END,f"\nCustomer category:\t\t{self.c_category}")
                self.textarea.insert(END,f"\nDiscount Amount:\t\tRs. {self.total_discount}")
                self.textarea.insert(END,f"\nGrand Total:\t\tRs. {self.grand_total}")
                self.textarea.insert(END,f"\n--------------------------------------")

            final_bills()
            self.save_records()

    def save_records(self):
        op=messagebox.askyesno("Save bill","Do you want to save this bill records.!!!") 
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            with open("customer_records/"+str(self.bill_number.get())+".txt","w") as file:
                file.write(self.bill_data)
                file.close()
            messagebox.showinfo("Saved","records saved successfully!")
                

        else:
            return 

    def search_records(self):
        #present="no"
        for i in os.listdir("customer_records/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"customer_records/{i}","r")
                self.textarea.delete('1.0',END)
                for a in f1:
                    self.textarea.insert(END,a)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill number") 

    def clear_data(self):
        op=messagebox.askyesno("Clear","Would you like to clear this data?!")
        if op>0:
            #=====foods=====
            def foodings():
                self.momo.set(0)
                self.chowmein.set(0)
                self.burger.set(0)
                self.pizza.set(0)
                self.potato.set(0)
            foodings()

            #========beverages===========
            def beveragees():
                self.coke.set(0)
                self.fanta.set(0)
                self.dew.set(0)
                self.khukuri_rum.set(0)
                self.gold_lebel.set(0)
            beveragees()

            #========pastry======
            def pastries():
                self.black_forest.set(0)
                self.hot_choclate.set(0)
                self.jerry.set(0)
                self.kitkat.set(0)
                self.choco_pie.set(0)
            pastries()

            #=========bills and taxes=========
            def billings():
                self.foods_total.set("")
                self.beverages_total.set("")
                self.pastry_total.set("")
                self.foods_tax.set("")
                self.beverages_tax.set("")
                self.pastry_tax.set("")
            billings()

            def customers():
                self.c_name.set("")
                self.p_number.set("")
                self.bill_number.set("")
                x=random.randint(500,1000)
                self.bill_number.set(str(x))
                self.search_bill.set("")
            customers()
            
            def bill_final():
                self.total_bill_amount.set("")
                self.total_discount.set("")
                self.grand_total.set("")
            bill_final()

        self.bill_welcomes()

    def exit_system(self):
        op=messagebox.askyesno("Exit","Would you like to exit?!")
        if op>0:
            self.root.destroy()  

    def add_to_database(self):
    #-----defining the methods for the databases-----
        con=pymysql.connect(host="localhost",user="root",password="",database="students")
        cur=con.cursor()
        cur.execute("insert into sales_records values(%s,%s,%s,%s,%s,%s)",(self.c_name.get(),
                                                                self.p_number.get(),
                                                                self.bill_number.get(),
                                                                self.total_bill_amount.get(),
                                                                self.total_discount.get(),
                                                                self.grand_total.get('1.0',END)
                                                                            ))

        con.commit()
        con.close()
    

        #sending email code:
        
        '''
        import smtplib, ssl
        def mails():

            port = 587  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = input("Enter the sender email address:") #"beesalsk@gmail.com"  Enter your address
            password =  input("Enter the sender email password: ")
            receiver_email = input("Enter the receiver email address:") #"bishal.kunwar487@gmail.com" Enter receiver address
            message = """\
            Subject: Hi there

            This message is sent from Python."""
            print("Welcome")
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

        mails()
        
        '''



root = Tk()
obj = billings(root)
root.mainloop()