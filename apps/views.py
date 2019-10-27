from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def test(request):
    response = requests.get('http://192.168.198.140:5555/images/json')
    data = response.json()
    return render(request, 'ssh/base.html', {
        'Id': data['Id'],
        'RepoTags': data['RepoTags']
    })

def index(request):
    import paramiko
    ssh = paramiko.SSHClient()
    # Auto add host to known hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to server
    ssh.connect("192.168.198.140", username="tbv", password="iamTR")
    # Do command
    (ssh_stdin, ssh_stdout, ssh_stderr) = ssh.exec_command("ifconfig")
    # Get status code of command
    exit_status = ssh_stdout.channel.recv_exit_status()
    # Print status code
    print ("exit status: %s" % exit_status)
    # Print content
    for line in ssh_stdout.readlines():
        print(line.rstrip())
    # Close ssh connect
    ssh.close()
    return render(request, 'ssh/base.html', {'exit_status' : exit_status})
