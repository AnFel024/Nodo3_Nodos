from django.http import response

from equipo.Nodo import getValue, setValue

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

import requests
import json

headers = {
    "Content-Type":"application/json",
    "X-Frame-Options":"DENY",
    "X-Content-Type-Options":"nosniff"
    }

class setNodoValue(APIView):
    def get(self, request, *args, **kwargs):
        value = kwargs.get('value',0)
        setValue(value=value)

        return Response({
            '192.168.0.7:8014': getValue()
            }, status=status.HTTP_200_OK)

class getNodoValue(APIView):
    def get(self, request, *args, **kwargs):
        value = getValue()
        print(value)
        return Response({
            '192.168.0.7:8014': value
            }, status=status.HTTP_200_OK)

class sumaNodos(APIView):
    def get(self, request, *args, **kwars):

        pairList = [
            '192.168.0.7:8010',
            '192.168.0.7:8011',
            '192.168.0.7:8012',
            '192.168.0.7:8013',
            '192.168.0.7:8014',
            '192.168.0.7:8015',]

        try:
            values = {}
            for web in pairList:
                url = f'http://{web}/api/getValue'
                try:
                    response = requests.request('GET', url, headers=headers, verify=False)
                    
                    data = json.loads(response.text)
                    if response.status_code == status.HTTP_200_OK:
                        values.update(data)
                    
                except Exception as e:
                    values[web] = 'El nodo no se encontraba disponible.'
                    
                print(values)

            r=0
            disable_nodes = []

            for key, value in zip(values.keys(), values.values()):
                if (type(value) == int):
                    r = r + value
                else:
                    disable_nodes.append(key)

            return Response({
                'resultado': r,
                'nodos_inhabilitados': disable_nodes    
            })

        except Exception as e:
                return Response({
                    'message': f'Ha habido un error: {e}'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
