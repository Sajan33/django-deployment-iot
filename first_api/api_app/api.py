from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from .serializers import *

class MonitorList(APIView):
    """In this class the APIView will look for some method that may be POST, GET, PUT, DELETE
    and this will give us the json format.""" 
    def get(self, request):
        """This method is used to get the data from the database in json format"""
        model = Monitor.objects.all() 
        serializer = MonitorSerializer(model, many=True)
        return Response(serializer.data)#Here, we are returning the api

    def post(self, request):
        """This method is used to post the data in the database"""
        serializer = MonitorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MonitorDetail(APIView):
    """In this class the APIView will look for some method that may be POST, GET, PUT, DELETE
    and this will give us the json format.""" 
    def get_user(self, temp_id):
        """This method is used to get the employee_id"""
        try:
            model = Monitor.objects.get(id=temp_id)
            return model
        except:
            return 

    def get(self, request, temp_id):
        """This method is used to get the data from the database in json format"""
        if not self.get_user(temp_id):
           return Response('User Not Found.', status=status.HTTP_404_NOT_FOUND)

        serializer = MonitorSerializer(self.get_user(temp_id))
        return Response(serializer.data)#Here, we are returning the api

    def put(self, request, temp_id):
        """This method is used to post the date in the database"""

        serializer = MonitorSerializer(self.get_user(temp_id), data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, temp_id):
        """This method is used to delete the particular id from database"""
        if not self.get_user(temp_id):
           return Response('User Not Found.', status=status.HTTP_404_NOT_FOUND)

        model = self.get_user(temp_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



