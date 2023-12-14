import numpy as np
import pandas as pd
import json
from shapely import geometry
from pathlib import Path
import rasterio as rio

shape_fpath = Path("/home/abhisek/Documents/train/via_region_data.json")
aoi_df = pd.DataFrame(columns=('FileName', 'Polygon', 'ClassName'))
with open(shape_fpath) as json_file:
    annotations = json.load(json_file) 
    for fkey in annotations.keys():
        fregions = annotations[fkey]['regions']
        if isinstance(fregions, list):
            labeled_aois = [
                (
                    fkey, 
                    geometry.Polygon(
                        list(
                            zip(
                                r['shape_attributes']['all_points_x'], 
                                r['shape_attributes']['all_points_y']
                            )
                        )
                    ), 
                    list(r['region_attributes']['name'].keys())[0]
                )
                for r in fregions
            ]
            fdf = pd.DataFrame(labeled_aois, columns=('FileName', 'Polygon', 'ClassName'))
            aoi_df = pd.concat((aoi_df, fdf), ignore_index=True)

u_class = set(aoi_df['ClassName'].tolist())
u_files = set(aoi_df['FileName'].tolist())

label_map = {'nodata': 0}
l = 1
for c in u_class:
    label_map[c] = l
    l += 1
    
    
    def pixel_check(x, y, a_polygon, true_val=True, false_val=False):
        if a_polygon.contains(geometry.Point(x, y)):
            return true_val
        else:
            return false_val
    image_check = np.vectorize(pixel_check, excluded=['a_polygon', 'true_val', 'false_val'])
    def create_image_mask(a_polygon, class_name, img_shape):
        assert isinstance(img_shape, tuple) and len(img_shape) == 2
        r, c = img_shape
        r_grid, c_grid = np.meshgrid(np.arange(r), np.arange(c))
        image_mask = image_check(
            a_polygon=a_polygon, 
            x=r_grid, 
            y=c_grid, 
            true_val=label_map[class_name], 
            false_val=label_map['nodata']
        )
        return image_mask