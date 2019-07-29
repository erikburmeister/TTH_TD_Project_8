def alphabet_upper(request):
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z'
    ]

    return {'alphabet_upper': alphabet}


def mineral_groups(request):
    groups = [
        'Silicates', 'Oxides', 'Sulfates', 'Sulfides', 'Carbonates',
        'Halides', 'Sulfosalts', 'Phosphates', 'Borates',
        'Organic Minerals', 'Arsenates', 'Native Elements', 'Other'
    ]

    return {'mineral_groups': groups}


def mineral_diaphaneity(request):
    diaphaneity = [
        'Transparent', 'Semitransparent', 'Subtransparent',
        'Translucent', 'Semitranslucent', 'Subtranslucent',
        'Opaque'
    ]

    return {'mineral_diaphaneity': diaphaneity}