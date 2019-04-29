# texture-utils

## About

This generates some textures useful for testing 3d graphics 
(Checkerboard patterns in multiple colors, and a palette texture)


## Usage

```
usage: python make_test_textures.py [-h] [--outdir OUTDIR]
                                    [--texturesize TEXTURESIZE] [--dim DIM]
                                    count
```

## Example

```
python make_test_textures.py 4 --texturesize 128 --dim 4 --outdir examples
```

In an "Examples" folder:

### Palette
![Palette](examples/palette.png?raw=true "Palette")

### Checkboard Textures
![Checker #1](examples/img-0.png?raw=true "Checker #1")
![Checker #2](examples/img-1.png?raw=true "Checker #2")
![Checker #3](examples/img-2.png?raw=true "Checker #3")
![Checker #4](examples/img-3.png?raw=true "Checker #4")


### Matrix
![Matrix](examples/matrix.png?raw=true "Matrix")



