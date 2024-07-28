from rest_framework import serializers
from rest_framework.response import Response
from watchlist_app.models import WatchList,StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    # name_length = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = '__all__'
        # exclude = ['name']

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only = True,
    #     view_name='movie_detail'
    # )
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        
    # def get_name(self,object):
    #     length = len(object.name)
    #     return length
        
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Title and Description must be Different')
    #     else:
    #         return data
        
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Movie Name is too Short")
    #     elif len(value) >= 50:
    #         raise serializers.ValidationError("Movie Name is too Big")
    #     else:
    #         return value



 
# def validate_name(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Movie Name is too Short")
#     elif len(value) >= 50:
#         raise serializers.ValidationError("Movie Name is too Big") 
    
# class MovieSerializer(serializers.Serializer):
#     id =  serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[validate_name])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
        
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#     # Object-Level Validation
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description must be Different')
#         else:
#             return data
        
    # Field-level Validation
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Movie Name is too Short")
    #     elif len(value) >= 50:
    #         raise serializers.ValidationError("Movie Name is too Big")
    #     else:
    #         return value
        
            