from helper.messages import HELP
from .class_stock import Stock
class List(list):

    def help_list(self):
        return HELP.HELP_LIST

    def append_repeated(self, value):
        check = Stock.search_stock(value)
        if check == False:
            print(f'{value},dose not exist')
        else:
            if value in self:
                print("repeated")
            else:
                self.append(value)
                print(f"{value} added to list")

    def search_items(self, value):
        if not value in self:
            print(f' you have been never enter,{value}')
        else:
            print(value)

    def remove_list(self, value):
        if value not in self:
            print(f' you have been never enter,{value}')
        else:
            self.remove(value)
        return self

    def edit_list(self, value, new_value):
        if value in self:
            for index in range(0, len(self)):
                if self[index] == value:
                    self[index] = new_value
                
        else:
            print(f' you have been never enter,{value}')

    def beautify_list(self, value):
        for value in self:
            print(f"> {value}")

    def chose_count(self):
        for _ in self:
            yield _


class Count_list(List):

    pass

class Price_list(List):
    pass



