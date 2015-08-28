from django.template import Context
from django.template.loader import get_template
from django.template.loader_tags import BlockNode, ExtendsNode

IMAGE_LIST = [
    'assets/images/slider/Drobis_01.JPG',
    'assets/images/slider/Drobis_02.JPG',
    'assets/images/slider/Drobis_03.JPG',
    'assets/images/slider/Drobis_04.JPG',
    'assets/images/slider/Drobis_05.JPG'
]

def preBuildPage(site, page, context, data):
    context['slider_image_list'] = IMAGE_LIST
    return context, data
