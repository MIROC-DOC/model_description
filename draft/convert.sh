#!/bin/bash

for name in a-setup d-basic d-time d-vert ;do
	wkhtmltopdf ${name}.html ${name}.pdf
	rm ${name}.html
done
