import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import Courier
from .serializers import CourierSerializer


@csrf_exempt  # отключаем CSRF для простоты (убери, если хочешь защиту)
def courier_list(request):
    if request.method == 'GET':
        couriers = Courier.objects.all()
        serializer = CourierSerializer(couriers, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CourierSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def courier_detail(request, pk):
    try:
        courier = Courier.objects.get(pk=pk)
    except Courier.DoesNotExist:
        return JsonResponse({'error': 'Courier not found'}, status=404)

    if request.method == 'GET':
        serializer = CourierSerializer(courier)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CourierSerializer(courier, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        courier.delete()
        return JsonResponse({'message': 'Courier deleted'}, status=204)

    return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])



