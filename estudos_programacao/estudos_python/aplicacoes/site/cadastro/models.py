from typing import any
from django.db import models

class Aluno(models.Model):
    nomealuno = models.CharField(max_length=50)
    # ele retorna uma STRING
    def __str__(self):
        return self.nomealuno
    
class Professor(models.Model):
    nomeprofessor = models.CharField(max_length=50)
    def __str__(self):
        return self.nomeprofessor
    
class Disciplina(models.Model):
    nomedisciplina = models.CharField(max_length=50)
    def __str__(self):
        return self.nomedisciplina
    