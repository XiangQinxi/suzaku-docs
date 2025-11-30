# 快速开始

```{eval-rst}
.. toctree::
   :maxdepth: 1
    
   theme
```

## 下载与安装
第一步是下载`suzaku`。您可以通过`pip`轻松下载：
```bash
pip install suzaku
```

### Windows & MacOS
暂无其他注意事项

### Linux
`suzaku`依赖于`pyopengl`、`skia-python`和`glfw`库。
`Linux`用户可能需要运行`apt install libglfw3`来安装`glfw`库。

运行以下命令来安装`skia-python`的依赖项。
```bash
apt-get install libfontconfig1 libgl1-mesa-glx libgl1-mesa-egl libegl1 libglvnd0 libgl1-mesa-dri
```
## 示例
安装完成后，您可以通过运行来启动`suzaku`示例看看效果。
```bash
python -m suzaku
```

## requirements.txt
[PyOpenGL](https://pypi.org/project/PyOpenGL/)
[skia-python](https://pypi.org/project/skia-python/)
[glfw](https://pypi.org/project/glfw/) 