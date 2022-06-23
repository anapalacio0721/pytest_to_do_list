import pytest
from Call import Call
from User import User
from Item import Item

@pytest.fixture
def call():
    call = Call("purpose","leader","21/06/2022")
    return call

def user():
    user = User("cc","12345","Ana", "Palacio", call)
    return user

def item():
    item = Item("1","SGI","1", "Palacio", user)
    return item

def test_get_purpuse_of_call(call):
    purpose = call.get_purpose()
    assert "purpose" == purpose

def test_set_purpose_of_call(call):
    call.set_purpose("desarrollo")
    assert "desarrollo" == call.get_purpose()

def test_get_leader_of_call(call):
    leader = call.get_leader()
    assert "leader" == leader

def test_set_leader_of_call(call):
    call.set_leader("Andres")
    assert "Andres" == call.get_leader()

def test_get_document_type_of_user(user):
    document_type = user.get_document_type()
    assert "cc" == document_type

def test_set_document_type_of_user((user):
    user.set_document_type("cc")
    assert "cc" == user.get_document_type()

def test_get_document_number_of_user((user):
    document_number = user.get_document_number()
    assert "12345" == document_number

def test_set_document_number_of_user(user):
    user.set_document_number("12345")
    assert "12345" == user.get_document_number()

def test_get_name_of_user(user):
    name = user.get_name()
    assert "Ana" == name

def test_set_name_of_user(user):
    user.set_name("Ana")
    assert "Ana" == user.get_name()

def test_get_last_name_of_user(user):
    last_name = user.get_last_name()
    assert "Palacio" == last_name

def test_set_last_name_of_user(user):
    user.set_last_name("Palacio")
    assert "Palacio" == user.get_name()

def test_get_call_assigned_of_user(user):
    call_assigned = user.get_call_assigned()
    assert user == user.get.call_assigned

def test_set_call_assigned_of_user(user):
    user.set_call_assigned(call)
    assert call == user.call.get_call_assigned()

def test_get_id_of_item(item):
    iditem = item.get_iditem()
    assert "1" == iditem

def test_get_description_of_item(item):
    description = item.get_descripcion()
    assert "SGI" == description

def test_set_description_of_item(item):
    item.set_description("SGI")
    assert "SGI" == item.get_description()

def test_get_priority_of_item(item):
    priotity = item.get_priority()
    assert "alta" == priority

def test_set_priority_of_item(item):
    item.set_priority("alta")
    assert "alta" == item.get_priority()

def test_get_assigne_to_of_item(item):
    assigne_to = item.get_assigne_to()
    assert user == priority

def test_set_assigne_to_of_item(item):
    item.set_assigne_to(user)
    assert user == item.get_assigne_to()


    
    

    

    
