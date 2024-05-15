import requests
import json
import pandas as pd
import mplfinance as mpl
from tkinter import *

def get_data_and_plot():
    symbol = entryOne.get()
    interval = entryTwo.get()
    limit = entryThree.get()

    url = f'https://www.mexc.com/open/api/v2/market/kline?interval={interval}&limit={limit}&symbol={symbol}'
    response = requests.get(url)
    responseBody = response.text
    responseBodyJson = json.loads(responseBody)

    candlesData = responseBodyJson["data"]

    formattedCandlesData = []
    for candle in candlesData:
        formattedCandle = {
            'time': candle[0],
            'open': float(candle[1]),
            'close': float(candle[2]),
            'high': float(candle[3]),
            'low': float(candle[4])
        }
        formattedCandlesData.append(formattedCandle)

    df = pd.json_normalize(formattedCandlesData)
    df.time = pd.to_datetime(df.time, unit='s')
    df = df.set_index("time")

    mpl.plot(
        df,
        type="candle",
        title="Candle chart",
        style="nightclouds",
        mav=(3, 6, 9)
    )

root = Tk()
root.title('Candlestick Chart Generator')

canvas = Canvas(root, height=800, width=600)
canvas.pack()

background_image = PhotoImage(file='altum.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#ffffff')
frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.2, anchor='n')

labelOne = Label(frame, text="Symbol:")
labelOne.grid(row=0, column=0, padx=5, pady=5)

entryOne = Entry(frame, font=40)
entryOne.grid(row=0, column=1, padx=5, pady=5)

labelTwo = Label(frame, text="Interval:")
labelTwo.grid(row=1, column=0, padx=5, pady=5)

entryTwo = Entry(frame, font=40)
entryTwo.grid(row=1, column=1, padx=5, pady=5)

labelThree = Label(frame, text="Limit:")
labelThree.grid(row=2, column=0, padx=5, pady=5)

entryThree = Entry(frame, font=40)
entryThree.grid(row=2, column=1, padx=5, pady=5)

plot_button = Button(frame, text="Plot Candlestick Chart", command=get_data_and_plot)
plot_button.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()

# # -*- coding: utf-8 -*-
# from tkinter import *
#
# root = Tk()
# root.title('MyGUIApp')
# canvas = Canvas(root, height=800, width=600)
# canvas.pack()
#
# background_image = PhotoImage(file='altum.png')
# background_label = Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)
#
# frame = Frame(root, bg='#ffffff')
# frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.1, anchor='n')
#
# labelOne = Label(frame)
# labelOne.place(relx=0.05, rely=0.15, relwidth=0.18, relheight=0.3)
#
# labelOne.configure(text="Label One")
#
# entryOne = Entry(frame, font=40)
# entryOne.place(relx=0.25, rely=0.15, relwidth=0.3, relheight=0.3)
#
# labelTwo = Label(frame)
# labelTwo.place(relx=0.05, rely=0.55, relwidth=0.18, relheight=0.3)
# labelTwo.configure(text="Label One")
#
# entryTwo = Entry(frame, font=40)
# entryTwo.place(relx=0.25, rely=0.55, relwidth=0.3, relheight=0.3)
#
# entryOne.insert(0, "Hello")
# entryTwo.insert(0, "Hi")
#
# def printTextEnteredInEntryOne():
#     print(entryOne.get())
#
# printInputButton = Button(frame, text="Print Text", command=printTextEnteredInEntryOne)
# printInputButton.place(relx=0.6, rely=0.16, relwidth=0.35, relheight=0.7)
#
# secondFrame = Frame(root, bg='#ffffff')
# secondFrame.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor='n')
#
# selectedOption = StringVar(root, 'FIRST_OPTION')
#
# def printSelectedOption():
#     print(selectedOption.get())
#
# optionOne = Radiobutton(secondFrame, text="Option One", variable=selectedOption, value='FIRST_OPTION')
# optionOne.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.3)
# optionTwo = Radiobutton(secondFrame, text="Option Two", variable=selectedOption, value='SECOND_OPTION')
# optionTwo.place(relx=0.1, rely=0.55, relwidth=0.3, relheight=0.3)
# printSelectButton = Button(secondFrame, text="Button One", command=printSelectedOption)
# printSelectButton.place(relx=0.6, rely=0.16, relwidth=0.35, relheight=0.7)
#
# root.mainloop()


