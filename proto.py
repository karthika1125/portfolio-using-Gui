import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Function to update content based on the selected section
def show_section(section):
    for widget in content_frame.winfo_children():
        widget.destroy()

    if section == "About Me":
        tk.Label(content_frame, text="Modeling Portfolio", 
        font=("Algerian", 20)).place(x=850,y=100)
        tk.Label(content_frame, text="I am Sara David, a passionate and driven model from Los Angeles.", 
        font=("Arial ", 12)).place(x=650,y=200)
        tk.Label(content_frame, text="Growing up in a humble environment, I’ve always believed that challenges shape character.", 
        font=("Arial ",12)).place(x=650,y=230)
        tk.Label(content_frame, text="My journey into the modeling industry has been fueled by resilience, creativity, and a commitment ", 
        font=("Arial", 12)).place(x=650,y=260)
        tk.Label(content_frame, text="to showcasing beauty in all its forms.rom grassroots fashion shows to bold photoshoots,I bring authenticity and ", 
        font=("Arial", 12)).place(x=650,y=290)
        tk.Label(content_frame, text="energy to every project. My goal is to collaborate with brands and creators who value diversity and individuality.", 
        font=("Arial", 12)).place(x=650,y=320)

        

    elif section == "Projects":
        tk.Label(content_frame, text="My Projects", font=("Baskerville Old Face", 30)).place(x=900,y=50)
        tk.Label(content_frame, text="Runway Debut- LA Local Fashion Week (2020)",font=("Baskerville Old Face",18)).place(x=700,y=150)
        
        tk.Label(content_frame, text="Editorial Feature – Urban Vogue  (2021)",font=("Baskerville Old Face",18)).place(x=700,y=180)
        
        tk.Label(content_frame, text="Campaign – “Dare to Dream” by EverGlow Cosmetics  (2022)",font=("Baskerville Old Face",18)).place(x=700,y=210)

        tk.Label(content_frame, text="Photoshoot – “Desert Elegance” (2023)",font=("Baskerville Old Face",18)).place(x=700,y=250)
        
        tk.Label(content_frame, text="Commercial – [Gucci] Activewear (2024)",font=("Baskerville Old Face",18)).place(x=700,y=280)
        
    
    elif section == "Contact":
        tk.Label(content_frame, text="Contact Me", font=("Arial Rounded MT Bold", 30)).place(x=700,y=50)
        tk.Label(content_frame, text="Email: saradavid@gmail.com.com\nPhone: +1234567890 \nAddress :1234 Model Lane,\n Apt 56Los Angeles,\n CA 90001United States", font=("Arial Rounded MT Bold",18)).place(x=700,y=150)
               
    elif section == "Home":
        tk.Label(content_frame, text="Etherea", font=("Imprint MT Shadow", 50)).place(x=800,y=100)
        tk.Label(content_frame, text="Visions", font=("Imprint MT Shadow",50)).place(x=900,y=200)
        tk.Label(content_frame, text="Studio", font=("Imprint MT Shadow", 50)).place(x=1000,y=300)
        tk.Label(content_frame, text="The journey is as beautiful as the destination—walk your runway with pride.",font=("Brush Script MT",20)).place(x=700,y=500)
        
  

# Main application window
root = tk.Tk()
root.title("Protofoil")
root.geometry("2000x2000")

# Title Frame
title_frame = tk.Frame(root, bg="black", height=80)
title_frame.pack(fill="x")

tk.Label(title_frame, text="Sara David",  fg="white",bg="black", font=("Harlow Solid Italic", 14)).place(x=10,y=15)


# Navigation Frame
# nav_frame = tk.Frame(root, height=50)
# nav_frame.pack(fill="x")

for section in ["About Me"]:
    btn1 = ttk.Button(title_frame, text=section, command=lambda s=section: show_section(s))
    btn1.place(x=1100,y=50,)

for section in [ "Projects"]:
    btn2 = ttk.Button(title_frame, text=section, command=lambda s=section: show_section(s))
    btn2.place(x=1200,y=50,)
for section in [ "Contact"]:
    btn3 = ttk.Button(title_frame, text=section, command=lambda s=section: show_section(s))
    btn3.place(x=1300,y=50,)
for section in [ "Home"]:
    btn4 = ttk.Button(title_frame, text=section, command=lambda s=section: show_section(s))
    btn4.place(x=1400,y=50,)    

# Content Frame
content_frame = tk.Frame(root, padx=20, pady=20)
content_frame.pack(fill="both", expand=True)
path = Image.open("C:/Users/HP/OneDrive/Desktop/python1/model.png")
image = path.resize((600,750))  
photo = ImageTk.PhotoImage(image)



label_image = tk.Label(root, image=photo)
label_image.place(x=0,y=80)
label_image.image = photo


# Show the default section
show_section("Home")

# Run the application
root.mainloop()
