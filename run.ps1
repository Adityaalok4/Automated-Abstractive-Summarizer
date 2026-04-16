#!/usr/bin/env pwsh
# Run this from the project root in PowerShell to start the Flask dev server.
# It will activate .venv if present, otherwise runs with the current Python.

$venv = Join-Path $PSScriptRoot '.venv'
if (Test-Path $venv) {
    $activate = Join-Path $venv 'Scripts\Activate.ps1'
    if (Test-Path $activate) {
        Write-Output "Activating virtual environment at $venv"
        & $activate
    }
}

Write-Output "Starting Flask dev server..."
python -m backend.app
