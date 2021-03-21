# BookProject

Book Store Project(DRF)
Authentication Used-Token Authentication
UserLog App-->For creating Authentication token for admin and non-admin users.
    -->Model used-->User Model
    -->Request used-->
          -->POST Method(for creeating auth token)-->http://127.0.0.1:8000/api/token/auth/
              -->Body - {"username":"aaa","password":"aaa"}-->(For admin user)
                        {"username":"xxx","password":"xxx"}-->(for non-admin user)
              -->Response - status code 200 OK  
          -->GET Method(Permission given to admin users for listing all users.)-->>http://127.0.0.1:8000/api/users/
Admin/Superuser - can register, login, authenticate and perform all CRUD operations including search operations. Normal Users - can login, authenticate and view list of books and perform search operations.

Using Class Based Views - viewsets.ModelViewSet

APIs - Requests and Responses

Request Method : GET (Search Fields - Author Name) Url - http://127.0.0.1:8000/bookstore/booklist/ (Complete List of Books) Url - http://127.0.0.1:8000/book/int:pk/detail/ (Particular Book) Response - status 200 ok

Request Method : POST Url - http://127.0.0.1:8000/bookstore/bookcreate/ Body - { "author_name": [ { "author_name": "APJ Abdul Kalam" } ], "title": "Ignited Minds", "publication_date": "2012-03-19" } Response - status 201 created

Request Method : PUT Url - http://127.0.0.1:8000/book/int:pk/update/ Body - { "author_name": [ { "author_name": "APJ Abdul Kalam" } ], "title": "Ignited Minds", "publication_date": "2021-03-19" } Response - status 200 ok

Request Method : PATCH Url - http://127.0.0.1:8000/book/int:pk/update/ Body - { "title": "Ignited Minds 22", "publication_date": "2012-03-19" } Response - status 200 ok

Request Method : DELETE Url - http://127.0.0.1:8000/book/int:pk/delete/ Response - status 204 no content

Additional Features - Searching list of books with search filters applied in GET method above that searches availability of books using author name or book name.
