from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen

class MainApp(MDApp):
    def __init__(self, _table_records, **kwargs):
        super().__init__(**kwargs)
        self.table_records=_table_records

    def build(self):
        mainScreen = Screen()
        mainLayout = BoxLayout(orientation = 'vertical')
        self.create_buttons(mainLayout)
        self.create_table(mainLayout)
        mainScreen.add_widget(mainLayout)
        return mainScreen
    
    def create_buttons(self, layout):
        self.btnLayout = BoxLayout(orientation='horizontal', size_hint =(1,0.1),pos_hint = {'top': 1})
        self.btn_search = Button(text ='Search',font_size=dp(30))
        self.btn_add = Button(text ='Add',font_size=dp(30))
        self.btn_del = Button(text = 'Delete',font_size=dp(30))
        self.btn_save = Button(text = 'Save',font_size=dp(30))
        self.btn_load = Button(text = 'Load',font_size=dp(30))
        self.buttons = list((self.btn_search,self.btn_add,self.btn_del, self.btn_save, self.btn_load))
        for btn in self.buttons:
            self.btnLayout.add_widget(btn)
        layout.add_widget(self.btnLayout)
    
    def create_table(self, layout):
        self.tblLayout = BoxLayout()
        self.table = MDDataTable(
            check=True,
            use_pagination=True,
            column_data =
            [
                ('FullName:', dp(80)),
                ('Rank:',dp(30)),
                ('Sport:',dp(30)),
                ('Position:',dp(30)),
                ('Squad:', dp(30)),
                ('Titles:', dp(180))
            ],
            row_data = 
            [
                (f"{record[0]}",f"{record[1]}",f"{record[2]}",f"{record[3]}",f"{record[4]}",f"{record[5]}") for record in self.table_records
            ]
        )
        self.tblLayout.add_widget(self.table)
        layout.add_widget(self.tblLayout)


