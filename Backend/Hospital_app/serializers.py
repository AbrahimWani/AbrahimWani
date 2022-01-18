from Backend.Hospital_app.models import User_table
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


# user Table_serialzer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_table
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "gender",
            "email",
            "phone_no",
            "country",
            "state",
            "city",
            "dob",
            "expertise",
            "qualification",
            "user_type",
            "user_status",
            "created_at",
            "password",
            "modified_at",
        ]

    def get__id(self, obj):
        return obj.id


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User_table
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "gender",
            "email",
            "phone_no",
            "country",
            "state",
            "city",
            "dob",
            "expertise",
            "qualification",
            "user_type",
            "user_status",
            "created_at",
            "password",
            "modified_at",
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
