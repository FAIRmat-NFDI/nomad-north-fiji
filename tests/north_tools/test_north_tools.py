def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails
    from nomad_north_fiji.north_tools import fiji

    assert fiji.id_url_safe == 'fiji' or fiji.id == 'nomad-north-fiji', (
        'NORTHTool entry point has incorrect id or id_url_safe'
    )
