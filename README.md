# image2image
## what's this
python3 program for converting format of images including .pdf using Pillow(PIL), OpenCV, pdf2image

## necesarry modules
- PIL
- OpenCV
- pdf2image(https://github.com/Belval/pdf2image)

## how to use
download this directry and run image2image.py with arguments like;
<br>
`python image2image.py {directry_name} {before_format} {after_format}`
<br>
for example, 
<br>
`python image2image.py images_jpg .jpg .png`
<br>
then a directry named `result` will be created and converted images will be put in.

## available formats
*.bmp .dib .eps .gif .hdr .ico .im .jp2 .jpe .jpeg .jpg .pbm .pcx .pdf .pgm .pic .png .pnm .ppm .pxm .ras .sgi .sr .tif .tiff .webp*

can be transfomed each other.
