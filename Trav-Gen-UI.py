from TravelerGenerator import *
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image as ImagePIL
import configparser
from datetime import date as todayDate

def select_input_file():
    global inputFile
    initial_dir = os.getcwd() 
    inputFile = filedialog.askopenfilename(initialdir=initial_dir, title="Select Input File", filetypes=(("Excel Files", "*.xlsx*"), ("all files","*.*")))
    label_gen.configure(text=f"{inputFile} Selected", wraplength=250)

def select_folder_structure():
    global folderStructure
    initial_dir = os.getcwd() 
    folderStructure = filedialog.askopenfilename(initialdir=initial_dir, title="Select JSON File", filetypes=(("JSON Files", "*.json*"), ("all files","*.*")))
    label_gen.configure(text=f"{folderStructure} Selected", wraplength=250)

def genTravellers():
    if inputFile != "" and month.get() != "Select Month" and year.get() != "Select Year" and batch.get() != "" and batch.get() != "Enter Batch":
        global date
        global time
        time = todayDate.today()
        date = year.get()[2:] + month.get()
        try:
            candidates = getInput(inputFile)
        except ValueError as e:
            label_gen.configure(text=e, wraplength=200)
            return
        prefix = candidates[0].uniqueId[:3]
        if read_existing_folders(target, prefix, batch.get()):
            print("Generating Folders")
            with open(folderStructure, 'r') as json_file:
                data = json.load(json_file)
            create_folders(data["structure"], target, batch.get(), prefix, candidates, date)
            label_gen.configure(text="Travellers generated successfully!", wraplength=300)
            print("Completed Tasks")
        else:
            label_gen.configure(text="Travellers could not be generated, batch already exists for these IDs.", wraplength=250)


    else:
        print("Not all files selected.")
        label_gen.configure(text="Please input all required values!", wraplength=300)

config = configparser.ConfigParser()
config.read('TravellerGen/config.ini')

global target
target = config['DEFAULT']['outputPath']
print(f"Loaded Config, Output path set to {target}")

if target == "":
    cwd = os.getcwd()
    target = os.path.join(cwd, "output")


window = Tk()

window.title('Traveller Generator')
window.config(background = "white")
instructions = "This is the Traveller Generator.\n\nIt takes in potential candidate alloy information and will automatically populate traveller templates for TAMU and UCSD with the appropriate information.\n\nPlease select the input candidate alloy data, the month / year, and the batch.\nInput file must be in .xlsx format."

month = StringVar(window)
month.set("Month")
year = StringVar(window)
year.set("Year")
batch = StringVar(window)
batch.set("Batch")

# INPUT TEXT
label_input = Label(window, text=instructions,
                            width = 35, height = 10, fg = "black", background = "white", wraplength= 300, font=("Arial", 12))
label_input.grid(column = 1, row = 1, padx = 4, rowspan=4)

# OUTPUT WINDOW
label_gen = Label(window, text="Output Window",
                            width = 35, height = 4, fg = "black", relief = "sunken")
label_gen.grid(column = 1, row = 5, padx = 4, pady = 10)

# DATE DROPDOWNS
month_dropdown = OptionMenu(window, month, "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
month_dropdown.grid(column = 2, row = 4)
year_dropdown = OptionMenu(window, year, "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030")
year_dropdown.grid(column = 3, row = 4)

# LOGO
logo = ImageTk.PhotoImage(ImagePIL.open("TravellerGen/AM_Research_Logo.png"))
label_image = Label(window, image=logo, background = "white")
label_image.grid(column = 1, row = 0, padx = 4, pady = 10, columnspan = 3)

# FILE INPUT
button_bI = Button(window, text = "Select Input File", command = select_input_file, width= 30, height = 4, wraplength=300)
button_bI.grid(column = 2, row = 1, padx = 4, columnspan=2, pady=1)

# BATCH INPUT
entry = OptionMenu(window, batch, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X" "Y", "Z")
entry.grid(column = 2, row = 3, columnspan=2, pady=1)

# FOLDER STRUCTURE
button_select_structure = Button(window, text="Select Folder JSON", command = select_folder_structure, width = 30, height = 2)
button_select_structure.grid(column = 2, row = 2, padx=4, columnspan=2, pady=1)
# GENERATE BUTTON
button_gen = Button(window, text= "Generate Travellers", command = genTravellers, width = 30, height = 4)
button_gen.grid(column = 2, row = 5, padx = 4, columnspan=2, pady=1)

window.mainloop()