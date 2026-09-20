from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.validators import UniqueValidator

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only = True, trim_whitespace = False)

    def validate(self, data):
        user = authenticate(request=self.context.get("request"), username = data["username"], password = data["password"])


        if user is None or not user.is_active:
            raise serializers.ValidationError("Неверное имя пользователя или пароль")
        return{"user": user}

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,trim_whitespace=False)
    password_confirm = serializers.CharField(write_only=True,trim_whitespace=False)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all(),lookup="iexact",message="Эта почта уже используется.")]
    )
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "password",
            "password_confirm"
        ]
        read_only_fields = ["id"]

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError({"password_confirm": "Пароли не совпадают․"})
        user = get_user_model()(
            username = data["username"],
            email = data["email"]
        )

        try:
            validate_password(data["password"], user = user)
        except DjangoValidationError as error:
            raise serializers.ValidationError({
                "password": error.messages
            })

        return data


    def create(self, validated_data):
        validated_data.pop("password_confirm")
        return get_user_model().objects.create_user(
            **validated_data
        )

    
        # vibecode chem anum aperiknerrrrrr 1488
    