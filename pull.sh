# arm64
cat to_pull.txt | awk '{print "docker pull --platform linux/arm64 " $1}'
cat to_pull.txt | awk '{print "docker pull --platform linux/arm64 " $1}' | sh
cat to_pull.txt | awk '{print "docker tag " $1 " '"$registry/$namespace/"'" $2 "-arm64"}'
cat to_pull.txt | awk '{print "docker tag " $1 " '"$registry/$namespace/"'" $2 "-arm64"}' | sh
cat to_pull.txt | awk '{print "docker push " "'"$registry/$namespace/"'" $2 "-arm64"}'
cat to_pull.txt | awk '{print "docker push " "'"$registry/$namespace/"'" $2 "-arm64"}' | sh

# amd64/x86-64
cat to_pull.txt | awk '{print "docker pull --platform linux/amd64 " $1}'
cat to_pull.txt | awk '{print "docker pull --platform linux/amd64 " $1}' | sh
cat to_pull.txt | awk '{print "docker tag " $1 " '"$registry/$namespace/"'" $2 "-amd64"}'
cat to_pull.txt | awk '{print "docker tag " $1 " '"$registry/$namespace/"'" $2 "-amd64"}' | sh
cat to_pull.txt | awk '{print "docker push " "'"$registry/$namespace/"'" $2 "-amd64"}'
cat to_pull.txt | awk '{print "docker push " "'"$registry/$namespace/"'" $2 "-amd64"}' | sh
