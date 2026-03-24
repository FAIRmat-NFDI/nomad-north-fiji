from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

fiji = NORTHTool(
    short_description='Use FIJI to visualize and analyze your images in NOMAD.',
    image='ghcr.io/fairmat-nfdi/nomad-north-fiji:main',
    description="""### **FIJI**:

    [Fiji Is Just ImageJ to visualize and analyze your images in NOMAD.](https://imagej.net/learn/)

    [Research article about the software](https://doi.org/10.1038/nmeth.2019)""",
    external_mounts=[],
    file_extensions=['tif, tiff, jpeg, png, gif, bmp, avi'],
    icon='https://raw.githubusercontent.com/FAIRmat-NFDI/nomad-north-fiji/main/src/nomad_north_fiji/north_tools/fiji/fiji.png',
    image_pull_policy='Always',
    default_url='/desktop',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='fiji',
)

north_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad-north-fiji-fiji',
    north_tool=fiji,
)
