from PIL import Image, ImageDraw
import csv
import os

#Convert min/max set of coordinates to min/max set of pixels of image
def convert_minmax(row):
    lat_coor = hei - (float(row[0]) - min_lat) / (max_lat - min_lat) * (hei - 0) + 0
    lon_coor = (float(row[1]) - min_lon) / (max_lon - min_lon) * (wid - 0) + 0
    return lat_coor, lon_coor

#Visualize points from csv onto map with trace of coordinates
def create_map(path, csv_path, final_map_path, coords):

    global min_lat, max_lat, min_lon, max_lon
    min_lat = coords[0]
    max_lat = coords[1]
    min_lon = coords[2]
    max_lon = coords[3]

    img = Image.open(path)
    global wid, hei
    wid, hei = img.size # Width and height of image in pixles
    f_const = 10 # Cirlce size constant

    file = open(csv_path, 'r', newline='')
    reader = csv.reader(file)

    img_points = []
    start_point = []
    end_point = []

    reader_list = list(reader)

    # Convert all points in list and add to img_points
    for i, row in enumerate(reader_list):
        if i == 0:
            lat_coor, lon_coor = convert_minmax(row)
            start_point.append([lon_coor, lat_coor])
        elif i == len(reader_list) - 1:
            lat_coor, lon_coor = convert_minmax(row)
            end_point.append([lon_coor, lat_coor])
        else:
            lat_coor, lon_coor = convert_minmax(row)
            img_points.append([lon_coor, lat_coor])

    draw = ImageDraw.Draw(img)

    #Draw line for image points and circle with color for flag points
    for i in range(len(img_points) - 1):
        if img_points[i+1]:
            line = img_points[i][0], img_points[i][1], img_points[i+1][0], img_points[i+1][1]
            draw.line(line, fill=(0,0,255), width=4)
        else:
            break

    for flag in start_point: #Draw start circle
        draw.ellipse((flag[0]-f_const, flag[1]-f_const, flag[0]+f_const, flag[1]+f_const), fill='green', outline=(0,0,0))

    for flag in end_point: #Draw end circle
        draw.ellipse((flag[0]-f_const, flag[1]-f_const, flag[0]+f_const, flag[1]+f_const), fill='red', outline=(0,0,0))

    img.save(final_map_path)
    os.remove(path)
