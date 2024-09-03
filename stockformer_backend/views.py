# from django.http import JsonResponse
# from .models import ModelObj
# from rest_framework.decorators import api_views

# @api_views('GET','POST')
# def model_list(request):

#     if request.method == 'GET':
#         model_objects = ModelObj.objects.all
#         return JsonResponse(model_objects)
#     if request.method =='POST':

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def interact(request):
    if request.method == 'GET':
        # Retrieve query parameters from the request
        symbol = request.query_params.get('symbol', None)
        prediction_length = request.query_params.get('prediction_length', None)
        
        # Dummy response for demonstration
        if symbol and prediction_length:
            return Response({
                "message": f"Received GET request with symbol: {symbol} and prediction_length: {prediction_length}. Returning Inference Response..."
            
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Missing parameters"
            }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        # Retrieve JSON body parameters from the request
        symbol = request.data.get('symbol')
        prediction_length = request.data.get('prediction_length')

        # Dummy response for demonstration
        if symbol and prediction_length:
            return Response({
                "message": f"Received POST request with symbol: {symbol} and prediction_length: {prediction_length}"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Missing parameters"
            }, status=status.HTTP_400_BAD_REQUEST)