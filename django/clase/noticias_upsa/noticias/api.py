from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from noticias.models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    autor = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "texto", "fecha_publicacion", "autor")
        model = Comentario


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def comentarios(request):

    if request.method == "GET":
        queryset = Comentario.objects.all()
        serializer = ComentarioSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comentario = Comentario(**serializer.validated_data)
            comentario.user = request.user
            comentario.save()

            response_serializer = ComentarioSerializer(comentario)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class ComentarioView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]
