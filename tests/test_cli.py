from daedalus_playground.cli import main


def test_cli_prints_selected_greeting(capsys) -> None:
    exit_code = main(["greeting", "Hermes"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "Hello, Hermes!\n"
    assert captured.err == ""


def test_cli_prints_selected_salutation_with_default_name(capsys) -> None:
    exit_code = main(["salutation"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "Salutations, Daedalus.\n"
    assert captured.err == ""


def test_cli_reports_unknown_greeting_type(capsys) -> None:
    exit_code = main(["unknown", "Hermes"])

    captured = capsys.readouterr()
    assert exit_code != 0
    assert captured.out == ""
    assert "Unknown greeting type: unknown." in captured.err
    assert "greeting" in captured.err
    assert "salutation" in captured.err
