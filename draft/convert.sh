#!/bin/bash

for name in a-setup d-basic d-time d-vert ;do
	if [ -e ${name}.html ];then
		wkhtmltopdf ${name}.html ${name}.pdf
		rm ${name}.html
	fi
done

