from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Courier
from .serializers import CourierSerializer


# Чтобы убрать декораторы @csrf_exempt, оставим как есть или будем ставить явно. Можно убрать, если включена настройка CSRF.

@method_decorator(csrf_exempt, name='dispatch')
def courier_list(request):
    """
    GET - вернуть список всех курьеров
    POST - создать нового курьера
    """
    if request.method == 'GET':
        couriers = Courier.objects.all()
        serializer = CourierSerializer(couriers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CourierSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@method_decorator(csrf_exempt, name='dispatch')
def courier_detail(request, pk):
    """
    GET - получить курьера по id
    PUT - обновить курьера
    DELETE - удалить курьера
    """
    try:
        courier = Courier.objects.get(pk=pk)
    except Courier.DoesNotExist:
        return JsonResponse({'error': 'Courier not found'}, status=404)

    if request.method == 'GET':
        serializer = CourierSerializer(courier)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CourierSerializer(courier, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        courier.delete()
        return JsonResponse({'message': 'Courier deleted'}, status=204)

    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

# Create your views here.
