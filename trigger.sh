api="https://devserver.icodetest.com:8080/authenticate"
data="{\"username\":\"shai\",\"password\":\"password\",\"requestByExtension\":false}"
response=$(curl -s -X POST  -H "Content-Type: application/json" --data "$data" https://devserver.icodetest.com:8080/authenticate)
sudo yum -y install jq
token=$(echo "$response" | jq -r '."token"')
bearer="Bearer ${token}"
projectName='project1'
suiteName='onlyStep'
response1=$(curl -X POST -H "Authorization: ${bearer}" -H "Content-Type: multipart/form-data" -F "suitename=${suiteName}" -F "projectname=${projectName}" -F "file=@/home/ec2-user/ata_server/suite.csv" https://devserver.icodetest.com:8080/execute/pipeline/suite)


