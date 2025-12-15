import wx
import csv
import tkinter as tk
from tkinter import messagebox
from sklearn.tree import DecisionTreeClassifier

def on_button1(event):
    wx.MessageBox("BMI CALCULATOR SELECTED ✅", "Info")    
    global height_input, weight_input       

    app = wx.App(False)
    frame = wx.Frame(None, title="BMI CALCULATOR", size=(1200, 800))
    panel = wx.Panel(frame)
    panel.SetBackgroundColour("#F8C2AF")

    # HEADING
    heading = wx.StaticText(panel, label="BMI CALCULATOR", pos=(450, 60))
    heading.SetFont(wx.Font(36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    heading.SetForegroundColour("#C0392B")

    # SUBHEADING
    sub_heading = wx.StaticText(panel, label="Body Mass Index", pos=(450, 120))
    sub_heading.SetFont(wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    sub_heading.SetForegroundColour("#922B21")

    #BMI IMAGE
    bmi_img = wx.Image("bmi2.png")      
    bmi_img = bmi_img.Scale(350, 170)
    bmi_bmp = wx.Bitmap(bmi_img)

    bmi_icon = wx.StaticBitmap(panel, bitmap=bmi_bmp, pos=(40, 20))


    # BMI DESCRIPTION
    text = (
        "Body Mass Index (BMI) is a popular metric to help you track your health based on body fat constituency.\n"
        "You can use this BMI calculator to know your health status.\n\n"
        "In today's world of changing lifestyles, stress and unhealthy eating habits, it is highly important to "
        "keep track of your health.\n"
        "By keeping track of your weight, you can take timely measures to reduce the chances of obesity-related health issues."
    )

    paragraph = wx.StaticText(panel, label=text, pos=(40, 200))
    paragraph.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    #panel 2
    # SHADOW PANEL
    shadow = wx.Panel(panel, pos=(40, 360), size=(460, 260))
    shadow.SetBackgroundColour("#FFF9DB")

    # FORM PANEL
    form_panel = wx.Panel(panel, pos=(30, 350), size=(450, 250))
    form_panel.SetBackgroundColour("#FCE5B2")
    form_panel.Raise()

    # GENDER LABEL
    gender = wx.StaticText(form_panel, label="Gender:", pos=(20, 20))
    gender.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

    btn_male = wx.RadioButton(form_panel, label="Male", pos=(120, 20))
    btn_female = wx.RadioButton(form_panel, label="Female", pos=(200, 20))

    # HEIGHT
    height_label = wx.StaticText(form_panel, label="Height (cm):", pos=(20, 70))
    height_label.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

    height_input = wx.TextCtrl(form_panel, pos=(150, 70), size=(120, 25))

    # WEIGHT
    weight_label = wx.StaticText(form_panel, label="Weight (kg):", pos=(20, 120))
    weight_label.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

    weight_input = wx.TextCtrl(form_panel, pos=(150, 120), size=(120, 25))

    #CALCULATE BMI
    def calculate_BMI(event):
        
        height=float(height_input.GetValue())
        weight=float(weight_input.GetValue())
        bmi=((weight*10000)/(height)**2)
        if bmi>0:
            if (bmi<18.5):
                message="you are underweight!"
            elif (bmi<=24.9):
                message="you are normal weight!"
            elif (bmi<=29.9):
                message="you are overweight!"
            elif (bmi<=34.9):
                message="you are obese!"
            elif (bmi<=39.9):
                message="you are severely obese!"
            elif (bmi>=40):
                message="you are morbidly obese!"
        else:
            message="Please enter valid inputs"
        wx.MessageBox(f"YOUR BMI IS {bmi:.1f} \n {message}")


    #BMI BUTTON
    btn = wx.Button(form_panel, label="Calculate your BMI", pos=(20, 180), size=(150, 35))
    btn.Bind(wx.EVT_BUTTON, calculate_BMI)

    frame.Show()
    app.MainLoop()


def on_button2(event):
    wx.MessageBox("SYMPTOMS CHECKER SELECTED ✅", "Info")
    X = []
    y = []

    f=open("dataset_8symptoms_final.csv", "r")
    reader = csv.reader(f)
    next(reader)
    for row in reader:
            y.append(row[0])
            X.append([int(row[1]), int(row[2]), int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7]),int(row[8])])

    model = DecisionTreeClassifier()
    model.fit(X, y)

    # RESULT WINDOW

    def show_result_window(result):
        frame1 = wx.Frame(None, title="Prediction", size=(400,200))
        p = wx.Panel(frame1)
        p.SetBackgroundColour("light blue")

        lbl = wx.StaticText(p,label=f"Predicted Disease:\n{result}", pos=(100,40))
        lbl.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        ok = wx.Button(p,label="OK", pos=(160,120))
        ok.Bind(wx.EVT_BUTTON,lambda x:frame1.Close())

        frame1.Centre()
        frame1.Show()

    # -------------------------
    # MAIN WINDOW
    # -------------------------
    app = wx.App()
    frame = wx.Frame(None, title="Disease Predictor", size=(1600,880))

    # --- Load background image ---
    bg = wx.Image("bg.png", wx.BITMAP_TYPE_ANY)
    bg = bg.Scale(1600,800,wx.IMAGE_QUALITY_HIGH)
    bg_bitmap = wx.Bitmap(bg)

    # --- Paint background ---
    def paint_background(event):
        dc = wx.PaintDC(frame)
        dc.DrawBitmap(bg_bitmap,0,0)

    frame.Bind(wx.EVT_PAINT, paint_background)

    # -------------------------
    # WIDGETS DIRECTLY ON FRAME
    # -------------------------

    title = wx.StaticText(frame, label="Disease Prediction System", pos=(550,20))
    title.SetFont(wx.Font(28, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    title.SetForegroundColour("black")

    subtitle = wx.StaticText(frame, label="Select your Symptoms:", pos=(600, 160))
    subtitle.SetFont(wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
    subtitle.SetForegroundColour("black")

    # Checkboxes
    cb1 = wx.CheckBox(frame, label="Fever", pos=(600,220),size=(200,20))
    cb2 = wx.CheckBox(frame, label="Body Pain", pos=(600,260),size=(200,20))
    cb3 = wx.CheckBox(frame, label="Vomiting", pos=(600,300),size=(200,20))
    cb4 = wx.CheckBox(frame, label="Cough", pos=(600,340),size=(200,20))
    cb5 = wx.CheckBox(frame, label="Cold", pos=(600,380),size=(200,20))
    cb6 = wx.CheckBox(frame, label="Headache", pos=(600,420),size=(200,20))
    cb7 = wx.CheckBox(frame, label="Fatigue", pos=(600,460),size=(200,20))
    cb8 = wx.CheckBox(frame, label="Diarrhea", pos=(600,500),size=(200,20))

    for cb in (cb1, cb2, cb3, cb4, cb5, cb6, cb7, cb8):
        cb.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        cb.SetForegroundColour("black")

    # Predict button
    def on_predict(event):
        s1 = 1 if cb1.GetValue() else 0
        s2 = 1 if cb2.GetValue() else 0
        s3 = 1 if cb3.GetValue() else 0
        s4 = 1 if cb4.GetValue() else 0
        s5 = 1 if cb5.GetValue() else 0
        s6 = 1 if cb6.GetValue() else 0
        s7 = 1 if cb7.GetValue() else 0
        s8 = 1 if cb8.GetValue() else 0
        prediction = model.predict([[s1, s2, s3, s4, s5, s6, s7, s8]])[0]
        show_result_window(prediction)

    btn = wx.Button(frame, label="Predict Disease", size=(220,50), pos=(650,550))
    btn.SetFont(wx.Font(20,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL))
    btn.SetBackgroundColour("#2e7d32")
    btn.SetForegroundColour("black")
    btn.Bind(wx.EVT_BUTTON, on_predict)

    # --- SHOW EVERYTHING ---
    frame.Show()
    app.MainLoop()

def on_button3(event):
    wx.MessageBox("CALORIE COUNTER SELECTED ✅", "Info")
    # ------------------ LOAD CSV ------------------
    foodlisted = []

    with open('foodp.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            foodlisted.append(row)

    # ------------------ GLOBAL TOTALS ------------------
    kcal = []
    protein = []
    fats = []

    # ------------------ APP & FRAME ------------------
    app = wx.App()
    frame = wx.Frame(None, title="Calorie Counter", size=(700, 700))
    panel = wx.Panel(frame)
    panel.SetBackgroundColour("white")

    # ------------------ TITLE ------------------
    title = wx.StaticText(panel, label="Calorie Counter", pos=(220, 20))
    title.SetFont(wx.Font(22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

    # ------------------ SEARCH ------------------
    wx.StaticText(panel, label="Search:", pos=(50, 80))
    entry_search = wx.TextCtrl(panel, pos=(120, 75), size=(250, 25))
    listbox_search = wx.ListBox(panel, pos=(120, 110), size=(300, 100))

    def search_food(event):
        term = entry_search.GetValue().lower()
        listbox_search.Clear()

        for row in foodlisted:
            if term in row[0].lower():
                listbox_search.Append(row[0])

        if listbox_search.GetCount() == 0:
            listbox_search.Append("No match found")

    btn_search = wx.Button(panel, label="Search", pos=(400, 75))
    btn_search.Bind(wx.EVT_BUTTON, search_food)

    # ------------------ ADD INGREDIENT ------------------
    wx.StaticText(panel, label="Ingredient:", pos=(50, 240))
    entry_ingredient = wx.TextCtrl(panel, pos=(150, 235), size=(200, 25))

    wx.StaticText(panel, label="Grams:", pos=(50, 280))
    entry_grams = wx.TextCtrl(panel, pos=(150, 275), size=(200, 25))

    listbox_added = wx.ListBox(panel, pos=(50, 350), size=(580, 200))

    def update_totals():
        label_kcal.SetLabel(f"Total Calories: {sum(kcal):.2f}")
        label_protein.SetLabel(f"Total Protein: {sum(protein):.2f} g")
        label_fats.SetLabel(f"Total Fats: {sum(fats):.2f} g")

    def add_ingredient(event):
        a = entry_ingredient.GetValue().lower()
        grams = entry_grams.GetValue()

        if a == "" or grams == "":
            wx.MessageBox("Enter ingredient and grams", "Error")
            return

        try:
            grams = float(grams)
        except:
            wx.MessageBox("Grams must be a number", "Error")
            return

        found = False

        for i in range(1, len(foodlisted)):
            if foodlisted[i][0].lower() == a:
                found = True

                kc = (float(foodlisted[i][1]) / 100) * grams
                pr = (float(foodlisted[i][2]) / 100) * grams
                ft = (float(foodlisted[i][3]) / 100) * grams

                kcal.append(kc)
                protein.append(pr)
                fats.append(ft)

                listbox_added.Append(
                    f"{a} ({grams}g) → {kc:.2f} kcal, {pr:.2f}g protein, {ft:.2f}g fats"
                )

        if not found:
            wx.MessageBox("Food item not found", "Error")

        update_totals()
        entry_ingredient.Clear()
        entry_grams.Clear()

    btn_add = wx.Button(panel, label="Add Ingredient", pos=(150, 315))
    btn_add.Bind(wx.EVT_BUTTON, add_ingredient)

    # ------------------ TOTAL LABELS ------------------
    label_kcal = wx.StaticText(panel, label="Total Calories: 0", pos=(50, 570))
    label_protein = wx.StaticText(panel, label="Total Protein: 0 g", pos=(50, 600))
    label_fats = wx.StaticText(panel, label="Total Fats: 0 g", pos=(50, 630))

    label_kcal.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    label_protein.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    label_fats.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

    # ------------------ SHOW ------------------
    frame.Centre()
    frame.Show()
    app.MainLoop()



def on_exit(event):
    frame.Close()

# Create application
app = wx.App()

# Create main window
frame = wx.Frame(None, title="HEALTH ASSISTANT", size=(400, 350))
panel = wx.Panel(frame)
panel.SetBackgroundColour("#D5D1E9")

# Create buttons
btn1 = wx.Button(panel, label="bmi calculator", size=(200, 40))
btn1.SetBackgroundColour("#D0E4EE")
btn2 = wx.Button(panel, label="symptom checker", size=(200, 40))
btn2.SetBackgroundColour("#F3F5A9")
btn3 = wx.Button(panel, label="calorie counter", size=(200, 40))
btn3.SetBackgroundColour("#F5CF9F")
btn4 = wx.Button(panel, label="Exit", size=(200, 40))
btn4.SetBackgroundColour("#F5A7A6")

# Bind events
btn1.Bind(wx.EVT_BUTTON, on_button1)
btn2.Bind(wx.EVT_BUTTON, on_button2)
btn3.Bind(wx.EVT_BUTTON, on_button3)
btn4.Bind(wx.EVT_BUTTON, on_exit)

# Layout
vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(btn1, 0, wx.ALL | wx.CENTER, 10)
vbox.Add(btn2, 0, wx.ALL | wx.CENTER, 10)
vbox.Add(btn3, 0, wx.ALL | wx.CENTER, 10)
vbox.Add(btn4, 0, wx.ALL | wx.CENTER, 10)

panel.SetSizer(vbox)

frame.Centre()
frame.Show()

app.MainLoop()


