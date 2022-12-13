#!/bin/bash


# read -p "Dime tu nombre: " nombre
# read -p "Mascota: " nombre_mascota
# # Si queremos concatenar con guiones bajos, entonces:
# mensaje="El correo de $nombre es ${nombre_mascota}_12@gmail.com"
# echo $mensaje

read -p "Commit name: " name
read -p "Branch: " branch
git add .
git commit -m "$name"
git push origin $branch