from django.shortcuts import render
from rest_framework import response,status
from rest_framework.decorators import api_view,permission_classes
from api.serializer import SheduleSerializers
from base.models import Shedule
from base.services import create_shedule as create_shedule_service
from django.core.exceptions import PermissionDenied
from api.permissions import IsOwner,IsAuthoenticated


@permission_classes([IsOwner])
@api_view(['GET'])
def get_shedule(request,id):
    shedule = Shedule.objects.filter(id=id).first()
    if shedule is None:
        return response.Response({},status=status.HTTP_404_NOT_FOUND)
    shedule_data = SheduleSerializers(shedule)
    return response.Response(shedule_data.data,status=status.HTTP_200_OK)


@permission_classes([IsAuthoenticated])
@api_view(['GET'])
def get_all_shedule(request,id):
    shedule = Shedule.objects.all()
    if shedule is None:
        return response.Response({},status=status.HTTP_404_NOT_FOUND)
    shedule_data = SheduleSerializers(shedule,many=True)
    return response.Response(shedule_data.data,status=status.HTTP_200_OK)


@permission_classes([IsAuthoenticated])
@api_view(['POST'])
def create_shedule(request):
    title = request.data['title'].strip()
    if len(title)<1 or len(title)>20:
        return response.Response({'message':'not a valid priority'},status=status.HTTP_400_BAD_REQUEST)
    
    description=request.data['description'].strip()
    if len(description)<1 or len(description)>500:
        return response.Response({'message':'not a valid priority'},status=status.HTTP_400_BAD_REQUEST)
    
    priority = request.data['priority']
    if int(priority)<1 or int(priority)>3:
        return response.Response({'message':'not a valid priority'},status=status.HTTP_400_BAD_REQUEST)

    create_shedule_service(request.user,title,description,priority)
    return response.Response({},status=status.HTTP_201_CREATED)


@permission_classes([IsOwner])
@api_view(['PUT','PATCH','POST'])
def update_shedule(request,id):
    shedule = Shedule.objects.filter(id=id).first()
    if shedule is None:
        return response.Response({},status=status.HTTP_404_NOT_FOUND)
    
    shedule_data = SheduleSerializers(shedule,data=request.data,partial=True)
    shedule_data.is_valid(raise_exception=True)
    shedule_data.save()
    return response.Response(shedule_data.data,status=status.HTTP_200_OK)


@permission_classes([IsOwner])
@api_view(['DELETE'])
def delete_shedule(request,id):
    shedule = Shedule.objects.filter(id=id).first()
    if shedule is None:
        return response.Response({},status=status.HTTP_404_NOT_FOUND)
    
    shedule.delete()
    return response.Response({},status=status.HTTP_204_NO_CONTENT)
