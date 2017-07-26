from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import Ticket, File
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    parser_classes = (MultiPartParser,)

    def create(self, request):
        queryset = self.get_queryset()

        _file = request.data.getlist('files__file')
        _name = request.data.getlist('files__name')
        n_files = len(_file)

        # con el n_files puedes comprobar que el numero de file es el correcto
        # o mostrar un error.


        serializer = self.get_serializer_class()(data=request.data, context={'request': request})
        if serializer.is_valid():

            files = [] # Almacena todos los files si pasa tu validacion
            for x in _file:
                obj_file = File()
                obj_file.name = _name[len(files)]
                obj_file.file = x
                files.append(obj_file)
                obj_file.save()


            ticket = serializer.save()
            ticket.files.set(files)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
           
