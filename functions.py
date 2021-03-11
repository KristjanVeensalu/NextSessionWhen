import subprocess,sys,json,os,time

def install(package):
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if package in installed_packages:
        pass
    else:
        import pip
        os.system("pip install --user "+ package)