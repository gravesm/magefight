from fight.models import Mage, Spell, Fight
from fight.serializers import MageSerializer, FightSerializer, SpellSerializer
from rest_framework import generics


class MageList(generics.ListCreateAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer


class MageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer


class SpellList(generics.ListCreateAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer


class SpellDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer


class FightList(generics.ListCreateAPIView):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer


class FightDetail(generics.RetrieveAPIView):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer
