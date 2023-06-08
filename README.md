# `sw`

Small utility for managing services in a swarm easily

**Usage**:

```console
$ sw [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--folder PATH`: The folder containing the services  [default: ~/mistborn/services]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `d`: Deploys the service to the swarm
* `r`: Removes the service from the swarm
* `s`: Shows the status of the service

## `sw d`

Deploys the service to the swarm

**Usage**:

```console
$ sw d [OPTIONS]
```

**Options**:

* `--service TEXT`: [default: (dynamic)]
* `--force / --no-force`: Force the deployment, even if the service is excluded  [default: no-force]
* `--redeploy / --no-redeploy`: Force redeployment if the service is already deployed  [default: no-redeploy]
* `--help`: Show this message and exit.

## `sw r`

Removes the service from the swarm

**Usage**:

```console
$ sw r [OPTIONS]
```

**Options**:

* `--service TEXT`: [default: (dynamic)]
* `--help`: Show this message and exit.

## `sw s`

Shows the status of the service

**Usage**:

```console
$ sw s [OPTIONS] SERVICE
```

**Arguments**:

* `SERVICE`: The name of the service  [required]

**Options**:

* `-t, --truncate`: Truncate the output
* `--help`: Show this message and exit.
