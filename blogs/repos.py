from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from blogs import models


class BlogReposInterface(Protocol):
    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blogs(self) -> QuerySet[models.Blog]: ...


class BlogReposV1:
    def create_blog(self, data: OrderedDict) -> models.Blog:
        return models.Blog.objects.create(**data)

    def get_blogs(self) -> QuerySet[models.Blog]:
        return models.Blog.objects.all()
