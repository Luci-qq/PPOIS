from Controller import Controller
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen

class MainScreen(Screen):
    def __init__(self,_controller:Controller, **kw):
        super().__init__(**kw)
        self.controller=_controller
        self.mainLayout = BoxLayout(orientation = 'vertical')
        self.checked_rows=[]
        self.create_buttons(self.mainLayout)
        self.create_table(self.mainLayout)
        self.fill_table()
        self.add_widget(self.mainLayout)

    def btn_del_press(self,instance):
        if not self.table.get_row_checks():
            print('checked rows empty')
        else:
            for row in self.table.get_row_checks():
                self.controller.remove_elm(row[0])
            self.checked_rows=[]
            self.fill_table()
    
    def btn_save_press(self,instance):
        print("Save Pressed")
    
    def btn_load_press(self,instance):
        print("Load pressed")

    def btn_add_press(self, instance):
        print("Add pressed")
    
    def btn_search_press(self,instance):
        self.get_data
    
    def create_buttons(self, layout):
        self.btnLayout = BoxLayout(orientation='horizontal', size_hint =(1,0.1),pos_hint = {'top': 1})
        self.btn_search = Button(text ='Search',font_size=dp(30))
        self.btn_search.bind(on_press= self.btn_search_press)
        self.btn_add = Button(text ='Add',font_size=dp(30))
        self.btn_add.bind(on_press= self.btn_add_press)
        self.btn_del = Button(text = 'Delete',font_size=dp(30))
        self.btn_del.bind(on_press=self.btn_del_press)
        self.btn_save = Button(text = 'Save',font_size=dp(30))
        self.btn_save.bind(on_press= self.btn_save_press)
        self.btn_load = Button(text = 'Load',font_size=dp(30))
        self.btn_load.bind(on_press= self.btn_load_press)
        self.buttons = list((self.btn_search,self.btn_add,self.btn_del, self.btn_save, self.btn_load))
        for btn in self.buttons:
            self.btnLayout.add_widget(btn)
        layout.add_widget(self.btnLayout)
    
    def fill_table(self):
         self.table.row_data=[]
         self.table.row_data=self.controller.get_record_list()
         
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
            ]
        )
        self.tblLayout.add_widget(self.table)
        layout.add_widget(self.tblLayout)



class MainApp(MDApp):
    def __init__(self, _table_records, **kwargs):
        super().__init__(**kwargs)
        self.table_records = _table_records
    def build(self):
        return MainScreen(self.table_records)
    
    

