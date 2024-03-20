import os


class Paths:
    __basedir = os.path.dirname(__file__)

    path_to_logo = os.path.join(__basedir, 'icons', 'logo.ico')

    path_to_graph_icon = os.path.join(__basedir, 'icons', 'graph.png')

    path_to_bw_graph_icon = os.path.join(__basedir, 'icons', 'graph-bw.png')

    path_to_tmp = os.path.join(__basedir, 'tmp')

    path_to_style = os.path.join(__basedir, 'style', 'style.qss')

    path_to_bw_style = os.path.join(__basedir, 'style', 'style_bw.qss')

    path_to_uniform_distribution_img = ":/icons/pngs/vybrano_ravnomernoe_raspredelenie.png"

    path_tu_concentrated_distribution_img = ":/icons/pngs/vybrano_sosredotochennoe_raspredelenie.png"

    path_to_distribution_img = ":/icons/pngs/vybor_raspredelenia.png"

    path_to_inorganic_img = ":/icons/pngs/neorganika_vybrano.png"

