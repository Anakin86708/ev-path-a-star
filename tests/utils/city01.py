# Road insersections
import pickle

from ev_path.nodes import StreetIntersectionNode

edges_roads = []


def insert_data():
    INCREMENT_X = 140
    INCREMENT_Y = 100
    roads_x = [
        'Taylor',
        'Mason',
        'Powell',
        'Stockton',
        'Grant',
        'Kearny',
        'Montgomery',
    ]
    roads_y = [
        'California',
        'Sacramento',
        'Clay',
    ]

    def ask_height(index_x, road_x, index_y, road_y):
        intersection_name = f'{road_x} X {road_y}'
        height = float(input(f'What is the height for {intersection_name}: '))
        return StreetIntersectionNode(intersection_name, index_x * INCREMENT_X, index_y * INCREMENT_Y, height)

    return [
        ask_height(index_x, road_x, index_y, road_y)
        for index_x, road_x in enumerate(roads_x)
        for index_y, road_y in enumerate(roads_y)
    ]


if __name__ == '__main__':
    heights = insert_data()
    with open('heights.pkl', 'wb') as file:
        pickle.dump(heights, file)
