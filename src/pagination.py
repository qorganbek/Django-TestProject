from rest_framework import pagination


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'


class CustomCursorPagination(pagination.CursorPagination):
    ordering = 'createdAt'
    page_size_query_param = 'page_size'

