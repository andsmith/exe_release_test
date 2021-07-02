
REM ---> RUN IN WINDOWS POWER SHELL - Administrator priv.
pyinstaller --onefile -w test_cam.py
pyinstaller --onefile -w test_plot.py


New-SelfSignedCertificate -Type Custom -Subject "CN=andsmith, O=Andrew T Smith, C=US" -KeyUsage DigitalSignature -FriendlyName "Andrew T Smith" -CertStoreLocation "Cert:\CurrentUser\My" -TextExtension @("2.5.29.37={text}1.3.6.1.5.5.7.3.3", "2.5.29.19={text}")

REM Example of correct output:

REM PSParentPath: Microsoft.PowerShell.Security\Certificate::CurrentUser\My

REM Thumbprint                                Subject
REM ----------                                -------
REM DEA276E521277CF8D8F2B86730E833C9D4830BAD  CN=andsmith, O=Andrew T Smith, C=US

$password = ConvertTo-SecureString -String And$m7th -Force -AsPlainText 
Export-PfxCertificate -cert "Cert:\CurrentUser\My\DEA276E521277CF8D8F2B86730E833C9D4830BAD" -FilePath andsmith_cert.pfx -Password $password


    REM Directory: C:\Users\andrew\Desktop\old\projects\exe_release_test


REM Mode                 LastWriteTime         Length Name
REM ----                 -------------         ------ ----
REM -a----          7/2/2021   6:41 AM           2734 andsmith_cert.pfx


SignTool sign /fd SHA256 /a /f andsmith_cert.pfx /p And$m7th dist\test_plot.exe
SignTool sign /fd SHA256 /a /f andsmith_cert.pfx /p And$m7th dist\test_plot.exe
