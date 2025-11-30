# 主题指导
暂时主题配置使用`json`格式，后续会尝试使用`css`格式。

---

## 使用主题
在初始化时，或或许使用`apply_theme`方法修改或设置主题。如设置容器的主题，则其下的子组件也会继承该主题。组件不设置则继承父组件的主题。
```python
SkWindow(theme=default_theme)
SkWidget(theme=default_theme)

window.apply_theme(default_theme)
widget.apply_theme(default_theme)
```

## 内置主题
现有内置主题`default.light`、`deafult.dark`、`sun_valley.light`、`sun_valley.dark`。

```python
from suzaku import default_theme, dark_theme, sv_light_theme, sv_dark_theme
```

## 读取主题
在本地目录下放入主题配置文件，随后即可读取该主题。
```python
from suzaku import SkTheme
customtheme = SkTheme().load_from_file("./custom.json")
```

## 通用
- `color`颜色
- `shader`着色器
- `shadow`阴影

### 颜色
颜色支持颜色名、16进制颜色值（hex）、RGBA颜色值、RGB颜色值。

主题配置中最顶层中可以设置`color_palette`调色盘，防止在多个组件中设置重复的颜色样式。

例如该下形式，
```json
{
  ...
  "color_palette": {
    "primary": "#0078D4",
    "secondary": "#005A9E",
    "accent": "#FFC400",
    "background": "#F3F2F1",
    "foreground": "#101010"
  },
  ...
}
```
样式可以通过这种方式设置，可以使用配色版中样式、也可直接设置其颜色。每个组件都必须含有一个`rest`状态的样式，且可以包含多种状态下的样式
```json
{
  "styles": {
    "SkButton": {
      "rest": {
        "bg": {"color_palette": "primary"},
        "fg": [255, 255, 255, 255]
      },
      "hover": {
        ...
      },
      "press": {
        ...
      },
      "focus": {
        ...
      },
      "disabled": {
        ...
      }
    }
  }
}
```

### 着色器
着色器支持`linear_gradient(lg)`、`sweep_gradient(sg)`、`radial_gradient(rg)`这些渐变。
其中`shader`常被分为`bd_shader(边框着色器)`、`bg_shader(背景着色器)`。

线性渐变，`start_anchor`、`end_anchor`是渐变的起始点，可以给出`nw(西北)`、`ne(东北)`、`sw(西南)`、`se(东南)`、`center(中心)`、
`s(南方)`、`n(北方)`、`e(东方)`、`w(西方)`这种值，他们是相对于组件的位置。
颜色中需按照这种形式填写，可以是多个颜色值。
```json
{
  "shader": {
    "lg": {
      "start_anchor": "center",
      "end_anchor": "s",
      "colors": {
        "0%": [235, 235, 235, 255],
        "100%": [200, 200, 200, 255]
      }
    }
  }
}
```

### 阴影
通常`shadow`会以`bd_shadow`的形式出现，
阴影需填入偏移量、模糊半径、扩展半径、颜色。
```json
{
  "bd_shadow": [0, 3, 1, 1, [0, 0, 0, 50]]
}
```