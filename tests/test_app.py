from app import main

def test_main_prints_hello_world(capsys):
    main()
    out = capsys.readouterr().out.strip()
    assert out == "Hello, world"
