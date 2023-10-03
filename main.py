from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


class Customer(FloatLayout):
    pass

class Interface(App):
    def build(self):
        Builder.load_file("interface.kv")
        return Customer()

if __name__ =="__main__":
    Interface().run()