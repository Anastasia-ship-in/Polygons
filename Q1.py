from shapely.geometry import LineString, Polygon


def create_rectangle(seg1, seg2):
    line1 = LineString(seg1)
    line2 = LineString(seg2)

    minx1, miny1, maxx1, maxy1 = line1.bounds
    minx2, miny2, maxx2, maxy2 = line2.bounds

    if miny1 == maxy1 and miny2 == maxy2:
        if minx1 > maxx2 or minx2 > maxx1:
            return None

        rect_miny = min(miny1, miny2)
        rect_maxy = max(maxy1, maxy2)
        rect_minx = max(minx1, minx2)
        rect_maxx = min(maxx1, maxx2)

    elif minx1 == maxx1 and minx2 == maxx2:
        if miny1 > maxy2 or miny2 > maxy1:
            return None

        rect_minx = min(minx1, minx2)
        rect_maxx = max(maxx1, maxx2)
        rect_miny = max(miny1, miny2)
        rect_maxy = min(maxy1, maxy2)

    else:
        return None

    rectangle = Polygon([(rect_minx, rect_miny), (rect_maxx, rect_miny),
                         (rect_maxx, rect_maxy), (rect_minx, rect_maxy)])

    return rectangle


def rectangle_dimensions(rect):
    minx, miny, maxx, maxy = rect.bounds

    length = maxx - minx
    width = maxy - miny

    return length, width


def calculate_distance(rect1, rect2):
    if rect1 is None or rect2 is None:
        return None

    distance = rect1.distance(rect2)
    return distance


rectangles = []

# rectangle 1
seg1 = [(0, 1), (7, 1)]
seg2 = [(1, 0), (6, 0)]

polygon_1 = create_rectangle(seg1, seg2)
if polygon_1:
    rectangles.append(polygon_1)

# rectangle 2
seg1 = [(1, -3), (6, -3)]
seg2 = [(1, -4), (5, -4)]

polygon_2 = create_rectangle(seg1, seg2)
if polygon_2:
    rectangles.append(polygon_2)

# rectangle 3
seg1 = [(3, -6), (5, -6)]
seg2 = [(3, -7), (5, -7)]

polygon_3 = create_rectangle(seg1, seg2)
if polygon_3:
    rectangles.append(polygon_3)

count_width_1 = sum(1 for rect in rectangles if rectangle_dimensions(rect)[1] == 1)


print(f"Count of rectangle polygons* with a width of 1 unit (between lines): {count_width_1}")

for i, rect in enumerate(rectangles, start=1):
    cords = rect.bounds
    length, width = rectangle_dimensions(rect)
    print(f"Rectangle {i}: coordinates: {cords}, length: {length}, width: {width}")

print(f"Distance between Rectangle 1 and Rectangle 2: {calculate_distance(polygon_1, polygon_2)} and between "
      f"Rectangle 2 and Rectangle 3: {calculate_distance(polygon_2, polygon_3)}")


