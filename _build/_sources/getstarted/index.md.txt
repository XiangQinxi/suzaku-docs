# Get started

```{eval-rst}
.. toctree::
   :maxdepth: 1

   zh-hans
```

## Download & Install
The first step is to download `Suzaku`. You can easily download it using `pip`:
```bash
pip install suzaku
```
But note that `Suzaku` depends on `pyopengl`, `skia-python`, and `glfw` libraries. 

`Linux` users may need to run `apt install libglfw3` to install `glfw` library.

`apt-get install libfontconfig1 libgl1-mesa-glx libgl1-mesa-egl libegl1 libglvnd0 libgl1-mesa-dri` to install `skia-python` dependencies.

## Example
After that, you can run `Suzaku` by running `python -m suzaku`.

## requirements.txt
[PyOpenGL](https://pypi.org/project/PyOpenGL/)
[skia-python](https://pypi.org/project/skia-python/)
[glfw](https://pypi.org/project/glfw/)