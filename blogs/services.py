from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from blogs import models, repos


class BlogReposInterface(Protocol):
    repos: repos.BlogReposInterface

    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blogs(self) -> QuerySet[models.Blog]: ...


class BlogReposV1:
    blog_repos: repos.BlogReposInterface = repos.BlogReposV1()

    def create_blog(self, data: OrderedDict) -> models.Blog:
        print('create blog in service layer')
        return self.blog_repos.create_blog(**data)

    def get_blogs(self) -> QuerySet[models.Blog]:
        print('get blogs in service layer')
        return self.blog_repos.get_blogs()
