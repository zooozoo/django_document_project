from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership',
)


class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateTimeField()
    members = models.ManyToManyField(
        Idol,
        through='Membership',
        through_fields=('group', 'idol'),
    )

    # 괄호 안에는 (소스, 타겟) 순서로 넣어준다. 안의 이름은 클래스 이름이 아니라 Membership클래스 안의 두 필드의 이름이다.
    # (many-to-many관계를 선안한 쪽을 선언 한 쪽을 소스, 그 대상이 되는 쪽이 타겟)
    # Through='Membership' 구문을 통해 자동으로 intermediate테이블을 만드는 것이 아닌
    # intermediate모델인 Membership테이블로 연결된다.

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(
        Idol,
        on_delete=models.CASCADE,
        related_name='membership_set',  # 기본 값이기 때문에 이름을 넣지 않아도 되는데 지금은 의미상 넣어둔 것임
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # recommender = models.ForeignKey(
    #     Idol,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     related_name='recommend_membership_set'
    # )
    recommenders = models.ManyToManyField(
        Idol,
        blank=True,
        related_name='recommend_membership_set',
    )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name}' \
               f'{self.idol.name}' \
               f'({self.is_active})'
