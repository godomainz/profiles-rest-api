from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list APIView features"""
        an_apiview = ['Uses HTTP methods as function (get,pot,patch,put,delete)',
                      'Is similar toa traditional Django views',
                      'Gives you the most control over you application logic',
                      'Is mapped manually to URLs'
                      ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})