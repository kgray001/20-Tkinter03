###############################################################################
# DONE: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk

form = tk.Tk()
form.title("Form")
# https://stackoverflow.com/questions/2744795/background-color-for-tk-in-python
form.configure(background = "black")

form.columnconfigure([0,1,2], weight = 1, minsize = 50)
form.rowconfigure([0,1,2,3,4,5], weight = 1, minsize = 75)

welcome = tk.Frame(
    master = form,
    relief = tk.RAISED,
    borderwidth = 5
)
welcome.grid(row = 0, column = 1)
welcome_label = tk.Label(
    master = welcome,
    text = "Hello!\nPlease fill out all given\n fields before submitting!",
    bg = "#37799a",
    fg = "black"
)
welcome_label.pack()
name_frame = tk.Frame(
    master = form
)
name_frame.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
name = tk.Label(
    master = name_frame,
    text = "Name:",
    bg =  "#37799a",
    fg = "black" 
)
name.pack(fill = tk.X)
name_2 = tk.Entry(
    master = name_frame
)
name_2.pack(fill = tk.X)

address_frame = tk.Frame(
    master = form
)
address_frame.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
A1 = tk.Label(
    master = address_frame,
    text = "Adress Line 1:",
    bg =  "#37799a",
    fg = "black" 
)
A1.pack(fill = tk.X)
A1_2 = tk.Entry(
    master = address_frame
)
A1_2.pack(fill = tk.X)

address_frame_2 = tk.Frame(
    master = form
)
address_frame_2.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
A2 = tk.Label(
    master = address_frame_2,
    text = "Address Line 2:",
    bg =  "#37799a",
    fg = "black" 
)
A2.pack(fill = tk.X)
A2_2 = tk.Entry(
    master = address_frame_2
)
A2_2.pack(fill = tk.X)

city_frame = tk.Frame(
    master = form
)
city_frame.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
city = tk.Label(
    master = city_frame,
    text = "City:",
    bg =  "#37799a",
    fg = "black" 
)
city.pack(fill = tk.X)
city_2 = tk.Entry(
    master = city_frame
)
city_2.pack(fill = tk.X)

state_frame = tk.Frame(
    master = form
)
state_frame.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
state = tk.Label(
    master = state_frame,
    text = "State:",
    bg =  "#37799a",
    fg = "black" 
)
state.pack(fill = tk.X)
state_2 = tk.Entry(
    master = state_frame
)
state_2.pack(fill = tk.X)

zip_frame = tk.Frame(
    master = form
)
zip_frame.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
zip = tk.Label(
    master = zip_frame,
    text = "Zip Code:",
    bg =  "#37799a",
    fg = "black" 
)
zip.pack(fill = tk.X)
zip_2 = tk.Entry(
    master = zip_frame
)
zip_2.pack(fill = tk.X)

number_frame = tk.Frame(
    master = form
)
number_frame.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
number = tk.Label(
    master = number_frame,
    text = "Phone Number:",
    bg =  "#37799a",
    fg = "black" 
)
number.pack(fill = tk.X)
number_2 = tk.Entry(
    master = number_frame
)
number_2.pack(fill = tk.X)

email_frame = tk.Frame(
    master = form
)
email_frame.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
email = tk.Label(
    master = email_frame,
    text = "Email Address:",
    bg =  "#37799a",
    fg = "black" 
)
email.pack(fill = tk.X)
email_2 = tk.Entry(
    master = email_frame
)
email_2.pack(fill = tk.X)

submit = tk.Button(
    form,
    text = "Submit",
    bg = "white",
    fg = "black"
)
submit.grid(row = 5, column = 1)

form.mainloop()