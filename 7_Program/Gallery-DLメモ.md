#Gallery-DLの使い方
$G=get-content list.txt
        
foreach($k in $G){
    gallery-dl $k
    Write-Host "ok!"
}