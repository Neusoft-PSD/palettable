from .colorbrewer import _load_maps_by_type

globals().update(_load_maps_by_type('qualitative'))
