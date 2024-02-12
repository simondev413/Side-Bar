import customtkinter as ct
from PIL import Image,ImageTk

root =  ct.CTk()
class UI:
    
    def __init__(self):
        self.app = root
        self.config()
        self.sidebar()
        self.app.mainloop()

    def config(self)  :
        self.app.geometry('1020x860')
        self.app.title('Python with Simon Dev')
    
    def sidebar(self):
        side_width = 160
        min_side_width = 60
        side_height = 600

        side_image = Image.open('simbolo-de-setas-duplas-para-a-direita-para-avancar.png')
        close_icon = side_image.resize((12,12))
    
        close_icon = ImageTk.PhotoImage(close_icon)

        side_image = Image.open('menu-hamburguer.png')
        menu_icon = side_image.resize((20,20))
        menu_icon = ImageTk.PhotoImage(menu_icon)

        self.bar = ct.CTkFrame(
            self.app,
            height= side_height,
            width= min_side_width,
            fg_color='#343434')
        self.bar.place(x=10,y=70)

        def move():
            if self.bar['width'] > min_side_width:
                self.bar.configure(width= min_side_width)
                self.move_btn.configure(image=menu_icon,compound='center')
                self.move_btn.place(x=20,y=75)
                self.home_btn.configure(text='',width=0)
                self.user_btn.configure(text='',width=0)
                self.chart_btn.configure(text='',width=0)
                self.config.configure(text='',width=0)
            else:
                self.bar.configure(width = side_width)
                self.move_btn.configure(image = close_icon)
                self.move_btn.place(x=130,y=75)
                self.home_btn.configure(
                    text='Home',
                    font = ('Lucida-sans',15,'bold'),
                )
                self.user_btn.configure(
                    text='User',
                    font = ('Lucida-sans',15,'bold'),
          
                )
                self.chart_btn.configure(
                    text='Charts',
                    font = ('Lucida-sans',15,'bold'),
                   
                )
                self.config.configure(
                    text='Manage',
                    font = ('Lucida-sans',15,'bold'),
                
                )
        
        
        self.move_btn = ct.CTkButton(
            self.app,
            image= menu_icon ,
            text='',
            width=0,
            fg_color= '#343434',
            bg_color='#343434',
            hover=False,
            command= move
        )
        self.move_btn.place(x=20,y=75)


        home_ico = Image.open('8666691_home_icon -white.png').resize((26,26))
        home_ico = ImageTk.PhotoImage(home_ico)

        self.home_btn = ct.CTkButton(
            self.app,
            text='',
            image=home_ico,
            width=0,
            hover=False,
            fg_color='#343434',
            bg_color='#343434'

        )
        self.home_btn.place(x=15,y=150)

        user_ico = Image.open('do-utilizador.png').resize((26,26))
        user_ico = ImageTk.PhotoImage(user_ico)
    
        self.user_btn = ct.CTkButton(
            self.app,
            text='',
            image= user_ico,
            width=0,
            hover=False,
            fg_color='#343434',
            bg_color='#343434'
        )
        self.user_btn.place(x=15,y= 230)

        chart_ico = Image.open('line-chart.png').resize((26,26))
        chart_ico = ImageTk.PhotoImage(chart_ico)

        self.chart_btn = ct.CTkButton(
        self.app,
        text='',
        image= chart_ico,
        width=0,
        hover=False,
        bg_color='#343434',
        fg_color='#343434')
        self.chart_btn.place(x=15,y=310)

        config_ico =Image.open('engrenagem.png').resize((26,26))
        config_ico = ImageTk.PhotoImage(config_ico)

        self.config = ct.CTkButton(
            self.app,
            width=0,
            image=config_ico,
            text='',
            hover=False,
            fg_color='#343434',
            bg_color='#343434')
        self.config.place(x=15,y=600)
UI()