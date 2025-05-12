
import subprocess
import re

def get_free_apps():
    """
    Retrieves a list of free apps from the Microsoft Store using PowerShell.
    """
    try:
        # PowerShell command to search for free apps
        powershell_command = """
        $apps = Get-AppxPackage | Where-Object {$_.IsFramework -eq $false}
        $freeApps = @()
        foreach ($app in $apps) {
            try {
                $storeApp = Get-AppxPackageManifest -Package $app | Select-Xml -XPath "/*[local-name()='Package']/*[local-name()='Applications']/*[local-name()='Application']/*[local-name()='VisualElements']" | ForEach-Object {$_.Node.GetAttribute('DisplayName')}
                if ($storeApp) {
                    $freeApps += $app.Name
                }
            } catch {}
        }
        $freeApps | ConvertTo-Json
        """

        # Execute the PowerShell command
        process = subprocess.Popen(['powershell', '-Command', powershell_command],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            print(f"Error retrieving app list: {stderr.decode()}")
            return []

        app_list_json = stdout.decode('utf-8').strip()

        # Basic parsing of the JSON-like output (not perfect, but avoids dependencies)
        app_list = re.findall(r'"([^"]*)"', app_list_json)

        return app_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def install_app(app_name):
    """
    Installs an app from the Microsoft Store using PowerShell.
    """
    try:
        # PowerShell command to install the app
        powershell_command = f"""
        try {{
            Add-AppxPackage -DisableDevelopmentMode -Register "C:\\Program Files\\WindowsApps\\{app_name}\\AppxManifest.xml"
        }} catch {{
            Write-Host "Failed to install {app_name}: $($_.Exception.Message)"
        }}
        """

        # Execute the PowerShell command
        process = subprocess.Popen(['powershell', '-Command', powershell_command],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            print(f"Error installing {app_name}: {stderr.decode()}")
        else:
            print(f"Successfully installed {app_name}")

    except Exception as e:
        print(f"An error occurred while installing {app_name}: {e}")


if __name__ == "__main__":
    free_apps = get_free_apps()

    if free_apps:
        print("Found the following free apps:")
        for app in free_apps:
            print(f"- {app}")
            install_app(app)
    else:
        print("No free apps found or an error occurred.")

