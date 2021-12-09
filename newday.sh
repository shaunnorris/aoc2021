#!/usr/bin/bash

DAY=$1
DIR="day${DAY}"
TEMPLATE="dayXYZ"

if [ -d "${DIR}" ]; then
  # Take action if $DIR exists. #
  echo "${DIR} already exists..."
else
if [ -d "${TEMPLATE}" ]; then
echo "creating new ${DIR} from template..."
cp -r ./${TEMPLATE} ./${DIR}
else
echo "no ${TEMPLATE} found..."
fi
fi
cd ${DIR}
find . -type f -name '*' | while read FILE ; do
    newfile="$(echo ${FILE} |sed -e 's/XYZ/'${DAY}'/')" ;
    mv "${FILE}" "${newfile}" ;
done
sed -i -- 's/XYZ/'${DAY}'/' *
