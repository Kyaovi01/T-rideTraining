#Define source and destination paths 
$source = "C:\Users"
$currentUserDesktop = [Environement]::GetFolderPath("Desktop")
$destination = "$currentUserDesktop\backup_$(Get-date -Format yyyyMMddhhmmss)"
#Create a new directory  for today's backup 
New-Item -ItemType Directory -Force -Path $destination

#Copy all user Data to the backup directory 
Get-ChildItem -Path $source -Recurse | Copy-Item -Destination {
$destination +$_.FullName.Substring($source.Length)
} -Container

#Log the backup operation 
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$logFile = "$currentUserDesktop\backup_logs.txt"
$logEntry = "$timestamp | Backup completed for source : $source to destination : $destination"
Add-Content -Path $logFile -Value $logEntry

Write-Output "Backup completed successfully" 