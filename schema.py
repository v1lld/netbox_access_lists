import strawberry
from strawberry import auto
from strawberry.django import type as django_type
from . import filtersets, models

# Объектные типы

@django_type(models.AccessList)
class AccessListType:
    id: strawberry.ID
    name: str
    default_action: str = auto
    comments: str = auto

@django_type(models.AccessListRule)
class AccessListRuleType:
    id: strawberry.ID
    index: int
    protocol: str = auto
    action: str = auto
    description: str = auto

# Запросы

@strawberry.type
class Query:
    access_list: AccessListType = strawberry.field(resolver=lambda: models.AccessList.objects.first())
    access_list_list: list[AccessListType] = strawberry.field(resolver=lambda: list(models.AccessList.objects.all()))
    access_list_rule: AccessListRuleType = strawberry.field(resolver=lambda: models.AccessListRule.objects.first())
    access_list_rule_list: list[AccessListRuleType] = strawberry.field(resolver=lambda: list(models.AccessListRule.objects.all()))

# Создание схемы

schema = strawberry.Schema(query=Query)
