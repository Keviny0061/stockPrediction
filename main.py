from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from fetch_data import fetch_data
from kivy.lang import Builder


class StockApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='Stock Analysis App', font_size=32, size_hint_y=None, height=44))

        self.ticker_input = TextInput(hint_text='Enter Stock Ticker', multiline=False, size_hint_y=None, height=88)
        self.add_widget(self.ticker_input)

        self.fetch_button = Button(text='Fetch Data', size_hint_y=None, height=88)
        self.fetch_button.bind(on_press=self.fetch_stock_data)
        self.add_widget(self.fetch_button)

        self.output_label = Label(font_size=16, size_hint_y=0.7, text='')
        self.add_widget(self.output_label)

    def fetch_stock_data(self, instance):
        try:
            ticker = self.ticker_input.text
            print("Fetching data for:", ticker)
            data = fetch_data(ticker)  # this function is from fetch_data.py
            self.output_label.text = str(data)
        except Exception as e:
            print(f"An error occurred: {e}")
            self.output_label.text = f"An error occurred: {e}"

class StockAnalysisApp(App):
    def build(self):
        return StockApp()
if __name__ == "__main__":
    Builder.load_file('main.kv')
    StockAnalysisApp().run()

