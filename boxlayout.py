from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation = "horizontal", spacing = 10, padding =[20, 10])
        botao1 = Button(text = "botao 1")
        botao2 = Button(text = "botao 2")
        botao3 = Button(text = "botao 3")
        layout.add_widget(botao1)
        layout.add_widget(botao2)
        layout.add_widget(botao3)
        return layout

MyApp().run()