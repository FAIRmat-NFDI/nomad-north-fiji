#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

fiji = NORTHTool(
    image='ghcr.io/fairmat-nfdi/nomad-north-fiji:v0.1.0',
    description="""### **FIJI**:

    [Fiji Is Just ImageJ to visualize and analyze your images in NOMAD](https://imagej.net/learn/)

    [Research article about the software](https://doi.org/10.1038/nmeth.2019)""",
    short_description='Use FIJI to visualize and or analyze your images in NOMAD.',
    external_mounts=[],
    file_extensions=['tif, tiff, jpeg, png, gif, bmp, avi'],
    icon='fiji.png',
    image_pull_policy='Always',
    default_url='/desktop',
    maintainer=[{'email': 'markus.kuehbach@physik.hu-berlin.de', 'name': 'Markus Kühbach'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='fiji',
)

north_tool_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad_north_fiji', north_tool=fiji
)
