class Item:
    def __init__(self, iditem, description, priority, assigne_to):
        self.iditem = iditem
        self.description = description
        self.priority= priority
        self.assigne_to = assigne_to

    def get_id(self):
        return self.iditem

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description =  description

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority

    def get_assigne_to(self):
        return self.assigne_to

    def set_assigne_to(self, user):
        self.assigne_to = user
        

