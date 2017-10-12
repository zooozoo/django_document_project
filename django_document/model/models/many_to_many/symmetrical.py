from django.db import models

__all__ = (
    'InstagramUser',
)

class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    # symmetrical=False 옵션으로성
    # 자기 자신을 참조하는 following 필드 1개 생
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.name
