import phonenumbers
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from phonenumbers import carrier
import matplotlib.pyplot as plt
from opencage.geocoder import OpenCageGeocode
import  folium
import pandas as pd
from phonenumbers import geocoder
import tkinter.ttk as ttk
from phonenumbers import timezone
import  gmaps
from tkinter import *
import tkinter as tk
from tkinter import Tk, Button, Text
import win32print
import csv


Key="79cddf3cc33c4231b61622f917ea8850"
print('ENSURE YOU INCLUDE COUNTRY CODE BEFORE NUMBER eg(+2349080249554)')
c=input("ENTER NUMBER:")
phone_number = phonenumbers.parse(c)
location = geocoder.description_for_number(phone_number, "en")
geocoder = OpenCageGeocode(Key)
query = str(location)
result = geocoder.geocode(query)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
long = result[0]['geometry']['lng']
mytime = timezone.time_zones_for_number(phone_number)
parsed_number = phonenumbers.parse(c, "CH")
valid_check = phonenumbers.is_valid_number(parsed_number)
mymap = folium.Map(location=[lat, lng], zoom_start=9)
mymap1 = gmaps.Map(location=[lat, lng], zoom_start=9)
mymap.save("maplocation.html")
print(c)
print(f"Number valid: {valid_check}")
print(location)
print(carrier.name_for_number(phone_number, "en"))
print("Latitude:", lat)
print("Longtitude:", lng)
print("Longtitudemum:", long)
print(mytime)
print(result)


file_object = open("trackdetails.csv", "a")
writer = csv. writer(file_object, delimiter = ",")
writer. writerow([c,carrier.name_for_number(phone_number, "en"),f"{valid_check}",f"{mytime}",f"{lat}",f"{long}"])
file_object.close()


login_screen = Tk()
login_screen.title("(Tracker)")
login_screen.config(bg="white")

fmbar2=tk.Frame(login_screen,bg="white",width=500,height=300)
fmbar2.pack(side=tk.RIGHT, fill=tk.BOTH)

F5 = Frame(login_screen,bg="white",width=700,height=350,relief=GROOVE, bd=10)
F5.pack(side=tk.LEFT, fill=tk.BOTH)
lndrq = Label(F5, text='Numbers,Service Providers,Number Validity,Country,Lat,Long',anchor="w", font='arial 15',relief=GROOVE, bd=4).pack(fill=X)

df = pd.read_csv (r'trackdetails.csv')
figure2 = plt.Figure(figsize=(5, 2), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, fmbar2)
line2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
yer=df.groupby('Service Providers')['Service Providers'].size()
yer.plot(kind="pie",autopct='%1.1f%%',shadow=True,ax=ax2, startangle=90, fontsize=6)
ax2.set_title("STATISTIC OF SERVICE PROVIDERS",font="century",fontsize=9)
ax2.legend(bbox_to_anchor=(1,0),loc='lower right',bbox_transform=figure2.transFigure,prop={'size':8})
print (df)



element_header = ['1st', '2nd', '3rd', '4th', '5th','6th']
treeSpen = tk.Scrollbar(F5)
treeSpen.pack(side='right', fill='y')


tree =ttk.Treeview(F5, columns=element_header,height=20, show="headings")
tree.configure(yscrollcommand=treeSpen.set)
tree.column('1st', width=150, minwidth=100, stretch=tk.NO)
tree.column('2nd', width=70, minwidth=100, stretch=tk.NO)
tree.column('3rd', width=70, minwidth=100, stretch=tk.NO)
tree.column('4th', width=100, minwidth=100, stretch=tk.NO)
tree.column('5th', width=100, minwidth=100, stretch=tk.NO)
tree.column('6th', width=100, minwidth=100, stretch=tk.NO)

with open("trackdetails.csv") as myfile:
    reader = csv.DictReader(myfile, delimiter=',')
    for row_id in reader:
        nmb=row_id['Numbers']
        name = row_id['Service Providers']
        nsurname = row_id['Number Validity']
        nsurnj = row_id['Country']
        nsnj = row_id['Lat']
        nlnj = row_id['Long']
        tree.insert(parent='', index='end',  text='', values=(nmb,name, nsurname,nsurnj,nsnj,nlnj))
        tree.pack(side='left', padx=0, pady=0)
        treeSpen.config(command=tree.yview)

login_screen.mainloop()









