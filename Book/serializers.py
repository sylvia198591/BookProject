import re
from itertools import count

from django.db.models import Max, Sum,Count
from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User, Group
from Book.models import *
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age']


    def validate_age(self, value):
        if value>200:
            raise serializers.ValidationError('Pls check the age.Age has to be less than 200.')
        return value
    def validate_name(self, value):
        res = bool(re.match('[a-zA-Z.\s]+$', value))
        print("res::",str(res))
        # res = value != '' and all(chr.isalpha() or chr.isspace() for chr in value)
        if (str(res)=='False' ):
            print("ehr")
            raise serializers.ValidationError('Name should have only alphabets,space and dot')
        return value
class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer()
    rating = serializers.ChoiceField(choices=[1, 2, 3, 4, 5])
    class Meta:
        model = Book
        fields = ['name', 'price','description','rating','isbn','pub_date','author','url']
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Book.objects.all(),
        #         fields=['name', 'isbn']
        #     )
        # ]
    def create(self, validated_data):
        # partial=True
        print(validated_data)
        author_update=validated_data
        author = validated_data.pop('author')
        name = validated_data.get('name')
        rating = validated_data.get('rating')
        print("name:::",name)
        print("autn::",author)
        # auth_name=validated_data.get(author['name'])
        a_name=author['name']
        print("aname::",author['name'])
        auth_rate=Book.objects.filter(author__name=a_name).aggregate(Total=Sum('rating'))
        auth_cnt = Book.objects.filter(author__name=a_name).count()
        print("ar:::", auth_cnt)
        # if()
        if(auth_rate['Total'] is None):
            auth_rate['Total']=0
        tot_rat=rating+auth_rate['Total']
        print("ar:::",auth_rate['Total'])
        auth_avg=tot_rat/(auth_cnt+1)
        print("aavg::",auth_avg)
        author_id=Author.objects.filter(name=author['name'],age=author['age']).count()

        author_id, created = Author.objects.get_or_create(name=author['name'], age=author['age'])
        author_id.auth_rate=auth_avg

        author_id.save()
        book = Book.objects.create(author=author_id,**validated_data)
        # book.save()
        return book
    def update(self, instance, validated_data):
        print("vd",validated_data)
        author = validated_data.pop('author')
        # instance.author=validated_data.pop('author')
        # print("auth::",instance.author)
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.description = validated_data['description']
        instance.rating = validated_data['rating']
        instance.isbn = validated_data['isbn']
        # instance.name = validated_data['author_name']
        instance.pub_date = validated_data['pub_date']
        # print("aname::",author['name'])
        auth_rate=Book.objects.filter(author__name=instance.name).aggregate(Total=Sum('rating'))
        auth_cnt = Book.objects.filter(author__name=instance.name).count()
        print("ar:::", auth_cnt)
        # if()
        if(auth_rate['Total'] is None):
            auth_rate['Total']=0
        tot_rat=instance.rating+auth_rate['Total']
        print("ar:::",auth_rate['Total'])
        auth_avg=tot_rat/(auth_cnt+1)
        print("aavg::",auth_avg)
        author_id=Author.objects.filter(name=author['name'],age=author['age']).count()
        authors_list = []
        author_id,created = Author.objects.get_or_create(name=author['name'], age=author['age'])
        # authors_list.append(author_id)
        # instance.author_id.set(authors_list)
        # print("aid::",author_id)
        author_id.auth_rate = auth_avg
        author_id.save()
        instance.author_id=author_id.id
        print("autid::",author_id.id)
        # if(author_id.id>0):
        print("aid::",author_id)
        # author_id.save()
        # author_id.auth_rate = auth_avg
        instance.save()
        return instance
    # def save(self):
    #     super(BookSerializer, self).save()

    def validate_isbn(self, value):


        if (len(value) !=10):
            raise serializers.ValidationError('ISBN code should have 10 digits')
        return value


class BookSerializer1(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    rating = serializers.ChoiceField(choices=[1, 2, 3, 4, 5])
    class Meta:
        model = Book
        fields = ['name', 'price','description','rating','isbn','pub_date','author']
    # def update(self, instance, validated_data):
    #     author = validated_data.pop('author')
    #     # author_id = Author.objects.filter(name=instance.author['name'], age=instance.author['age']).count()
    #
    #     author_id, created = Author.objects.get_or_create(name=author['name'], age=author['age'])
    #     # author_id.auth_rate = auth_avg
    #
    #     author_id.save()
    #     book = Book.objects.create(author=author_id, **validated_data)
    #     # book.save()
    #     return book

class AuthorDetailSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='books-detail'
    )
    class Meta:
        model = Author
        fields = ['name','age','books']

class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id','url','name', 'age']


    # id = serializers.ReadOnlyField()
    # url= serializers.HyperlinkedIdentityField(
    #     many=True,
    #     # read_only=True,
    #     view_name='books-list',lookup_field='pk'
    # )
    # track_listing = serializers.HyperlinkedIdentityField(
    #     many=True,
    #     # read_only=True,
    #     view_name='track-list',
    # )
    # url = serializers.HyperlinkedIdentityField(
    #     # many=True,
    #     # read_only=True,
    #     view_name='Album_update', lookup_field='pk'
    # )


# def validate_price(self, value):
#     if isinstance(value, float):
#         raise serializers.ValidationError('Pls check the float')
#     return value
# def validate_rating(self, value):
#     if isinstance(value, float):
#         raise serializers.ValidationError('Pls check the age.Age has to be less than 200.')
#     return value



# class RegisterSerializer(serializers.Serializer):
#     model = User
#     fields = ['id', 'username', 'email', 'first_name', 'last_name', 'isadmin', 'isstaff']
#
#     def validate_username(self, value):
#         if len(value)<=8:
#             raise serializers.ValidationError('Length of the username has to be more than 8')
#         return value
#     def validate_isadmin(self, email):
#         email = get_adapter().clean_email(email)
#         if allauth_settings.UNIQUE_EMAIL:
#             if email and email_address_exists(email):
#                 raise serializers.ValidationError(
#                     _("A user is already registered with this e-mail address."))
#         return email
#
#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)
#
#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError(_("The two password fields didn't match."))
#         return data
#
#     def custom_signup(self, request, user):
#         pass
#
#     def get_cleaned_data(self):
#         return {
#             'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', '')
#         }
#
#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         adapter.save_user(request, user, self)
#         self.custom_signup(request, user)
#         setup_user_email(request, user, [])
#         return user

# def multiple_of_one(value):
#
#     if isinstance(value, int):
#         if(value>0 and value<=5):
#             if value%1!=0
#             raise serializers.ValidationError('The rating can ony be 1,2,3,4,5')
#         return value
