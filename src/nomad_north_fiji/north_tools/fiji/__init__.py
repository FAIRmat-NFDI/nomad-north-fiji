from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

fiji = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-fiji.',
    image='ghcr.io/FAIRmat-NFDI/nomad-north-fiji:latest',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-fiji.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='fiji',
)

north_tool_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad_north_fiji_fiji', north_tool=fiji
)
