# BookProject

Book Store Project(DRF)
Authentication Used-Token Authentication
UserLog App-->For creating Authentication token for admin(perform create,update,list,retrieve and delete operations) and non-admin(List operations) users.
    -->Model used-->User Model
    -->Request used-->
          -->POST Method(for creeating auth token)-->http://127.0.0.1:8000/api/token/auth/
              -->Body - {"username":"aaa","password":"aaa"}-->(For admin user)
                        {"username":"xxx","password":"xxx"}-->(for non-admin user)
              -->Response - status code 200 OK  
          -->GET Method(Permission given to admin users for listing all users.)-->>http://127.0.0.1:8000/api/users/
              -->Auth-->Type-->Inherit auth from parents
                        Headers-->Authoriztion-->token (generated token key)
Book App-->For creating,updating,retrieving,deleting,listing and searching Author and Book details
    -->Model used-->Author Model and Book Model(author field in Book model has a foreign key relationship to Author model)
Viewsets:
    -->Request used-->(For Creating and listing Author)
          -->POST Method(for creeating Author model)-->http://127.0.0.1:8000/book/Author/
              -->Body - {"name":"Mario Puzzo","age":70}-->(For admin user)
              -->Response - status code 201 Created  
          -->GET Method(for listing all Authors.)(For all authenticated users)-->>http://127.0.0.1:8000/book/Author
              -->Response - status code 200 OK
    -->Request used-->
          -->DETAIL Method(for retrieving Author model  based on a key value for all authenticated user)-->http://127.0.0.1:8000/book/Author/<int:pk>/              
              -->Response - status code 200 OK  
          -->PUT Method(for updating all Authors based on a key value)(For all admin users)-->>http://127.0.0.1:8000/book/Author/<int:pk>/ 
              -->Body - {"name":"Mario Puzzo","age":71}
              -->Response - status code 200 OK    
          -->PATCH Method(for updating particular fields of Author table based on a key value)(For all admin users)-->>http://127.0.0.1:8000/book/Author/<int:pk>/ 
              -->Body - {"age":71}
              -->Response - status code 200 OK 
          -->DELETE Method(for deleting record from author table based on a key value)(For all admin users)-->>http://127.0.0.1:8000/book/Author/<int:pk>/ 
              -->Body - {"age":71}
              -->Response - status code 204 NO CONTENT          
ListCreate APIView(Book Model):
    -->Request used-->(For Creating and listing Book)
          -->POST Method(for creeating Book model done by all admin users)-->http://127.0.0.1:8000/book/BookCreate/
              -->Body - {"name":"GodFather","price":250.00,"description":"About the Dons of Italy","rating":
                                5,"isbn":"10234485","pub_date":"1969-05-01 00:00:00","author":{"name":"Mario Puzzo","age":71}}
              -->Response - status code 201 Created  
          -->GET Method(for listing all Books.)(For all authenticated users)-->>http://127.0.0.1:8000/book/BookCreate/
              -->Response - status code 200 OK 
RetrieveUpdateDestroy APIView(Book Model):
    -->Request used-->
          -->DETAIL Method(for retrieving Book model  based on a key value for all authenticated user)-->http://127.0.0.1:8000/book/BookRetrieveUpdateDestroy/<int:pk>/           
              -->Response - status code 200 OK  
          -->PUT Method(for updating all Books based on a key value)(For all admin users)-->http://127.0.0.1:8000/book/BookRetrieveUpdateDestroy/<int:pk>/ 
              -->Body - {"name":"GodFather","price":350.00,"description":"About the Dons of Italy","rating":
                                5,"isbn":"10234485","pub_date":"1969-05-01 00:00:00","author":{"name":"Mario Puzzo","age":71}}
              -->Response - status code 200 OK    
          -->PATCH Method(for updating particular fields of Book table based on a key value)(For all admin users)-->>http://127.0.0.1:8000/book/BookRetrieveUpdateDestroy/<int:pk>/ 
              -->Body - {"name":"GodFather part-1"}
              -->Response - status code 200 OK 
          -->DELETE Method(for deleting record from author table based on a key value)(For all admin users)-->>http://127.0.0.1:8000/book/BookRetrieveUpdateDestroy/<int:pk>/ 
              -->Body - {"age":71}
              -->Response - status code 204 NO CONTENT 
SearchList(Book):
    -->Request used-->
          -->DETAIL Method(for searching books based on author name,book name, isbn,rating,description for all authenticated user)-->http://127.0.0.1:8000/book/BookAuthorSearchList/   
              -->Params-->Search(key)-->name(value)
              -->Response - status code 200 OK 
              
