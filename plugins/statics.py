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

HEADER_BACKGROUND = "assets/images/header-bg.jpg"

def preBuildPage(site, page, context, data):
    context['header_background'] = HEADER_BACKGROUND
    context['header_links'] = PAGE_LINKS
    context['footer_links'] = [
        PAGE_LINKS[:len(PAGE_LINKS)/2],
        PAGE_LINKS[len(PAGE_LINKS)/2:],
    ]
    context['social_links'] = SOCIAL_LINKS
    return context, data
