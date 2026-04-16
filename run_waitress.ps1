#!/usr/bin/env pwsh
param(
	[int]$Port = 5000
)

Write-Output "Starting Waitress server on port $Port..."
.venv\Scripts\Activate.ps1 -ErrorAction SilentlyContinue
$env:PORT = $Port
python -m backend.run_waitress
