from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MyApp(App):
    def build(self):
        return  AsyncImage(source="https://aventurasnahistoria.uol.com.br/media/_versions/curiosidades/blade_runner_capa_widelg.jpg")

if __name__ == "__main__":
    MyApp().run()