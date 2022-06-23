from Item import Item
from User import User
from Call import Call

class To_Do_List:
    def __init__(self):
        self.items= []

    def add_item(self, item):
        self.items.append(item)

    def delete_item(self, iditem):
        for i in self.items:
            if (i.getId()== iditem):
                items.remove(i)

    def get_item(self, iditem):
        for i in self.items:
            if (i.getId()== iditem):
                print("id:" + i.iditem)
                print("description:" + i.description)
                print("priority:" + i.priority)
                print("use name:" + i.assigne_to.name)
                print("use last_name:" + i.assigne_to.last_name)

    def show_items(self):
        for i in self.items:
                print("id:" + i.iditem)
                print("description:" + i.description)
                print("priority:" + i.priority)
                print("use name:" + i.assigne_to.name)
                print("use last_name:" + i.assigne_to.last_name)


def main():
    call = Call("Desarrollo", "Andrea", "16 de Junio 2022")    
    user = User("CC", "1234", "Ana", "Palacio", call)
    item = Item("1", "Afiliar", "1", user)
    to_do_list = To_Do_List()
    to_do_list.add_item(item)
    to_do_list.show_items()
     
    
    
if __name__== "__main__":
    main()
