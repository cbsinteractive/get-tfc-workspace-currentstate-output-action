#!/usr/bin/env python3
import json
import os
import subprocess
import sys


def _get_cli_path():
    return "/tfc-cli"


def run():
    try:
        workspace_name = os.environ["INPUT_WORKSPACENAME"]
        output_variable_name = os.environ["INPUT_VARIABLE"]
    except KeyError as e:
        print(f"Environment variable not set: {e}")
        sys.exit(1)
    body = json.loads(
        subprocess.check_output(
            [
                _get_cli_path(),
                "stateversions",
                "current",
                "getoutput",
                "-workspace",
                workspace_name,
                "-name",
                output_variable_name,
            ],
            text=True,
        )
    )
    print(f"::set-output name=value::{body['result']}")


if __name__ == "__main__":
    run()
