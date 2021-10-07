k8s_yaml('kubernetes.yaml')
k8s_resource('digital-identity-check', port_forwards=8000)
docker_build('digital-identity-check', '.',
  live_update = [
    sync('.', '/app'),
    run('pip install -r requirements.txt', trigger='requirements.txt')
  ])
