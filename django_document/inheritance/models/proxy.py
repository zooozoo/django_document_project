from django.db import models
from django.db.models import Manager

__all__ = (
    'Champion',
)


class Champion(models.Model):
    CHOICE_TYPE = (
        ('magician', '마법사'),
        ('supporter', '서포터'),
        ('ad', '원거리 딜러'),
    )
    champion_type = models.CharField(max_length=20, choices=CHOICE_TYPE)
    rank = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = '챔피언'
        ordering = ['rank']

    def __str__(self):
        return f'{self.name} ({self.get_champion_type_display()})'


class SupporterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(champion_type='supporter')


class Supporter(Champion):
    objects = SupporterManager()

    class Meta:
        proxy = True

    def buy_supporter_item(self):
        print(f'{self.name}은 서포터 아이템을 샀다')


class Midliner(Champion):
    class Meta:
        proxy = True

    def go_to_mid(self):
        print(f'{self.name}은 미드에 도착했다')
