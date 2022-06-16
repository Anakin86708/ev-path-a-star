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
    # Leavenworth to N San Francisco
    StreetEdge(nodes['Leavenworth X California'], nodes['Leavenworth X Sacramento'], 105.5),
    StreetEdge(nodes['Leavenworth X California'], nodes['Jones X California'], 146.9),

    StreetEdge(nodes['Leavenworth X Sacramento'], nodes['Leavenworth X California'], 105.5),
    StreetEdge(nodes['Leavenworth X Sacramento'], nodes['Leavenworth X Clay'], 100.3),

    StreetEdge(nodes['Leavenworth X Clay'], nodes['Leavenworth X Sacramento'], 100.3),
    StreetEdge(nodes['Leavenworth X Clay'], nodes['Leavenworth X Washington'], 101.6),
    StreetEdge(nodes['Leavenworth X Clay'], nodes['Jones X Clay'], 151.8),

    StreetEdge(nodes['Leavenworth X Washington'], nodes['Leavenworth X Clay'], 101.6),
    StreetEdge(nodes['Leavenworth X Washington'], nodes['Leavenworth X Jackson'], 100.5),
    StreetEdge(nodes['Leavenworth X Washington'], nodes['Jones X Washington'], 151.1),

    StreetEdge(nodes['Leavenworth X Jackson'], nodes['Leavenworth X Washington'], 100.5),
    StreetEdge(nodes['Leavenworth X Jackson'], nodes['Leavenworth X Pacific Ave'], 100.2),

    StreetEdge(nodes['Leavenworth X Pacific Ave'], nodes['Leavenworth X Jackson'], 100.2),
    StreetEdge(nodes['Leavenworth X Pacific Ave'], nodes['Leavenworth X Broadway'], 100.3),
    StreetEdge(nodes['Leavenworth X Pacific Ave'], nodes['Jones X Pacific Ave'], 146.1),

    StreetEdge(nodes['Leavenworth X Broadway'], nodes['Leavenworth X Pacific Ave'], 100.3),
    StreetEdge(nodes['Leavenworth X Broadway'], nodes['Leavenworth X Valejo'], 118.1),
    StreetEdge(nodes['Leavenworth X Broadway'], nodes['Jones X Broadway'], 145.4),

    StreetEdge(nodes['Leavenworth X Valejo'], nodes['Leavenworth X Broadway'], 118.1),
    StreetEdge(nodes['Leavenworth X Valejo'], nodes['Jones X Valejo'], 149.8),

    # Jones to N San Francisco
    StreetEdge(nodes['Jones X California'], nodes['Leavenworth X California'], 146.9),
    StreetEdge(nodes['Jones X California'], nodes['Jones X Sacramento'], 102.2),
    StreetEdge(nodes['Jones X California'], nodes['Taylor X California'], 147.4),

    StreetEdge(nodes['Jones X Sacramento'], nodes['Jones X California'], 102.2),
    StreetEdge(nodes['Jones X Sacramento'], nodes['Leavenworth X Sacramento'], 147.1),
    StreetEdge(nodes['Jones X Sacramento'], nodes['Jones X Clay'], 100.3),

    StreetEdge(nodes['Jones X Clay'], nodes['Jones X Sacramento'], 100.3),
    StreetEdge(nodes['Jones X Clay'], nodes['Taylor X Clay'], 145.8),
    StreetEdge(nodes['Jones X Clay'], nodes['Jones X Washington'], 101.6),

    StreetEdge(nodes['Jones X Washington'], nodes['Jones X Clay'], 101.6),
    StreetEdge(nodes['Jones X Washington'], nodes['Taylor X Washington'], 144.6),
    StreetEdge(nodes['Jones X Washington'], nodes['Jones X Jackson'], 100.4),

    StreetEdge(nodes['Jones X Jackson'], nodes['Jones X Washington'], 100.4),
    StreetEdge(nodes['Jones X Jackson'], nodes['Leavenworth X Jackson'], 148.9),
    StreetEdge(nodes['Jones X Jackson'], nodes['Jones X Pacific Ave'], 101.6),

    StreetEdge(nodes['Jones X Pacific Ave'], nodes['Jones X Jackson'], 101.6),
    StreetEdge(nodes['Jones X Pacific Ave'], nodes['Leavenworth X Pacific Ave'], 148.9),
    StreetEdge(nodes['Jones X Pacific Ave'], nodes['Taylor X Pacific Ave'], 145.6),
    StreetEdge(nodes['Jones X Pacific Ave'], nodes['Jones X Broadway'], 100.5),

    StreetEdge(nodes['Jones X Broadway'], nodes['Jones X Pacific Ave'], 100.5),
    StreetEdge(nodes['Jones X Broadway'], nodes['Leavenworth X Broadway'], 148.9),
    StreetEdge(nodes['Jones X Broadway'], nodes['Taylor X Broadway'], 148.7),
    StreetEdge(nodes['Jones X Broadway'], nodes['Jones X Valejo'], 117.1),

    StreetEdge(nodes['Jones X Valejo'], nodes['Jones X Broadway'], 117.1),
    StreetEdge(nodes['Jones X Valejo'], nodes['Leavenworth X Valejo'], 149.8),

    # Taylor to N San Francisco
    StreetEdge(nodes['Taylor X California'], nodes['Jones X California'], 147.4),
    StreetEdge(nodes['Taylor X California'], nodes['Mason X California'], 144.9),
    StreetEdge(nodes['Taylor X California'], nodes['Taylor X Sacramento'], 102.3),

    StreetEdge(nodes['Taylor X Sacramento'], nodes['Taylor X California'], 102.3),
    StreetEdge(nodes['Taylor X Sacramento'], nodes['Jones X Sacramento'], 143.9),
    StreetEdge(nodes['Taylor X Sacramento'], nodes['Taylor X Clay'], 100),

    StreetEdge(nodes['Taylor X Clay'], nodes['Taylor X Sacramento'], 100),
    StreetEdge(nodes['Taylor X Clay'], nodes['Mason X Clay'], 150.4),
    StreetEdge(nodes['Taylor X Clay'], nodes['Taylor X Washington'], 100.3),

    StreetEdge(nodes['Taylor X Washington'], nodes['Taylor X Clay'], 100.3),
    StreetEdge(nodes['Taylor X Washington'], nodes['Mason X Washington'], 147.2),
    StreetEdge(nodes['Taylor X Washington'], nodes['Taylor X Jackson'], 101.3),

    StreetEdge(nodes['Taylor X Jackson'], nodes['Taylor X Washington'], 101.3),
    StreetEdge(nodes['Taylor X Jackson'], nodes['Jones X Jackson'], 146.9),
    StreetEdge(nodes['Taylor X Jackson'], nodes['Taylor X Pacific Ave'], 100.5),

    StreetEdge(nodes['Taylor X Pacific Ave'], nodes['Taylor X Jackson'], 100.5),
    StreetEdge(nodes['Taylor X Pacific Ave'], nodes['Jones X Pacific Ave'], 145.6),
    StreetEdge(nodes['Taylor X Pacific Ave'], nodes['Mason X Pacific Ave'], 146.6),
    StreetEdge(nodes['Taylor X Pacific Ave'], nodes['Taylor X Broadway'], 100.9),

    StreetEdge(nodes['Taylor X Broadway'], nodes['Taylor X Pacific Ave'], 100.9),
    StreetEdge(nodes['Taylor X Broadway'], nodes['Jones X Broadway'], 148.7),
    StreetEdge(nodes['Taylor X Broadway'], nodes['Mason X Broadway'], 147.3),
    StreetEdge(nodes['Taylor X Broadway'], nodes['Taylor X Valejo'], 118.2),

    # Mason to N San Francisco
    StreetEdge(nodes['Mason X California'], nodes['Taylor X California'], 144.9),
    StreetEdge(nodes['Mason X California'], nodes['Mason X Sacramento'], 103.5),
    StreetEdge(nodes['Mason X California'], nodes['Powell X California'], 143.4),

    StreetEdge(nodes['Mason X Sacramento'], nodes['Mason X California'], 103.5),
    StreetEdge(nodes['Mason X Sacramento'], nodes['Taylor X Sacramento'], 148.2),
    StreetEdge(nodes['Mason X Sacramento'], nodes['Mason X Clay'], 100.0),

    StreetEdge(nodes['Mason X Clay'], nodes['Mason X Sacramento'], 100.0),
    StreetEdge(nodes['Mason X Clay'], nodes['Powell X Clay'], 146.8),
    StreetEdge(nodes['Mason X Clay'], nodes['Mason X Washington'], 100.2),

    StreetEdge(nodes['Mason X Washington'], nodes['Mason X Clay'], 100.2),
    StreetEdge(nodes['Mason X Washington'], nodes['Powell X Washington'], 146.1),
    StreetEdge(nodes['Mason X Washington'], nodes['Mason X Jackson'], 102.3),

    StreetEdge(nodes['Mason X Jackson'], nodes['Mason X Washington'], 102.3),
    StreetEdge(nodes['Mason X Jackson'], nodes['Taylor X Jackson'], 146.7),
    StreetEdge(nodes['Mason X Jackson'], nodes['Mason X Pacific Ave'], 100),

    StreetEdge(nodes['Mason X Pacific Ave'], nodes['Mason X Jackson'], 100),
    StreetEdge(nodes['Mason X Pacific Ave'], nodes['Taylor X Pacific Ave'], 146.6),
    StreetEdge(nodes['Mason X Pacific Ave'], nodes['Powell X Pacific Ave'], 145.5),
    StreetEdge(nodes['Mason X Pacific Ave'], nodes['Mason X Broadway'], 100.1),

    StreetEdge(nodes['Mason X Broadway'], nodes['Mason X Pacific Ave'], 100.1),
    StreetEdge(nodes['Mason X Broadway'], nodes['Taylor X Broadway'], 147.3),
    StreetEdge(nodes['Mason X Broadway'], nodes['Powell X Broadway'], 147.4),
    StreetEdge(nodes['Mason X Broadway'], nodes['Mason X Valejo'], 115.8),

    StreetEdge(nodes['Mason X Valejo'], nodes['Mason X Broadway'], 115.8),
    StreetEdge(nodes['Mason X Valejo'], nodes['Powell X Valejo'], 146.7),

    # Powell to N San Francisco
    StreetEdge(nodes['Powell X California'], nodes['Mason X California'], 143.4),
    StreetEdge(nodes['Powell X California'], nodes['Powell X Sacramento'], 103.1),
    StreetEdge(nodes['Powell X California'], nodes['Stockton X California'], 150.1),

    StreetEdge(nodes['Powell X Sacramento'], nodes['Powell X California'], 103.1),
    StreetEdge(nodes['Powell X Sacramento'], nodes['Mason X Sacramento'], 147.3),
    StreetEdge(nodes['Powell X Sacramento'], nodes['Powell X Clay'], 101.2),

    StreetEdge(nodes['Powell X Clay'], nodes['Powell X Sacramento'], 101.2),
    StreetEdge(nodes['Powell X Clay'], nodes['Stockton X Clay'], 147.3),
    StreetEdge(nodes['Powell X Clay'], nodes['Powell X Washington'], 100.7),

    StreetEdge(nodes['Powell X Washington'], nodes['Powell X Clay'], 100.7),
    StreetEdge(nodes['Powell X Washington'], nodes['Powell X Jackson'], 100.9),

    StreetEdge(nodes['Powell X Jackson'], nodes['Powell X Washington'], 100.9),
    StreetEdge(nodes['Powell X Jackson'], nodes['Mason X Jackson'], 145.9),
    StreetEdge(nodes['Powell X Jackson'], nodes['Stockton X Jackson'], 146.5),
    StreetEdge(nodes['Powell X Jackson'], nodes['Powell X Pacific Ave'], 102.0),

    StreetEdge(nodes['Powell X Pacific Ave'], nodes['Powell X Jackson'], 102.0),
    StreetEdge(nodes['Powell X Pacific Ave'], nodes['Mason X Pacific Ave'], 145.5),
    StreetEdge(nodes['Powell X Pacific Ave'], nodes['Powell X Broadway'], 101.3),

    StreetEdge(nodes['Powell X Broadway'], nodes['Powell X Pacific Ave'], 101.3),
    StreetEdge(nodes['Powell X Broadway'], nodes['Mason X Broadway'], 147.4),
    StreetEdge(nodes['Powell X Broadway'], nodes['Stockton X Broadway'], 145.5),
    StreetEdge(nodes['Powell X Broadway'], nodes['Powell X Valejo'], 107.5),

    StreetEdge(nodes['Powell X Valejo'], nodes['Powell X Broadway'], 107.5),
    StreetEdge(nodes['Powell X Valejo'], nodes['Stockton X Valejo'], 149.1),
    StreetEdge(nodes['Powell X Valejo'], nodes['Mason X Valejo'], 146.7),

    # Stockton to N San Francisco
    StreetEdge(nodes['Stockton X California'], nodes['Powell X California'], 150.1),
    StreetEdge(nodes['Stockton X California'], nodes['Grant X California'], 142.5),
    StreetEdge(nodes['Stockton X California'], nodes['Stockton X Sacramento'], 106.4),

    StreetEdge(nodes['Stockton X Sacramento'], nodes['Stockton X California'], 106.4),
    StreetEdge(nodes['Stockton X Sacramento'], nodes['Powell X Sacramento'], 151.3),
    StreetEdge(nodes['Stockton X Sacramento'], nodes['Stockton X Clay'], 100.3),

    StreetEdge(nodes['Stockton X Clay'], nodes['Stockton X Sacramento'], 100.3),
    StreetEdge(nodes['Stockton X Clay'], nodes['Grant X Clay'], 143.7),
    StreetEdge(nodes['Stockton X Clay'], nodes['Stockton X Washington'], 100.8),

    StreetEdge(nodes['Stockton X Washington'], nodes['Stockton X Clay'], 100.8),
    StreetEdge(nodes['Stockton X Washington'], nodes['Powell X Washington'], 149.1),
    StreetEdge(nodes['Stockton X Washington'], nodes['Stockton X Jackson'], 100.8),

    StreetEdge(nodes['Stockton X Jackson'], nodes['Stockton X Washington'], 100.8),
    StreetEdge(nodes['Stockton X Jackson'], nodes['Grant X Jackson'], 143.4),
    StreetEdge(nodes['Stockton X Jackson'], nodes['Stockton X Pacific Ave'], 100.5),

    StreetEdge(nodes['Stockton X Pacific Ave'], nodes['Stockton X Jackson'], 100.5),
    StreetEdge(nodes['Stockton X Pacific Ave'], nodes['Powell X Pacific Ave'], 148.2),
    StreetEdge(nodes['Stockton X Pacific Ave'], nodes['Stockton X Broadway'], 102.7),

    StreetEdge(nodes['Stockton X Broadway'], nodes['Stockton X Pacific Ave'], 102.7),
    StreetEdge(nodes['Stockton X Broadway'], nodes['Grant X Broadway'], 160.2),
    StreetEdge(nodes['Stockton X Broadway'], nodes['Powell X Broadway'], 145.5),
    StreetEdge(nodes['Stockton X Broadway'], nodes['Stockton X Valejo'], 107.5),

    StreetEdge(nodes['Stockton X Valejo'], nodes['Stockton X Broadway'], 107.5),
    StreetEdge(nodes['Stockton X Valejo'], nodes['Columbus Ave X Valejo'], 90.7),
    StreetEdge(nodes['Stockton X Valejo'], nodes['Stockton X Powell'], 149.1),

    # Grant to N San Francisco
    StreetEdge(nodes['Grant X California'], nodes['Stockton X California'], 142.5),
    StreetEdge(nodes['Grant X California'], nodes['Kearny X California'], 140.0),
    StreetEdge(nodes['Grant X California'], nodes['Grant X Sacramento'], 103.8),

    StreetEdge(nodes['Grant X Sacramento'], nodes['Stockton X Sacramento'], 145.3),
    StreetEdge(nodes['Grant X Sacramento'], nodes['Grant X Clay'], 100.8),

    StreetEdge(nodes['Grant X Clay'], nodes['Kearny X Clay'], 140.5),
    StreetEdge(nodes['Grant X Clay'], nodes['Grant X Washington'], 100.5),

    StreetEdge(nodes['Grant X Washington'], nodes['Stockton X Washington'], 144.7),
    StreetEdge(nodes['Grant X Washington'], nodes['Grant X Jackson'], 101.7),

    StreetEdge(nodes['Grant X Jackson'], nodes['Kearny X Jackson'], 140.2),
    StreetEdge(nodes['Grant X Jackson'], nodes['Grant X Pacific Ave'], 100.2),

    StreetEdge(nodes['Grant X Pacific Ave'], nodes['Stockton X Pacific Ave'], 143.4),
    StreetEdge(nodes['Grant X Pacific Ave'], nodes['Grant X Broadway'], 101.5),
    StreetEdge(nodes['Grant X Broadway'], nodes['Stockton X Broadway'], 160.2),
    StreetEdge(nodes['Grant X Broadway'], nodes['Columbus Ave X Broadway'], 0),

    # Kearny to N San Francisco
    StreetEdge(nodes['Kearny X California'], nodes['Grant X California'], 140.0),
    StreetEdge(nodes['Kearny X California'], nodes['Kearny X Sacramento'], 104.9),

    StreetEdge(nodes['Kearny X Sacramento'], nodes['Grant X Sacramento'], 140.2),
    StreetEdge(nodes['Kearny X Sacramento'], nodes['Kearny X Clay'], 100.8),

    StreetEdge(nodes['Kearny X Clay'], nodes['Kearny X Washington'], 100.5),

    StreetEdge(nodes['Kearny X Washington'], nodes['Grant X Washington'], 140.9),
    StreetEdge(nodes['Kearny X Washington'], nodes['Kearny X Jackson'], 104.5),

    StreetEdge(nodes['Kearny X Jackson'], nodes['Kearny X Pacific Ave'], 101.4),
    StreetEdge(nodes['Kearny X Jackson'], nodes['Columbus Ave X Kearny'], 101.4),

    StreetEdge(nodes['Kearny X Pacific Ave'], nodes['Grant X Pacific Ave'], 140.6),

    
    # Columbus Ave to N San Francisco
    StreetEdge(nodes['Columbus Ave X Kearny'], nodes['Grant X Pacific Ave'], 140.6),
    StreetEdge(nodes['Columbus Ave X Pacific Ave'], nodes['Columbus Ave X Broadway'], 159.0),
    StreetEdge(nodes['Columbus Ave X Broadway'], nodes['Columbus Ave X Pacific Ave'], 159.0),
    StreetEdge(nodes['Columbus Ave X Broadway'], nodes['Columbus Ave X Valejo'], 140.0),
    StreetEdge(nodes['Columbus Ave X Broadway'], nodes['Grant X Broadway'], 0),
    StreetEdge(nodes['Columbus Ave X Valejo'], nodes['Columbus Ave X Broadway'], 140.0),
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
        'Columbus Ave X Kearny',
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
