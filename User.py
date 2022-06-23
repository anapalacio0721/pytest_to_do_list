class User:
    def __init__(self, document_type, document_number, name, last_name, cell_assigned):
        self.document_type = document_type
        self.document_number = document_number
        self.name= name
        self.last_name= last_name
        self.cell_assigned = cell_assigned


    def get_document_type(self):
        return self.document_type

    def set_document_type(self, document_type):
        self.document_type = document_type

    def get_document_number(self):
        return self.document_number

    def set_document_number(self, document_number):
        self.document_number = document_number
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name= name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name= last_name

    def get_call_assigned(self):
        return self.cell_assigned

    def set_call_assigned(self, cell_assigned):
        self.cell_assigned = cell_assigned
        
