#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAGE_LINKS = [
    {'url':'index.html', 'title':'Inicio'},
    {'url':'about.html', 'title':'Nosotros'},
    {'url':'challenge.html', 'title':'El Desafío'},
    {'url':'leadership.html', 'title':'Programa de Liderazgo'},
    {'url':'alumni.html', 'title':'Alumni'},
    {'url':'allies.html', 'title':'Aliados'},
]

SOCIAL_LINKS = [
    {'icon':'fa-facebook', 'url':'https://www.facebook.com/ensenaxpanama'},
    {'icon':'fa-twitter', 'url':'https://twitter.com/ensenaxpanama'},
    {'icon':'fa-instagram', 'url':'https://instagram.com/ensenaxpanama/'},
]

SLIDER_IMAGE_LIST = [
    'assets/images/slider/Drobis_01.JPG',
    'assets/images/slider/Drobis_02.JPG',
    'assets/images/slider/Drobis_03.JPG',
    'assets/images/slider/Drobis_04.JPG',
    'assets/images/slider/Drobis_05.JPG'
]

HEADER_BACKGROUND = "assets/images/header-bg.jpg"

CONTACT_EMAIL = "info@ensenaporpanama.com"
CONTACT_PHONE = "+507 322 0437"
CONTACT_ADDRESS = "Edif. 909, Calle 74 con Calle 50, San Francisco"

def preBuildPage(site, page, context, data):
    context['header_background'] = HEADER_BACKGROUND
    context['header_links'] = PAGE_LINKS
    context['footer_links'] = [
        PAGE_LINKS[:len(PAGE_LINKS)/2],
        PAGE_LINKS[len(PAGE_LINKS)/2:],
    ]
    context['slider_image_list'] = SLIDER_IMAGE_LIST
    context['social_links'] = SOCIAL_LINKS
    context['contact_email'] = CONTACT_EMAIL
    context['contact_phone'] = CONTACT_PHONE
    context['contact_address'] = CONTACT_ADDRESS
    context['contact_email_link'] = "mailto:" + CONTACT_EMAIL
    context['contact_phone_link'] = "tel:" + CONTACT_PHONE.replace(" ", "")
    return context, data
