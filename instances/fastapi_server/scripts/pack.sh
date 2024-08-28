#!/bin/bash

# ⚠️注意：需要在项目根目录执行该命令

# 设置项目名称
PROJECT_NAME="BYTECH" 

if [ -f ${PROJECT_NAME}.tar.gz ]; then
    echo "[0] Removing old package ..."
    rm ${PROJECT_NAME}.tar.gz
fi 

ORI_REAL_DIR=$(readlink -f ./)
echo "[1] Getting absolute path of project: ${ORI_REAL_DIR}"

if [ -d $ORI_REAL_DIR ]; then
    echo "[2] Change to upper folder ..."
    cd .. 

    echo "[3] Make temp folder ..."
    mkdir -p ${PROJECT_NAME}

    echo "[4] Entering temp folder ..."
    cd ${PROJECT_NAME}

    echo "[5] Duplicating project files ..."
    cp -r ${ORI_REAL_DIR}/* .

    echo "[6] Removing extra files ..."
    rm -r ./.git ./.idea ./.DS_Store ./.ipynb_checkpoints ./tmp/ ./__pycache__ ./.vscode ./logs/ ./data ./_build

    PACKTIME=$(date +"%Y%m%d_%H%M%S")
    echo "[7] Packing at: ${PACKTIME}"
    echo "${PACK_TIME}" > PACKTIME

    echo "[8] Back to parent folder ..."
    cd ..

    echo "[9] Starting to packing ..."
    tar -zcvf ${PROJECT_NAME}.tar.gz ${PROJECT_NAME}

    echo "[10] Packing complete, removing temp folder ..."
    rm -r ${PROJECT_NAME}

    echo "[11] Moving package to current folder ..."
    mv ${PROJECT_NAME}.tar.gz ${ORI_REAL_DIR}/${PROJECT_NAME}.tar.gz

fi 

echo "Done !"