
##This program prints the list of first name of the athletes and when clicked on the name of any athletes displays all the details of respective athletes
## and takes the input of sports in the entry widget and displays the first name of the athletes of respective sport


from tkinter import *

# Create main window
window = Tk()
#title for main window
window.title("Athletes App")
#provide the size of the window
window.geometry('1500x600')
# Create list of athletes
ATHLETES = [
    ["Bart", "Walsh", "Male", 23, 75, 178, "Blue", "Tennis", "B"],
    ["Beth", "Wolf", "Female", 25, 55, 162, "Black", "Tabletennis", "A"],
    ["Blaine", "Mann", "Male", 18, 70, 172, "Gray", "Volleyball", "A"],
    ["Chris", "House", "Female", 17, 60, 170, "Brown", "Netball", "C"],
    ["Dawn", "Holt", "Female", 26, 62, 177, "Green", "Volleyball", "B"],
    ["Earle", "Hobbs", "Male", 27, 80, 185, "Blue", "Basketball", "B"],
    ["Fay", "Nash", "Female", 19, 56, 158, "Amber", "Cycling", "A"],
    ["Gayle", "Pierce", "Female", 19, 57, "159", "Hazel", "Gymnastics", "A"],
    ["Glenn", "Green", "Male", 21, 71, 166, "Amber", "Tabletennis", "C"],
    ["Jacques", "Pace", "Male", 26, 65, 163, "Gray", "Swimming", "A"],
    ["Jeanne", "Riggs", "Female", 18, 62, 172, "Blue", "Netball", "B"],
    ["Jim", "Leach", "Male", 16, 72, 164, "Brown", "Cycling", "C"],
    ["Joan", "Hill", "Female", 16, 53, 164, "Black", "Netball", "C"],
    ["Jon", "Webb", "Male", 30, 63, 175, "Green", "Gymnastics", "A"],
    ["Leigh", "Graves", "Female", 31, 70, 180, "Black", "Volleyball", "A"],
    ["Marc", "Klein", "Male", 32, 79, 188, "Blue", "Volleyball", "C"],
    ["Merle", "Joyce", "Male", 24, 74, 183, "Green", "Basketball", "B"],
    ["Pearl", "Roach", "Female", 23, 63, 182, "Gray", "Tennis", "C"],
    ["Reid", "Short", "Male", 20, 66, 168, "Hazel", "Swimming", "A"],
    ["Shawn", "Kane", "Female", 20, 61, 174, "Brown", "Tabletennis", "A"]]

#label to display the heading
label1 = Label(window,  text='Welcome to Athletes App (Stage 2)!!', font=('Times', 24))
label1.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

#label to display the text for the listbox of the athletes
label2 = Label(window,  text='Athletes list')
label2.grid(row = 1)

# Create listbox to display athletes' first names
athlete_listbox = Listbox(window)
athlete_listbox.grid()
for athlete in ATHLETES:
    athlete_listbox.insert(END, athlete[0])

# Create entry widgets to display athlete details
first_name_entry = Entry(window)
last_name_entry = Entry(window)
gender_entry = Entry(window)
age_entry = Entry(window)
weight_entry = Entry(window)
height_entry = Entry(window)
eye_color_entry = Entry(window)
sport_entry = Entry(window)
level_entry = Entry(window)
l1 = Label(window, text="Firstname")
l1.grid(row=1, column=1)
l2 = Label(window, text="Lastname")
l2.grid(row=1, column=2)
l3 = Label(window, text="Gender")
l3.grid(row=1, column=3)
l4 = Label(window, text="Age")
l4.grid(row=1, column=4)
l5 = Label(window, text="Weight")
l5.grid(row=1, column=5)
l6 = Label(window, text="Height")
l6.grid(row=1, column=6)
l7 = Label(window, text="Eye color")
l7.grid(row=1, column=7)
l8 = Label(window, text="Sport")
l8.grid(row=1, column=8)
l9 = Label(window, text="Class")
l9.grid(row=1, column=9)

first_name_entry.grid(row=2, column=1, padx=5)
last_name_entry.grid(row=2, column=2, padx=5)
gender_entry.grid(row=2, column=3, padx=5)
age_entry.grid(row=2, column=4, padx=5)
weight_entry.grid(row=2, column=5, padx=5)
height_entry.grid(row=2, column=6, padx=5)
eye_color_entry.grid(row=2, column=7, padx=5)
sport_entry.grid(row=2, column=8, padx = 5)
level_entry.grid(row=2, column=9, padx=5)

# Create function to display athlete details in entry widgets
def printinfo(event):
    athlete_index = athlete_listbox.curselection()[0]
    #index of the details
    athlete = ATHLETES[athlete_index]
    first_name_entry.delete(0, END)
    first_name_entry.insert(0, athlete[0])
    last_name_entry.delete(0, END)
    last_name_entry.insert(0, athlete[1])
    gender_entry.delete(0, END)
    gender_entry.insert(0, athlete[2])
    age_entry.delete(0, END)
    age_entry.insert(0, athlete[3])
    weight_entry.delete(0, END)
    weight_entry.insert(0, athlete[4])
    height_entry.delete(0, END)
    height_entry.insert(0, athlete[5])
    eye_color_entry.delete(0, END)
    eye_color_entry.insert(0, athlete[6])
    sport_entry.delete(0, END)
    sport_entry.insert(0, athlete[7])
    level_entry.delete(0, END)
    level_entry.insert(0, athlete[8])

# Bind function to listbox
athlete_listbox.bind('<<ListboxSelect>>', printinfo)

# Create a label for the search entry
label = Label(window, text="Enter a sport to search:")
label.grid(row=3, column =3)

# Create a search entry
search_entry = Entry(window)
search_entry.grid(row=3, column=4)

# Create a listbox to display the search results
result_listbox = Listbox(window)
result_listbox.grid(row=7)

# Create a label for the search entry
l0 = Label(window, text="Search result list")
l0.grid(row=4, column=0)

sport = []
# Define the search function
def search_athletes():
    # Get the search term from the entry
    sport = search_entry.get()

    # Clear the listbox
    result_listbox.delete(0, END)


    found = False
    for athlete in ATHLETES:
        if athlete[7] == sport:
            # Add the first name of the athlete to the listbox
            result_listbox.insert(END, athlete[0])
            found = True

    if not found:
        # If no athletes were found, display "Invalid" in the listbox
        result_listbox.insert(END, "Not found the sport")


# Create a search button
button = Button(window, text="Search", command=search_athletes)
button.grid(row=4, column=4)

# Create the Quit button
quit_button = Button(window, text="Quit", command=window.destroy)
quit_button.grid(row=5, column=4)

window.mainloop()
