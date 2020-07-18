from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from . import serializers
from . import models


class CategoriesCoursesAPIView(APIView):
    '''
    Input: None
    Output: API to get list of Categories , each containing the list of courses names
    [
        {
            "name": "Category1",
            "courses": [
                "Course Name 1",
                "Course Name 2",
                "Course Name 3",
                "Course Name 4"
            ]
        },
        {
            "name": "Category2",
            "courses": [
                "Course Name 5",
                "Course Name 6",
                "Course Name 7"
            ]
        }
    ]

    '''

    def get(self, request):
        data = {
            "id1": {
                "name": "Course Name 1",
                "category": "Category1",
                "type": "Type 1"
            },
            "id2": {
                "name": "Course Name 2",
                "category": "Category1",
                "type": "Type 1"
            },
            "id3": {
                "name": "Course Name 3",
                "category": "Category1",
                "type": "Type 1"
            },
            "id4": {
                "name": "Course Name 4",
                "category": "Category1",
                "type": "Type 2"
            },
            "id5": {
                "name": "Course Name 5",
                "category": "Category2",
                "type": "Type 2"
            },
            "id6": {
                "name": "Course Name 6",
                "category": "Category2",
                "type": "Type 3"
            },
            "id7": {
                "name": "Course Name 7",
                "category": "Category2",
                "type": "Type 3"
            }
        }

        category_dict = {

        }

        for item in data:
            category_name = data[item]['category']
            if category_name not in category_dict:
                category_dict[category_name] = {
                    'name': category_name,
                    'courses': []
                }

            category = category_dict[category_name]

            category['courses'].append(data[item]['name'])

        result = [category_dict[key] for key in category_dict]

        return Response(result)


class EmailModelViewSet(viewsets.ModelViewSet):
    '''
    list: API
    input: None
    output: last 10 success emails
    [
        {
            "id": 4,
            "created": "2020-07-18T10:57:26.287385Z",
            "modified": "2020-07-18T10:57:26.550326Z",
            "email": "xyy@dsfs.com",
            "is_success": true
        },
        {
            "id": 3,
            "created": "2020-07-18T10:57:17.924340Z",
            "modified": "2020-07-18T10:57:19.449100Z",
            "email": "xyy@dsfs.com",
            "is_success": true
        }
    ]

    create: API
    input:
    {
        "email": "xyy@dsfs.com"
    }
    output:
    {
        "id": 5,
        "created": "2020-07-18T10:59:55.424034Z",
        "modified": "2020-07-18T10:59:56.924007Z",
        "email": "xyy@dsfs.com",
        "is_success": true
    }

    '''
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailSerializer

    def get_queryset(self):
        if self.action in ['list']:
            return self.queryset.get_success_emails()[:10]

        return self.queryset
