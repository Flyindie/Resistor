import tkinter as tk
from tkinter import ttk

def play():
    #เริ่มรับค่า
    text1 = combox1.get()
    text2 = combox2.get()
    text3 = combox3.get()
    text4 = combox4.get()
    last_text = combox5.get()

    #รับเลข3ตัวแรก
    for i in range(len(main_color)):
        if text1 == main_color[i]:
            num1 = i*100
    for i in range(len(main_color)):
        if text2 == main_color[i]:
            num2 = i*10
    for i in range(len(main_color)):
        if text3 == main_color[i]:
            num3 = i

    #รับตัวยกกำลัง
    if text4 == "ม่วง":
        upnum = ""
    elif text4 == "ทอง":
        upnum = "x10ยกกำลัง-1"
    else:
        upnum = "x10ยกกำลัง-2"
    for i in range(6):
        if text4 == minor_color[i]:
            upnum = "x10ยกกำลัง" + str(i)

    #รับโอกาศผิดพลาด
    if last_text == "เงิน":
        last = "(+-10%)"
    elif last_text == "ทอง":
        last = "(+-5%)"
    else:
        last = "(+-20%)"

    #เอามารวม
    run = num1+num2+num3
    output = str(run) + upnum + last
    outlabel.configure(text=output)

#ตัวuiทั้งหมด
window = tk.Tk()
window.title("โปรแกรมคำนวนตัวต้านทาน")
window.minsize(width=400, height=400)

label = tk.Label(master=window, text="คำนวนตัวต้านทาน", font=15)

#สีตัวต้านทาน
main_color = ["ดำ", "นํ้าตาล", "แดง", "ส้ม", "เหลือง", "เขียว", "นํ้าเงิน", "ม่วง", "เทา", "ขาว"]
minor_color = ["ดำ", "นํ้าตาล", "แดง", "ส้ม", "เหลือง", "เขียว", "นํ้าเงิน", "ม่วง", "ทอง", "เงิน"]
last_color = ["ไม่มี", "ทอง", "เงิน"]

#ที่เลือกสี
combox1 = ttk.Combobox(master=window, value=(main_color))
combox1.current(0)
combox2 = ttk.Combobox(master=window, value=(main_color))
combox2.current(0)
combox3 = ttk.Combobox(master=window, value=(main_color))
combox3.current(0)
combox4 = ttk.Combobox(master=window, value=(minor_color))
combox4.current(0)
combox5 = ttk.Combobox(master=window, value=(last_color))
combox5.current(0)

#ปุ่มกด
button = tk.Button(master=window, text="คำนวน", font=15, comman=play)
outlabel = tk.Label(master=window, font=15, text="")

#กำหนดตำแหน่งของUiทั้งหมด
label.pack(pady=5)

combox1.pack(pady=5)
combox2.pack(pady=5)
combox3.pack(pady=5)
combox4.pack(pady=5)
combox5.pack(pady=5)

button.pack(pady=5)
outlabel.pack(pady=5)

window.mainloop()
