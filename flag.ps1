Flag
##Uncomplete Power shell script. Will print american flag hopefully...

for ($o=0; $o -le 5; $o ++){

    for ($i=0; $i -le 9; $i++)
    {
    $BlueStar = Write-Host "*" -BackgroundColor Blue -ForegroundColor White
    $x = $i
    $y = $o
    $Host.UI.RawUI.CursorPosition = New-Object System.Management.Automation.Host.Coordinates $x , $y
    $Host.UI.Write($BlueStar)
    Start-Sleep .3

    }



}

$RedStrip = Write-Host "               " -BackgroundColor Red
$x = $11
$y = 0
$Host.UI.RawUI.CursorPosition = New-Object System.Management.Automation.Host.Coordinates $x , $y
$Host.UI.Write($RedStrip)
Start-Sleep .3
Read-Host "Press ENTER"
