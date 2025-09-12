#!/bin/bash

echo "Testing Java Backend Service..."
curl http://localhost:8080/api/books/1

echo
echo -e "\nTesting Python ML Service..."
curl http://localhost:8000/api/books/1/ 

echo
echo -e "\nTesting cross-service communication..."
curl http://localhost:8080/api/genres/predictGenre?title=Python+Programming

echo
read -p "Press enter to exit"