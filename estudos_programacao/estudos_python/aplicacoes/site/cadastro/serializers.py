from rest_framework import serializers
from .models import Aluno

class AlunoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id', 'name')
        