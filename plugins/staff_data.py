#!/usr/bin/env python
# -*- coding: utf-8 -*-

STAFF_DATA = [
    {
        'name': 'Lorena Valencia',
        'photo': 'assets/images/staff/lorena_valencia.jpg' ,
        'tagline': 'Directora Ejecutiva y Co-Fundadora',
    },
    {
        'name': 'David Alexander Bernal Díaz',
        'photo': 'assets/images/staff/david_bernal.jpg',
        'tagline': 'Director de Reclutamiento, Selección y Colocación',
    },
    {
        'name': 'Daniel McKee',
        'photo': 'assets/images/staff/dan_mckee.jpg',
        'tagline': 'Director de Formación y Apoyo',
    },
    {
        'name': 'Julio Germán Arias Castillo',
        'photo': 'assets/images/staff/julio_german.jpg',
        'tagline': 'Director de Relaciones Públicas Internacionales',
    },
    {
        'name': 'Marisa Arias',
        'photo': 'assets/images/staff/marisa_arias.jpg',
        'tagline': 'Directora',
    },
    {
        'name': 'Jorge Arosemena',
        'photo': 'assets/images/staff/jorge_arosemena.jpg',
        'tagline': 'Director',
    },
    {
        'name': 'Julio Escobar Villarué',
        'photo': 'assets/images/staff/julio_escobar.jpg',
        'tagline': 'Asesor',
    },
    {
        'name': 'Marta Amorós',
        'photo': 'assets/images/staff/marta_amoros.jpg',
        'tagline': 'Tutora',
    },
    {
        'name': 'Mercedes Gaitán',
        'photo': 'assets/images/staff/mercedes_gaitan.jpg',
        'tagline': 'Tutora',
    }
]

# Adds extra attributes programatically to the staff items.
def parse_staff_data(index, item):

    #Adds a link-able ID to the object, used for anchors
    item['link'] = item['name'].lower().replace(" ", "")

    # Return the item
    return item

# Executed before the page is built
def preBuildPage(site, page, context, data):

    # Iterates through the entire STAFF_DATA list, and executes the 'parse_staff_data' function
    parsed_data =  map(
        parse_staff_data,
        range(len(STAFF_DATA)),
        STAFF_DATA
    )

    # Pass the data to the template
    context['staff_data'] = parsed_data

    return context, data
