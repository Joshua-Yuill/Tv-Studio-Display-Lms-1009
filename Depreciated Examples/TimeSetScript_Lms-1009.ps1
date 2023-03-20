$port= new-Object System.IO.Ports.SerialPort COM3,9600,None,8,one
$port.open()
$port.WriteLine("<ID**><MC>")
Start-Sleep -Milliseconds 50
$port.WriteLine("<ID01><HR><FU>")
Start-Sleep -Milliseconds 50
$port.WriteLine("<ID02><HG><FU>")
Start-Sleep -Milliseconds 50
$port.WriteLine("<ID01><M2>")
Start-Sleep -Milliseconds 50
$port.WriteLine("<ID02><M1>")
Start-Sleep -Milliseconds 50

$hour = (Get-Date).Hour
$min = (Get-Date).Minute
$sec = (Get-Date).Second


$port.WriteLine("<T$($hour)$($min)$($sec)>")
Start-Sleep -Milliseconds 3
$port.close()