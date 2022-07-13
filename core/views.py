from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.models import Editora

from core.serializers import CategoriaSerializer
from core.serializers import EditoraSerializer



class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

 