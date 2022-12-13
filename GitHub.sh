#!/bin/bash

read -p "Commit name: " name
read -p "Branch: " branch
git add .
git commit -m "$name"
git push origin $branch