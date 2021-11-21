from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDFillRoundFlatIconButton



Window.size = (320, 600)


#Define our different screens
class MainWindow(Screen):
    pass

class UsheringWindow(Screen):
    pass

class EvangelismWindow(Screen):
    pass

class PraiseWorshipWindow(Screen):
    pass

class DecorWindow(Screen):
    pass

class MediaWindow(Screen):
    pass

class SoundWindow(Screen):
    pass

class SanctuaryKeepingWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass






class MainApp(MDApp):
    def build(self):
        
        
        self.theme_cls.theme_style = 'Dark'
        kv = Builder.load_file('main.kv')
        
        return kv 


MainApp().run()