from rest_framework.pagination import PageNumberPagination


class SmallPagePagination(PageNumberPagination):
    page_size = 3
