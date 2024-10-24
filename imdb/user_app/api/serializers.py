from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']  

    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data.get('password2')

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'})

        account = User(username=self.validated_data['username'], email=self.validated_data['email'])
        account.set_password(password)
        account.save()
        return account