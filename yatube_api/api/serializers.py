from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import *

class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
        slug_field='username')
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('following', 'user'),
                message='Вы уже подписаны на этого автора!'
            )
        ]

    def validate(self, data):
        if 'following' in data:
            if data['following'] == self.context['request'].user:
                raise serializers.ValidationError(
                    'Нельзя подписаться на самого себя!')
            return data
        raise serializers.ValidationError('Ошибка переданных данных.')
