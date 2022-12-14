from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=200)
    year = models.IntegerField()
    movie_dir = models.CharField(max_length=100)
    movie_act = models.CharField(max_length=200)
    movie_ger = models.CharField(max_length=200)
    movie_text = models.TextField(null=True)
    movie_poster = models.ImageField(null=True)

    def __str__(self):
        return f'[{self.movie_id}] : {self.movie_name}({self.year})'


class Ost(models.Model):
    movie_id = models.ForeignKey('Movie', related_name='post', on_delete=models.CASCADE, db_column='movie_id')
    ost_name = models.CharField(max_length=200)
    valence = models.FloatField(null=True, blank=True)
    acousticness = models.FloatField(null=True, blank=True)
    danceability = models.FloatField(null=True, blank=True)
    energy = models.FloatField(null=True, blank=True)
    loudness = models.FloatField(null=True, blank=True)
    tempo = models.FloatField(null=True, blank=True)
    cluster = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.movie_id} : {self.ost_name}'

    # class Movie_recommand(models.Model):
    #     ost_id = models.ForeignKey('Ost', on_delete=models.CASCADE, db_column='ost_id')
    #     user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    #     recodation = models.CharField(max_length=200)
    #
    # class User_rating(models.Model):
    #     recommand_id = models.ForeignKey('Movie_recommand', on_delete=models.CASCADE, db_column='recommand_id')
    #     review = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2), ], null=True)
    #     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='movie_id')

    def ost_search(movie_all):
        mo_id = movie_all
        ost_all = []
        for mov_id in mo_id:
            forign = Ost.objects.filter(movie_id_id=mov_id)
            ost_one = []
            for ost_num in forign:
                ost_one.append(ost_num.ost_name)
            ost_all.append(ost_one)
        return (ost_all)
