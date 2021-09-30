import json
import os
from unittest.mock import patch

import pytest

from entrypoint import run


def test_default(capsys):
    env = {
        "INPUT_WORKSPACENAME": "some-workspace-name",
        "INPUT_VARIABLE": "some_variable_name",
    }
    with patch.dict(os.environ, env, clear=True), patch(
        "entrypoint.subprocess.check_output"
    ) as m:
        m.return_value = json.dumps({"result": "some value"})
        run()
    assert m.call_args_list[0][0][0] == [
        "/tfc-cli",
        "stateversions",
        "current",
        "getoutput",
        "-workspace",
        "some-workspace-name",
        "-name",
        "some_variable_name",
    ]
    captured = capsys.readouterr()
    assert captured.out.strip() == "::set-output name=value::some value"


def test_error_without_workspace():
    env = {
        "INPUT_VARIABLE": "some_variable_name",
    }
    with patch.dict(os.environ, env, clear=True), pytest.raises(SystemExit):
        # Code under test
        run()


def test_error_without_variable_name():
    env = {
        "INPUT_WORKSPACENAME": "some-workspace-name",
    }
    with patch.dict(os.environ, env, clear=True), pytest.raises(SystemExit):
        # Code under test
        run()
