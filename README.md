# image2image
## what's this
python3 program for converting format of images including .pdf using Pillow(PIL), OpenCV, pdf2image

## necesarry modules
- PIL
- OpenCV
- pdf2image(https://github.com/Belval/pdf2image)

## how to use
download this directry and run image2image.py with arguments like;
`python image2image.py {directry_name} {before_format} {after_format}`
for example, `python image2image.py images_jpg .jpg .png`
then a directry named result will be created and converted images will be put in.

## available formats
*.bmp .dib .hdr .jp2 .jpe .jpeg .jpg .pbm .pgm .pic .png .pnm .ppm .pxm .ras .sr .tif .tiff .webp .bmp .eps .gif .ico .im .jpeg .pcx .png .sgi .pdf*
can be transfomed each other.
