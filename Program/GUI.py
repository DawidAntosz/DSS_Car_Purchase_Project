#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
import customtkinter
import Topsis_method
import RMS_method
import UTA_method

from dataStructures import Car2, getALLMatchingCarsAsLstOfCars

from typing import Tuple, List

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SWD System")
        self.geometry(f"{1100}x{650}")

        # configure grid layout  
        self.grid_columnconfigure(3, weight=2)
        

        # First frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=300, corner_radius=20)
        self.sidebar_frame.grid(row=0, column=0)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="SWD System", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False, command=self.button_change_event1,
                                                        values=["Opel", "Audi", "BMW", "Volvo", "Ford", "Honda", "Hyundai"])
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady=(5, 10))
        
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False, command=self.button_change_event2,
                                                        values=["SUV", "Sedan", "Coupe", "hatchback"])
        self.optionmenu_2.grid(row=2, column=0, padx=20, pady=(5, 10))
        
        

        self.price = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Cena [zł]", )
        self.price.grid(row=3, column=0, padx=10, pady=(5, 10))
        
        self.power = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Moc [KM]", )
        self.power.grid(row=4, column=0, padx=10, pady=(5, 10))
        
        self.engine_capacity = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Poj. silnika [cm^3]", )
        self.engine_capacity.grid(row=5, column=0, padx=10, pady=(5, 10))
        
        self.max_torque = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Moment [Nm]", )
        self.max_torque.grid(row=6, column=0, padx=10, pady=(5, 10))
        
        self.max_speed = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Max. prędkosc [km/h]", )
        self.max_speed.grid(row=7, column=0, padx=10, pady=(5, 10))

        self.acceleration = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Przyspieszenie 0-100/[s]", )
        self.acceleration.grid(row=8, column=0, padx=10, pady=(5, 10))

        self.consumption = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Zużycie [l/100km]", )
        self.consumption.grid(row=9, column=0, padx= 10, pady=(5, 10))
        
        self.tank_capacity = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Pojemnosc baku [l]", )
        self.tank_capacity.grid(row=10, column=0, padx= 10, pady=(5, 10))


        ## Botton search
        self.button_search = customtkinter.CTkButton(self.sidebar_frame, text = "Szukaj", command=self.button_Search)
        self.button_search.grid(row=13, column=0, padx=20, pady=(5, 10))

        
        # set default values        
        self.optionmenu_1.set("Marka")
        self.optionmenu_2.set("Typ nadwozia")
        
        # Slicer window
        self.slice_frame = customtkinter.CTkFrame(self, width=150,height=300, corner_radius=0)
        self.slice_frame.grid(row=0, column=1, columnspan=2, padx=(10, 0), pady=(20, 0), sticky="nsew")

        self.logo_slice = customtkinter.CTkLabel(self.slice_frame, text="Waga [%]", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_slice.grid(row=1, column=0)
        
        
        self.slider_1 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_1.grid(row=2, column=0, padx=(20, 10), pady=(20, 10), sticky="ew")
        
        self.slider_2 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_2.grid(row=3, column=0, padx=(20, 10), pady=(20, 10), sticky="ew")
        
        self.slider_3 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_3.grid(row=4, column=0, padx=(20, 10), pady=(15, 10), sticky="ew")
        
        self.slider_4 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_4.grid(row=5, column=0, padx=(20, 10), pady=(15, 10), sticky="ew")
        
        self.slider_5 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_5.grid(row=6, column=0, padx=(20, 10), pady=(17, 10), sticky="ew")
        
        self.slider_6 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_6.grid(row=7, column=0, padx=(20, 10), pady=(17, 10), sticky="ew")
        
        self.slider_7 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_7.grid(row=8, column=0, padx=(20, 10), pady=(17, 10), sticky="ew")
        
        self.slider_8 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_8.grid(row=9, column=0, padx=(20, 10), pady=(17, 10), sticky="ew")
        
        self.slider_9 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_9.grid(row=10, column=0, padx=(20, 10), pady=(17, 10), sticky="ew")
        
        self.slider_10 = customtkinter.CTkSlider(self.slice_frame, from_= 0, to=1, number_of_steps=100)
        self.slider_10.grid(row=11, column=0, padx=(20, 10), pady=(17, 10), sticky="ew")



        self.label_op3 = customtkinter.CTkLabel(self.slice_frame, text="Select Method:", anchor="w")
        self.label_op3.grid(row=12, column=0, padx=20, pady=(10, 0))

        self.optionmenu_3 = customtkinter.CTkOptionMenu(self.slice_frame, dynamic_resizing=False, command=self.button_change_event3,
                                                        values=["Fuzi Topsis", "RSM", "UTA"])
        self.optionmenu_3.grid(row=13, column=0, padx=20, pady=(5, 10))
        self.optionmenu_3.set("--")

        


        # Result window
        self.Result_frame = customtkinter.CTkFrame(self, width=200,height=200, corner_radius=0)
        self.Result_frame.grid(row=0, column=3,columnspan=3,  padx=(10, 0), pady=(20, 0), sticky="nsew")

        self.logo_res = customtkinter.CTkLabel(self.Result_frame, text="Wyniki wyszukiwania :", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_res.grid(row=1, column=0)
        
        self.textbox = customtkinter.CTkTextbox(self.Result_frame, width=600, height =450)
        self.textbox.grid(row=2, column=0,padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def button_change_event1(self,mode: str):
        #print( mode)
        return mode
    
    def button_change_event2(self,mode: str):
        #print( mode)
        return mode

    def button_change_event3(self, mode: str):
        #print(mode)

        self.label_metric = customtkinter.CTkLabel(self.slice_frame, text="Metric:", anchor="w")
        self.label_metric.grid(row=14, column=0, padx=20, pady=(10, 0))

        self.optionmenu_metric = customtkinter.CTkOptionMenu(self.slice_frame, dynamic_resizing=False, command=self.button_change_event_metric)
        self.optionmenu_metric.grid(row=15, column=0, padx=20, pady=(5, 10))
        self.optionmenu_metric.set("--")

        if mode == 'Fuzi Topsis':
             self.optionmenu_metric.configure(values = ["Euclidean", "Chebyshev"])
        if mode == 'RSM':
            self.optionmenu_metric.configure(values = ["Euclidean"])
        if mode == 'UTA':
            self.optionmenu_metric.configure(values = ["Euclidean"])

        return mode
    
    def button_change_event_metric(self, mode: str):
        #print( mode)
        return mode
        
    
    def button_Search(self)-> List:
        
        ## dane szukania
        Data_search = [[self.optionmenu_1.get(), round(self.slider_1.get(),2)],
                       [self.optionmenu_2.get(), round(self.slider_2.get(),2)],
                       [self.price.get(), round(self.slider_3.get(),2)],
                       [self.power.get(), round(self.slider_4.get(),2)],
                       [self.engine_capacity.get(), round(self.slider_5.get(),2)],
                       [self.max_torque.get(), round(self.slider_6.get(),2)],
                       [self.max_speed.get(), round(self.slider_7.get(),2)],
                       [self.acceleration.get(), round(self.slider_8.get(),2)],
                       [self.consumption.get(), round(self.slider_9.get(),2)],
                       [self.tank_capacity.get(), round(self.slider_10.get(),2)],
                       [self.optionmenu_3.get()],
                       [self.optionmenu_metric.get()]]

        car_table_search = []
        #print(Data_search)
        

        marka = self.optionmenu_1.get()
        typ = self.optionmenu_2.get()
        metric = self.optionmenu_metric.get()

        weight_table = [
        round(self.slider_1.get(),2), round(self.slider_2.get(),2),
        round(self.slider_3.get(),2), round(self.slider_4.get(),2),
        round(self.slider_5.get(),2), round(self.slider_6.get(),2),
        round(self.slider_7.get(),2), round(self.slider_8.get(),2),
        round(self.slider_9.get(),2), round(self.slider_10.get(),2)
        ]
        

        if self.optionmenu_3.get() == "Fuzi Topsis":
            
            car_table_search = Topsis_method.Topsis(getALLMatchingCarsAsLstOfCars(marka, typ), weight_table, metric)
            self.Print_Result(car_table_search)
            

        if self.optionmenu_3.get() == "RSM":
            
            car_table_search = RMS_method.RMS_fun(getALLMatchingCarsAsLstOfCars(marka, typ), weight_table, metric)
            self.Print_Result(car_table_search)

        if self.optionmenu_3.get() == "UTA":

            car_table_search = UTA_method.UTA_fun(getALLMatchingCarsAsLstOfCars(marka, typ), weight_table, metric) 
            self.Print_Result(car_table_search)

        #print(Data_search)
        return Data_search


    
    def Print_Result(self, tab_car):
        
        #self.textbox.configure(state = not "disabled")
        #tab_car=list(reversed(tab_car))
        counter = 11
        for text in tab_car:
            counter -=1
            self.textbox.insert("0.0", str(counter)+")  " +  text + "\n\n")
            
        #self.textbox.configure(state="disabled")

    
    
    