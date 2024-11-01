# function prompt {
#     # Get the current directory
#     $p = Split-Path -Leaf -Path (Get-Location)

#     # Get the current Git branch
#     $branch = ''
#     $branchColor = 'Green'
#     if (Test-Path .git) {
#         $branch = & git rev-parse --abbrev-ref HEAD 2>$null
#         if ($branch) {
#             if ($branch -eq 'master' -or $branch -eq 'main') {
#                 $branchColor = 'Red'
#             }
#             $branch = "[$branch] "
#         }
#     }

#     # Get the Python virtual environment
#     $venv = ''
#     if ($env:VIRTUAL_ENV) {
#         $venvName = Split-Path -Leaf -Path $env:VIRTUAL_ENV
#         $venv = "(venv: $venvName) "
#     }

#     # Set colored prompt
#     Write-Host -NoNewline -ForegroundColor Blue "$p "
#     Write-Host -NoNewline -ForegroundColor $branchColor "$branch"
#     Write-Host -NoNewline -ForegroundColor Yellow "$venv"
#     return '> '
# }

function prompt {
    # Get the current directory
    $currentDir = Get-Location
    $p = Split-Path -Leaf -Path $currentDir

    # Function to find the Git root directory
    function Get-GitRoot {
        $path = Get-Location
        while ($path -and !(Test-Path (Join-Path $path '.git'))) {
            $parentPath = Split-Path -Parent $path
            if ($parentPath -eq $path) {
                return $null
            }
            $path = $parentPath
        }
        return $path
    }

    # Get the current Git branch
    $branch = ''
    $branchColor = 'Green'
    $gitRoot = Get-GitRoot
    if ($gitRoot) {
        # Change location to Git root and get branch
        Set-Location $gitRoot
        $branch = & git rev-parse --abbrev-ref HEAD 2>$null
        # Return to the original directory
        Set-Location $currentDir
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
    return '>>> '
}