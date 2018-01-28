import Tkinter as tk
import win32clipboard
import win32api
import _thread
import api_calling
import webbrowser
import urllib


def start_module():
    state_left=win32api.GetAsyncKeyState(0x12)     #get the key state
    while True:
        a=win32api.GetAsyncKeyState(0x12)
        if (a != state_left):
            state_left=a
            if(a<0):
                print()

            else:
                try:
                    win32clipboard.OpenClipboard()
                    a=win32clipboard.GetClipboardData()    #taking clipborad data
                    win32clipboard.CloseClipboard()
                except: start_module()

                main=tk.Tk()              #starting Tkinter window
                main.configure(background="#8cb3d9")
                var=tk.StringVar()  #string variable

                main.overrideredirect(True)
                main.wm_attributes('-alpha',0.5)
                main.wm_attributes('-topmost',True)
                data=win32api.GetCursorPos()
                x,y=data
                main.geometry("+%d+%d"%(x-30,y+10))
                def start(event,self):                  #dragging the window
                    self.x = event.x 
                    self.y = event.y
                def motion(event,self):
                    deltax = event.x - self.x
                    deltay = event.y - self.y
                    x = self.winfo_x() + deltax
                    y = self.winfo_y() + deltay
                    self.geometry("+%s+%s" % (x, y))

                def StopMove(self, event):
                    self.x = None
                    self.y = None
                main.bind('<ButtonPress-1>',lambda event,arg=main:start(event,arg))
                main.bind('<B1-Motion>',lambda event,arg=main:motion(event,arg))
                global response
                response=[]


                def check_length(response):

                    if(len(response)>=100):                      #if length is more, than displaying in more lines
                        value=int(len(response)/100)
                        response_edit=""
                        for i in range(1,value+2):       #iterating with adding \n at every 100 characters
                            response_edit+=response[(i-1)*100:i*100]+'\n'
                        var.set(response_edit)

                    else:
                        #print(response)
                        var.set(response)


                def api_call(a):    #gets the response from the api
                    global response
                    response=api_calling.get_response(a)

                    check_length(response[0])

                # heading=tk.Canvas(width=100,height=10,background="#333333")
                # heading.pack()
                # label=tk.Label(heading,text=a)
                # label.pack(expand='true',fill='both')
                canvas=tk.Canvas(main,height=10,width=600)           #title Bar
                canvas.pack(side='left')

                def close(event):
                    main.destroy()
                #layout creationn
                btn=tk.Button(canvas,text='X',relief=tk.GROOVE,font=('Lithos Pro Regular',8),fg="#bbbbbb",width=7,anchor=tk.CENTER,background='#333333')
                btn.bind('<Button-1>',close)
                btn.pack(side='left')
                more_btn=tk.Button(canvas,text="More",relief=tk.GROOVE,font=('Lithos Pro Regular',8),width=7,fg='#bbbbbb',background="#333333")
                more_btn.pack(side='left')
                search_btn=tk.Button(canvas,text="Search",background='#333333',fg="#bbbbbb",width=7,relief=tk.GROOVE,font=('Lithos Pro Regular',8))
                search_btn.pack(side='left')
                youtube_btn=tk.Button(canvas,text="Youtube",background="#333333",fg="#bbbbbb",width=7,relief=tk.GROOVE,font=('Lithos Pro Regular',8))
                youtube_btn.pack(side='left')

                label=tk.Label(main,textvariable=var,bd=0,highlightthickness="4",highlightbackground="#333333",background="#c6d9ec",fg="#333300",width=80,font=('calibri',10))
                label.pack(side='left')
                global flag
                flag=0
                def more(event):
                    global response,flag
                    #print(flag)
                    if(flag<4):
                        flag+=1
                        check_length(response[flag])
                def browsing(event):
                    webbrowser.open('https://www.google.co.in/search?dcr=0&source=hp&ei=pulsWuDXF4OSvQTtza64CA&q='+urllib.quote(a)+'+&oq='+urllib.quote(a)+'+&gs_l=psy-ab.3..0l10.5783.9141.0.9586.25.14.4.2.2.0.307.2266.0j1j7j1.9.0....0...1c.1.64.psy-ab..10.15.2286.0..0i67k1j0i131k1.0.teo2iQHj36g')
                    close(event)
                def youtube(event):
                    webbrowser.open('https://www.youtube.com/results?search_query='+urllib.quote(a))
                    close(event)


                more_btn.bind("<Button-1>",lambda event:more(event))   #bindings for all the buttons
                search_btn.bind('<Button-1>',browsing)
                youtube_btn.bind("<Button-1>",youtube)
                _thread.start_new_thread(api_call,(a,))




                def opaque(event):
                    main.wm_attributes('-alpha',1)

                def tspnt(event):
                    main.wm_attributes('-alpha',0.5)
                main.bind("<Enter>",opaque)
                main.bind("<Leave>",tspnt)
                main.mainloop()


try:
    start_module()

except:
    start_module()
