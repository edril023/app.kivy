from kivy.app import App
from kivy.uix.slider import Slider

class MinhaApp(App):
    def build(self):
        return Slider(min=7, max=180, value=5)
    
if __name__ == '__main__':
    MinhaApp().run()