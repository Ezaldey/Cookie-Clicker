from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '700')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget

BG_COLOR = (0.8235, 0.4118, 0.1176, 1)  # #D2691E

# ---------------------------------------------------------------------------
# SAVE SYSTEM (unchanged from the Tkinter version)
# ---------------------------------------------------------------------------

f = open("variables/cookies.var")
cookies = int(f.read())
f.close()

# CookieClicks
f = open("variables/CookieClick.var")
CookieClick = int(f.read())
f.close()

f = open("variables/CookieClick_Price.var")
CookieClick_Price = int(f.read())
f.close()

f = open("variables/CookieClickLVL2_Price.var")
CookieClickLVL2_Price = int(f.read())
f.close()

f = open("variables/CookieClickLVL3_Price.var")
CookieClickLVL3_Price = int(f.read())
f.close()

f = open("variables/CookieClickLVL4_Price.var")
CookieClickLVL4_Price = int(f.read())
f.close()

f = open("variables/CookieClickLVL5_Price.var")
CookieClickLVL5_Price = int(f.read())
f.close()


def UpdateCookies():
    global cookies, f

    Cookies_text.text = f"Cookies: {cookies}"
    f = open("variables/cookies.var", "w")
    f.write(str(cookies))
    f.close()

    CookieClick_text.text = f"CookieClicks: {CookieClick}"
    f = open("variables/cookieclick.var", "w")
    f.write(str(CookieClick))
    f.close()

    CookieClick_Price_text.text = f"Price: {CookieClick_Price}"
    f = open("variables/CookieClick_Price.var", "w")
    f.write(str(CookieClick_Price))
    f.close()

    CookieClickLVL2_Price_text.text = f"Price: {CookieClickLVL2_Price}"
    f = open("variables/CookieClickLVL2_Price.var", "w")
    f.write(str(CookieClickLVL2_Price))
    f.close()

    CookieClickLVL3_Price_text.text = f"Price: {CookieClickLVL3_Price}"
    f = open("variables/CookieClickLVL3_Price.var", "w")
    f.write(str(CookieClickLVL3_Price))
    f.close()

    CookieClickLVL4_Price_text.text = f"Price: {CookieClickLVL4_Price}"
    f = open("variables/CookieClickLVL4_Price.var", "w")
    f.write(str(CookieClickLVL4_Price))
    f.close()

    CookieClickLVL5_Price_text.text = f"Price: {CookieClickLVL5_Price}"
    f = open("variables/CookieClickLVL5_Price.var", "w")
    f.write(str(CookieClickLVL5_Price))
    f.close()


def Click(instance):
    global cookies, f

    f = open("variables/cookies.var")
    cookies = int(f.read())
    f.close()

    cookies += CookieClick
    UpdateCookies()


def Buy_Cookie_Upgrade(instance):
    global cookies, CookieClick_Price
    if cookies > CookieClick_Price:
        global CookieClick, f
        cookies -= CookieClick_Price
        CookieClick_Price += 5
        CookieClick += 1
        UpdateCookies()


def Buy_CookieLVL2_Upgrade(instance):
    global cookies, CookieClickLVL2_Price
    if cookies > CookieClickLVL2_Price:
        global CookieClick, f
        cookies -= CookieClickLVL2_Price
        CookieClickLVL2_Price += 25
        CookieClick += 5
        UpdateCookies()


def Buy_CookieLVL3_Upgrade(instance):
    global cookies, CookieClickLVL3_Price
    if cookies > CookieClickLVL3_Price:
        global CookieClick, f
        cookies -= CookieClickLVL3_Price
        CookieClickLVL3_Price += 125
        CookieClick += 25
        UpdateCookies()


def Buy_CookieLVL4_Upgrade(instance):
    global cookies, CookieClickLVL4_Price
    if cookies > CookieClickLVL4_Price:
        global CookieClick, f
        cookies -= CookieClickLVL4_Price
        CookieClickLVL4_Price += 125
        CookieClick += 125
        UpdateCookies()


def Buy_CookieLVL5_Upgrade(instance):
    global cookies, CookieClickLVL5_Price
    if cookies > CookieClickLVL5_Price:
        global CookieClick, f
        cookies -= CookieClickLVL5_Price
        CookieClickLVL5_Price += 525
        CookieClick += 525
        UpdateCookies()


# ---------------------------------------------------------------------------
# UI (Kivy widgets replacing the Tkinter widgets)
# ---------------------------------------------------------------------------

class BGBoxLayout(BoxLayout):
    """A BoxLayout that paints itself with the game's background color,
    since Kivy widgets are transparent by default (unlike Tk frames)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*BG_COLOR)
            self._rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, *args):
        self._rect.pos = self.pos
        self._rect.size = self.size


def make_upgrade_row(title, description, price_text, image_source, on_press):
    """Builds one upgrade row (title/description/price/button), mirroring
    each CookieClickLVLx_Frame block from the Tkinter version."""
    frame = BGBoxLayout(orientation='vertical', size_hint_y=None, height=140, padding=4, spacing=2)

    title_label = Label(text=title, font_size=16, size_hint_y=None, height=24, color=(0, 0, 0, 1))
    frame.add_widget(title_label)

    price_label = Label(text=price_text, font_size=14, size_hint_y=None, height=20, color=(0, 0, 0, 1))
    frame.add_widget(price_label)

    bottom_row = BGBoxLayout(orientation='horizontal', spacing=6)
    description_label = Label(text=description, font_size=12, color=(0, 0, 0, 1))
    bottom_row.add_widget(description_label)

    button = Button(size_hint=(None, None), size=(64, 64), background_normal=image_source,
                     background_down=image_source, border=(0, 0, 0, 0))
    button.bind(on_press=on_press)
    bottom_row.add_widget(button)

    frame.add_widget(bottom_row)

    return frame, price_label


class CookieClickerApp(App):
    def build(self):
        global Cookies_text, CookieClick_text
        global CookieClick_Price_text, CookieClickLVL2_Price_text
        global CookieClickLVL3_Price_text, CookieClickLVL4_Price_text
        global CookieClickLVL5_Price_text

        self.title = "Cookie Clicker"
        Window.clearcolor = BG_COLOR

        root = BoxLayout(orientation='horizontal')

        # Left side: cookie counter, click counter, and the clickable cookie
        left_side = BGBoxLayout(orientation='vertical')

        Cookies_text = Label(text=f"Cookies: {cookies}", font_size=20, size_hint_y=None, height=40,
                              color=(0, 0, 0, 1))
        left_side.add_widget(Cookies_text)

        CookieClick_text = Label(text=f"CookieClicks: {CookieClick}", font_size=14, size_hint_y=None, height=30,
                                  color=(0, 0, 0, 1))
        left_side.add_widget(CookieClick_text)

        # Spacer to push the big cookie button toward the bottom, like pack(side=BOTTOM)
        left_side.add_widget(Widget())

        cookie_button = Button(background_normal='assets/Cookie.png', background_down='assets/Cookie.png',
                                border=(0, 0, 0, 0), size_hint=(None, None), size=(250, 250),
                                pos_hint={'center_x': 0.5})
        cookie_button.bind(on_press=Click)
        left_side.add_widget(cookie_button)

        root.add_widget(left_side)

        # Right side: upgrade menu
        upgrade_menu = BGBoxLayout(orientation='vertical', size_hint_x=0.4, padding=8, spacing=8)

        row1, CookieClick_Price_text = make_upgrade_row(
            "Upgrade Cookies", "Make Clicking Cookies Give +1 Cookie",
            f"Price: {CookieClick_Price}", 'assets/Cookie.png', Buy_Cookie_Upgrade)
        upgrade_menu.add_widget(row1)

        row2, CookieClickLVL2_Price_text = make_upgrade_row(
            "Pea Cookies", "Make Clicking Cookies Give +5 Cookie",
            f"Price: {CookieClickLVL2_Price}", 'assets/CookieLVL2.png', Buy_CookieLVL2_Upgrade)
        upgrade_menu.add_widget(row2)

        row3, CookieClickLVL3_Price_text = make_upgrade_row(
            "Plant Cookies", "Make Clicking Cookies Give +25 Cookie",
            f"Price: {CookieClickLVL3_Price}", 'assets/CookieLVL3.png', Buy_CookieLVL3_Upgrade)
        upgrade_menu.add_widget(row3)

        row4, CookieClickLVL4_Price_text = make_upgrade_row(
            "Firey Cookies", "Make Clicking Cookies Give +125 Cookie",
            f"Price: {CookieClickLVL4_Price}", 'assets/CookieLVL4.png', Buy_CookieLVL4_Upgrade)
        upgrade_menu.add_widget(row4)

        row5, CookieClickLVL5_Price_text = make_upgrade_row(
            "Icey Cookies", "Make Clicking Cookies Give +525 Cookie",
            f"Price: {CookieClickLVL5_Price}", 'assets/CookieLVL5.png', Buy_CookieLVL5_Upgrade)
        upgrade_menu.add_widget(row5)

        root.add_widget(upgrade_menu)

        return root


if __name__ == "__main__":
    CookieClickerApp().run()
