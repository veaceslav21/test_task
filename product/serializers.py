from rest_framework import serializers
from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(source='productimage_set', many=True, read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'author', 'images')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        new_product = Product.objects.create(**validated_data)
        for img in images_data.values():
            ProductImage.objects.create(product=new_product, image=img)
        return new_product

    def update(self, instance, validated_data):
        images_data = self.context.get('view').request.FILES
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        if images_data:
            post_image_model_instance = [ProductImage(product=instance, image=image)
                                         for image in images_data.values()]
            ProductImage.objects.bulk_create(
                post_image_model_instance
            )
        return instance


