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

def preBuildPage(site, page, context, data):
    context['header_background'] = "assets/images/header-bg.jpg"
    context['header_links'] = PAGE_LINKS
    context['footer_links'] = [
        PAGE_LINKS[:len(PAGE_LINKS)/2],
        PAGE_LINKS[len(PAGE_LINKS)/2:],
    ]
    return context, data
