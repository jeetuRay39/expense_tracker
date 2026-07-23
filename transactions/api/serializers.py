from rest_framework import serializers
from transactions.models import Transaction
from categories.models import Category

class TransactioinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__" 
        read_only_fields = (
            "user",
            "created_at",
            "updated_at",

        )


    def validate_amount(self, value):

        if value <=0:
            raise serializers.ValidationError(
                "Amout must be greater than zero"
            )
        return value
    
    def validate_category(self , value):

        request = self.context.get("request")

        if request and value.user != request.user:
            raise serializers.ValidationError(
                "you can only use your own category"
            )
        return value
    
    def validate(self , attrs):

        category = attrs.get("category")
        transaction_type = attrs.get("transaction_type") 

        if category and transaction_type:
            if category.category_type != transaction_type:
                raise serializers.ValidationError(
                    {
                        "category": ("Category type must match the transaction type")
                    }
                )
            
        return attrs