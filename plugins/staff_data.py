#!/usr/bin/env python
# -*- coding: utf-8 -*-

STAFF_DATA = [
    {
        'name': 'Lorena Valencia',
        'photo': 'assets/images/staff/lorena_valencia.jpg' ,
        'tagline': 'Directora Ejecutiva y Co-Fundadora',
        'social_links': [
            {'icon': 'fa-facebook', 'url': "#"},
            {'icon': 'fa-twitter', 'url': "#"},
            {'icon': 'fa-linkedin', 'url': "#"}
        ]
    },
    {
        'name': 'David Alexander Bernal Díaz',
        'photo': 'assets/images/staff/david_bernal.jpg',
        'tagline': 'Director de Reclutamiento, Selección y Colocación',
        'social_links': [
            {'icon': 'fa-facebook', 'url': "#"},
            {'icon': 'fa-twitter', 'url': "#"},
            {'icon': 'fa-linkedin', 'url': "#"}
        ]
    },
    {
        'name': 'Daniel McKee',
        'photo': 'assets/images/staff/dan_mckee.jpg',
        'tagline': 'Director de Formación y Apoyo',
        'social_links': [
            {'icon': 'fa-facebook', 'url': "#"},
            {'icon': 'fa-twitter', 'url': "#"},
            {'icon': 'fa-linkedin', 'url': "#"}
        ]
    },
    {
        'name': 'Julio Germán Arias Castillo',
        'photo': 'assets/images/staff/julio_german.jpg',
        'tagline': 'Director de Relaciones Públicas Internacionales',
        'social_links': [
            {'icon': 'fa-facebook', 'url': "#"},
            {'icon': 'fa-twitter', 'url': "#"},
            {'icon': 'fa-linkedin', 'url': "#"}
        ]
    },
    {
        'name': 'Marisa Arias',
        'photo': 'assets/images/staff/david_bernal.jpg',
        'tagline': 'Directora',
        'social_links': [
            {'icon': 'fa-facebook', 'url': "#"},
            {'icon': 'fa-twitter', 'url': "#"},
            {'icon': 'fa-linkedin', 'url': "#"}
        ]
    },
    {
        'name': 'Jorge Arosemena',
        'photo': 'assets/images/staff/jorge_arosemena.jpg',
        'tagline': 'Director',
        'social_links': [
            {'icon': 'fa-facebook', 'url': "#"},
            {'icon': 'fa-twitter', 'url': "#"},
            {'icon': 'fa-linkedin', 'url': "#"}
        ]
    },
    {
        'name': 'Julio Escobar Villarué',
        'photo': 'assets/images/staff/julio_escobar.jpg',
        'tagline': 'Asesor',
        'social_links': [
            {'icon': 'fa-facebook', 'url': "#"},
            {'icon': 'fa-twitter', 'url': "#"},
            {'icon': 'fa-linkedin', 'url': "#"}
        ]
    },
]


def preBuildPage(site, page, context, data):

    def generate_alt_class(index, item):
        if (index % 4)  > 1:
            item['extra_classes'] = 'staff-item-alt'
        return item

    # Iterates through the entire STAFF_DATA list, and adds extra classes if necessary
    context['staff_data'] = map(
        generate_alt_class,
        range(len(STAFF_DATA)),
        STAFF_DATA
    )
    
    return context, data
