from marketpulse.main import main


def test_main_prints_startup_message(capsys):
    main()

    captured = capsys.readouterr()

    assert captured.out == "MarketPulse is starting...\n"