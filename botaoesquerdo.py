from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

def BotaoP(instance):
    print("Botão pressionado")

class MyApp(App):
    def build(self):
        btn =Button(text='clique aqui', background_color = get_color_from_hex("#FF007F"), size_hint = (0.5,0.2))
        btn.bind(on_press=BotaoP)
        return btn
    
    
    
    
if __name__ =="__main__":
    MyApp().run()