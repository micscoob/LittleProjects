##Randooo##
## Prints Warning in Random places and in Random colors. ##

$color = 0,"Black", 1,"DarkBlue",2,"DarkGreen",3,"DarkCyan",4,"DarkRed",5,"DarkMagenta",6,"DarkYellow",7,"Gray",8,"DarkGray",9,"Blue",10,"Green",11,"Cyan",12,"Red",13,"Magenta",14,"Yellow",15,"White"

#function move([int]$x, [int] $y, $message)
#{
# $Host.UI.RawUI.CursorPosition = New-Object System.Management.Automation.Host.Coordinates $x , $y
#  $Host.UI.Write('$message')
#  }

while($i -lt 99)
{
$var1 = Get-Random -Maximum 16
$var2 = Get-Random -Maximum 16
$x = $var1
$y = $var2
$Host.UI.RawUI.CursorPosition = New-Object System.Management.Automation.Host.Coordinates $x , $y
$prints=Write-Host "WARNING!!" -BackgroundColor $color[$var1] -ForegroundColor $color[$var2]
$Host.UI.Write($prints)
Start-Sleep 1
$i ++

}
