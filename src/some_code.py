from .dao.some_dao import DAO

def code1():
    
    dao = DAO() 
    dao.insert("insert data")
    print("insert end")
   
def code2():
    
    dao = DAO()
    print(dao.name)