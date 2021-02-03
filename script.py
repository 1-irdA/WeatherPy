import tkinter as tk
from tkinter import messagebox
import requests

HEIGHT = 480
WIDTH = 600

# Get weather from Open weather map with requests module
def get_weather(location):
    api_key = '101fdd7570f19a3a046ed848bd0311ad'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': api_key, 'q': location.title(), 'units': 'metric',
              'lang': 'fr'}
    response = requests.get(url, params=params)

    if (response.status_code == 200):
        weather = response.json()
        label['text'] = format_reponse(weather)
    else:
    	tk.messagebox.showerror(title="Unavailable weather", message="Error during weather access")

# Format the weather response
def format_reponse(weather):
    location = weather['name']
    country = weather['sys']['country']
    description = weather['weather'][0]['description']
    temp = weather['main']['temp']
    min_temp = weather['main']['temp_min']
    max_temp = weather['main']['temp_max']

    desc = description[0].upper() + description[1:]

    return '{} ({})\n{} °C\n'\
    '{}\n'\
    'Température maximale : {} °C\n'.format(location,country,temp,desc,max_temp)

# Design application

root = tk.Tk()
root.title('Today\'s weather')
root.iconbitmap('sun_16.ico')
root.resizable(False,False)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Search", font=40,
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=40)
label.place(relwidth=1, relheight=1)

root.mainloop()