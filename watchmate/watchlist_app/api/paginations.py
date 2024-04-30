from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
class WatchListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "page"
    page_size_query_param = "size"
    last_page_strings = ('last',)
    
    
class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4    
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'