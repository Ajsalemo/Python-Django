
ssh -o StrictHostKeyChecking=no root@$DIGITAL_OCEAN_IP_ADDRESS << 'ENDSSH'
  cd /pythondjango/
  export $(cat .env | xargs)
  docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY
  cd /
  docker pull $IMAGE:postgres
  docker pull $IMAGE:web
  docker pull $IMAGE:nginx
  docker-compose -f docker-compose.prod.yml up -d
ENDSSH