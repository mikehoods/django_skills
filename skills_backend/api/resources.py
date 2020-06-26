from tastypie.resources import ModelResource
from api.models import Skill

class SkillResource(ModelResource):
    class Meta:
        queryset = Skill.objects.all()
        resource_name = 'skill'