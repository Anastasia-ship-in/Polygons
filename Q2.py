from shapely.geometry import Polygon, box
from shapely.ops import unary_union


def calculate_x_area():
    polygon1 = Polygon([(7, 5), (9, 5), (9, 6), (7, 6)])
    polygon2 = Polygon([(1, 2), (1, 1), (9, 1), (9, 4.5), (8, 4.5), (8, 2)])
    polygon3 = Polygon([(1, 2), (2, 2), (2, 5), (1, 5)])
    polygon4 = Polygon([(1, 5), (6, 5), (6, 6), (1, 6)])

    polygons = [polygon1.buffer(0), polygon2.buffer(0), polygon3.buffer(0), polygon4.buffer(0)]

    union_polygons = unary_union(polygons)
    minx, miny, maxx, maxy = union_polygons.bounds
    outer_rect = box(minx, miny, maxx, maxy)
    inner_area_polygon = outer_rect.difference(union_polygons)

    return inner_area_polygon.area


x_area = calculate_x_area()
print(f"The calculated area of the 'X' region is: {x_area}")