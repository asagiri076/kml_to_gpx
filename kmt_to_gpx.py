#!usr/bin/python3

import xml.etree.ElementTree as ET
import sys
from datetime import datetime, timedelta


def kml_to_gpx(kml_file_path, gpx_file_path):
    # KMLファイルの読み込み
    tree = ET.parse(kml_file_path)
    root = tree.getroot()

    # 名前空間の定義
    ns = {
        'kml': 'http://www.opengis.net/kml/2.2',
        'gx': 'http://www.google.com/kml/ext/2.2'
    }

    # GPXファイルのヘッダー部分
    gpx = ET.Element('gpx', version="1.1", creator="ExampleCreator")
    trk = ET.SubElement(gpx, 'trk')
    trkseg = ET.SubElement(trk, 'trkseg')

    # KML内のすべてのPlacemarkをループ
    for placemark in root.findall('.//kml:Placemark', ns):
        timespan = placemark.find('.//kml:TimeSpan', ns)
        begin = timespan.find(
            'kml:begin', ns).text if timespan is not None else None
        end = timespan.find(
            'kml:end', ns).text if timespan is not None else None

        # Pointの座標取得
        point = placemark.find('.//kml:Point/kml:coordinates', ns)
        if point is not None:
            parse_coordinates(point.text, trkseg, begin, end)

        # LineStringの座標取得
        linestring = placemark.find('.//kml:LineString/kml:coordinates', ns)
        if linestring is not None:
            parse_coordinates(linestring.text, trkseg, begin, end)

    # 生成したGPXデータの保存
    tree = ET.ElementTree(gpx)
    tree.write(gpx_file_path, encoding='utf-8', xml_declaration=True)


def parse_coordinates(coordinates_text, trkseg, begin, end):
    # 座標のパースとGPXへの追加
    coords = coordinates_text.strip().split()
    begin_time = datetime.fromisoformat(begin[:-1])
    end_time = datetime.fromisoformat(end[:-1])
    if len(coords) > 1:
        delta = (end_time - begin_time) / len(coords)
    else:
        delta = timedelta(0)

    for i, coord in enumerate(coords):
        lon, lat, ele = coord.split(',')
        trkpt = ET.SubElement(trkseg, 'trkpt', lat=lat, lon=lon)
        ele_tag = ET.SubElement(trkpt, 'ele')
        ele_tag.text = ele
        if begin:
            time = begin_time + delta * i
            timetag = ET.SubElement(trkpt, 'time')
            timetag.text = time.isoformat()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py input.kml output.gpx")
    else:
        kml_file = sys.argv[1]
        gpx_file = sys.argv[2]
        kml_to_gpx(kml_file, gpx_file)
