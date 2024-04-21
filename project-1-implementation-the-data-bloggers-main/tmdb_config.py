
def tmdb_collection_mappings(key):
    tmdb_collection_map = {
        'overview': 'overview',
        'name' : 'name',
        'type': 'show_details.type',
        'tagline' : 'show_details.tagline',
        'status' : 'show_details.status',
        'languages' : 'show_details.languages',
        'origin_country': 'show_details.origin_country',
        'production_companies': 'show_details.production_companies',
        'created_by': 'show_details.created_by',
        'episode_run_time': 'show_details.episode_run_time',
        'generas' : 'show_details.generas',
        'production_countries' : 'show_details.production_countries'
    }

    return tmdb_collection_map[key]
