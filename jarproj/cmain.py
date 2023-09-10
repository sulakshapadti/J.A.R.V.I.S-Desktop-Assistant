from lispk import speak, takeCommand
from conv import wishme, conver
from tkinter import *
root = Tk()
root.geometry("800x800")
# root.maxsize(800, 800)
# root.minsize(800, 800)
root.title = "Jarvis"
c = PhotoImage(file="ssss.png")


def topic_to_chat():

    chat()


def submit():
    """
function for producing response of
        request of user

    """

    global chat_raw
    chat_raw = entry.get('1.0', 'end-1c')

    entry.delete('1.0', END)

    chat = chat_raw.lower()
    chat = chat.replace(' ', '')
    global label_request
    label_request = Label(frame_chats, text=chat_raw, bg="blue", fg="white",
                          justify=RIGHT, wraplength=300, font='Verdana 10 bold')

    label_request.pack(anchor='w')
    global answer
    answer = StringVar()
    answer.set(conver(chat_raw))

    get_response()


def get_response():

    global label_response
    label_response = Label(frame_chats, text=answer.get(), bg="white", fg="black",
                           justify=RIGHT, wraplength=300, font='Verdana 10 bold')

    label_response.pack(anchor='e')

    if answer == 'Bye':
        root.destroy()


# def func():
#     res1 = StringVar()
#     res1.set(conver(takeCommand()))
#     print(res1.get())
#     Label(root, text=res1.get()).pack()

#     # print(res1.set(res))
""" main chat frame"""


def chat():
    frame_welcome.pack_forget()
    frame_chat = Frame(root, bg="grey", height='670', width='550')
    frame_chat.pack_propagate(0)

    frame_top = Frame(frame_chat, bg="#9adcfe", height='100', width='550')
    frame_top.pack()

    label_topic = Label(frame_top, bg="#9adcfe", text="welcome to JARVIS", fg='black',
                        font='Verdana 20 bold ')
    label_topic.pack(pady='40')

    frame_spacer = Frame(frame_top, bg="black", height="10", width="550")
    frame_spacer.pack()
    bottom_frame = Frame(frame_chat, bg="black", height='100', width='550')
    bottom_frame.pack_propagate(0)
    bottom_frame.pack(side=BOTTOM)
    button = Button(bottom_frame, image=c, relief="flat",
                    font='Vardana 10 bold', bg="black", command=submit)
    button.place(x=410, y=27)

    def callback(self, event):
        format(event.keysym)
    global entry
    entry = Text(bottom_frame, bg="white", fg="black", height='5',
                 width='45', font='Verdana 10')
    entry.bind('<Return>', submit)
    entry.place(x=30, y=10)
    global frame_chats
    frame_chats = Frame(frame_chat, bg="grey", height='450', width='500')
    frame_chats.pack_propagate(0)
    frame_chats.pack()

    # Label(frame_chats, bg="#7B68EE").pack()

    frame_chat.pack()


# welcome frame
frame_welcome = Frame(root, bg="#7B68EE", height='670', width='550')
frame_welcome.pack_propagate(0)
frame_welcome.pack()
welcome = Label(frame_welcome, text='Welcome',
                font="Vardana 40 bold", bg="#7B68EE", fg="black")
welcome.place(x=160, y=200)

welcome_chatbot = Label(frame_welcome, text='I am JARVIS ! ',
                        font="Vardana 15 bold italic", bg="#7B68EE", fg="black")
welcome_chatbot.place(x=200, y=270)
A = PhotoImage(file='image_5.png')
b = PhotoImage(file="fw.png")
pic_1 = Label(frame_welcome, image=A)
pic_1.place(x=-2, y=357)
Button(root, image=b, bg="#7B68EE", relief="flat",
       bd="3px solid black",  command=chat).place(x=360, y=310)


# conver(takeCommand())
root.mainloop()
