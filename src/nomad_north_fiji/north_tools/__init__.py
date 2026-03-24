from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

fiji = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-fiji.',
    image='ghcr.io/fairmat-nfdi/nomad-north-fiji:main',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-fiji.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='https://raw.githubusercontent.com/FAIRmat-NFDI/nomad-north-fiji/main/src/nomad_north_fiji/north_tools/fiji/fiji.png',
    image_pull_policy='Always',
    default_url='/lab',
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
