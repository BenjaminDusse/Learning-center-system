from rest_framework import pagination
from rest_framework.response import Response


class PageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.page.next_page_number() if self.page.paginator.num_pages > self.page.number else None,
            'previous': self.page.previous_page_number() if self.page.number > 1 else None,
            'results': data
        })

    # def get_paginated_response(self, data):
    #     return Response({
    #         'links': {
    #             'next': self.get_next_link(),
    #             'previous': self.get_previous_link()
    #         },
    #         'next': self.page.next_page_number(),
    #         'previous': self.page.previous_page_number() if self.page.number > 1 else None,
    #         'count': self.page.paginator.count,
    #         'results': data
    #     })

    # def paginate_queryset(self, queryset, request, view=None):
    #     return super().paginate_queryset(queryset, request, view)
