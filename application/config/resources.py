"""In this module we define all Resources (except apps in the gallery) and exposes
them via the RESOURCES list.
"""
# pylint: disable=line-too-long
from awesome_panel.application.models import Resource

from application.config import authors, tags
from application.config.settings import THUMBNAILS_ROOT

# panel FILE ROOTS

# https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-dino
# https://mybinder.org/v2/gh/julioasotodv/panel-dashboard-demo/master?urlpath=/proxy/5006/dashboard
# https://github.com/holoviz/panel/issues/972#issue-552507960
# https://github.com/julioasotodv/panel-dashboard-demo

# https://github.com/julioasotodv/gradient-descent-demo
# https://mybinder.org/v2/gh/holoviz/panel/binder?urlpath=
# https://medium.datadriveninvestor.com/streamlit-vs-dash-vs-voil%C3%A0-vs-panel-battle-of-the-python-dashboarding-giants-177c40b9ea57
# https://medium.datadriveninvestor.com/panel-everything-you-need-to-know-9bca61532e12
# https://dmnfarrell.github.io/bioinformatics/abm-mesa-network
# https://github.com/holoviz-demos/minimal-heroku-demo
# https://vizartpandey.com/30-best-design-resources-for-your-next-tableau-dashboard/
# ttps://vizartpandey.com/5-hci-principles-for-an-amazing-data-visualisation/
# https://towardsdatascience.com/advanced-data-visualization-with-holoviews-e7263ad202e
# https://protect2.fireeye.com/v1/url?k=7f6b8b93-20f0b2f2-7f6b65dc-86d8a30ca42b-455dc19b6233bbd3&q=1&e=e5b506b5-487c-4db8-8728-0b4d615ccdca&u=https%3A%2F%2Fwww.quansight.com%2Fpost%2Fworking-across-panel-and-ipywidgets-ecosystems
# http://www.hyamani.eu/2021/01/02/dashboards-for-iot-sensors/#A_full_fledge_Dashboard
# http://bonegen.nti.tul.cz/BoneGen_server_version
# https://github.com/dhruvbalwada/glider-panel-demo https://twitter.com/BalwadaDhruv/status/1375303891751870474?s=20
RESOURCES = [
    Resource(
        name="statseuro2020",
        url="https://www.statseuro2020.com/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.APP,
            tags.CODE,
        ],
        author=authors.PIERRE_OLIVIER_SIMONARD,
    ),
    Resource(
        name="Game of Dashboards",
        url="https://neurosnippets.com/posts/game-of-dashboards-2/#post",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.APP,
            tags.CODE,
            tags.REVIEW,
        ],
        author=authors.MATTEO_Mancini,
    ),
    Resource(
        name="Battle of The Python Dashboarding Giants",
        url="https://medium.datadriveninvestor.com/streamlit-vs-dash-vs-voil%C3%A0-vs-panel-battle-of-the-python-dashboarding-giants-177c40b9ea57",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.APP,
            tags.CODE,
            tags.REVIEW,
        ],
        author=authors.MATTEO_Mancini,
    ),
    Resource(
        name="Digital Vulnerabilities Map",
        url="https://discourse.holoviz.org/t/a-map-to-help-local-policies-to-detect-digital-vulnerabilities/1580",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.APP,
            tags.CODE,
            tags.TUTORIAL,
        ],
        author=authors.THOMAS_PEDOT,
    ),
    Resource(
        name="Panel/Holoviews Learning Aid",
        url="https://www.quansight.com/post/panel-holoviews-learning-aid",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL],
        author=authors.QUANSIGHT,
    ),
    Resource(
        name="Quick Dashboard with Panel",
        url="https://www.quansight.com/post/quick-dashboarding-with-panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL],
        author=authors.QUANSIGHT,
    ),
    Resource(
        name="Holo Grid Generator",
        url="https://github.com/pygridgen/holo-gridgen",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.APP, tags.CODE],
        author=authors.PYGRIDGEN,
    ),
    Resource(
        name="World Glaciers Explorer",
        url="https://edu.oggm.org/en/latest/explorer.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.APP, tags.VIDEO],
        author=authors.OGGM_EDU,
    ),
    Resource(
        name="Experimental Machine Learning with HoloViz and PyTorch in Jupyterlab ",
        url="https://pyvideo.org/pydata-la-2019/experimental-machine-learning-with-holoviz-and-pytorch-in-jupyterlab.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL, tags.VIDEO],
        author=authors.HAYLEY_SONG,
    ),
    Resource(
        name="Panel Tutorial by vda-lab",
        url="https://vda-lab.github.io/visualisation-tutorial/holoviz-what-is-panel.html#",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL, tags.CODE, tags.APP],
        author=authors.VDA_LAB,
    ),
    Resource(
        name="Panel Dashboards by Nic Fox",
        url="https://foxnic.github.io/projects.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.APP,
            tags.CODE,
        ],
        author=authors.NIC_FOX,
    ),
    Resource(
        name="How to Create an Interactive Dashboard in Python Using HoloViz Panel",
        url="https://dev.to/nicfoxds/how-to-create-an-interactive-dashboard-in-python-using-holoviz-panel-5bhp",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.TUTORIAL,
            tags.CODE,
        ],
        author=authors.NIC_FOX,
    ),
    Resource(
        name="Colormap Distorsions",
        url="https://github.com/mycarta/Colormap-distorsions-Panel-app",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.CODE, tags.APP],
        author=authors.MATTEO_NICCOLI,
    ),
    Resource(
        name="Elvis - Golden Layout",
        url="https://github.com/LeonvanKouwen/elvis",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.CODE],
        author=authors.LEON_VAN_KOUWEN,
    ),
    Resource(
        name="Color Dropper App",
        url="http://colordropper.herokuapp.com/colordropper",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.APP],
        author=authors.ANDREW_HUANG,
    ),
    Resource(
        name="A tour (of a small part) of the Python visualization landscape",
        url="https://indico.cern.ch/event/833895/contributions/3577846/attachments/1928191/3205023/PyHEP2019_slides.pdf",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ARTICLE],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Building Dashboards. Introduction to Data Analysis in Biological Sciences.",
        url="https://xavartley.github.io/#panel/vtk_examples/Gallery_VTK.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.APP, tags.INSPIRATION],
        author=authors.JUSTIN_BOIS,
    ),
    Resource(
        name="VTK Examples by xavArtley",
        url="http://bebi103.caltech.edu.s3-website-us-east-1.amazonaws.com/2019a/content/recitations/recitation_05/dashboards.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL, tags.INSPIRATION, tags.VTK],
        author=authors.XAVARTLEY,
    ),
    Resource(
        name="XrViz",
        url="https://github.com/intake/xrviz",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.APP,
            tags.CODE,
            tags.INSPIRATION,
        ],
        author=authors.INTAKE,
    ),
    Resource(
        name="Information is Beautiful",
        url=(
            "https://towardsdatascience.com/how-to-build-a-time-series-dashboard-in-python-with-"
            "panel-altair-and-a-jupyter-notebook-c0ed40f02289"
        ),
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.TUTORIAL,
            tags.ARTICLE,
        ],
        author=authors.BENJAMIN_COOLEY,
    ),
    Resource(
        name="Information is Beautiful",
        url="https://informationisbeautiful.net/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.INSPIRATION],
        author=authors.INFORMATIONISBEUTIFULL,
    ),
    Resource(
        name="Open Source Directions ep. 29: Panel",
        url="https://www.youtube.com/watch?v=hZOsxmM_wyg",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.VIDEO],
        author=authors.QUANSIGHT,
    ),
    Resource(
        name="Our World in Data",
        url="https://ourworldindata.org/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.INSPIRATION],
        author=authors.OURWORLDINDATA,
    ),
    Resource(
        name="Panel",
        url="https://panel.pyviz.org/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Discourse",
        url="https://discourse.holoviz.org/c/panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Getting Started",
        url="https://panel.pyviz.org/getting_started/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="User Guide",
        url="https://panel.pyviz.org/user_guide/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Gallery",
        url="https://panel.pyviz.org/gallery/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Reference Gallery",
        url="https://panel.pyviz.org/reference/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="GitHub",
        url="https://github.com/holoviz/panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PANEL,
    ),
    Resource(
        name="Announcing Article",
        url="https://medium.com/@philipp.jfr/panel-announcement-2107c2b15f52",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.PANEL],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Awesome-panel.org",
        url="https://awesome-panel.org",
        thumbnail_png_path=THUMBNAILS_ROOT + "awesome-panel-org.png?raw=true",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Github",
        url="https://github.com/marcskovmadsen/awesome-panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Docs",
        url="https://awesome-panel.readthedocs.io/en/latest/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Docker",
        url="https://hub.docker.com/r/marcskovmadsen/awesome-panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="PyPi",
        url="https://pypi.org/project/awesome-panel/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.AWESOME_PANEL_ORG],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Dashboards with PyViz Panel for interactive web apps",
        url="https://dmnfarrell.github.io/bioinformatics/pyviz-panel",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ARTICLE],
        author=authors.DAMIAN_FARRELL,
    ),
    Resource(
        name="Turn any Notebook into a Deployable Dashboard | SciPy 2019 | James Bednar",
        url="https://www.youtube.com/watch?v=L91rd1D6XTA&t=274s",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.VIDEO,
            tags.TUTORIAL,
        ],
        author=authors.JAMES_BEDNAR,
    ),
    Resource(
        name="Turn any notebook into a deployable dashboard|PyData Berlin 2019",
        url="https://www.youtube.com/watch?v=Ohr29FJjBi0&list=PLGVZCDnMOq0pNHTYo3i56zYU-Tdw5Uguw",
        thumbnail_png_path=THUMBNAILS_ROOT + "pydataberlin2019.png?raw=true",
        is_awesome=True,
        tags=[
            tags.VIDEO,
            tags.TUTORIAL,
        ],
        author=authors.PHILIPP_RUDIGER,
    ),
    Resource(
        name="Visualize any Data Easily, from Notebooks to Dashboards",
        url="https://www.youtube.com/watch?v=7deGS4IPAQ0&t=1326s",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[
            tags.VIDEO,
            tags.TUTORIAL,
        ],
        author=authors.JAMES_BEDNAR,
    ),
    Resource(
        name="HoloViz.org - Awesome Resources and Tutorials",
        url="http://holoviz.org/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.TUTORIAL],
        author=authors.HOLOVIZ,
    ),
    Resource(
        name="awesome-streamlit.org",
        url="https://awesome-streamlit.org",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.SISTER_SITES],
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Bokeh",
        url="https://bokeh.pydata.org/en/latest/index.html",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.BOKEH,
    ),
    Resource(
        name="Jupyter Voila",
        url="https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.VOILA,
    ),
    Resource(
        name="Plotly Dash",
        url="https://plot.ly/dash/",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.PLOTLY,
    ),
    Resource(
        name="Streamlit",
        url="https://streamlit.io",
        thumbnail_png_path=THUMBNAILS_ROOT + "",
        is_awesome=True,
        tags=[tags.ALTERNATIVE],
        author=authors.STREAMLIT,
    ),
]

TAGS = sorted(list({tag for resource in RESOURCES for tag in resource.tags}))
