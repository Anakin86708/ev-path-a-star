# Road insersections
import os
import pickle

from ev_path.edges import StreetEdge
from ev_path.nodes import StreetIntersectionNode

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

FILENAME_HEIGHTS = os.path.join(WORKING_DIR, 'heights.pkl')


def load_nodes():
    with open(FILENAME_HEIGHTS, 'rb') as f:
        return pickle.load(f)


nodes = {node.name: node for node in load_nodes()}
edges_roads = [
    StreetEdge(nodes['Leavenworth X California'], nodes['Leavenworth X Sacramento'], 105.5),
    StreetEdge(nodes['Leavenworth X California'], nodes['Jones X California'], 146.9),

    StreetEdge(nodes['Leavenworth X Sacramento'], nodes['Leavenworth X California'], 105.5),
    StreetEdge(nodes['Leavenworth X Sacramento'], nodes['Leavenworth X Clay'], 100.3),

    StreetEdge(nodes['Leavenworth X Clay'], nodes['Leavenworth X Sacramento'], 100.3),
    StreetEdge(nodes['Leavenworth X Clay'], nodes['Leavenworth X Washington'], 101.6),
    StreetEdge(nodes['Leavenworth X Clay'], nodes['Leavenworth X Jones'], 148.5),

    StreetEdge(nodes['Leavenworth X Washington'], nodes['Leavenworth X Clay'], 101.6),
    StreetEdge(nodes['Leavenworth X Washington'], nodes['Leavenworth X Jackson'], 100),  # shuld be 98.6
    StreetEdge(nodes['Leavenworth X Washington'], nodes['Leavenworth X Jones'], 146.7),

    StreetEdge(nodes['Jones X California'], nodes['Leavenworth X California'], 146.9),

]


def insert_data():
    INCREMENT_X = 140
    INCREMENT_Y = 100
    roads_x = [
        'Leavenworth',
        'Jones',
        'Taylor',
        'Mason',
        'Powell',
        'Stockton',
        'Grant',
        'Kearny',
    ]
    roads_y = [
        'California',
        'Sacramento',
        'Clay',
        'Washington',
        'Jackson',
        'Pacific Ave',
        'Broadway',
        'Valejo'
    ]

    skiping_intersections = [
        'Grant X Valejo'
        'Kearny X Valejo',
        'Kearny X Broadway',
    ]

    aditional_intersections = [
        'Columbus Ave X Valejo',
    ]

    def ask_height(index_x, road_x, index_y, road_y):
        intersection_name = f'{road_x} X {road_y}'
        if intersection_name in skiping_intersections: return None
        height = float(input(f'What is the height for {intersection_name}: '))
        return StreetIntersectionNode(intersection_name, index_x * INCREMENT_X, index_y * INCREMENT_Y, height)

    def ask_height_aditional(intersection_name: str):
        road_x = float(input(f'What is the x position for {intersection_name}: '))
        road_y = float(input(f'What is the y position for {intersection_name}: '))
        height = float(input(f'What is the height for {intersection_name}: '))
        return StreetIntersectionNode(intersection_name, road_x, road_y, height)

    heights_grid = list(filter(lambda x: x is not None,
                               [ask_height(index_x, road_x, index_y, road_y) for index_x, road_x in enumerate(roads_x)
                                for
                                index_y, road_y in enumerate(roads_y)]
                               ))
    heights_aditional = [ask_height_aditional(intersection_name) for intersection_name in aditional_intersections]

    return heights_grid.extend(heights_aditional)


if __name__ == '__main__':
    heights = insert_data()
    with open(FILENAME_HEIGHTS, 'wb') as file:
        pickle.dump(heights, file)
