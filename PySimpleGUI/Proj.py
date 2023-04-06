import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd

# Define the color scheme of the program
color_scheme = {
    'background': '#0B2447',
    'text': '#FFFFFF',
    'button': ('#FFFFFF', '#000000')
}

# Read the CSV files
df_stats = pd.read_csv('pokemon_stats.csv')
df_weight = pd.read_csv('pokemon_statsWeight.csv')
df_rarity = pd.read_csv('pokemon_statsRarity.csv')

# Define the layout of the window
button_text = ['Damage', 'Weight', 'Rarity']
layout = [
    [sg.Column([[sg.Text('All Pokemon Stats', background_color=color_scheme['background'], text_color=color_scheme['text'], font=('Helvetica', 20))]], 
               justification='center', pad=(0, 20))],
    [sg.Column([[sg.Button(button_text[0], size=(12, 2), button_color=color_scheme['button'], pad=(10, 10)), 
                 sg.Button(button_text[1], size=(12, 2), button_color=color_scheme['button'], pad=(10, 10))]], 
               justification='center', pad=(0, 10))],
    [sg.Column([[sg.Button(button_text[2], size=(12, 2), button_color=color_scheme['button'], pad=(10, 10))]], 
               justification='center', pad=(0, 20))]
]

# Create the window and display it
sg.theme_background_color(color_scheme['background'])
sg.theme_text_color(color_scheme['text'])
window = sg.Window('Pokemon Stats', layout, size=(350, 300), titlebar_font=('Helvetica', 14))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == button_text[0]:
        # Create a scatter chart using matplotlib
        x = df_stats['Attack']
        y = df_stats['Name']
        plt.scatter(x, y)
        plt.title('Pokemon Damage')
        plt.xlabel('Damage')
        plt.ylabel('Top 50 Pokemon')
        plt.show()
    elif event == button_text[1]:
        # Create a scatter chart using matplotlib
        x = df_weight['Weight_kg']
        y = df_weight['Name']
        plt.scatter(x, y)
        plt.title('Pokemon Weight')
        plt.xlabel('Weight (kg)')
        plt.ylabel('Top 50 Pokemon')
        plt.show()
    elif event == button_text[2]:
        # Create a bar chart using matplotlib
        x = df_rarity['Name']
        y = df_rarity['Rarity']
        plt.bar(y, x)
        plt.title('Pokemon Rarity')
        plt.xlabel('Pokemon')
        plt.ylabel('Rarity')
        plt.xticks(rotation=90)
        plt.show()

window.close()