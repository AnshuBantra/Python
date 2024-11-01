function prompt {
    # Get the current directory
    $p = Split-Path -Leaf -Path (Get-Location)

    # Get the current Git branch
    $branch = ''
    $branchColor = 'Green'
    if (Test-Path .git) {
        $branch = & git rev-parse --abbrev-ref HEAD 2>$null
        if ($branch) {
            if ($branch -eq 'master' -or $branch -eq 'main') {
                $branchColor = 'Red'
            }
            $branch = "[$branch] "
        }
    }

    # Get the Python virtual environment
    $venv = ''
    if ($env:VIRTUAL_ENV) {
        $venvName = Split-Path -Leaf -Path $env:VIRTUAL_ENV
        $venv = "(venv: $venvName) "
    }

    # Set colored prompt
    Write-Host -NoNewline -ForegroundColor Blue "$p "
    Write-Host -NoNewline -ForegroundColor $branchColor "$branch"
    Write-Host -NoNewline -ForegroundColor Yellow "$venv"
    return '> '
}