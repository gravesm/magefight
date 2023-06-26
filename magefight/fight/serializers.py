import random

from rest_framework import serializers
from fight.models import Mage, Spell, Fight


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = ["id", "name"]


class MageSerializer(serializers.ModelSerializer):
    spell_list = SpellSerializer(many=True, read_only=True, source="spells")

    class Meta:
        model = Mage
        fields = ["id", "name", "spells", "spell_list"]


class FightSerializer(serializers.ModelSerializer):
    winner = MageSerializer(read_only=True)

    class Meta:
        model = Fight
        fields = ["id", "mages", "winner"]

    def create(self, validated_data):
        mages = validated_data["mages"]
        random.shuffle(mages)
        fight = Fight(
            winner=mages[0]
        )
        fight.save()
        fight.mages.add(*validated_data["mages"])
        fight.save()
        return fight
