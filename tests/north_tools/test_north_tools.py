def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from nomad_north_fiji.north_tools.fiji import (
        north_tool_entry_point,
    )

    assert (
        north_tool_entry_point.id_url_safe == 'nomad_north_fiji'
        or north_tool_entry_point.id == 'nomad-north-fiji'
    ), 'NORTHTool entry point has incorrect id or id_url_safe'
