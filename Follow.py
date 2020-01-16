import requests
from bs4 import BeautifulSoup
import tkinter as tk


URL = "https://www.instagram.com/{}/"
master = tk.Tk()
master.title("---Instagram Account Analyzer ---")
master.geometry("300x100+500+500")

tk.Label(master,text ="Account Name").grid(row = 3)

e1 = tk.Entry(master)
e1.grid(row = 3,column = 1)

tk.Button(master, 
          text='Show In Terminal', 
          command=master.quit).grid(row=7, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)



def scrape(username):
	full_url = URL.format(username)
	r = requests.get(full_url)
	s = BeautifulSoup(r.text,'lxml')

	tag = s.find("meta",attrs = {"name":"description"})
	text = tag.attrs['content']
	main_text = text.split("-")[0]

	return main_text


master.mainloop()


accountname = e1.get()

USERNAME = accountname
data = scrape(USERNAME)


print(data)