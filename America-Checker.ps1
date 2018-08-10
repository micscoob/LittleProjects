#Flag
#Merica. Need to figure out how to get the correct stars and stripes.
#Checks to make sure the indivduals are american before running. 
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
$Answer = Read-Host "ARE YOU AN AMERICAN?[Y][N]"

$upperAnswer = $Answer.ToUpper()

Switch ($upperAnswer)
{
  Y { Write-Host "WELLCOME FELLOW AMERICAN!!" }
  YES { Write-Host "WELLCOME FELLOW AMERICAN!!" }
  N { Write-Host "GET OUT OF HERE YA COMMIE!" ; Start-Sleep 3; exit }
  NO { Write-Host "GET OUT OF HERE YA COMMIE!" ; Start-Sleep 3;  exit }
  Default { Write-Host "YOU DIDN'T ANSWER YES OR NO. ONLY COMMIES CAN'T READ!"; Start-Sleep 3;  exit}
 }

While($true)
{
$Answer2 = Read-Host "PRESS ANY KEY TO RUN SCRIPT. [Q] TO QUIT "

$upperAnswer2 = $Answer2.ToUpper()

Switch ($upperAnswer2)
{
  Q { Write-Host "GOOD BYE!"; ]Start-Sleep 3; exit }
  QUIT { Write-Host "GOOD BYE!"; ]Start-Sleep 3; exit }
  Default { Write-Host "RUNNING SCIPT" }
 }
 
 }
