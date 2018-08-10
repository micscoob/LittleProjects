#Flag
#Merica. Need to figure out how to get the correct stars and stripes.
Function BlueRed 
{ Param($x,$y)
  $BlueReds = Write-Host "**********" -b blue -f white -nonewline; Write-Host "                 " -b red;
  $Host.UI.RawUI.CursorPosition = New-Object System.Management.Automation.Host.Coordinates $x , $y
  $Host.UI.Write($BlueReds) 
    
}

Function BlueWhite 
{ Param($x,$y)
  $BlueWhies = Write-Host "**********" -b blue -f white -nonewline; Write-Host "                 " -b White;
  $Host.UI.RawUI.CursorPosition = New-Object System.Management.Automation.Host.Coordinates $x , $y
  $Host.UI.Write($BlueWhites) 
    
}

Function White 
{ Param($x,$y)
  $White = Write-Host "                           " -b White -nonewline
  $Host.UI.RawUI.CursorPosition = New-Object System.Management.Automation.Host.Coordinates $x , $y
  $Host.UI.Write($White) 
    
}

Function Red 
{ Param($x,$y)
  $Red = Write-Host "                           " -b Red -nonewline
  $Host.UI.RawUI.CursorPosition = New-Object System.Management.Automation.Host.Coordinates $x , $y
  $Host.UI.Write($Red) 
    
}

$a = 1
$b = 2
$c = 7
$d = 8

for($counter = 0; $counter -le 2; $counter++)
{
   BlueRed 0 $a
   BlueWhite 0 $b
   $a = $a +2
   $b = $b +2
}

for($counter = 0; $counter -le 2; $counter++)
{
   Red 0 $c
   White 0 $d
   $a = $a +2
   $b = $b +2
}


echo "`n"
Read-Host "Press ENTER"
