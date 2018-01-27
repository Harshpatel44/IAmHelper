import Tkinter as tk
import win32clipboard
import win32api
import requests
import _thread
import api_calling
import time

state_left=win32api.GetAsyncKeyState(0x12)
while True:
    a=win32api.GetAsyncKeyState(0x12)
    if (a != state_left):
        state_left=a
        if(a<0):
            print()

        else:
            win32clipboard.OpenClipboard()
            a=win32clipboard.GetClipboardData()    #taking clipborad data
            win32clipboard.CloseClipboard()

            main=tk.Tk()              #starting Tkinter window
            var=tk.StringVar()        #string variable
            main.overrideredirect(True)
            main.wm_attributes('-alpha',0.5)
            main.wm_attributes('-topmost',True)
            data=win32api.GetCursorPos()
            x,y=data

            main.geometry("+%d+%d"%(x-30,y+10))
            def api_call(a,cursor_btn):
                response=api_calling.get_response(a)
                if(len(response)>=100):                      #if length is more than displaying in more lines
                    value=int(len(response)/100)
                    response_edit=""
                    for i in range(1,value+2):       #iterating with adding \n at every 100 characters
                        response_edit+=response[(i-1)*100:i*100]+'\n'
                    var.set(response_edit)
                    #response=response[0:100]+"\n"+response[101:]

                #     current=response[0:100]
                #     var.set(current)
                #     def scroll(event,count=0):
                #         count+=1
                #         var.set(response[count:100+count])
                #     cursor_btn.bind("<Button-1>",scroll)
                else:
                    var.set(response)

            # def start(event,main):
            #     main.x=event.x
            #     main.y=event.y
            # def motion(event,main):
            #     widget=event.widget
            #     delta_x=event.x-main.x
            #     delta_y=event.y-main.y
            #     x=widget.winfo_x()+delta_x
            #     y=widget.winfo_y()+delta_y
            #     main.geometry("+%s+%s"%(x,y))

            # canvas=tk.Canvas(main,height=10,width=600)           #title Bar
            # canvas.pack()
            #canvas.bind('<ButtonPress-1>',lambda event,arg=main:start(event,arg))
            #canvas.bind('<B1-Motion>',lambda event,arg=main:motion(event,arg))
            def close(event):
                main.destroy()

            btn=tk.Button(main,text='X',highlightthickness="4",highlightbackground="#333333",relief=tk.SOLID,font=('Lithos Pro Regular',8),width=5,anchor=tk.CENTER,background='#555555')
            btn.bind('<Button-1>',close)
            btn.pack(side='left')
            cursor_btn=tk.Button(text=">")
            cursor_btn.pack(side='left')
            def scroll(event,count=0):

                    count+=1
                    string=var.get()
                    var.set(string[count:100+count])

            cursor_btn.bind("<ButtonPress>",scroll)
            label=tk.Label(main,textvariable=var,background="#c6d9ec",fg="#333300",width=80,font=('calibri',10))
            label.pack(side='left')
            _thread.start_new_thread(api_call,(a,cursor_btn,))
            def opaque(event):
                main.wm_attributes('-alpha',1)
            def tspnt(event):
                main.wm_attributes('-alpha',0.5)
            main.bind("<Enter>",opaque)
            main.bind("<Leave>",tspnt)
            main.mainloop()




