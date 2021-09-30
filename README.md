# Get TFC Workspace Current State Output Action

This action is used to query the current value of a Terraform Cloud workspace output variable.

## Inputs

The action expects the following inputs:

| Variable        | Required | Description                                                                  |
| --------------- | -------- | ---------------------------------------------------------------------------- |
| `tfcToken`      | Yes      | A Terraform Cloud API token with access to manage the workspace.             |
| `orgName`       | Yes      | The name of the Terraform Cloud organization in which the workspace resides. |
| `workspaceName` | Yes      | The name of the Terraform Cloud workspace to manage.                         |
| `variableName`  | Yes      | The name of the output variable.                                             |

## Outputs

### `value`

The value of the output variable.

## Example Usage

```yaml
- uses: cbsinteractive/get-tfc-workspace-currentstate-output-action@v1
  with:
    tfcToken: ${{ secrets.tfc_org_token }}
    orgName: ${{ secrets.tfc_org }}
    workspaceName: some-tfc-workspace-name
    variable: some_output_variable_name
```

This example assumes variables stored as GitHub [encrypted secrets][].

[encrypted secrets]: https://docs.github.com/en/actions/reference/encrypted-secrets
