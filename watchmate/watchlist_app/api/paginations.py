from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "page"
    page_size_query_param = "size"