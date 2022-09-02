from online_store.api.common.mixin import NestedCreateMixin, NestedUpdateMixin
from rest_framework import  serializers


class WritableNestedModelSerializer(NestedCreateMixin, NestedUpdateMixin, serializers.ModelSerializer):
    pass