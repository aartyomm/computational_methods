import os


class Paths:
    __basedir = os.path.dirname(__file__)

    path_to_logo = os.path.join(__basedir, 'icons', 'logo.ico')

    path_to_graph_icon = os.path.join(__basedir, 'icons', 'graph.png')

    path_to_tmp = os.path.join(__basedir, 'tmp')

    path_to_style = os.path.join(__basedir, 'style', 'style.qss')
