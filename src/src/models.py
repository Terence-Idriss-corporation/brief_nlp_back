from django.db import models

class Film(models.Model):
    titre = models.CharField(max_length=100)
    note_spectateur = models.IntegerField()
    note_presse = models.IntegerField()
    nombre_commentaires = models.IntegerField()

    def __str__(self):
        return self.titre
    
    class Meta:
        db_table = 'films'
    
class Commentaire(models.Model):
    pseudo = models.TextField(null=True)
    commentaire = models.TextField()
    note = models.IntegerField()

    def __str__(self):
        return self.commentaire
    
    class Meta:
        db_table = 'commentaire'
    
class NLP(models.Model):
    model = models.CharField(max_length=255)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    note = models.IntegerField()

    def __str__(self):
        return f"{self.model} - {self.film.titre}"
    
    class Meta:
        db_table = 'nlp'