from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    page_query_param = 'current'
    page_size_query_param = 'pageSize'
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'current': self.page.number,
            'data': data,
            'pageSize': self.page.paginator.per_page,
            'success': True,
            'total':self.page.paginator.count
        })

