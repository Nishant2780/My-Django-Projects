from dataclasses import fields
import string
from rest_framework import serializers
from .models import *
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):

    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        # fields = '__all__'
        # fields = ['todo_title']
        exclude = ['created_at']


    def get_slug(self, obj):       ## slug
        return slugify(obj.todo_title)

    def validate(self, validated_data):    #check field take special character or not
        # print(validated_data)
        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if len(todo_title) < 3:
                raise serializers.ValidationError('todo title must have 3 chars')
            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('cannot accept special character')
        return validated_data

class TimingTodoSerializer(serializers.ModelSerializer):

    todo = TodoSerializer()        #It is used to show ForeignKey data but it will show only data we want to show
    class Meta:
        model = TimingTodo
        fields = '__all__'
        depth = 1               #Depth is used to show ForeignKey data, but one problem with depth is
                                #it show all the data from ForeignKey table




# class ProductTypeSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ProductType
#         # fields = '__all__'
#         exclude = ['added_date']

# class Products_DetailsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Products_Details
#         fields = '__all__'   
#         # exclude = []     