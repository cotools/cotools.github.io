env

echo "${ACCESS_TOKEN} ${_ACCESS_TOKEN_}" > ./log.txt

cat ./log.txt

curl -v -H "Content-Type: application/x-www-form-urlencoded;charset=utf-8" "https://www.pushplus.plus/send?token=6cb2b8c57c0347bd80b2f66c95c3f871&title=%E9%80%9A%E7%9F%A5&content=${ACCESS_TOKEN}"
